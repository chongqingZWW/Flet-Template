import flet as ft
from app.view.base_view import BaseView

class ExampleView(BaseView):
    """
    示例视图
    演示基本的UI组件构建和事件处理
    """
    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        self.items_list = ft.ListView(expand=1, spacing=10, padding=20)
        self.search_box = ft.TextField(
            label="搜索",
            prefix_icon=ft.icons.SEARCH,
            on_change=self._on_search
        )
        self.view = self._build_view()

    def _build_view(self):
        """构建视图"""
        return ft.Container(
            content=ft.Column([
                # 顶部工具栏
                ft.Container(
                    content=ft.Row([
                        self.search_box,
                        ft.IconButton(
                            icon=ft.icons.REFRESH,
                            tooltip="刷新",
                            on_click=self._on_refresh
                        )
                    ]),
                    padding=10
                ),
                # 列表区域
                self.items_list
            ]),
            expand=True
        )

    def _on_search(self, e):
        """搜索事件处理"""
        keyword = self.search_box.value.lower()
        filtered_items = [
            item for item in self.viewmodel.items 
            if keyword in item["name"].lower()
        ]
        self._refresh_list(filtered_items)

    def _on_refresh(self, e):
        """刷新事件处理"""
        self.viewmodel.load_items()

    def _refresh_list(self, items):
        """刷新列表显示"""
        self.items_list.controls.clear()
        
        for item in items:
            self.items_list.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        leading=ft.Icon(ft.icons.ARTICLE),
                        title=ft.Text(item["name"]),
                        subtitle=ft.Text(item["description"] or ""),
                        on_click=lambda x, id=item["id"]: 
                            self.viewmodel.select_item(id)
                    ),
                    border=ft.border.all(1, ft.colors.BLACK12),
                    border_radius=8,
                    padding=5
                )
            )
        
        self.page.update() 