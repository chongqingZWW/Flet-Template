import flet as ft
from app.view.base_view import BaseView


class FavoritesView(BaseView):
    """收藏夹视图"""

    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        self.view = self._build_view()

    def _build_view(self):
        return ft.Container(
            content=ft.Column([
                # 标题栏
                ft.Container(
                    content=ft.Row([
                        ft.Text("收藏夹", size=30, weight=ft.FontWeight.BOLD),
                        ft.IconButton(
                            icon=ft.icons.GRID_VIEW,
                            tooltip="切换视图",
                            on_click=lambda _: print("切换视图")
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    margin=ft.margin.only(bottom=20)
                ),

                # 收藏项目网格
                ft.GridView(
                    expand=1,
                    runs_count=5,
                    max_extent=200,
                    child_aspect_ratio=1.0,
                    spacing=10,
                    run_spacing=10,
                    controls=[
                        self._build_favorite_card(
                            f"项目 {i}",
                            "这是一个示例项目的描述...",
                            ft.icons.FOLDER
                        ) for i in range(1, 11)
                    ]
                )
            ]),
            padding=20
        )

    def _build_favorite_card(self, title: str, desc: str, icon: str):
        """构建收藏卡片"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(icon),
                        ft.Text(title, weight=ft.FontWeight.BOLD)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(
                        content=ft.Text(
                            desc,
                            size=12,
                            color=ft.colors.GREY,
                            text_align=ft.TextAlign.CENTER
                        ),
                        margin=ft.margin.symmetric(vertical=10)
                    ),
                    ft.Row([
                        ft.IconButton(
                            icon=ft.icons.STAR,
                            icon_color=ft.colors.YELLOW,
                            tooltip="取消收藏",
                            on_click=lambda _: print("取消收藏")
                        ),
                        ft.IconButton(
                            icon=ft.icons.OPEN_IN_NEW,
                            tooltip="打开",
                            on_click=lambda _: print("打开项目")
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ]),
                padding=10
            )
        ) 