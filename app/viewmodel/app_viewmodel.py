import flet as ft
from app.component.SystemSettingsDialog import SystemSettingsDialog
from app.repository.system_config_repository import SystemConfigRepository
from app.viewmodel.system_config_viewmodel import SystemConfigViewModel
from app.tasks.SchedulerManager import SchedulerManager
from collections import defaultdict
import json
import os
from pathlib import Path


class AppViewModel:
    """
    应用程序主视图模型
    负责管理全局状态和业务逻辑
    """
    def __init__(self, system_config_repo: SystemConfigRepository):
        # 初始化系统配置视图模型
        self.system_config_viewmodel = SystemConfigViewModel(system_config_repo)
        
        # 全局状态
        self.current_route = "/"  # 当前路由
        self.selected_nav_index = 0  # 当前选中的导航项
        
        # 观察者（订阅者）字典
        self.observers = {
            "route_changed": [],      # 路由变化
            "nav_changed": [],        # 导航选择变化
            "theme_changed": [],      # 主题变化
            "settings_updated": [],   # 设置更新
            "detail_changed": []      # 详情变化
        }

        self.system_config_repo = system_config_repo
        self._subscribers = defaultdict(list)
        self._detail_data = {
            "name": "示例项目",
            "description": "这是一个示例项目的详细描述..."
        }

        self.subscribers = {}
        self.settings = self._load_settings()
        self.scheduler = SchedulerManager()  # 添加调度器实例
        self.scheduler.start()  # 启动调度器

        # 初始化系统配置
        self.system_config = {
            "theme": self.get_setting("theme", "light"),
            "language": self.get_setting("language", "zh_CN"),
            "window_width": self.get_setting("window_width", 1200),
            "window_height": self.get_setting("window_height", 800),
            "opacity": self.get_setting("opacity", 1.0),
        }

    def _load_settings(self):
        """加载设置"""
        settings_file = Path("settings.json")
        if settings_file.exists():
            try:
                with open(settings_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_settings(self):
        """保存设置"""
        try:
            with open("settings.json", "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"保存设置失败: {e}")

    def get_setting(self, key, default=None):
        """获取设置值"""
        return self.settings.get(key, default)

    def save_setting(self, key, value):
        """保存设置值"""
        self.settings[key] = value
        self._save_settings()
        # 如果有对应的事件，触发通知
        if key == "theme":
            self.notify("theme_changed", value)
        elif key == "language":
            self.notify("language_changed", value)

    # ---- 观察者模式实现 ----
    def subscribe(self, event_name: str, callback):
        """订阅事件"""
        if event_name in self.observers:
            self.observers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback):
        """取消订阅"""
        if event_name in self.observers:
            self.observers[event_name].remove(callback)

    def notify(self, event_name: str, *args, **kwargs):
        """通知观察者"""
        if event_name in self.observers:
            for callback in self.observers[event_name]:
                callback(*args, **kwargs)

    # ---- 路由管理 ----
    def navigate_to(self, route: str):
        """
        导航到指定路由
        :param route: 目标路由路径
        """
        self.current_route = route
        self.notify("route_changed", route)

    # ---- 导航管理 ----
    def select_nav_item(self, index: int):
        """
        选择导航项
        :param index: 导航项索引
        """
        self.selected_nav_index = index
        self.notify("nav_changed", index)

    # ---- 设置管理 ----
    def show_settings(self, page: ft.Page):
        """
        显示设置对话框
        :param page: 当前页面实例
        """
        settings_dialog = SystemSettingsDialog(
            page=page, 
            view_model=self.system_config_viewmodel,
            on_settings_changed=lambda: self.notify("settings_updated")
        )
        settings_dialog.show()

    def update_setting(self, key: str, value: str):
        """
        更新系统配置项
        :param key: 配置键
        :param value: 新的配置值
        """
        success = self.system_config_viewmodel.update_config(key, {"config_value": value})
        if success:
            self.notify("settings_updated")
        return success

    # ---- 主题管理 ----
    def toggle_theme(self):
        """切换明暗主题"""
        current_theme = self.get_setting("theme", "light")
        new_theme = "dark" if current_theme == "light" else "light"
        self.save_setting("theme", new_theme)

    def update_detail(self, field: str, value: str):
        """更新详情数据"""
        self._detail_data[field] = value
        self.notify("detail_changed", self._detail_data)

    def get_detail(self, field: str) -> str:
        """获取详情数据"""
        return self._detail_data.get(field, "")

    def __del__(self):
        """清理资源"""
        if hasattr(self, 'scheduler'):
            self.scheduler.shutdown()
