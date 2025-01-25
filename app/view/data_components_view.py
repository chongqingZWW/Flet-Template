import flet as ft
from app.view.base_view import BaseView


class DataComponentsView(BaseView):
    """数据展示组件示例"""

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
                                text="表格",
                                content=self._build_table_section()
                            ),
                            ft.Tab(
                                text="数据表格",
                                content=self._build_datatable_section()
                            ),
                            ft.Tab(
                                text="卡片",
                                content=self._build_card_section()
                            ),
                            ft.Tab(
                                text="进度指示器",
                                content=self._build_progress_section()
                            ),
                        ],
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            padding=20
        )

    def _build_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("数据展示组件", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Flet 提供的数据展示组件示例", size=16, color=ft.colors.GREY_700),
            ]),
            margin=ft.margin.only(bottom=20)
        )

    def _build_table_section(self):
        """基础表格示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("基础表格"),
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("ID")),
                                ft.DataColumn(ft.Text("名称")),
                                ft.DataColumn(ft.Text("状态")),
                                ft.DataColumn(ft.Text("操作")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(f"{i}")),
                                        ft.DataCell(ft.Text(f"项目 {i}")),
                                        ft.DataCell(ft.Text("进行中" if i % 2 == 0 else "已完成")),
                                        ft.DataCell(
                                            ft.Row([
                                                ft.IconButton(ft.icons.EDIT),
                                                ft.IconButton(ft.icons.DELETE),
                                            ])
                                        ),
                                    ],
                                ) for i in range(1, 6)
                            ],
                        ),

                        self._build_section_title("带边框表格"),
                        ft.DataTable(
                            border=ft.border.all(1, ft.colors.GREY_400),
                            border_radius=10,
                            vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_400),
                            horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_400),
                            columns=[
                                ft.DataColumn(ft.Text("产品")),
                                ft.DataColumn(ft.Text("价格"), numeric=True),
                                ft.DataColumn(ft.Text("数量"), numeric=True),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("商品 A")),
                                        ft.DataCell(ft.Text("¥100")),
                                        ft.DataCell(ft.Text("50")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("商品 B")),
                                        ft.DataCell(ft.Text("¥200")),
                                        ft.DataCell(ft.Text("30")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("商品 C")),
                                        ft.DataCell(ft.Text("¥150")),
                                        ft.DataCell(ft.Text("40")),
                                    ],
                                ),
                            ],
                        ),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_datatable_section(self):
        """高级数据表格示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("可选择表格"),
                        ft.DataTable(
                            show_checkbox_column=True,
                            columns=[
                                ft.DataColumn(ft.Text("用户名")),
                                ft.DataColumn(ft.Text("邮箱")),
                                ft.DataColumn(ft.Text("角色")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("用户1")),
                                        ft.DataCell(ft.Text("user1@example.com")),
                                        ft.DataCell(ft.Text("管理员")),
                                    ],
                                    selected=True,
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("用户2")),
                                        ft.DataCell(ft.Text("user2@example.com")),
                                        ft.DataCell(ft.Text("普通用户")),
                                    ],
                                ),
                            ],
                        ),

                        self._build_section_title("可排序表格"),
                        ft.DataTable(
                            sort_column_index=0,
                            sort_ascending=True,
                            columns=[
                                ft.DataColumn(ft.Text("文件名"), on_sort=lambda e: print("排序")),
                                ft.DataColumn(ft.Text("大小"), numeric=True),
                                ft.DataColumn(ft.Text("修改日期")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("文档.docx")),
                                        ft.DataCell(ft.Text("1.2MB")),
                                        ft.DataCell(ft.Text("2024-01-01")),
                                    ],
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("图片.jpg")),
                                        ft.DataCell(ft.Text("2.5MB")),
                                        ft.DataCell(ft.Text("2024-01-02")),
                                    ],
                                ),
                            ],
                        ),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_card_section(self):
        """卡片示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("基础卡片"),
                        ft.Row([
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column([
                                        ft.Text("标题", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("这是一段描述文本"),
                                    ]),
                                    padding=15,
                                    width=200,
                                )
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column([
                                        ft.ListTile(
                                            leading=ft.Icon(ft.icons.ALBUM),
                                            title=ft.Text("标题"),
                                            subtitle=ft.Text("副标题"),
                                        ),
                                        ft.Row([
                                            ft.TextButton("取消"),
                                            ft.TextButton("确定"),
                                        ], alignment=ft.MainAxisAlignment.END),
                                    ]),
                                    width=250,
                                )
                            ),
                        ], spacing=20),

                        self._build_section_title("图片卡片"),
                        ft.Row([
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column([
                                        ft.Image(
                                            src="https://picsum.photos/200/100",
                                            width=200,
                                            height=100,
                                            fit=ft.ImageFit.COVER,
                                        ),
                                        ft.Container(
                                            content=ft.Column([
                                                ft.Text("图片标题"),
                                                ft.Text("图片描述", size=12, color=ft.colors.GREY_700),
                                            ]),
                                            padding=10,
                                        ),
                                    ]),
                                ),
                            ),
                        ]),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_progress_section(self):
        """进度指示器示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("进度条"),
                        ft.ProgressBar(value=0.5, width=400),
                        ft.ProgressBar(
                            value=0.7,
                            color=ft.colors.GREEN,
                            bgcolor=ft.colors.GREEN_100,
                            width=400,
                        ),

                        self._build_section_title("环形进度"),
                        ft.Row([
                            ft.ProgressRing(value=0.3),
                            ft.ProgressRing(
                                value=0.6,
                                color=ft.colors.BLUE,
                                bgcolor=ft.colors.BLUE_100,
                            ),
                            ft.ProgressRing(
                                value=0.9,
                                color=ft.colors.GREEN,
                                bgcolor=ft.colors.GREEN_100,
                                stroke_width=8,
                            ),
                        ], spacing=20),

                        self._build_section_title("不确定进度"),
                        ft.Row([
                            ft.ProgressBar(width=200),
                            ft.ProgressRing(),
                        ], spacing=20),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_section_title(self, title: str):
        return ft.Text(title, size=16, weight=ft.FontWeight.BOLD) 