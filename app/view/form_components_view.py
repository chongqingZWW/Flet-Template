import flet as ft
from app.view.base_view import BaseView


class FormComponentsView(BaseView):
    """表单组件示例"""

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
                                text="输入框",
                                content=self._build_textfield_section()
                            ),
                            ft.Tab(
                                text="选择器",
                                content=self._build_selector_section()
                            ),
                            ft.Tab(
                                text="开关",
                                content=self._build_switch_section()
                            ),
                            ft.Tab(
                                text="滑块",
                                content=self._build_slider_section()
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
                ft.Text("表单组件", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Flet 提供的表单组件示例", size=16, color=ft.colors.GREY_700),
            ]),
            margin=ft.margin.only(bottom=20)
        )

    def _build_textfield_section(self):
        """输入框示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("基础输入框"),
                        ft.TextField(
                            label="用户名",
                            hint_text="请输入用户名",
                            prefix_icon=ft.icons.PERSON,
                        ),
                        ft.TextField(
                            label="密码",
                            hint_text="请输入密码",
                            password=True,
                            can_reveal_password=True,
                            prefix_icon=ft.icons.LOCK,
                        ),

                        self._build_section_title("输入框状态"),
                        ft.TextField(
                            label="禁用状态",
                            value="这是禁用状态的输入框",
                            disabled=True,
                        ),
                        ft.TextField(
                            label="错误状态",
                            value="输入有误",
                            error_text="这是一条错误提示",
                        ),

                        self._build_section_title("特殊输入框"),
                        ft.TextField(
                            label="多行文本",
                            hint_text="请输入多行文本",
                            multiline=True,
                            min_lines=3,
                            max_lines=5,
                        ),
                        ft.TextField(
                            label="带计数器",
                            hint_text="最多输入50个字符",
                            max_length=50,
                            counter_text="0/50",
                        ),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_selector_section(self):
        """选择器示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("单选框"),
                        ft.RadioGroup(
                            content=ft.Column([
                                ft.Radio(value="1", label="选项一"),
                                ft.Radio(value="2", label="选项二"),
                                ft.Radio(value="3", label="选项三", disabled=True),
                            ])
                        ),

                        self._build_section_title("复选框"),
                        ft.Column([
                            ft.Checkbox(label="选项一", value=True),
                            ft.Checkbox(label="选项二"),
                            ft.Checkbox(label="选项三", disabled=True),
                        ], spacing=10),

                        self._build_section_title("下拉选择"),
                        ft.Dropdown(
                            label="选择一个选项",
                            hint_text="请选择",
                            options=[
                                ft.dropdown.Option("1", "选项一"),
                                ft.dropdown.Option("2", "选项二"),
                                ft.dropdown.Option("3", "选项三"),
                            ],
                            width=200,
                        ),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_switch_section(self):
        """开关示例"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column([
                        self._build_section_title("基础开关"),
                        ft.Row([
                            ft.Switch(label="默认开关"),
                            ft.Switch(label="选中状态", value=True),
                            ft.Switch(label="禁用状态", disabled=True),
                        ], spacing=20),

                        self._build_section_title("带图标开关"),
                        ft.Row([
                            ft.Switch(
                                label="静音",
                            ),
                            ft.Switch(
                                label="主题",
                            ),
                        ], spacing=20),

                        self._build_section_title("开关颜色"),
                        ft.Row([
                            ft.Switch(
                                label="蓝色开关",
                                active_color=ft.colors.BLUE,
                            ),
                            ft.Switch(
                                label="绿色开关",
                                active_color=ft.colors.GREEN,
                            ),
                            ft.Switch(
                                label="红色开关",
                                active_color=ft.colors.RED,
                            ),
                        ], spacing=20),
                    ], spacing=30),
                    padding=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def _build_slider_section(self):
        """滑块示例"""
        return ft.Container(
            content=ft.Column([
                self._build_section_title("基础滑块"),
                ft.Slider(
                    min=0,
                    max=100,
                    divisions=10,
                    label="{value}",
                ),

                self._build_section_title("带颜色滑块"),
                ft.Slider(
                    min=0,
                    max=100,
                    divisions=10,
                    label="{value}",
                    active_color=ft.colors.GREEN,
                ),

                self._build_section_title("范围滑块"),
                ft.RangeSlider(
                    min=0,
                    max=100,
                    start_value=20,
                    end_value=80,
                    divisions=10,
                    label="{value}",
                ),
            ], spacing=30),
            padding=20,
        )

    def _build_section_title(self, title: str):
        return ft.Text(title, size=16, weight=ft.FontWeight.BOLD) 