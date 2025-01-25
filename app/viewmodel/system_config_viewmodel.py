class SystemConfigViewModel:
    """系统配置业务逻辑"""

    def __init__(self, repository):
        self.repository = repository
        self.configs = []

    def load_configs(self):
        """加载所有系统配置"""
        self.configs = self.repository.get_all_configs()
        return self.configs

    def add_config(self, config_data):
        """新增系统配置"""
        new_config = self.repository.add_config(config_data)
        if new_config:
            self.configs.append(new_config)
        return new_config

    def update_config(self, config_id, updates):
        """更新系统配置"""
        return self.repository.update_config(config_id, updates)

    def delete_config(self, config_id):
        """删除系统配置"""
        success = self.repository.delete_config(config_id)
        if success:
            self.configs = [cfg for cfg in self.configs if cfg["id"] != config_id]
        return success

    def get_config_by_key(self, config_key):
        """根据配置键获取系统配置"""
        return self.repository.get_config_by_key(config_key)
