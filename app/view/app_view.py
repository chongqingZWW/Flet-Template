import flet as ft

from app.component.TrayIconManager import TrayIconManager


class AppView:
    """主界面管理"""

    def __init__(self, page: ft.Page, viewmodel):
        self.page = page
        self.viewmodel = viewmodel
        self.tray_manager = TrayIconManager(page)

        # 订阅主题变化
        self.viewmodel.subscribe("theme_changed", self._on_theme_changed)
        self.viewmodel.subscribe("nav_changed", self._on_nav_changed)

        # 当前选中的导航项
        self.current_nav_index = 0

    def build(self):
        """构建并显示主界面"""
        self.page.add(self.build_main_layout())
        self.page.update()
        self.tray_manager.start()

    def build_main_layout(self):
        """构建主界面布局"""
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
                    ft.Container(
                        content=self._build_content_area(),
                        bgcolor=ft.colors.SURFACE,
                        expand=3,
                        padding=ft.padding.all(20),
                    ),
                    # 右侧详情区
                    ft.Container(
                        content=self._build_detail_area(),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        expand=2,
                        padding=ft.padding.all(10),
                    ),
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
            leading=ft.FloatingActionButton(
                icon=ft.icons.CREATE,
                text="新建",
                on_click=lambda e: print("新建按钮被点击")
            ),
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="收藏夹"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon=ft.icons.HOME,
                    label="首页"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS,
                    label="设置"
                ),
            ],
            on_change=lambda e: self.viewmodel.select_nav_item(e.control.selected_index)
        )

    def _build_content_area(self):
        """构建中间内容区"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("内容区域", size=20, weight=ft.FontWeight.BOLD),
                    margin=ft.margin.only(bottom=20)
                ),
                ft.ListView(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ARTICLE),
                            title=ft.Text(f"项目 {i}"),
                            subtitle=ft.Text(f"这是项目 {i} 的描述"),
                        ) for i in range(1, 6)
                    ],
                    spacing=10,
                    padding=10,
                    expand=True,
                )
            ],
            expand=True,
        )

    def _build_detail_area(self):
        """构建右侧详情区"""
        return ft.Column(
            controls=[
                ft.Text("详情区域", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.TextField(label="名称", value="示例项目"),
                ft.TextField(
                    label="描述",
                    value="这是一个示例项目的详细描述...",
                    multiline=True,
                    min_lines=3,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="保存",
                            icon=ft.icons.SAVE,
                            on_click=lambda e: print("保存按钮被点击")
                        ),
                        ft.OutlinedButton(
                            text="取消",
                            on_click=lambda e: print("取消按钮被点击")
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _on_theme_changed(self, theme):
        """主题变化回调"""
        print(f"主题已切换为: {theme}")
        self.page.update()

    def _on_nav_changed(self, index):
        """导航选择变化回调"""
        self.current_nav_index = index
        print(f"导航已切换到: {index}")
        self.page.update()
