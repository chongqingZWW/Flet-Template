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
                    content=ft.Column([
                        ft.Text("设置", size=30, weight=ft.FontWeight.BOLD),
                        ft.Text("自定义应用程序设置", size=16, color=ft.colors.GREY_700),
                    ]),
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
        def on_window_size_changed(e):
            try:
                width = int(window_width.value)
                height = int(window_height.value)
                if width >= 800 and height >= 600:
                    self.page.window_width = width
                    self.page.window_height = height
                    self.viewmodel.save_setting("window_width", width)
                    self.viewmodel.save_setting("window_height", height)
                    self.page.show_snack_bar(
                        ft.SnackBar(content=ft.Text("窗口大小已保存"))
                    )
            except ValueError:
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("请输入有效的数值"))
                )

        def on_opacity_changed(e):
            try:
                opacity = float(e.control.value)
                if 0.1 <= opacity <= 1.0:
                    self.page.window_opacity = opacity
                    self.viewmodel.save_setting("opacity", opacity)
            except ValueError:
                pass

        window_width = ft.TextField(
            label="窗口宽度",
            value=str(self.page.window_width),
            on_change=on_window_size_changed,
            suffix_text="px",
            width=200,
        )

        window_height = ft.TextField(
            label="窗口高度",
            value=str(self.page.window_height),
            on_change=on_window_size_changed,
            suffix_text="px",
            width=200,
        )

        return ft.Container(
            content=ft.Column([
                ft.Text("窗口设置", size=20, weight=ft.FontWeight.BOLD),
                ft.Row([
                    window_width,
                    window_height,
                ], alignment=ft.MainAxisAlignment.START, spacing=20),
                ft.Text("窗口透明度", size=16),
                ft.Slider(
                    min=0.1,
                    max=1.0,
                    value=self.page.window_opacity,
                    divisions=9,
                    label="{value}",
                    on_change=on_opacity_changed,
                ),
            ], spacing=20),
            padding=20
        )

    def _build_theme_settings(self):
        """构建主题设置"""
        def on_theme_changed(e):
            self.viewmodel.save_setting("theme", e.control.value)
            self.viewmodel.toggle_theme()
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text("主题已更改"))
            )

        def on_color_changed(color):
            # 实现主题色切换
            pass

        return ft.Container(
            content=ft.Column([
                ft.Text("主题模式", size=20, weight=ft.FontWeight.BOLD),
                ft.RadioGroup(
                    content=ft.Column([
                        ft.Radio(value="light", label="浅色主题"),
                        ft.Radio(value="dark", label="深色主题"),
                        ft.Radio(value="system", label="跟随系统"),
                    ]),
                    value="light" if self.page.theme_mode == ft.ThemeMode.LIGHT else "dark",
                    on_change=lambda e: on_theme_changed(e),
                ),
                ft.Divider(),
                ft.Text("主题颜色", size=20, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.Container(
                        bgcolor=color,
                        width=40,
                        height=40,
                        border_radius=ft.border_radius.all(5),
                        on_click=lambda e, c=color: on_color_changed(c)
                    ) for color in [
                        ft.colors.BLUE,
                        ft.colors.RED,
                        ft.colors.GREEN,
                        ft.colors.PURPLE,
                        ft.colors.ORANGE
                    ]
                ], spacing=10),
            ], spacing=20),
            padding=20
        )

    def _build_system_settings(self):
        """构建系统设置"""
        def on_auto_start_changed(e):
            try:
                self.viewmodel.save_setting("auto_start", e.control.value)
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text(
                        "已启用开机自启" if e.control.value else "已禁用开机自启"
                    ))
                )
            except Exception as e:
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text(f"设置失败: {str(e)}"))
                )

        def on_minimize_to_tray_changed(e):
            self.viewmodel.save_setting("minimize_to_tray", e.control.value)

        return ft.Container(
            content=ft.Column([
                ft.Text("系统设置", size=20, weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.Text("开机自启", size=16),
                    ft.Switch(
                        value=self.viewmodel.get_setting("auto_start", False),
                        on_change=on_auto_start_changed,
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([
                    ft.Text("最小化到托盘", size=16),
                    ft.Switch(
                        value=self.viewmodel.get_setting("minimize_to_tray", True),
                        on_change=on_minimize_to_tray_changed,
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(),
                ft.Row([
                    ft.Text("版本信息", size=16),
                    ft.Text("v1.0.0", size=16, color=ft.colors.GREY),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ], spacing=20),
            padding=20
        ) 