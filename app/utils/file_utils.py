import ctypes
import os
import platform
import socket
import sys
import tarfile
import uuid
from tkinter import messagebox


def get_resource_path(relative_path):
    """获取资源的绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_mac_address():
    """获取MAC地址"""
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    return mac


def get_ip_address():
    """获取IP地址"""
    return socket.gethostbyname(socket.gethostname())

def get_operating_system():
    """获取操作系统名称"""
    return platform.system()


def check_if_already_running():
    """使用互斥体检查是否已经有一个实例在运行"""
    mutex_name = "UniqueAppMutexNameHk"  # 设置唯一的互斥体名称
    mutex = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)
    if ctypes.windll.kernel32.GetLastError() == 183:
        messagebox.showwarning("警告", "程序已经在运行中！")
        ctypes.windll.kernel32.ReleaseMutex(mutex)  # 释放互斥体
        sys.exit()  # 立即退出程序
    return False


def extract_tar(self, tar_path, extract_to):
    """解压 tar 文件到指定目录"""
    try:
        with tarfile.open(tar_path, "r") as tar:
            tar.extractall(path=extract_to)
        self.logger.debug(f"解压 {tar_path} 到 {extract_to} 成功。")
        return True
    except Exception as e:
        self.logger.error(f"解压 {tar_path} 失败：{e}")
        return False
