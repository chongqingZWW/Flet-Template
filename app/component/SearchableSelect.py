import flet as ft


class SearchableSelect(ft.UserControl):
    def __init__(
            self,
            options,
            placeholder="请选择",
            on_select=None,
            width=250,
            dropdown_height=200,
    ):
        """
        自定义搜索下拉组件（带图标，圆角，小尺寸美观）
        :param options: 选项数据 [{"key": "value1", "text": "显示文本1"}, ...]
        :param placeholder: 输入框的占位文本
        :param on_select: 选中某一项时的回调函数
        :param width: 下拉组件的整体宽度
        :param dropdown_height: 下拉框最大高度
        """
        super().__init__()
        self.options = options  # 全部选项数据
        self.filtered_options = options  # 搜索过滤后的选项
        self.on_select = on_select  # 用户选择后的回调
        self.dropdown_open = False  # 下拉框是否展开
        self.width = width
        self.dropdown_height = dropdown_height  # 设置下拉框最大高度
        self.value = None  # 当前选中的值
        self._pending_options = None  # 用于存储待更新的选项

        # 输入框 (点击后展开/关闭下拉列表)
        self.input_field = ft.TextField(
            hint_text=placeholder,
            read_only=True,
            border_radius=15,
            content_padding=ft.padding.all(10),
            text_style=ft.TextStyle(size=14),
            expand=True,
            suffix_icon=ft.icons.ARROW_DROP_DOWN,  # 在右侧显示一个下拉箭头图标
            on_click=self.toggle_dropdown,
        )

        # 搜索框（展开后出现在面板顶端）
        self.search_field = ft.TextField(
            hint_text="输入搜索内容...",
            prefix_icon=ft.icons.SEARCH,  # 搜索图标
            border_radius=15,
            content_padding=ft.padding.all(10),
            text_style=ft.TextStyle(size=14),
            on_change=self.filter_options,
        )

        # 下拉结果列表
        self.results_list = ft.ListView(
            spacing=5,
            padding=0,
            auto_scroll=False,  # 禁止自动滚动
            height=self.dropdown_height,  # 限制列表高度
        )

        # 下拉框容器（搜索框 + 列表）
        self.dropdown_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.search_field,
                    self.results_list,
                ],
                spacing=5,
            ),
            visible=False,
            border_radius=15,
            bgcolor=ft.colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=4, color="#CCCCCC"),
            width=self.width,
            padding=ft.padding.symmetric(horizontal=8, vertical=8),
        )

    def did_mount(self):
        """当组件被添加到页面时调用"""
        # 如果有待更新的选项，现在更新它们
        if self._pending_options is not None:
            self._do_update_options(self._pending_options)
            self._pending_options = None

    def _do_update_options(self, new_options):
        """实际执行更新选项的操作"""
        self.options = new_options
        self.filtered_options = new_options
        self.input_field.value = ""
        self.value = None
        if self.page:  # 只在组件已添加到页面时更新
            self.update_dropdown_options(new_options)
            self.input_field.update()
            self.dropdown_container.update()
            self.update()

    def update_options(self, new_options):
        """更新选项并强制刷新"""
        if not self.page:  # 如果组件还未添加到页面
            self._pending_options = new_options  # 存储待更新的选项
        else:
            self._do_update_options(new_options)  # 直接更新

    def toggle_dropdown(self, e):
        """展开或关闭下拉框"""
        self.dropdown_open = not self.dropdown_open
        self.dropdown_container.visible = self.dropdown_open
        if self.dropdown_open:
            # 每次展开时，都刷新一下列表
            self.update_dropdown_options(self.filtered_options)
            # 清空搜索框
            self.search_field.value = ""
            self.search_field.update()
        self.update()

    def filter_options(self, e):
        """根据搜索框的输入过滤选项"""
        query = e.control.value.strip().lower()
        self.filtered_options = [
            opt for opt in self.options if query in opt["text"].lower()
        ]
        self.update_dropdown_options(self.filtered_options)

    def update_dropdown_options(self, options):
        """更新下拉结果列表"""
        if not self.page:  # 如果组件还未添加到页面，直接返回
            return

        self.results_list.controls.clear()
        if not options:
            # 若无匹配项，可显示一个提示
            self.results_list.controls.append(
                ft.Text("无匹配项", size=14, color=ft.colors.GREY_600)
            )
        else:
            for opt in options:
                self.results_list.controls.append(
                    ft.Container(
                        content=ft.TextButton(
                            text=opt["text"],
                            on_click=lambda e, key=opt["key"], text=opt["text"]: self.select_option(key, text),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                padding=ft.padding.symmetric(horizontal=6, vertical=8),
                            )
                        ),
                        border_radius=10,
                    )
                )
        if self.page:  # 只在组件已添加到页面时更新
            self.results_list.update()

    def select_option(self, key, text):
        """处理用户选择的选项"""
        self.input_field.value = text
        self.value = key
        self.dropdown_open = False
        self.dropdown_container.visible = False
        self.update()
        if self.on_select:
            self.on_select({"key": key, "text": text})

    def build(self):
        """构建组件"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=self.input_field,
                    border_radius=15,
                    bgcolor=ft.colors.WHITE,
                    padding=0,
                    width=self.width,
                ),
                self.dropdown_container,
            ],
            spacing=5,
        )
