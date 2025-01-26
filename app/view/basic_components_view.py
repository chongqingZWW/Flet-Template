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
        """按钮示例"""
        return ft.Container(
            content=ft.Column([
                # 按钮类型示例
                self._build_example_section(
                    title="按钮类型",
                    description="Flet 提供了三种基础按钮类型：ElevatedButton（主按钮）、OutlinedButton（次要按钮）和TextButton（文本按钮）。",
                    demo_content=ft.Row([
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
                    code="""
# ElevatedButton 用于主要操作
ft.ElevatedButton(
    text="主按钮",
    icon=ft.icons.SEND,
)

# OutlinedButton 用于次要操作
ft.OutlinedButton(
    text="次要按钮",
    icon=ft.icons.BOOKMARK_BORDER,
)

# TextButton 用于不太重要的操作
ft.TextButton(
    text="文本按钮",
    icon=ft.icons.INFO,
)""",
                    notes=["ElevatedButton：凸起的按钮，用于强调主要操作",
                          "OutlinedButton：带边框的按钮，用于次要操作",
                          "TextButton：文本按钮，用于不太重要的操作"]
                ),

                # 按钮状态示例
                self._build_example_section(
                    title="按钮状态",
                    description="按钮可以有不同的状态：正常、禁用和加载中。",
                    demo_content=ft.Row([
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
                    code="""
# 正常状态
ft.ElevatedButton(
    text="正常按钮",
)

# 禁用状态
ft.ElevatedButton(
    text="禁用按钮",
    disabled=True
)

# 加载状态
ft.ElevatedButton(
    text="加载中",
    icon=ft.ProgressRing(width=16, height=16),
)""",
                    notes=["disabled=True：禁用按钮",
                          "icon=ft.ProgressRing：添加加载动画",
                          "可以通过 on_click 添加点击事件处理"]
                ),
            ], spacing=40),
            padding=20,
        )

    def _build_example_section(self, title: str, description: str, demo_content, code: str, notes: list = None):
        """构建示例区块"""
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
                                content=ft.Column([
                                    ft.Markdown(
                                        f"```python\n{code.strip()}\n```",
                                        selectable=True,
                                        extension_set="gitHubWeb",
                                        code_theme="atom-one-dark",
                                        code_style=ft.TextStyle(
                                            font_family="monospace",
                                            size=14,
                                        ),
                                    ),
                                ]),
                                bgcolor=ft.colors.SURFACE_VARIANT,
                                padding=10,
                                border_radius=5,
                            ),
                        ]),
                        expand=True,
                    ),
                ], spacing=20),

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
                ) if notes else ft.Container(),
            ]),
            bgcolor=ft.colors.SURFACE,
            padding=20,
            border_radius=10,
            border=ft.border.all(1, ft.colors.OUTLINE),
        )

    def _show_code_dialog(self, code: str):
        """显示代码对话框"""
        self.page.dialog = ft.AlertDialog(
            title=ft.Text("示例代码"),
            content=ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Text(
                            code.strip(),
                            selectable=True,
                            font_family="monospace",
                            size=14,
                        ),
                        bgcolor=ft.colors.BLACK,
                        padding=10,
                        border_radius=5,
                    ),
                    ft.Row([
                        ft.TextButton(
                            "复制代码",
                            icon=ft.icons.COPY,
                            on_click=lambda _: self.page.set_clipboard(code.strip())
                        )
                    ], alignment=ft.MainAxisAlignment.END)
                ]),
                width=600,
                padding=20,
            ),
            actions=[
                ft.TextButton("关闭", on_click=lambda _: self.close_dialog()),
            ],
        )
        self.page.dialog.open = True
        self.page.update()

    def close_dialog(self):
        """关闭对话框"""
        self.page.dialog.open = False
        self.page.update()

    def _build_icons_section(self):
        """图标示例"""
        # 常用图标字典，包含中英文描述
        ICONS_MAP = {
            "HOME": {"name": "首页", "icon": ft.icons.HOME},
            "SETTINGS": {"name": "设置", "icon": ft.icons.SETTINGS},
            "PERSON": {"name": "用户", "icon": ft.icons.PERSON},
            "SEARCH": {"name": "搜索", "icon": ft.icons.SEARCH},
            "ADD": {"name": "添加", "icon": ft.icons.ADD},
            "EDIT": {"name": "编辑", "icon": ft.icons.EDIT},
            "DELETE": {"name": "删除", "icon": ft.icons.DELETE},
            "MENU": {"name": "菜单", "icon": ft.icons.MENU},
            "CLOSE": {"name": "关闭", "icon": ft.icons.CLOSE},
            "REFRESH": {"name": "刷新", "icon": ft.icons.REFRESH},
            "DOWNLOAD": {"name": "下载", "icon": ft.icons.DOWNLOAD},
            "UPLOAD": {"name": "上传", "icon": ft.icons.UPLOAD},
            "SHARE": {"name": "分享", "icon": ft.icons.SHARE},
            "FAVORITE": {"name": "收藏", "icon": ft.icons.FAVORITE},
            "STAR": {"name": "星标", "icon": ft.icons.STAR},
            "WARNING": {"name": "警告", "icon": ft.icons.WARNING},
            "INFO": {"name": "信息", "icon": ft.icons.INFO},
            "CHECK_CIRCLE": {"name": "完成", "icon": ft.icons.CHECK_CIRCLE},
            "SEND": {"name": "发送", "icon": ft.icons.SEND},
            "MORE_VERT": {"name": "更多", "icon": ft.icons.MORE_VERT},
            # 添加分页相关图标
            "FIRST_PAGE": {"name": "首页", "icon": ft.icons.FIRST_PAGE},
            "LAST_PAGE": {"name": "末页", "icon": ft.icons.LAST_PAGE},
            "NAVIGATE_BEFORE": {"name": "上一页", "icon": ft.icons.NAVIGATE_BEFORE},
            "NAVIGATE_NEXT": {"name": "下一页", "icon": ft.icons.NAVIGATE_NEXT},
        }

        def create_icon_container(icon_key: str, icon_info: dict):
            """创建图标容器"""
            return ft.Container(
                content=ft.Column([
                    ft.Icon(
                        name=icon_info["icon"],
                        size=32,
                    ),
                    ft.Text(
                        icon_key,
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        icon_info["name"],
                        size=12,
                        color=ft.colors.GREY_700,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5,
                ),
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=10,
                border_radius=10,
                on_click=lambda _, k=icon_key: self._show_icon_details(k, ICONS_MAP[k]["icon"]),
            )

        # 创建图标网格并初始化所有图标
        icons_grid = ft.GridView(
            expand=True,
            max_extent=120,
            spacing=10,
            run_spacing=10,
            padding=20,
            controls=[
                create_icon_container(icon_key, icon_info)
                for icon_key, icon_info in ICONS_MAP.items()
            ]
        )

        def update_icons(e):
            """更新图标显示"""
            if not e or not e.control.value:
                # 显示所有图标
                icons_grid.controls = [
                    create_icon_container(icon_key, icon_info)
                    for icon_key, icon_info in ICONS_MAP.items()
                ]
            else:
                # 根据搜索关键词过滤图标
                keyword = e.control.value.upper()
                icons_grid.controls = [
                    create_icon_container(icon_key, icon_info)
                    for icon_key, icon_info in ICONS_MAP.items()
                    if keyword in icon_key or keyword in icon_info["name"].upper()
                ]
            self.page.update()

        # 搜索框
        search_box = ft.TextField(
            label="搜索图标",
            hint_text="输入图标英文名称或中文描述",
            prefix_icon=ft.icons.SEARCH,
            on_change=update_icons,
            expand=True,
        )

        return ft.Container(
            content=ft.Column([
                # 搜索区域
                ft.Container(
                    content=ft.Column([
                        ft.Text("图标搜索", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("点击图标可查看详细信息和使用方法", size=14, color=ft.colors.GREY_700),
                        search_box,
                    ]),
                    padding=20,
                ),
                # 图标展示区域
                icons_grid,
            ]),
            padding=20,
        )

    def _build_text_section(self):
        """文本示例"""
        return ft.Container(
            content=ft.Column([
                # 基础文本示例
                self._build_example_section(
                    title="基础文本",
                    description="Text 组件用于显示各种样式的文本内容，支持设置大小、颜色、字重等属性。",
                    demo_content=ft.Column([
                        ft.Text("普通文本 - 这是一段基础文本"),
                        ft.Text("大号文本", size=24),
                        ft.Text("带颜色的文本", color=ft.colors.BLUE),
                        ft.Text("粗体文本", weight=ft.FontWeight.BOLD),
                    ], spacing=10),
                    code="""
# 基础文本
ft.Text("普通文本 - 这是一段基础文本")

# 设置文本大小
ft.Text("大号文本", size=24)

# 设置文本颜色
ft.Text("带颜色的文本", color=ft.colors.BLUE)

# 设置文本粗细
ft.Text("粗体文本", weight=ft.FontWeight.BOLD)
""",
                    notes=[
                        "Text 是最基础的文本显示组件",
                        "可以通过 size 属性设置文本大小",
                        "color 属性可以设置文本颜色",
                        "weight 属性控制文本粗细"
                    ]
                ),

                # 文本样式示例
                self._build_example_section(
                    title="文本样式",
                    description="Text 组件支持多种样式装饰，包括下划线、删除线、斜体等。",
                    demo_content=ft.Column([
                        ft.Text("斜体文本", italic=True),
                        ft.Text(
                            "下划线文本",
                            style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                        ),
                        ft.Text(
                            "删除线文本",
                            style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
                        ),
                        ft.Text(
                            "组合样式文本",
                            size=20,
                            color=ft.colors.BLUE,
                            weight=ft.FontWeight.BOLD,
                            italic=True,
                        ),
                    ], spacing=10),
                    code="""
# 斜体文本
ft.Text("斜体文本", italic=True)

# 下划线文本
ft.Text(
    "下划线文本",
    style=ft.TextStyle(
        decoration=ft.TextDecoration.UNDERLINE
    )
)

# 删除线文本
ft.Text(
    "删除线文本",
    style=ft.TextStyle(
        decoration=ft.TextDecoration.LINE_THROUGH
    )
)

# 组合多种样式
ft.Text(
    "组合样式文本",
    size=20,
    color=ft.colors.BLUE,
    weight=ft.FontWeight.BOLD,
    italic=True,
)
""",
                    notes=[
                        "italic=True 设置斜体文本",
                        "使用 TextStyle 设置更复杂的文本装饰",
                        "可以组合多个样式属性",
                        "text_align 属性可以设置文本对齐方式"
                    ]
                ),

                # 文本颜色示例
                self._build_example_section(
                    title="文本颜色",
                    description="Text 组件支持丰富的颜色设置，可以使用预定义颜色或自定义颜色。",
                    demo_content=ft.Column([
                        ft.Text("主要文本", color=ft.colors.PRIMARY),
                        ft.Text("成功文本", color=ft.colors.GREEN),
                        ft.Text("警告文本", color=ft.colors.ORANGE),
                        ft.Text("错误文本", color=ft.colors.RED),
                        ft.Text("自定义颜色", color="#FF6B6B"),
                    ], spacing=10),
                    code="""
# 使用预定义颜色
ft.Text("主要文本", color=ft.colors.PRIMARY)
ft.Text("成功文本", color=ft.colors.GREEN)
ft.Text("警告文本", color=ft.colors.ORANGE)
ft.Text("错误文本", color=ft.colors.RED)

# 使用自定义颜色（十六进制）
ft.Text("自定义颜色", color="#FF6B6B")
""",
                    notes=[
                        "可以使用 ft.colors 中的预定义颜色",
                        "支持十六进制颜色值",
                        "color 属性接受任何有效的颜色表示",
                        "可以通过颜色来表达文本的重要程度或状态"
                    ]
                ),
            ], spacing=40),
            padding=20,
        )

    def _build_image_section(self):
        """图片示例"""
        return ft.Container(
            content=ft.Column([
                # 基础图片示例
                self._build_example_section(
                    title="基础图片",
                    description="Image 组件用于显示图片，支持网络图片和本地图片，可以设置大小、圆角等属性。",
                    demo_content=ft.Row([
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
                    code="""
# 基础图片
ft.Image(
    src="https://example.com/image.jpg",  # 图片URL
    width=150,                            # 宽度
    height=150,                           # 高度
    fit=ft.ImageFit.COVER,               # 填充模式
    border_radius=ft.border_radius.all(8) # 圆角
)

# 圆形图片
ft.Image(
    src="https://example.com/image.jpg",
    width=150,
    height=150,
    fit=ft.ImageFit.CONTAIN,
    border_radius=ft.border_radius.all(75)  # 设置为宽高的一半实现圆形
)""",
                    notes=[
                        "src 支持网络URL和本地文件路径",
                        "fit 属性控制图片如何填充容器",
                        "border_radius 可以设置圆角",
                        "可以通过 width 和 height 控制大小"
                    ]
                ),

                # 图片适应模式示例
                self._build_example_section(
                    title="图片适应模式",
                    description="Image 组件提供了多种适应模式，可以控制图片如何填充指定的空间。",
                    demo_content=ft.Row([
                        ft.Container(
                            content=ft.Column([
                                ft.Text("ImageFit.COVER", size=12),
                                ft.Image(
                                    src="https://picsum.photos/300/200",
                                    width=200,
                                    height=150,
                                    fit=ft.ImageFit.COVER,
                                ),
                            ]),
                            border=ft.border.all(1, ft.colors.GREY_400),
                            border_radius=8,
                            padding=10,
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("ImageFit.CONTAIN", size=12),
                                ft.Image(
                                    src="https://picsum.photos/300/200",
                                    width=200,
                                    height=150,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                            ]),
                            border=ft.border.all(1, ft.colors.GREY_400),
                            border_radius=8,
                            padding=10,
                        ),
                    ], spacing=20),
                    code="""
# COVER 模式：填充整个容器，可能裁剪部分图片
ft.Image(
    src="image.jpg",
    width=200,
    height=150,
    fit=ft.ImageFit.COVER,
)

# CONTAIN 模式：完整显示图片，可能有空白
ft.Image(
    src="image.jpg",
    width=200,
    height=150,
    fit=ft.ImageFit.CONTAIN,
)""",
                    notes=[
                        "COVER：填充整个容器，保持比例，可能裁剪",
                        "CONTAIN：完整显示图片，保持比例，可能有空白",
                        "FILL：拉伸填充，可能变形",
                        "NONE：原始大小，可能超出或不足"
                    ]
                ),

                # 高级用法示例
                self._build_example_section(
                    title="高级用法",
                    description="Image 组件还支持更多高级特性，如加载占位、错误处理、重复平铺等。",
                    demo_content=ft.Column([
                        ft.Row([
                            ft.Image(
                                src="https://picsum.photos/100/100",
                                width=100,
                                height=100,
                                fit=ft.ImageFit.COVER,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                                gapless_playback=True,
                                tooltip="带有提示的图片",
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src="https://picsum.photos/50/50",
                                    width=50,
                                    height=50,
                                    fit=ft.ImageFit.COVER,
                                ),
                                blur=5,  # 添加模糊效果
                                border_radius=25,
                                ink=True,  # 添加水波纹效果
                            ),
                        ], spacing=20),
                    ], spacing=10),
                    code="""
# 带提示的图片
ft.Image(
    src="image.jpg",
    width=100,
    height=100,
    fit=ft.ImageFit.COVER,
    repeat=ft.ImageRepeat.NO_REPEAT,
    gapless_playback=True,  # 平滑切换
    tooltip="带有提示的图片",
)

# 带模糊效果的图片
ft.Container(
    content=ft.Image(
        src="image.jpg",
        width=50,
        height=50,
        fit=ft.ImageFit.COVER,
    ),
    blur=5,               # 模糊效果
    border_radius=25,     # 圆角
    ink=True,            # 水波纹效果
)""",
                    notes=[
                        "gapless_playback：切换图片时平滑过渡",
                        "repeat：控制图片重复方式",
                        "可以结合 Container 实现更多效果",
                        "支持 tooltip 添加提示文本",
                        "可以通过 error_builder 自定义错误显示"
                    ]
                ),
            ], spacing=40),
            padding=20,
        )

    def _build_section_title(self, title: str):
        return ft.Text(title, size=16, weight=ft.FontWeight.BOLD)

    def _show_icon_details(self, icon_key: str, icon: str):
        """显示图标详细信息对话框"""
        code_example = f"""
    # 使用示例
    ft.Icon(
        name={icon},
        size=32,
        color=ft.colors.BLUE,
    )
        """.strip()

        self.page.dialog = ft.AlertDialog(
            title=ft.Text(f"图标详情 - {icon_key}"),
            content=ft.Column([
                ft.Row([
                    ft.Icon(icon, size=48, color=ft.colors.BLUE),
                    ft.Column([
                        ft.Text(f"Material 图标名称：", weight=ft.FontWeight.BOLD),
                        ft.Text(f"{icon}", selectable=True),
                    ], spacing=10),
                ], spacing=20),
                ft.Divider(height=20),
                ft.Row([
                    ft.Text("代码示例：", weight=ft.FontWeight.BOLD),
                    ft.IconButton(
                        icon=ft.icons.COPY,
                        on_click=lambda _: self.page.set_clipboard(code_example)
                    )
                ]),
                ft.Container(
                    ft.Text(code_example, font_family="monospace", selectable=True),
                    padding=10,
                    bgcolor=ft.colors.BLACK12,
                    border_radius=5,
                )
            ], tight=True),
            actions=[
                ft.TextButton("关闭", on_click=lambda _: self.close_dialog()),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        self.page.dialog.open = True
        self.page.update()