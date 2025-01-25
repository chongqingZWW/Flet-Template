import flet as ft
from app.view.base_view import BaseView


class BasicComponentsView(BaseView):
    """基础组件示例"""

    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        self.view = self._build_view()

    def _build_view(self):
        return ft.Container(
            content=ft.Column(
                [
                    self._build_header(),
                    ft.Divider(),
                    ft.Tabs(
                        selected_index=0,
                        animation_duration=300,
                        tabs=[
                            ft.Tab(
                                text="按钮",
                                content=self._build_buttons_section()
                            ),
                            ft.Tab(
                                text="图标",
                                content=self._build_icons_section()
                            ),
                            ft.Tab(
                                text="文本",
                                content=self._build_text_section()
                            ),
                            ft.Tab(
                                text="图片",
                                content=self._build_image_section()
                            ),
                        ],
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            padding=20,
        )

    def _build_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("基础组件", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Flet 提供的基础UI组件示例", size=16, color=ft.colors.GREY_700),
            ]),
            margin=ft.margin.only(bottom=20)
        )

    def _build_buttons_section(self):
        return ft.Container(
            content=ft.Column([
                self._build_section_title("按钮类型"),
                ft.Row([
                    ft.ElevatedButton(
                        text="主按钮",
                        icon=ft.icons.SEND,
                    ),
                    ft.OutlinedButton(
                        text="次要按钮",
                        icon=ft.icons.BOOKMARK_BORDER,
                    ),
                    ft.TextButton(
                        text="文本按钮",
                        icon=ft.icons.INFO,
                    ),
                ], spacing=20),

                self._build_section_title("按钮状态"),
                ft.Row([
                    ft.ElevatedButton(
                        text="正常按钮",
                    ),
                    ft.ElevatedButton(
                        text="禁用按钮",
                        disabled=True
                    ),
                    ft.ElevatedButton(
                        text="加载中",
                        icon=ft.ProgressRing(width=16, height=16),
                    ),
                ], spacing=20),

                self._build_section_title("按钮尺寸"),
                ft.Row([
                    ft.ElevatedButton(
                        text="小型按钮",
                        style=ft.ButtonStyle(
                            padding=ft.padding.all(8),
                        ),
                    ),
                    ft.ElevatedButton(
                        text="中等按钮",
                    ),
                    ft.ElevatedButton(
                        text="大型按钮",
                        style=ft.ButtonStyle(
                            padding=ft.padding.all(20),
                        ),
                    ),
                ], spacing=20),
            ], spacing=30),
            padding=20
        )

    def _build_icons_section(self):
        """图标示例"""
        return ft.Container(
            content=ft.Column([
                self._build_section_title("图标大小"),
                ft.Row([
                    ft.Icon(ft.icons.FAVORITE, size=16),
                    ft.Icon(ft.icons.FAVORITE, size=24),
                    ft.Icon(ft.icons.FAVORITE, size=32),
                    ft.Icon(ft.icons.FAVORITE, size=48),
                ], spacing=20),

                self._build_section_title("图标颜色"),
                ft.Row([
                    ft.Icon(ft.icons.STAR, color=ft.colors.YELLOW),
                    ft.Icon(ft.icons.WARNING, color=ft.colors.RED),
                    ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                    ft.Icon(ft.icons.INFO, color=ft.colors.BLUE),
                ], spacing=20),

                self._build_section_title("常用图标"),
                ft.Row([
                    ft.Icon(name) for name in [
                        ft.icons.HOME,
                        ft.icons.SETTINGS,
                        ft.icons.PERSON,
                        ft.icons.SEARCH,
                        ft.icons.ADD,
                        ft.icons.EDIT,
                        ft.icons.DELETE,
                        ft.icons.MENU,
                    ]
                ], spacing=20, wrap=True),

                ft.Row([
                    ft.Icon(name) for name in [
                        ft.icons.CLOSE,
                        ft.icons.REFRESH,
                        ft.icons.DOWNLOAD,
                        ft.icons.UPLOAD,
                        ft.icons.SHARE,
                        ft.icons.MORE_VERT,
                    ]
                ], spacing=20, wrap=True),
            ], spacing=30, scroll=ft.ScrollMode.AUTO),
            padding=20,
        )

    def _build_text_section(self):
        return ft.Container(
            content=ft.Column([
                self._build_section_title("文本大小"),
                ft.Column([
                    ft.Text("特大文本", size=30),
                    ft.Text("大文本", size=24),
                    ft.Text("中等文本", size=16),
                    ft.Text("小文本", size=12),
                ], spacing=10),

                self._build_section_title("文本样式"),
                ft.Column([
                    ft.Text("粗体文本", weight=ft.FontWeight.BOLD),
                    ft.Text("斜体文本", italic=True),
                    ft.Text(
                        "带下划线文本",
                        style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                    ),
                    ft.Text(
                        "删除线文本",
                        style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
                    ),
                ], spacing=10),

                self._build_section_title("文本颜色"),
                ft.Column([
                    ft.Text("主要文本", color=ft.colors.PRIMARY),
                    ft.Text("成功文本", color=ft.colors.GREEN),
                    ft.Text("警告文本", color=ft.colors.ORANGE),
                    ft.Text("错误文本", color=ft.colors.RED),
                ], spacing=10),
            ], spacing=30),
            padding=20
        )

    def _build_image_section(self):
        return ft.Container(
            content=ft.Column([
                self._build_section_title("图片展示"),
                ft.Row([
                    ft.Image(
                        src="https://picsum.photos/150/150",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(8),
                    ),
                    ft.Image(
                        src="https://picsum.photos/150/150",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN,
                        border_radius=ft.border_radius.all(75),
                    ),
                ], spacing=20),

                self._build_section_title("图片适应"),
                ft.Row([
                    ft.Container(
                        content=ft.Image(
                            src="https://picsum.photos/300/200",
                            fit=ft.ImageFit.COVER,
                        ),
                        width=200,
                        height=150,
                        border_radius=8,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    ),
                    ft.Container(
                        content=ft.Image(
                            src="https://picsum.photos/300/200",
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        width=200,
                        height=150,
                        border_radius=8,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    ),
                ], spacing=20),
            ], spacing=30),
            padding=20
        )

    def _build_section_title(self, title: str):
        return ft.Text(title, size=16, weight=ft.FontWeight.BOLD) 