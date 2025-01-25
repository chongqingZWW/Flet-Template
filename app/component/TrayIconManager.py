from threading import Thread

from PIL import Image, ImageDraw
from pystray import Icon, Menu, MenuItem


class TrayIconManager:
    def     __init__(self, page, title="微信多开管理"):
        self.page = page
        self.title = title
        self.icon = None
        self.icon_path = "assets/tray.png"  # 替换为你的图标路径

    def create_tray_icon(self):
        """创建系统托盘图标和菜单"""

        def on_quit(icon, item):
            self.icon.stop()
            self.page.window.close()

        def show_window(icon, item):
            # 先让窗口可见
            self.page.window.visible = True

            # 如果已经最小化，则先还原
            # 若窗口本来就最小化，可以通过以下方式
            # 1. 强制最小化
            self.page.window.minimized = True
            self.page.update()

            # 2. 再还原
            self.page.window.minimized = False
            self.page.update()

            # 再结合 to_front，尝试置顶
            self.page.window.to_front()
            self.page.update()

        # 加载图标
        image = self._load_icon()

        # 创建托盘菜单
        menu = Menu(
            MenuItem('打开软件', show_window),
            MenuItem('退出', on_quit)
        )

        # 创建托盘图标
        self.icon = Icon(self.title, image, self.title, menu)

    def _load_icon(self):
        """加载托盘图标"""
        try:
            return Image.open(self.icon_path)
        except FileNotFoundError:
            # 如果图标文件不存在，则生成一个简单的占位图标
            image = Image.new('RGB', (64, 64), (255, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.rectangle((16, 16, 48, 48), fill=(255, 255, 255))
            return image

    def start(self):
        """启动系统托盘图标"""
        if self.icon is None:
            self.create_tray_icon()

        thread = Thread(target=self.icon.run)
        thread.daemon = True
        thread.start()

    def stop(self):
        """停止系统托盘图标"""
        if self.icon:
            self.icon.stop()
