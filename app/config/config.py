from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['app/config/settings.toml'],
)

# 颜色 & 背景等全局定义
WECHAT_GREEN = "#1AAD19"  # 微信绿色
BACKGROUND_LIGHT = "#F2F2F2"  # 浅背景
TEXT_COLOR = "#333333"  # 深色文字
ICON_COLOR = "#999999"  # 图标浅色
DIVIDER_COLOR = "#E5E5E5"  # 分割线浅色

# 左侧头像列颜色
AVATAR_LIST_COLOR = "#000000"  # 黑色

# 面板背景（区分左侧和中间背景色）
LEFT_PANEL_BG = "#1C1C1C"  # 深灰色背景（接近黑色）
MIDDLE_PANEL_BG = "#F9F9F9"  # 浅灰色背景（比浅背景稍亮）
RIGHT_PANEL_BG = BACKGROUND_LIGHT

# 最大缓存模型数量
MAX_CACHE_MODELS = 10

# 是否启用调试模式
DEBUG = True
