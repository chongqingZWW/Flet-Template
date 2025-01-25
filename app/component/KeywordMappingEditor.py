import flet as ft


class KeywordMappingEditor(ft.UserControl):
    """关键词映射编辑器组件"""

    def __init__(self, width=600, on_change=None, initial_data=None):
        super().__init__()
        self.width = width
        self.on_change = on_change
        
        # 创建输入框
        self.keyword_input = ft.TextField(
            label="关键词",
            hint_text="请输入触发关键词",
            width=180,  # 减小宽度
            border_radius=8,
            height=45,  # 固定高度
        )

        self.response_input = ft.TextField(
            label="回复内容",
            hint_text="请输入回复内容",
            width=280,  # 减小宽度
            multiline=True,
            min_lines=1,
            max_lines=2,  # 减少最大行数
            border_radius=8,
            height=45,  # 固定高度
        )

        # 添加按钮
        self.add_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE,
            icon_color=ft.colors.BLUE,
            tooltip="添加映射",
            on_click=self.add_mapping
        )

        # 输入区域
        self.input_row = ft.Row(
            controls=[
                self.keyword_input,
                self.response_input,
                self.add_button,
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=5,  # 减小间距
        )

        # 映射列表
        self.mappings_list = ft.ListView(
            spacing=5,  # 减小间距
            height=200,  # 减小高度
            padding=5,
        )

        # 主容器
        self.main_container = ft.Column(
            controls=[
                self.input_row,
                ft.Divider(height=1),  # 减小分割线高度
                self.mappings_list,
            ],
            spacing=5,  # 减小间距
            height=280,  # 固定总高度
        )

        # 存储映射数据
        self.mappings = []
        
        # 如果有初始数据，加载它
        if initial_data:
            self.set_data(initial_data)

    def add_mapping(self, e):
        """添加新的映射"""
        keyword = self.keyword_input.value.strip()
        response = self.response_input.value.strip()

        if not keyword or not response:
            if self.page:
                self.page.show_snack_bar(ft.SnackBar(
                    content=ft.Text("关键词和回复内容不能为空"),
                    show_close_icon=True
                ))
            return

        # 检查重复
        if any(m["keyword"] == keyword for m in self.mappings):
            if self.page:
                self.page.show_snack_bar(ft.SnackBar(
                    content=ft.Text("关键词已存在"),
                    show_close_icon=True
                ))
            return

        # 添加新映射
        self.mappings.append({
            "keyword": keyword,
            "response": response
        })

        # 清空输入框
        self.keyword_input.value = ""
        self.response_input.value = ""

        # 刷新列表
        self._refresh_list()

        # 触发回调
        if self.on_change:
            self.on_change(self.get_data())

    def delete_mapping(self, index):
        """删除映射"""
        self.mappings.pop(index)
        self._refresh_list()
        if self.on_change:
            self.on_change(self.get_data())

    def _refresh_list(self):
        """刷新映射列表"""
        self.mappings_list.controls.clear()
        
        for i, mapping in enumerate(self.mappings):
            self.mappings_list.controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(mapping["keyword"], width=150, size=14),  # 减小字体
                            ft.Text(mapping["response"], expand=True, size=14),  # 减小字体
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color=ft.colors.RED,
                                tooltip="删除",
                                data=i,
                                on_click=lambda e: self.delete_mapping(e.control.data)
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    bgcolor=ft.colors.BLUE_GREY_50,
                    padding=5,  # 减小内边距
                    border_radius=5,  # 减小圆角
                )
            )
        
        self.update()

    def get_data(self):
        """获取当前的映射数据"""
        return {m["keyword"]: m["response"] for m in self.mappings}

    def set_data(self, data: dict):
        """设置映射数据"""
        self.mappings = [
            {"keyword": k, "response": v}
            for k, v in (data or {}).items()  # 处理 data 为 None 的情况
        ]
        self._refresh_list()
        
        # 清空输入框
        self.keyword_input.value = ""
        self.response_input.value = ""
        if self.page:
            self.update()

    def build(self):
        return self.main_container
