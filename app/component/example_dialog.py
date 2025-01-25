import flet as ft

class ExampleDialog(ft.UserControl):
    """
    示例对话框组件
    演示自定义组件的创建和使用
    """
    def __init__(self, title: str, on_confirm=None):
        super().__init__()
        self.title = title
        self.on_confirm = on_confirm
        self.dialog = None

    def build(self):
        self.name_input = ft.TextField(
            label="名称",
            required=True,
            border=ft.InputBorder.OUTLINE
        )
        
        self.description_input = ft.TextField(
            label="描述",
            multiline=True,
            min_lines=3,
            border=ft.InputBorder.OUTLINE
        )

        self.dialog = ft.AlertDialog(
            title=ft.Text(self.title),
            content=ft.Column([
                self.name_input,
                self.description_input
            ], tight=True),
            actions=[
                ft.TextButton("取消", on_click=self._on_cancel),
                ft.TextButton("确定", on_click=self._on_confirm)
            ]
        )

        return self.dialog

    def _on_cancel(self, e):
        """取消按钮事件"""
        self.dialog.open = False
        self.page.update()

    def _on_confirm(self, e):
        """确定按钮事件"""
        if not self.name_input.value:
            self.name_input.error_text = "请输入名称"
            self.page.update()
            return

        if self.on_confirm:
            self.on_confirm({
                "name": self.name_input.value,
                "description": self.description_input.value
            })
        
        self.dialog.open = False
        self.page.update() 