from app.utils.log_utils import LogUtils


class GlobalConfig:
    """全局配置单例类"""
    db_manager = None
    wechat_bot_manager = None
    logger = LogUtils.get_logger("Global")
