from sqlalchemy import Column, Integer, String, DateTime, Text, JSON, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

__all__ = [
    "SystemConfig",  # 系统配置表
    "ExampleModel",  # 示例模型
]


class SystemConfig(Base):
    """
    系统配置表
    用于存储应用程序的全局配置项
    """
    __tablename__ = 'system_configs'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='配置ID')
    config_key = Column(String(255), nullable=False, unique=True, comment='配置键')
    config_value = Column(String(255), nullable=False, comment='配置值')
    description = Column(Text, nullable=True, comment='配置项描述')
    category = Column(String(50), nullable=True, comment='配置分类')
    enable = Column(Integer, default=1, comment='是否启用(1=启用,0=禁用)')
    created_at = Column(DateTime, default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), comment='更新时间')

    def __repr__(self):
        return f"<SystemConfig(key={self.config_key}, value={self.config_value})>"


class ExampleModel(Base):
    """
    示例数据模型
    演示基本的数据库表结构定义
    """
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID')
    name = Column(String(100), nullable=False, comment='名称')
    description = Column(String(255), nullable=True, comment='描述')
    type = Column(Integer, default=1, comment='类型(1=类型1,2=类型2)')
    status = Column(Integer, default=1, comment='状态(1=启用,0=禁用)')
    order_index = Column(Integer, default=0, comment='排序索引')
    settings = Column(JSON, nullable=True, comment='配置JSON')
    metadata_info = Column(JSON, nullable=True, comment='元数据信息')
    created_at = Column(DateTime, default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), comment='更新时间')

    def __repr__(self):
        return f"<ExampleModel(id={self.id}, name={self.name})>"

    def to_dict(self):
        """转换为字典"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "status": self.status,
            "order_index": self.order_index,
            "settings": self.settings,
            "metadata_info": self.metadata_info,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


# 系统配置的默认值
DEFAULT_CONFIGS = [
    {
        "config_key": "theme",
        "config_value": "light",
        "description": "应用主题(light/dark)",
        "category": "appearance"
    },
    {
        "config_key": "language",
        "config_value": "zh_CN",
        "description": "界面语言",
        "category": "locale"
    },
    {
        "config_key": "window_width",
        "config_value": "1200",
        "description": "窗口宽度",
        "category": "window"
    },
    {
        "config_key": "window_height",
        "config_value": "800",
        "description": "窗口高度",
        "category": "window"
    },
    {
        "config_key": "app_title",
        "config_value": "Flet Application",
        "description": "应用标题",
        "category": "application"
    }
]
