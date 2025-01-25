import os
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

from app.config.config import settings
from app.db.models import Base, SystemConfig, DEFAULT_CONFIGS

logger = logging.getLogger(__name__)


class DatabaseManager:
    """
    数据库管理类
    负责数据库初始化、会话管理和基础数据维护
    """

    def __init__(self):
        # 获取应用程序根目录
        app_dir = self.get_app_directory()

        # 设置数据库路径
        database_path = os.path.join(app_dir, settings.database.DB_PATH)
        os.makedirs(os.path.dirname(database_path), exist_ok=True)

        # 创建数据库引擎和会话工厂
        database_url = f"sqlite:///{database_path}"
        self.engine = create_engine(
            database_url,
            connect_args={'check_same_thread': False},
            echo=settings.get("database.echo", False)  # SQL 日志
        )
        
        self.SessionFactory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.SessionFactory)

        # 初始化数据库
        self._initialize_database(database_path)

    @staticmethod
    def get_app_directory() -> str:
        """
        获取应用程序根目录
        支持开发环境和打包后的环境
        """
        if getattr(sys, 'frozen', False):
            # 打包后的环境
            return os.path.dirname(sys.executable)
        else:
            # 开发环境
            return os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

    def _initialize_database(self, database_path: str):
        """
        初始化数据库
        创建表和初始化基础数据
        """
        try:
            # 检查数据库文件是否存在
            is_new_db = not os.path.exists(database_path)
            
            # 创建所有表
            Base.metadata.create_all(self.engine)
            logger.info("数据库表结构已创建或更新")

            # 如果是新数据库，初始化默认数据
            if is_new_db:
                self._initialize_default_data()
                logger.info("新数据库已初始化完成")
            else:
                logger.info("使用现有数据库")

        except SQLAlchemyError as e:
            logger.error(f"数据库初始化失败: {e}")
            raise

    def _initialize_default_data(self):
        """初始化默认数据"""
        try:
            with self.get_session_context() as session:
                # 初始化系统配置
                self._init_system_configs(session)
                
                # 可以在这里添加其他默认数据的初始化
                # self._init_other_data(session)

                session.commit()
                logger.info("默认数据初始化完成")

        except SQLAlchemyError as e:
            logger.error(f"初始化默认数据失败: {e}")
            raise

    def _init_system_configs(self, session):
        """初始化系统配置"""
        try:
            for config in DEFAULT_CONFIGS:
                existing = session.query(SystemConfig).filter_by(
                    config_key=config["config_key"]
                ).first()
                
                if not existing:
                    session.add(SystemConfig(**config))
                    logger.info(f"添加默认配置: {config['config_key']}")
                else:
                    logger.debug(f"配置已存在: {config['config_key']}")

        except SQLAlchemyError as e:
            logger.error(f"初始化系统配置失败: {e}")
            raise

    def get_session(self):
        """获取数据库会话"""
        return self.Session()

    def get_session_context(self):
        """
        获取数据库会话上下文管理器
        用于确保会话正确关闭
        使用示例:
            with db_manager.get_session_context() as session:
                session.query(...)
        """
        class SessionContext:
            def __init__(self, session_factory):
                self.session = session_factory()

            def __enter__(self):
                return self.session

            def __exit__(self, exc_type, exc_val, exc_tb):
                if exc_type is not None:
                    self.session.rollback()
                    logger.error(f"会话异常: {exc_val}")
                self.session.close()

        return SessionContext(self.Session)

    def dispose(self):
        """释放数据库连接池资源"""
        if self.engine:
            self.engine.dispose()
            logger.info("数据库连接池已释放")
