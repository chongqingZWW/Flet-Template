from sqlalchemy.orm import Session
from app.db.models import SystemConfig


class SystemConfigRepository:
    """
    系统配置仓储类
    负责系统配置的数据访问操作
    """

    def __init__(self, session: Session):
        self.session = session

    def get_all_configs(self):
        """
        获取所有系统配置
        :return: 配置列表
        """
        try:
            configs = self.session.query(SystemConfig).all()
            return [self._to_dict(config) for config in configs]
        except Exception as e:
            print(f"获取系统配置失败: {e}")
            return []

    def get_configs_by_category(self, category: str):
        """
        获取指定分类的配置
        :param category: 配置分类
        :return: 配置列表
        """
        try:
            configs = self.session.query(SystemConfig).filter_by(category=category).all()
            return [self._to_dict(config) for config in configs]
        except Exception as e:
            print(f"获取分类配置失败: {category}, 错误: {e}")
            return []

    def get_config_by_key(self, config_key: str):
        """
        根据键获取配置
        :param config_key: 配置键
        :return: 配置项或 None
        """
        try:
            config = self.session.query(SystemConfig).filter_by(config_key=config_key).first()
            return self._to_dict(config) if config else None
        except Exception as e:
            print(f"获取配置失败: {config_key}, 错误: {e}")
            return None

    def add_config(self, config_data: dict):
        """
        新增配置
        :param config_data: 配置数据字典
        :return: 新配置或 None
        """
        try:
            new_config = SystemConfig(**config_data)
            self.session.add(new_config)
            self.session.commit()
            return self._to_dict(new_config)
        except Exception as e:
            self.session.rollback()
            print(f"新增配置失败: {e}")
            return None

    def update_config(self, config_key: str, updates: dict):
        """
        更新配置
        :param config_key: 配置键
        :param updates: 更新的字段和值
        :return: 更新后的配置或 None
        """
        try:
            config = self.session.query(SystemConfig).filter_by(config_key=config_key).first()
            if config:
                for key, value in updates.items():
                    if hasattr(config, key):
                        setattr(config, key, value)
                self.session.commit()
                print(f"配置已更新: {config_key}")
                return self._to_dict(config)
            print(f"配置不存在: {config_key}")
            return None
        except Exception as e:
            self.session.rollback()
            print(f"更新配置失败: {config_key}, 错误: {e}")
            return None

    def delete_config(self, config_key: str):
        """
        删除配置
        :param config_key: 配置键
        :return: 是否成功
        """
        try:
            config = self.session.query(SystemConfig).filter_by(config_key=config_key).first()
            if config:
                self.session.delete(config)
                self.session.commit()
                print(f"配置已删除: {config_key}")
                return True
            print(f"配置不存在: {config_key}")
            return False
        except Exception as e:
            self.session.rollback()
            print(f"删除配置失败: {config_key}, 错误: {e}")
            return False

    def init_default_configs(self):
        """
        初始化默认配置
        从 models.py 中的 DEFAULT_CONFIGS 初始化系统配置
        """
        try:
            from app.db.models import DEFAULT_CONFIGS
            for config in DEFAULT_CONFIGS:
                existing = self.get_config_by_key(config["config_key"])
                if not existing:
                    self.add_config(config)
            print("默认配置已初始化")
            return True
        except Exception as e:
            print(f"初始化默认配置失败: {e}")
            return False

    @staticmethod
    def _to_dict(config: SystemConfig):
        """
        将配置模型转换为字典
        :param config: 配置模型实例
        :return: 字典
        """
        if not config:
            return None
        return {
            "id": config.id,
            "key": config.config_key,
            "value": config.config_value,
            "description": config.description,
            "category": config.category,
            "enable": config.enable
        }
