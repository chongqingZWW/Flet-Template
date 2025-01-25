import flet as ft
from app.view.base_view import BaseView


class HomeView(BaseView):
    """首页视图"""

    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        self.view = self._build_view()

    def _build_view(self):
        return ft.Container(
            content=ft.Column([
                # 顶部标题
                ft.Container(
                    content=ft.Text("首页", size=30, weight=ft.FontWeight.BOLD),
                    margin=ft.margin.only(bottom=20)
                ),
                
                # 统计卡片行
                ft.Row([
                    self._build_stat_card("总项目", "125", ft.icons.FOLDER),
                    self._build_stat_card("活跃项目", "45", ft.icons.TRENDING_UP),
                    self._build_stat_card("完成项目", "80", ft.icons.DONE_ALL),
                ], spacing=20),

                # 最近活动列表
                ft.Container(
                    content=ft.Column([
                        ft.Text("最近活动", size=20, weight=ft.FontWeight.BOLD),
                        ft.ListView(
                            controls=[
                                self._build_activity_item(
                                    "项目更新",
                                    "项目 A 完成了新版本发布",
                                    "10分钟前"
                                ),
                                self._build_activity_item(
                                    "新建项目",
                                    "创建了新项目 B",
                                    "1小时前"
                                ),
                                self._build_activity_item(
                                    "项目归档",
                                    "项目 C 已归档",
                                    "2小时前"
                                ),
                            ],
                            spacing=10,
                            height=200,
                        )
                    ]),
                    margin=ft.margin.only(top=20)
                ),
            ]),
            padding=20
        )

    def _build_stat_card(self, title: str, value: str, icon: str):
        """构建统计卡片"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(icon, size=30, color=ft.colors.BLUE),
                    ft.Text(value, size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(title, size=14, color=ft.colors.GREY),
                ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                width=150,
                padding=15,
            )
        )

    def _build_activity_item(self, title: str, desc: str, time: str):
        """构建活动列表项"""
        return ft.ListTile(
            leading=ft.CircleAvatar(
                content=ft.Icon(ft.icons.ACCESS_TIME),
                bgcolor=ft.colors.BLUE_100,
            ),
            title=ft.Text(title),
            subtitle=ft.Text(desc),
            trailing=ft.Text(time, size=12, color=ft.colors.GREY),
        ) 