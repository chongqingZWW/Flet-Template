import flet as ft

from app.component.ThemeManager import ThemeManager
from app.config.database import DatabaseManager
from app.config.global_config import GlobalConfig
from app.repository.system_config_repository import SystemConfigRepository
from app.repository.example_repository import ExampleRepository
from app.view.app_view import AppView
from app.viewmodel.app_viewmodel import AppViewModel

logger = GlobalConfig.logger  # 全局日志记录器


def initialize_db_manager():
    """初始化数据库管理器"""
    if GlobalConfig.db_manager is None:
        GlobalConfig.db_manager = DatabaseManager()
        logger.info("数据库管理器已初始化。")


def apply_global_settings(page: ft.Page, settings: dict, theme_manager: ThemeManager):
    """根据全局配置应用页面设置"""
    try:
        # 设置窗口宽高
        page.window.width = int(settings.get("window_width", 1200))
        page.window.height = int(settings.get("window_height", 800))
        page.window.opacity = float(settings.get("opacity", 1.0))
        
        # 设置窗口标题
        page.title = settings.get("app_title", "Flet Application")
        
        # 设置主题
        theme = settings.get("theme", "light")
        theme_manager.apply_theme(page, theme)

        logger.info("全局设置已成功应用。")
    except Exception as e:
        logger.error(f"应用全局设置时出错: {e}")


def main(page: ft.Page):
    """Flet 应用入口"""
    # 页面基础配置
    page.window.center()
    page.padding = 0  # 页面外边距
    page.spacing = 0  # 页面控件之间的间距

    # 初始化主题管理器
    theme_manager = ThemeManager()

    # 初始化数据库
    initialize_db_manager()

    # 创建数据库会话
    session = GlobalConfig.db_manager.get_session()

    try:
        # 初始化 Repository
        system_config_repo = SystemConfigRepository(session)
        example_repo = ExampleRepository(session)  # 示例仓储

        # 加载全局配置
        global_settings_list = system_config_repo.get_all_configs()
        logger.info(f"全局设置: {global_settings_list}")

        # 将全局设置转换为字典
        global_settings = {item["key"]: item["value"] for item in global_settings_list}
        logger.info(f"转换后的全局设置: {global_settings}")

        # 应用全局配置到页面
        apply_global_settings(page, global_settings, theme_manager)

        # 初始化 ViewModel
        app_viewmodel = AppViewModel(system_config_repo=system_config_repo)

        # 初始化 AppView
        app_view = AppView(page=page, viewmodel=app_viewmodel)
        app_view.build()  # 构建界面

    finally:
        # 确保会话被正确关闭
        session.close()


# 启动 Flet 应用
if __name__ == "__main__":
    ft.app(target=main)
