import flet as ft
from app.view.base_view import BaseView


class FeedbackComponentsView(BaseView):
    """反馈组件示例"""

    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        self.view = self._build_view()

    def _build_view(self):
        return ft.Container(
            content=ft.Column([
                self._build_header(),
                ft.Divider(),
                ft.Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=[
                        ft.Tab(
                            text="对话框",
                            content=self._build_dialog_section()
                        ),
                        ft.Tab(
                            text="消息提示",
                            content=self._build_snackbar_section()
                        ),
                        ft.Tab(
                            text="横幅",
                            content=self._build_banner_section()
                        ),
                        ft.Tab(
                            text="加载中",
                            content=self._build_loading_section()
                        ),
                    ],
                )
            ]),
            padding=20
        )

    def _build_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("反馈组件", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Flet 提供的反馈组件示例", size=16, color=ft.colors.GREY_700),
            ]),
            margin=ft.margin.only(bottom=20)
        )

    def _build_dialog_section(self):
        """对话框示例"""
        def show_alert_dialog(e):
            self.page.dialog = ft.AlertDialog(
                title=ft.Text("提示"),
                content=ft.Text("这是一个提示对话框"),
                actions=[
                    ft.TextButton("取消"),
                    ft.TextButton("确定"),
                ],
            )
            self.page.dialog.open = True
            self.page.update()

        def show_custom_dialog(e):
            self.page.dialog = ft.AlertDialog(
                title=ft.Text("自定义对话框"),
                content=ft.Container(
                    content=ft.Column([
                        ft.TextField(label="用户名"),
                        ft.TextField(label="密码", password=True),
                    ], tight=True),
                    padding=20,
                ),
                actions=[
                    ft.TextButton("取消"),
                    ft.ElevatedButton("登录"),
                ],
            )
            self.page.dialog.open = True
            self.page.update()

        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础对话框"),
                ft.ElevatedButton(
                    "显示对话框",
                    on_click=show_alert_dialog
                ),

                self._build_section_title("自定义对话框"),
                ft.ElevatedButton(
                    "显示登录对话框",
                    on_click=show_custom_dialog
                ),
            ], spacing=30),
            padding=20,
        )

    def _build_snackbar_section(self):
        """消息提示示例"""
        def show_snackbar(e, message, color=None):
            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(message),
                    action="关闭",
                    bgcolor=color,
                )
            )

        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础消息"),
                ft.Row([
                    ft.ElevatedButton(
                        "普通消息",
                        on_click=lambda e: show_snackbar(e, "这是一条普通消息")
                    ),
                    ft.ElevatedButton(
                        "成功消息",
                        on_click=lambda e: show_snackbar(e, "操作成功！", ft.colors.GREEN)
                    ),
                    ft.ElevatedButton(
                        "错误消息",
                        on_click=lambda e: show_snackbar(e, "操作失败！", ft.colors.RED)
                    ),
                ], spacing=20),
            ], spacing=30),
            padding=20,
        )

    def _build_banner_section(self):
        """横幅示例"""
        def show_banner(e, message, bgcolor=None):
            self.page.banner = ft.Banner(
                bgcolor=bgcolor,
                leading=ft.Icon(ft.icons.INFO),
                content=ft.Text(message),
                actions=[
                    ft.TextButton("忽略"),
                    ft.TextButton("查看"),
                ],
            )
            self.page.banner.open = True
            self.page.update()

        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础横幅"),
                ft.Row([
                    ft.ElevatedButton(
                        "显示提示横幅",
                        on_click=lambda e: show_banner(e, "您有一条新消息")
                    ),
                    ft.ElevatedButton(
                        "显示警告横幅",
                        on_click=lambda e: show_banner(
                            e, "系统将在10分钟后维护", ft.colors.ORANGE_100
                        )
                    ),
                ], spacing=20),
            ], spacing=30),
            padding=20,
        )

    def _build_loading_section(self):
        """加载中示例"""
        return ft.Container(
            content=ft.Column([
                self._build_section_title("加载指示器"),
                ft.Row([
                    ft.ProgressRing(),
                    ft.Text("加载中..."),
                ], spacing=10),

                self._build_section_title("自定义加载"),
                ft.Row([
                    ft.ProgressRing(
                        color=ft.colors.BLUE,
                        stroke_width=4,
                    ),
                    ft.Text(
                        "正在处理...",
                        color=ft.colors.BLUE,
                    ),
                ], spacing=10),

                self._build_section_title("加载按钮"),
                ft.ElevatedButton(
                    "提交",
                    icon=ft.ProgressRing(width=16, height=16),
                    disabled=True,
                ),
            ], spacing=30),
            padding=20,
        )

    def _build_section_title(self, title: str):
        return ft.Text(title, size=16, weight=ft.FontWeight.BOLD) 