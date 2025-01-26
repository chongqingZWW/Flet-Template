import flet as ft

from app.component.TrayIconManager import TrayIconManager
from app.view.home_view import HomeView
from app.view.settings_view import SettingsView
from app.view.basic_components_view import BasicComponentsView
from app.view.layout_components_view import LayoutComponentsView
from app.view.form_components_view import FormComponentsView
from app.view.data_components_view import DataComponentsView
from app.view.feedback_components_view import FeedbackComponentsView
from app.view.task_view import TaskView


class AppView:
    """主界面管理"""

    def __init__(self, page: ft.Page, viewmodel):
        self.page = page
        self.viewmodel = viewmodel
        self.tray_manager = TrayIconManager(page)

        # 订阅事件
        self.viewmodel.subscribe("theme_changed", self._on_theme_changed)
        self.viewmodel.subscribe("nav_changed", self._on_nav_changed)

        # 设置初始主题
        initial_theme = self.viewmodel.get_setting("theme", "light")
        self.page.theme_mode = (
            ft.ThemeMode.DARK if initial_theme == "dark" else ft.ThemeMode.LIGHT
        )
        self.page.update()

        # 当前选中的导航项
        self.current_nav_index = 0

        # 初始化所有视图
        self.views = {
            "home": HomeView(page, viewmodel),
            "basic": BasicComponentsView(page, viewmodel),
            "layout": LayoutComponentsView(page, viewmodel),
            "form": FormComponentsView(page, viewmodel),
            "data": DataComponentsView(page, viewmodel),
            "feedback": FeedbackComponentsView(page, viewmodel),
            "settings": SettingsView(page, viewmodel),
            "task": TaskView(page, viewmodel),
        }
        
        # 当前视图
        self.current_view = "home"
        self.content_area = None
        
        self.view = self._build_view()

    def build(self):
        """构建并显示主界面"""
        # 创建主布局
        main_layout = self.build_main_layout()
        
        # 清空页面并添加主布局
        self.page.clean()
        self.page.add(main_layout)
        self.page.update()
        
        # 启动托盘图标
        self.tray_manager.start()

    def _build_view(self):
        """构建主视图"""
        # 创建内容区域
        self.content_area = ft.Container(
            content=self.views[self.current_view].view,
            expand=True,
            animate_opacity=300,
        )

        # 构建主布局
        return ft.Row(
            [
                # 左侧导航栏
                self._build_nav_rail(),
                # 分隔线
                ft.VerticalDivider(width=1),
                # 内容区域
                self.content_area,
            ],
            expand=True,
        )

    def build_main_layout(self):
        """构建主布局"""
        return self.view

    def _build_nav_rail(self):
        """构建左侧导航栏"""
        return ft.NavigationRail(
            selected_index=self.current_nav_index,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=200,
            group_alignment=-0.9,  # 将导航项向上对齐
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon=ft.icons.HOME,
                    label="首页"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.WIDGETS_OUTLINED,
                    selected_icon=ft.icons.WIDGETS,
                    label="基础组件"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.DASHBOARD_OUTLINED,
                    selected_icon=ft.icons.DASHBOARD,
                    label="布局组件"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.INPUT_OUTLINED,
                    selected_icon=ft.icons.INPUT,
                    label="表单组件"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.DATA_USAGE,
                    selected_icon=ft.icons.DATA_USAGE,
                    label="数据展示"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.NOTIFICATIONS_OUTLINED,
                    selected_icon=ft.icons.NOTIFICATIONS,
                    label="反馈组件"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS,
                    label="设置"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SCHEDULE,
                    selected_icon=ft.icons.SCHEDULE,
                    label="任务管理",
                ),
            ],
            on_change=lambda e: self.viewmodel.select_nav_item(e.control.selected_index),
            # 主题切换按钮
            trailing=ft.Container(
                content=ft.IconButton(
                    icon=ft.icons.DARK_MODE if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE,
                    on_click=lambda _: self.viewmodel.toggle_theme(),
                    tooltip="切换主题",
                ),
                margin=ft.margin.only(bottom=20),
            ),
        )

    def _on_theme_changed(self, theme):
        """主题变化回调"""
        # 更新页面主题
        self.page.theme_mode = ft.ThemeMode.DARK if theme == "dark" else ft.ThemeMode.LIGHT
        # 只更新页面，不单独更新控件
        self.page.update()

    def _on_nav_changed(self, index):
        """导航选择变化回调"""
        self.current_nav_index = index
        
        # 根据索引获取新的视图名称
        new_view = {
            0: "home",
            1: "basic",
            2: "layout",
            3: "form",
            4: "data",
            5: "feedback",
            6: "settings",
            7: "task"
        }.get(index, "home")
        
        # 如果视图确实发生了变化
        if new_view != self.current_view:
            # 更新当前视图
            self.current_view = new_view
            
            # 使用动画切换内容
            self.content_area.opacity = 0
            self.content_area.content = self.views[self.current_view].view
            self.page.update()
            
            # 设置淡入效果
            self.content_area.opacity = 1
            self.content_area.update()