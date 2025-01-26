import flet as ft

from app.component.ThemeManager import ThemeManager
from app.component.notifications import NotificationManager


class SystemSettingsDialog:
    """系统设置弹窗，包含动态配置加载和保存功能"""

    def __init__(self, page: ft.Page, view_model):
        """
        :param page: Flet 页面实例
        :param view_model: 系统配置的视图模型（SystemConfigViewModel 实例）
        """
        self.page = page
        self.view_model = view_model
        self.dialog = None
        self.form_controls = {}
        self.theme_manager = ThemeManager()  # 初始化 ThemeManager

    def show(self):
        """显示系统设置弹窗"""
        # 加载配置数据
        settings_data = self.view_model.load_configs()

        # 构建弹窗内容
        settings_content = self._build_settings_content(settings_data)

        # 创建 AlertDialog
        self.dialog = ft.AlertDialog(
            title=ft.Text("系统设置", size=18, weight=ft.FontWeight.BOLD),
            content=settings_content,
            on_dismiss=lambda e: print("设置弹窗已关闭"),
        )

        # 打开弹窗
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def _build_settings_content(self, settings_data) -> ft.Column:
        """构建弹窗内部布局"""
        config_rows = []

        for config_item in settings_data:
            key = config_item["key"]
            config_val = config_item["value"]
            config_desc = config_item["description"]

            desc_text = ft.Text(
                f"{config_desc} ({key})",
                size=14,
                color="black",
            )

            # 如果是 "theme" 配置，使用下拉框
            if key == "theme":
                value_control = ft.Dropdown(
                    label="选择主题",
                    value=config_val,
                    width=200,
                    options=[
                        ft.dropdown.Option("light", "浅色"),
                        ft.dropdown.Option("dark", "深色"),
                        ft.dropdown.Option("blue", "蓝色"),
                        ft.dropdown.Option("green", "绿色"),
                    ],
                    on_change=lambda e, k=key: self._apply_setting(k, e.control.value),
                )
            # 如果是其他配置项，使用 TextField
            else:
                value_control = ft.TextField(
                    label="值",
                    value=config_val,
                    border=ft.InputBorder.OUTLINE,
                    width=200,
                    on_change=lambda e, k=key: self._apply_setting(k, e.control.value.strip()),
                )

            # 存储控件引用
            self.form_controls[key] = {
                "value": value_control,
            }

            # 配置项布局
            row = ft.Column(
                controls=[
                    desc_text,
                    ft.Row(controls=[value_control], spacing=10),
                ],
                spacing=5,
            )
            config_rows.append(row)

        # 底部按钮
        save_button = ft.ElevatedButton(
            text="保存",
            bgcolor="green",
            color="white",
            on_click=self._on_save_click,
        )
        cancel_button = ft.ElevatedButton(
            text="取消",
            bgcolor="red",
            color="white",
            on_click=self._on_cancel_click,
        )
        button_row = ft.Row(
            controls=[save_button, cancel_button],
            alignment=ft.MainAxisAlignment.END,
            spacing=20,
        )

        # 返回完整布局
        return ft.Column(
            controls=[
                *config_rows,
                ft.Divider(height=1, color="#CCCCCC"),
                button_row,
            ],
            spacing=10,
            width=400,
        )

    def _apply_setting(self, key, value):
        """实时应用设置到页面"""
        try:
            if key == "theme":
                # 动态切换主题
                self.theme_manager.apply_theme(self.page, value)  # 使用 ThemeManager 管理主题
            elif key == "opacity":
                # 验证并更新窗口透明度 (范围: 0.1 - 1.0)
                try:
                    opacity = float(value)
                    if 0.1 <= opacity <= 1.0:
                        self.page.window.opacity = opacity
                    else:
                        raise ValueError("透明度必须在 0.1 和 1.0 之间")
                except ValueError as ve:
                    NotificationManager.show_notification(
                        self.page, f"无效透明度值: {ve}", success=False
                    )
                    return
            elif key == "window_width":
                # 验证并更新窗口宽度 (范围: 300 - 3000)
                try:
                    width = int(value)
                    if 300 <= width <= 3000:
                        self.page.window.width = width
                    else:
                        raise ValueError("窗口宽度必须在 300 和 3000 之间")
                except ValueError as ve:
                    NotificationManager.show_notification(
                        self.page, f"无效窗口宽度: {ve}", success=False
                    )
                    return
            elif key == "window_height":
                # 验证并更新窗口高度 (范围: 300 - 3000)
                try:
                    height = int(value)
                    if 300 <= height <= 3000:
                        self.page.window.height = height
                    else:
                        raise ValueError("窗口高度必须在 300 和 3000 之间")
                except ValueError as ve:
                    NotificationManager.show_notification(
                        self.page, f"无效窗口高度: {ve}", success=False
                    )
                    return

            self.page.update()  # 刷新页面
        except Exception as e:
            NotificationManager.show_notification(
                self.page, f"应用设置时发生错误: {e}", success=False
            )

    def _on_save_click(self, e):
        """保存配置数据"""
        try:
            for key, controls in self.form_controls.items():
                # 提取控件值
                control = controls["value"]
                new_value = control.value.strip()

                # 更新配置到数据库
                self.view_model.update_config(
                    config_id=key,  # 使用 config_key 作为唯一标识
                    updates={"config_value": new_value},  # 确保键名与模型字段一致
                )

            # 弹出保存成功通知
            NotificationManager.show_notification(self.page, "设置保存成功！", success=True)

            # 关闭弹窗
            self.dialog.open = False
            self.page.update()
        except Exception as ex:
            # 弹出失败通知
            NotificationManager.show_notification(self.page, f"保存失败: {ex}", success=False)

    def _on_cancel_click(self, e):
        """取消修改，关闭弹窗"""
        self.dialog.open = False
        self.page.update()
