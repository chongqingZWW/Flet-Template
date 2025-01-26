<div align="center">
    <img src="assets/icon.png" alt="Logo" width="180"/>
    <h1>Flet Template</h1>
    <p>一个基于 MVVM 架构的 Flet 桌面应用程序模板</p>
    <p>
        <a href="https://github.com/yourusername/flet-template/stargazers">
            <img src="https://img.shields.io/github/stars/yourusername/flet-template" alt="Stars"/>
        </a>
        <a href="https://github.com/yourusername/flet-template/network/members">
            <img src="https://img.shields.io/github/forks/yourusername/flet-template" alt="Forks"/>
        </a>
        <a href="https://github.com/yourusername/flet-template/issues">
            <img src="https://img.shields.io/github/issues/yourusername/flet-template" alt="Issues"/>
        </a>
        <a href="https://github.com/yourusername/flet-template/blob/main/LICENSE">
            <img src="https://img.shields.io/github/license/yourusername/flet-template" alt="License"/>
        </a>
    </p>
    <p>
        <a href="README.md">简体中文</a> | 
        <a href="README_EN.md">English</a>
    </p>
</div>

## 📖 简介

Flet Template 是一个基于 [Flet](https://flet.dev/) 框架开发的桌面应用程序模板，采用 MVVM 架构设计。项目内置了丰富的 UI 组件示例和最佳实践，帮助开发者快速构建高质量的桌面应用。

### 特性

- 🏗️ **MVVM 架构**: 采用 Model-View-ViewModel 设计模式，实现关注点分离
- 🎨 **组件示例**: 包含 30+ 常用组件示例，快速上手无压力
- 🛠️ **工具支持**: 主题切换、路由管理、状态管理、数据持久化等开箱即用
- 📦 **代码规范**: 遵循 PEP8 规范，注重代码质量和可维护性
- 📚 **详细文档**: 提供完整的开发文档和最佳实践指南

## 🚀 快速开始

### 环境要求

- Python 3.9+
- pip 21.0+

### 安装

1. 克隆仓库
```bash
git clone https://github.com/yourusername/flet-template.git
cd flet-template
```

2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

### 运行

```bash
python main.py
```

## 📂 项目结构

```
flet-template/
├── app/                    # 应用程序主目录
│   ├── component/         # 公共组件
│   │   ├── dialog/       # 对话框组件
│   │   └── widget/       # 通用组件
│   ├── view/             # 视图层
│   ├── viewmodel/        # 视图模型层
│   ├── model/            # 数据模型层
│   ├── repository/       # 数据仓库层
│   ├── service/          # 服务层
│   ├── utils/            # 工具函数
│   └── config/           # 配置文件
├── assets/                # 静态资源
│   ├── images/           # 图片资源
│   └── icons/            # 图标资源
├── docs/                  # 文档
│   ├── components/       # 组件文档
│   └── guide/            # 开发指南
├── tests/                # 测试用例
├── .gitignore            # Git 忽略文件
├── LICENSE               # 开源协议
├── README.md             # 项目说明
├── README_EN.md          # 英文说明
├── requirements.txt      # 项目依赖
└── main.py              # 程序入口
```

## 📚 文档

- [快速上手](docs/guide/getting-started.md)
- [架构说明](docs/guide/architecture.md)
- [组件文档](docs/components/README.md)
- [最佳实践](docs/guide/best-practices.md)
- [常见问题](docs/guide/faq.md)

## 🤝 贡献指南

我们非常欢迎各种形式的贡献，包括但不限于：

- 提交问题和建议
- 改进文档
- 提交代码改进
- 分享使用经验

贡献前请阅读 [贡献指南](CONTRIBUTING.md)。

## 📄 开源协议

本项目采用 [MIT](LICENSE) 协议开源。

## 🙏 致谢

- [Flet](https://flet.dev/)
- [Material Design](https://material.io/)
- [所有贡献者](https://github.com/yourusername/flet-template/graphs/contributors)

## 📮 联系方式

- 作者：[Your Name](https://github.com/yourusername)
- 邮箱：986247535@qq.com 
- 问题反馈：[Issues](https://github.com/yourusername/flet-template/issues)