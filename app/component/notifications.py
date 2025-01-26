import flet as ft


class NotificationManager:
    """
    全局通知管理器，用于显示消息通知
    """

    @staticmethod
    def show_notification(page: ft.Page, message: str, success: bool = True, duration: int = 3000):
        """
        显示通知消息
        :param page: Flet 页面实例
        :param message: 通知内容
        :param success: 是否为成功通知（默认为 True）
        :param duration: 通知显示时间（毫秒）
        """
        color = "green" if success else "red"  # 成功通知为绿色，失败通知为红色
        page.snack_bar = ft.SnackBar(
            content=ft.Text(message, color="white"),
            bgcolor=color,
            duration=duration,
        )
        page.snack_bar.open = True  # 打开通知
        page.update()  # 更新页面
