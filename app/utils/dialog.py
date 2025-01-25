from flet.core.types import FontWeight
import flet as ft

def show_confirm_dialog(
    page: ft.Page,
    title: str,
    message: str,
    on_confirm,
    title_size: int = 16,
    message_size: int = 14,
    button_height: int = 40,
    button_radius: int = 5,
    dialog_radius: int = 8,
    cancel_color: str = "lightgray",
    confirm_color: str = "blue",
    confirm_text_color: str = "white",
):
    """
    显示美化后的确认弹窗
    :param page: Flet 页面实例
    :param title: 弹窗标题
    :param message: 弹窗内容
    :param on_confirm: 确认按钮的回调函数
    :param title_size: 标题字体大小（默认 16）
    :param message_size: 内容字体大小（默认 14）
    :param button_height: 按钮高度（默认 40）
    :param button_radius: 按钮圆角半径（默认 5）
    :param dialog_radius: 弹窗圆角半径（默认 8）
    :param cancel_color: 取消按钮颜色（默认 lightgray）
    :param confirm_color: 确认按钮颜色（默认 blue）
    :param confirm_text_color: 确认按钮文字颜色（默认 white）
    """
    dialog = ft.AlertDialog(
        title=ft.Text(
            title,
            size=title_size,
            weight=ft.FontWeight.BOLD,
            color="black",
        ),
        content=ft.Text(
            message,
            size=message_size,
            color="gray",
            text_align=ft.TextAlign.CENTER,
        ),
        actions=[
            ft.Row(
                [
                    ft.ElevatedButton(
                        "取消",
                        height=button_height,
                        style=ft.ButtonStyle(
                            bgcolor=cancel_color,
                            shape=ft.RoundedRectangleBorder(radius=button_radius),
                        ),
                        on_click=lambda e: (setattr(dialog, 'open', False), page.update()),
                    ),
                    ft.ElevatedButton(
                        "确认",
                        height=button_height,
                        style=ft.ButtonStyle(
                            bgcolor=confirm_color,
                            color=confirm_text_color,
                            shape=ft.RoundedRectangleBorder(radius=button_radius),
                        ),
                        on_click=lambda e: (setattr(dialog, 'open', False), page.update(), on_confirm(e)),
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=10,
            )
        ],
        modal=True,
        bgcolor="white",
        shape=ft.RoundedRectangleBorder(radius=dialog_radius),
        elevation=3,
    )
    page.dialog = dialog
    dialog.open = True
    page.update()


def show_warning_dialog(page: ft.Page, title: str, message: str):
    """
    显示警告提示弹窗
    :param page: Flet 页面实例
    :param title: 弹窗标题
    :param message: 弹窗内容
    """
    dialog = ft.AlertDialog(
        title=ft.Text(title, weight=FontWeight.BOLD),  # 修正 weight 的类型
        content=ft.Text(message),
        actions=[
            ft.TextButton(
                "确定",
                on_click=lambda e: (setattr(dialog, 'open', False), page.update())
            ),
        ],
        modal=True,
    )
    page.dialog = dialog
    dialog.open = True  # 打开弹窗
    page.update()  # 更新页面以显示弹窗
