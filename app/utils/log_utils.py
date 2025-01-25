import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


class LogUtils:
    @staticmethod
    def setup_logging(settings, enable_tkinter_log=False, on_close_callback=None):
        """
        根据提供的设置配置日志。
        :param enable_tkinter_log: 是否启用 Tkinter 日志显示。
        :param on_close_callback: 窗口关闭时的回调函数。
        """
        """设置全局日志配置，支持日志文件按天切割，文件名包含时间戳"""
        log_level = logging.DEBUG  # 可根据环境动态设置
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - Line: %(lineno)d - %(message)s'  # 包含文件名和行号

        logger = logging.getLogger()
        logger.setLevel(log_level)

        if not logger.hasHandlers():
            # 按日期切割日志文件的处理器
            log_dir = os.path.join(os.getcwd(), 'logs')
            os.makedirs(log_dir, exist_ok=True)

            # 动态设置日志文件名为 `application_YYYY-MM-DD.log`
            log_file = os.path.join(log_dir, f'application_{datetime.now().strftime("%Y-%m-%d")}.log')

            file_handler = TimedRotatingFileHandler(
                log_file,
                when='midnight',  # 每天午夜切割
                interval=1,  # 间隔1天
                backupCount=7,  # 保留最近7天的日志文件
                encoding='utf-8'  # 确保日志文件的编码
            )
            file_handler.setFormatter(logging.Formatter(log_format))
            logger.addHandler(file_handler)

            # 禁用 PIL 和 matplotlib 的 DEBUG 级别日志
            logging.getLogger('PIL').setLevel(logging.WARNING)
            logging.getLogger('matplotlib').setLevel(logging.WARNING)

    @staticmethod
    def get_logger(name):
        """
        获取一个指定名称的日志记录器。

        :param name: 日志记录器的名称。
        :return: Logger 对象。
        """
        return logging.getLogger(name)
