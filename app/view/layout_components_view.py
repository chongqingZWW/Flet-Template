import flet as ft
from app.view.base_view import BaseView


class LayoutComponentsView(BaseView):
    """布局组件示例"""

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
                            text="Row & Column",
                            content=self._build_row_column_section()
                        ),
                        ft.Tab(
                            text="Container",
                            content=self._build_container_section()
                        ),
                        ft.Tab(
                            text="Stack",
                            content=self._build_stack_section()
                        ),
                        ft.Tab(
                            text="GridView",
                            content=self._build_grid_section()
                        ),
                        ft.Tab(
                            text="ListView",
                            content=self._build_list_section()
                        ),
                    ],
                )
            ]),
            padding=20
        )

    def _build_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("布局组件", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Flet 提供的布局组件示例", size=16, color=ft.colors.GREY_700),
            ]),
            margin=ft.margin.only(bottom=20)
        )

    def _build_row_column_section(self):
        """Row和Column布局示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("Row 水平布局"),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("MainAxisAlignment.START", size=14),
                                ft.Row(
                                    [self._build_demo_box() for _ in range(3)],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.Text("MainAxisAlignment.CENTER", size=14),
                                ft.Row(
                                    [self._build_demo_box() for _ in range(3)],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Text("MainAxisAlignment.END", size=14),
                                ft.Row(
                                    [self._build_demo_box() for _ in range(3)],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                                ft.Text("MainAxisAlignment.SPACE_BETWEEN", size=14),
                                ft.Row(
                                    [self._build_demo_box() for _ in range(3)],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ], spacing=20),
                            bgcolor=ft.colors.BLACK12,
                            padding=20,
                        ),

                        self._build_section_title("Column 垂直布局"),
                        ft.Row([
                            ft.Container(
                                content=ft.Column(
                                    [self._build_demo_box(size=50) for _ in range(3)],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                bgcolor=ft.colors.BLACK12,
                                padding=20,
                                width=200,
                                height=300,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    [self._build_demo_box(size=50) for _ in range(3)],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor=ft.colors.BLACK12,
                                padding=20,
                                width=200,
                                height=300,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    [self._build_demo_box(size=50) for _ in range(3)],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                                bgcolor=ft.colors.BLACK12,
                                padding=20,
                                width=200,
                                height=300,
                            ),
                        ], spacing=20),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_container_section(self):
        """Container容器示例"""
        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础容器"),
                ft.Row([
                    ft.Container(
                        content=ft.Text("基础容器"),
                        bgcolor=ft.colors.BLUE_100,
                        padding=20,
                    ),
                    ft.Container(
                        content=ft.Text("带边框容器"),
                        border=ft.border.all(2, ft.colors.BLUE),
                        border_radius=10,
                        padding=20,
                    ),
                ], spacing=20),

                self._build_section_title("渐变背景"),
                ft.Row([
                    ft.Container(
                        content=ft.Text("线性渐变", color=ft.colors.WHITE),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=[ft.colors.BLUE, ft.colors.GREEN],
                        ),
                        padding=20,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Text("径向渐变", color=ft.colors.WHITE),
                        gradient=ft.RadialGradient(
                            center=ft.alignment.center,
                            radius=1.0,
                            colors=[ft.colors.YELLOW, ft.colors.RED],
                        ),
                        padding=20,
                        border_radius=10,
                    ),
                ], spacing=20),

                self._build_section_title("阴影效果"),
                ft.Container(
                    content=ft.Text("带阴影的容器"),
                    bgcolor=ft.colors.WHITE,
                    padding=20,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=10,
                        color=ft.colors.BLACK45,
                    ),
                ),
            ], spacing=30),
            padding=20,
        )

    def _build_stack_section(self):
        """Stack堆叠布局示例"""
        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础堆叠"),
                ft.Stack(
                    [
                        ft.Container(
                            bgcolor=ft.colors.BLUE_100,
                            width=300,
                            height=300,
                        ),
                        ft.Container(
                            bgcolor=ft.colors.RED_100,
                            width=200,
                            height=200,
                            left=50,
                            top=50,
                        ),
                        ft.Container(
                            bgcolor=ft.colors.GREEN_100,
                            width=100,
                            height=100,
                            left=100,
                            top=100,
                        ),
                    ],
                    width=300,
                    height=300,
                ),

                self._build_section_title("卡片堆叠"),
                ft.Stack(
                    [
                        ft.Container(
                            bgcolor=ft.colors.SURFACE,
                            border_radius=10,
                            padding=20,
                            width=300,
                            height=200,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=10,
                                color=ft.colors.BLACK45,
                            ),
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("标题", size=20, weight=ft.FontWeight.BOLD),
                                ft.Text("这是一段描述文本"),
                            ]),
                            padding=30,
                        ),
                        ft.Container(
                            content=ft.Icon(ft.icons.FAVORITE, color=ft.colors.RED),
                            alignment=ft.alignment.top_right,
                            padding=10,
                        ),
                    ],
                    width=300,
                    height=200,
                ),
            ], spacing=30),
            padding=20,
        )

    def _build_grid_section(self):
        """GridView网格布局示例"""
        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础网格"),
                ft.GridView(
                    expand=1,
                    runs_count=5,
                    max_extent=150,
                    child_aspect_ratio=1,
                    spacing=10,
                    run_spacing=10,
                    controls=[
                        ft.Container(
                            content=ft.Text(f"项目 {i}"),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLUE_100,
                            border_radius=5,
                        ) for i in range(1, 21)
                    ]
                ),
            ], spacing=30),
            padding=20,
            height=400,
        )

    def _build_list_section(self):
        """ListView列表布局示例"""
        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础列表"),
                ft.ListView(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.STAR),
                            title=ft.Text(f"列表项 {i}"),
                            subtitle=ft.Text(f"这是列表项 {i} 的描述"),
                            trailing=ft.Icon(ft.icons.ARROW_RIGHT),
                        ) for i in range(1, 11)
                    ],
                    spacing=2,
                    padding=20,
                    height=400,
                ),
            ], spacing=30),
            padding=20,
        )

    def _build_section_title(self, title: str):
        return ft.Text(title, size=16, weight=ft.FontWeight.BOLD)

    def _build_demo_box(self, size=80):
        return ft.Container(
            width=size,
            height=size,
            bgcolor=ft.colors.BLUE_100,
            border_radius=5,
            alignment=ft.alignment.center,
            content=ft.Text(str(size)),
        ) 