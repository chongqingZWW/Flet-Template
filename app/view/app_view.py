import flet as ft

from app.component.TrayIconManager import TrayIconManager
from app.view.home_view import HomeView
from app.view.settings_view import SettingsView
from app.view.basic_components_view import BasicComponentsView
from app.view.layout_components_view import LayoutComponentsView
from app.view.form_components_view import FormComponentsView
from app.view.data_components_view import DataComponentsView
from app.view.feedback_components_view import FeedbackComponentsView


class AppView:
    """主界面管理"""

    def __init__(self, page: ft.Page, viewmodel):
        self.page = page
        self.viewmodel = viewmodel
        self.tray_manager = TrayIconManager(page)

        # 订阅事件
        self.viewmodel.subscribe("theme_changed", self._on_theme_changed)
        self.viewmodel.subscribe("nav_changed", self._on_nav_changed)

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
        }
        
        # 当前视图
        self.current_view = "home"
        self.content_area = None
        
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

    def build_main_layout(self):
        """构建主界面布局"""
        # 创建内容区域容器
        self.content_area = ft.Container(
            content=self.views[self.current_view].view,
            bgcolor=ft.colors.SURFACE,
            expand=3,
            padding=ft.padding.all(20),
            animate_opacity=300,
        )

        return ft.Container(
            content=ft.Row(
                controls=[
                    # 左侧导航栏
                    ft.Container(
                        content=self._build_nav_rail(),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        expand=0.5,
                        padding=ft.padding.all(0),
                    ),
                    # 中间内容区
                    self.content_area,
                    # 右侧详情区
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=0,
            ),
            expand=True,
        )

    def _build_nav_rail(self):
        """构建左侧导航栏"""
        return ft.NavigationRail(
            selected_index=self.current_nav_index,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=200,
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
            ],
            on_change=lambda e: self.viewmodel.select_nav_item(e.control.selected_index)
        )

    def _on_theme_changed(self, theme):
        """主题变化回调"""
        print(f"主题已切换为: {theme}")
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
            6: "settings"
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