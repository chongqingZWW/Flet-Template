import flet as ft
from app.view.base_view import BaseView


class LayoutComponentsView(BaseView):
    """布局组件示例"""

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
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            padding=20,
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
        # 水平布局(Row)示例
        row_demo = ft.Column([
            ft.Row(
                [self._build_demo_box("1"), self._build_demo_box("2"), self._build_demo_box("3")],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
            ),
        ])

        # 垂直布局(Column)示例
        column_demo = ft.Column([
            ft.Column(
                [self._build_demo_box("1"), self._build_demo_box("2"), self._build_demo_box("3")],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
            ),
        ])

        return ft.Column([
            # 水平布局示例
            self._build_example_section(
                title="水平布局 (Row)",
                description="Row 用于水平排列子组件，可以通过下方控制调整布局效果。",
                demo_content=row_demo,
                code="""
# Row 水平布局示例
ft.Row(
    controls=[
        ft.Container(width=80, height=80, content=ft.Text("1")),
        ft.Container(width=80, height=80, content=ft.Text("2")),
        ft.Container(width=80, height=80, content=ft.Text("3")),
    ],
    alignment=ft.MainAxisAlignment.START,  # 主轴对齐方式
    spacing=20,                            # 子组件间距
)""",
                notes=[
                    "alignment: 控制主轴(水平)方向的对齐方式",
                    "spacing: 控制子组件之间的间距",
                    "vertical_alignment: 控制交叉轴(垂直)方向的对齐",
                    "wrap: 设置为True时允许换行",
                ]
            ),

            # 垂直布局示例
            self._build_example_section(
                title="垂直布局 (Column)",
                description="Column 用于垂直排列子组件，可以通过下方控制调整布局效果。",
                demo_content=column_demo,
                code="""
# Column 垂直布局示例
ft.Column(
    controls=[
        ft.Container(width=80, height=80, content=ft.Text("1")),
        ft.Container(width=80, height=80, content=ft.Text("2")),
        ft.Container(width=80, height=80, content=ft.Text("3")),
    ],
    alignment=ft.MainAxisAlignment.START,  # 主轴对齐方式
    spacing=20,                            # 子组件间距
)""",
                notes=[
                    "alignment: 控制主轴(垂直)方向的对齐方式",
                    "spacing: 控制子组件之间的间距",
                    "horizontal_alignment: 控制交叉轴(水平)方向的对齐",
                    "expand: 设置为True时填充可用空间",
                ]
            ),
        ], spacing=40)

    def _build_container_section(self):
        """Container容器示例"""
        return ft.Column([
            # 基础容器示例
            self._build_example_section(
                title="基础容器",
                description="Container 是一个多功能的容器组件,可以设置内边距、外边距、背景色、边框等样式。",
                demo_content=ft.Column([
                    ft.Row([
                        ft.Container(
                            content=ft.Text("基础容器"),
                            bgcolor=ft.colors.BLUE_100,
                            padding=20,
                            tooltip="基础容器示例",
                        ),
                        ft.Container(
                            content=ft.Text("带边框容器"),
                            border=ft.border.all(2, ft.colors.BLUE),
                            border_radius=10,
                            padding=20,
                            tooltip="带边框的容器示例",
                        ),
                    ], spacing=20),
                ]),
                code="""
# 基础容器
ft.Container(
    content=ft.Text("基础容器"),
    bgcolor=ft.colors.BLUE_100,
    padding=20,
)

# 带边框容器
ft.Container(
    content=ft.Text("带边框容器"),
    border=ft.border.all(2, ft.colors.BLUE),
    border_radius=10,
    padding=20,
)""",
                notes=[
                    "content: 容器的内容",
                    "padding: 内边距",
                    "margin: 外边距",
                    "bgcolor: 背景颜色",
                    "border: 边框",
                    "border_radius: 圆角"
                ]
            ),

            # 渐变背景示例
            self._build_example_section(
                title="渐变背景",
                description="Container 支持线性渐变和径向渐变背景。",
                demo_content=ft.Column([
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
                            tooltip="线性渐变示例",
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
                            tooltip="径向渐变示例",
                        ),
                    ], spacing=20),
                ]),
                code="""
# 线性渐变
ft.Container(
    content=ft.Text("线性渐变", color=ft.colors.WHITE),
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_left,
        end=ft.alignment.bottom_right,
        colors=[ft.colors.BLUE, ft.colors.GREEN],
    ),
    padding=20,
    border_radius=10,
)

# 径向渐变
ft.Container(
    content=ft.Text("径向渐变", color=ft.colors.WHITE),
    gradient=ft.RadialGradient(
        center=ft.alignment.center,
        radius=1.0,
        colors=[ft.colors.YELLOW, ft.colors.RED],
    ),
    padding=20,
    border_radius=10,
)""",
                notes=[
                    "LinearGradient: 线性渐变,可设置起点和终点",
                    "RadialGradient: 径向渐变,可设置中心点和半径",
                    "colors: 渐变的颜色列表",
                    "可以通过 begin/end 或 center 控制渐变方向"
                ]
            ),

            # 阴影和变换示例
            self._build_example_section(
                title="阴影和变换",
                description="Container 支持阴影效果和各种变换。",
                demo_content=ft.Column([
                    ft.Row([
                        ft.Container(
                            content=ft.Text("阴影效果"),
                            bgcolor=ft.colors.WHITE,
                            padding=20,
                            border_radius=10,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=10,
                                color=ft.colors.BLACK45,
                            ),
                            tooltip="带阴影的容器",
                        ),
                        ft.Container(
                            content=ft.Text("旋转45度"),
                            bgcolor=ft.colors.ORANGE_100,
                            padding=20,
                            border_radius=10,
                            rotate=ft.transform.Rotate(45, alignment=ft.alignment.center),
                            tooltip="旋转的容器",
                        ),
                        ft.Container(
                            content=ft.Text("缩放1.2倍"),
                            bgcolor=ft.colors.GREEN_100,
                            padding=20,
                            border_radius=10,
                            scale=ft.transform.Scale(scale=1.2),
                            animate_scale=300,
                            tooltip="缩放的容器(悬停时)",
                            on_hover=lambda e: self._update_container_scale(e.control, e.data),
                        ),
                    ], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
                ]),
                code="""
# 阴影效果
ft.Container(
    content=ft.Text("阴影效果"),
    bgcolor=ft.colors.WHITE,
    padding=20,
    border_radius=10,
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=10,
        color=ft.colors.BLACK45,
    ),
)

# 旋转效果
ft.Container(
    content=ft.Text("旋转45度"),
    bgcolor=ft.colors.ORANGE_100,
    padding=20,
    border_radius=10,
    rotate=ft.transform.Rotate(45, alignment=ft.alignment.center),
)

# 缩放效果
ft.Container(
    content=ft.Text("缩放1.2倍"),
    bgcolor=ft.colors.GREEN_100,
    padding=20,
    border_radius=10,
    scale=ft.transform.Scale(scale=1.2),
    animate_scale=300,  # 动画持续时间(毫秒)
)""",
                notes=[
                    "shadow: 设置阴影效果",
                    "rotate: 旋转变换",
                    "scale: 缩放变换",
                    "可以添加 animate_ 前缀实现动画效果",
                    "支持组合多种变换效果"
                ]
            ),
        ], spacing=40)

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

    def _build_demo_box(self, text="", size=80):
        """创建演示用的盒子"""
        return ft.Container(
            content=ft.Text(text, size=12, text_align=ft.TextAlign.CENTER),
            width=size,
            height=size,
            bgcolor=ft.colors.BLUE_100,
            border_radius=5,
            alignment=ft.alignment.center,
            tooltip=f"大小: {size}x{size}",
        )

    def _build_example_section(self, title: str, description: str, demo_content: ft.Column, code: str, notes: list):
        """构建示例区块"""
        # 获取实际的布局控件 (Row 或 Column)
        layout_control = demo_content.controls[0]  # Row 或 Column 直接就是第一个控件
        
        return ft.Container(
            content=ft.Column([
                # 标题和描述
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
                ft.Text(description, size=14, color=ft.colors.GREY_700),
                ft.Divider(height=20, thickness=1),

                # 示例和代码并排
                ft.Row([
                    # 左侧：示例展示
                    ft.Container(
                        content=ft.Column([
                            ft.Text("示例展示", size=14, weight=ft.FontWeight.BOLD),
                            ft.Container(
                                content=demo_content,
                                padding=20,
                                bgcolor=ft.colors.SURFACE_VARIANT,
                                border_radius=10,
                            ),
                        ]),
                        expand=True,
                    ),
                    # 右侧：代码展示
                    ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Text("示例代码", size=14, weight=ft.FontWeight.BOLD),
                                ft.IconButton(
                                    icon=ft.icons.COPY,
                                    tooltip="复制代码",
                                    on_click=lambda _: self.page.set_clipboard(code.strip())
                                ),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.Container(
                                content=ft.Markdown(
                                    f"```python\n{code.strip()}\n```",
                                    selectable=True,
                                    extension_set="gitHubWeb",
                                    code_theme="atom-one-dark",
                                    code_style=ft.TextStyle(
                                        font_family="monospace",
                                        size=14,
                                    ),
                                ),
                                bgcolor=ft.colors.SURFACE_VARIANT,
                                padding=10,
                                border_radius=5,
                            ),
                        ]),
                        expand=True,
                    ),
                ], spacing=20),

                # 交互控制区
                ft.Container(
                    content=ft.Column([
                        ft.Text("布局调整", size=14, weight=ft.FontWeight.BOLD),
                        ft.Row([
                            ft.Text("间距 (spacing):", size=12),
                            ft.Slider(
                                min=0,
                                max=50,
                                value=layout_control.spacing,
                                label="{value}",
                                width=200,
                                on_change=lambda e: self._update_demo_spacing(layout_control, e.control.value),
                            ),
                        ]),
                        ft.Row([
                            ft.Text("对齐方式:", size=12),
                            ft.Dropdown(
                                options=[
                                    ft.dropdown.Option("START", "靠左/顶对齐"),
                                    ft.dropdown.Option("CENTER", "居中对齐"),
                                    ft.dropdown.Option("END", "靠右/底对齐"),
                                    ft.dropdown.Option("SPACE_BETWEEN", "两端对齐"),
                                ],
                                value=str(layout_control.alignment).split('.')[-1],
                                width=200,
                                on_change=lambda e: self._update_demo_alignment(layout_control, e.control.value),
                            ),
                        ]),
                    ]),
                    padding=20,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    border_radius=10,
                ),

                # 注意事项
                ft.Container(
                    content=ft.Column([
                        ft.Text("注意事项：", size=14, weight=ft.FontWeight.BOLD),
                        ft.Column([
                            ft.Row([
                                ft.Icon(ft.icons.ARROW_RIGHT, size=16, color=ft.colors.BLUE),
                                ft.Text(note, size=14),
                            ]) for note in (notes or [])
                        ], spacing=10),
                    ]),
                    padding=ft.padding.only(top=20),
                ),
            ]),
            bgcolor=ft.colors.SURFACE,
            padding=20,
            border_radius=10,
            border=ft.border.all(1, ft.colors.OUTLINE),
        )

    def _update_demo_spacing(self, layout_control, value):
        """更新示例间距"""
        layout_control.spacing = value
        self.page.update()

    def _update_demo_alignment(self, layout_control, value):
        """更新示例对齐方式"""
        layout_control.alignment = getattr(ft.MainAxisAlignment, value)
        self.page.update()

    def _update_container_scale(self, container, hover):
        """更新容器缩放"""
        container.scale = ft.transform.Scale(scale=1.2 if hover else 1.0)
        self.page.update() 