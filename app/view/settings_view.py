import flet as ft
from app.view.base_view import BaseView


class SettingsView(BaseView):
    """设置页面视图"""

    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        self.view = self._build_view()

    def _build_view(self):
        return ft.Container(
            content=ft.Column([
                # 标题
                ft.Container(
                    content=ft.Text("设置", size=30, weight=ft.FontWeight.BOLD),
                    margin=ft.margin.only(bottom=20)
                ),

                # 设置选项卡
                ft.Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=[
                        ft.Tab(
                            text="常规设置",
                            icon=ft.icons.SETTINGS,
                            content=self._build_general_settings()
                        ),
                        ft.Tab(
                            text="主题设置",
                            icon=ft.icons.COLOR_LENS,
                            content=self._build_theme_settings()
                        ),
                        ft.Tab(
                            text="系统设置",
                            icon=ft.icons.ADMIN_PANEL_SETTINGS,
                            content=self._build_system_settings()
                        ),
                    ],
                    expand=True,
                )
            ]),
            padding=20
        )

    def _build_general_settings(self):
        """构建常规设置"""
        return ft.Container(
            content=ft.Column([
                ft.TextField(
                    label="应用名称",
                    value=self.viewmodel.get_setting("app_title", "Flet Application"),
                    on_change=lambda e: self.viewmodel.update_setting("app_title", e.control.value)
                ),
                ft.Slider(
                    label="窗口透明度",
                    min=0.1,
                    max=1.0,
                    value=float(self.viewmodel.get_setting("opacity", "1.0")),
                    divisions=9,
                    on_change=lambda e: self.viewmodel.update_setting("opacity", str(e.control.value))
                ),
                ft.Switch(
                    label="开机自启",
                    value=self.viewmodel.get_setting("auto_start", "false") == "true",
                    on_change=lambda e: self.viewmodel.update_setting("auto_start", str(e.control.value).lower())
                )
            ], spacing=20),
            padding=20
        )

    def _build_theme_settings(self):
        """构建主题设置"""
        return ft.Container(
            content=ft.Column([
                ft.RadioGroup(
                    content=ft.Column([
                        ft.Radio(value="light", label="浅色主题"),
                        ft.Radio(value="dark", label="深色主题"),
                        ft.Radio(value="system", label="跟随系统"),
                    ]),
                    value=self.viewmodel.get_setting("theme", "light"),
                    on_change=lambda e: self.viewmodel.update_setting("theme", e.control.value)
                ),
                ft.Divider(),
                ft.Text("主题色", size=16, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.Container(
                        bgcolor=color,
                        width=40,
                        height=40,
                        border_radius=ft.border_radius.all(5),
                        on_click=lambda e, c=color: self.viewmodel.update_setting("primary_color", c)
                    ) for color in [
                        ft.colors.BLUE,
                        ft.colors.RED,
                        ft.colors.GREEN,
                        ft.colors.PURPLE,
                        ft.colors.ORANGE
                    ]
                ], spacing=10)
            ], spacing=20),
            padding=20
        )

    def _build_system_settings(self):
        """构建系统设置"""
        return ft.Container(
            content=ft.Column([
                ft.TextField(
                    label="缓存目录",
                    value=self.viewmodel.get_setting("cache_dir", "./cache"),
                    read_only=True,
                    suffix=ft.IconButton(
                        icon=ft.icons.FOLDER_OPEN,
                        on_click=lambda _: print("选择目录")
                    )
                ),
                ft.Row([
                    ft.TextField(
                        label="日志级别",
                        value=self.viewmodel.get_setting("log_level", "INFO"),
                        width=200
                    ),
                    ft.TextField(
                        label="最大日志文件大小(MB)",
                        value=self.viewmodel.get_setting("max_log_size", "10"),
                        width=200
                    )
                ]),
                ft.ElevatedButton(
                    "清除缓存",
                    icon=ft.icons.CLEANING_SERVICES,
                    on_click=lambda _: print("清除缓存")
                )
            ], spacing=20),
            padding=20
        ) 