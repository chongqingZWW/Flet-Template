import flet as ft

class CustomAppBar(ft.UserControl):
    """
    自定义AppBar，支持拖拽、最小化、最大化、关闭按钮
    """
    def __init__(self, title: str, bgcolor: str, on_minimize=None, on_maximize=None, on_close=None):
        super().__init__()
        self.title = title
        self.bgcolor = bgcolor
        self.on_minimize = on_minimize
        self.on_maximize = on_maximize
        self.on_close = on_close

    def build(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.GestureDetector(  # 添加拖拽支持
                        mouse_cursor=ft.MouseCursor.MOVE,
                        on_pan_start=self.start_drag,
                        on_pan_update=self.update_drag,
                        content=ft.Text(self.title, expand=True, size=18, text_align="center"),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.REMOVE,
                        tooltip="最小化",
                        on_click=self.on_minimize,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.CROP_SQUARE,
                        tooltip="最大化",
                        on_click=self.on_maximize,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        tooltip="关闭",
                        on_click=self.on_close,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=self.bgcolor,
            height=50,
            padding=ft.Padding(10, 0, 10, 0),
        )

    def start_drag(self, e):
        """开始拖拽"""
        self.page.window.start_drag(e)

    def update_drag(self, e):
        """更新拖拽位置"""
        pass


def main(page: ft.Page):
    """Flet 应用入口"""
    # 隐藏系统标题栏
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True

    # 页面基础配置
    page.title = "微信多开管理"
    page.window.width = 1000
    page.window.height = 700
    page.window.center()

    # 定义按钮回调函数
    def handle_minimize(e):
        page.window.minimized = True  # 系统自带最小化
        print("窗口已最小化")

    def handle_maximize(e):
        if page.window.maximized:
            page.window.restore()
            print("窗口已恢复")
        else:
            page.window.maximized = True
            print("窗口已最大化")

    def handle_close(e):
        print("窗口已关闭")
        page.window.close()

    # 创建自定义 AppBar
    custom_appbar = CustomAppBar(
        title="微信多开管理系统",
        bgcolor=ft.Colors.BLUE_GREY_800,
        on_minimize=handle_minimize,
        on_maximize=handle_maximize,
        on_close=handle_close,
    )

    # 构建页面
    page.add(
        custom_appbar.build(),
        ft.Container(content=ft.Text("这是一个带拖拽的自定义菜单栏！"), expand=True),
    )


# 启动 Flet 应用
if __name__ == "__main__":
    ft.app(target=main)
