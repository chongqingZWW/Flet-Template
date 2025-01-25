## 扣排器 - 项目文档

### 基于最新版微信接口和自动化答题功能的实现

- **任务类型**：异步答题、定时任务
- **自动回复消息**：支持自定义消息
- **微信API**：支持与微信对接，处理群聊消息
- **任务管理**：通过数据库调度任务，定时执行

### 配置项

1. **自动回复设置**：
   - \`auto_reply_message\`: 自动回复内容，默认值：\`谢谢提问，稍后我会回答！\`
   - \`question_answer_timeout\`: 回答问题的超时时间，单位秒，默认值：60
   - \`scheduled_task_time\`: 定时任务的执行时间（24小时制），默认值：08:00
   - \`group_message_interval\`: 群聊消息发送间隔，单位秒，默认值：5
   - \`message_max_length\`: 每条消息的最大字符长度，默认值：500

### 打包

```bash
PyInstaller main.spec
````

### 安装依赖

```bash
pipenv run pyinstaller main.spec
````

自动处理包：

```bash
pip install pipreqs
pipreqs . --force
pipenv install -r requirements.txt
```

### 签名

#### 签名证书

1. 首先使用 PowerShell 生成证书：

```shell
New-SelfSignedCertificate -Type Custom -Subject "CN=智雾网科技, O=重庆智雾网科技有限公司, C=CN, L=重庆, S=重庆, E=xiongbiao@zwwai.com" -KeyUsage DigitalSignature -FriendlyName "热成像智能报警系统" -CertStoreLocation "Cert:\CurrentUser\My" -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.3", "2.5.29.19={text}") -NotAfter (Get-Date).AddYears(100)
```

```shell
$password = ConvertTo-SecureString -String white_zzw -Force -AsPlainText
```

```shell

https://developer.aliyun.com/article/1600913?utm_source=chatgpt.com


https://www.modelscope.cn/models/qwen/Qwen2-VL-2B-Instruct

https://huggingface.co/spaces/Qwen/Qwen2-VL 在线使用（API 的形式）

https://github.com/tesseract-ocr/tesseract 文字识别

https://github.com/openai/CLIP 问答

```


1. 功能模块概述
该系统的核心功能包括多种即时通讯服务，如文字问答、图片识别问答、语音条、表情和引用功能，结合群聊管理、定时任务和个性化设置，提供丰富的用户交互体验。

2. 界面设计与用户体验
不需要登录界面支持多开：

登录后自动刷新群聊列表。
群聊背景颜色：提供三种颜色方案，红色为置顶群聊背景色。
群聊成员显示：
蓝底表示管理员用户。
白底表示普通用户，显示用户名。
菜单栏：显示微信头像，支持多开功能，点击“+”号可启动新的微信头像窗口。
总设置：

包括总开关、皮肤切换等功能。
后续计划添加更多自定义设置选项。
3. 聊天与互动功能
问答功能：

支持文字问答和图片问答。
语音条、表情和引用功能。
拍一拍功能：支持指定“拍谁”，用于群聊中快速互动。
图片识别与回复：

支持图片识别，自动识别图片内容并进行相应回复。
识别后可进行定制回复。
4. 群聊设置
群聊功能开启：

可以选择是否开启群聊功能。
支持指定群聊发言人，用户可以从群成员中选择或通过搜索功能指定发言人。
秘书功能：

选择指定的秘书角色，秘书为固定类型。
关键字与排队：

支持设置关键字扣排功能，根据群聊中的特定关键字进行处理。
定时任务与排队：

支持定时任务设置，根据指定时间进行群聊管理。
送否启动通宵排（定时任务），根据指定的时间执行相关操作。
卡点功能：

支持卡点设置，可以选择特定时间进行任务或群聊管理操作。
5. 广告位置
后续将在界面中预留广告位置，待进一步优化和确定。
6. 后期优化计划
功能扩展：在现有功能基础上，后期将扩展更多个性化和智能化的功能，如自动化排队、智能聊天助手等。
界面优化：进一步细化界面设计，提升用户体验，增加更多主题皮肤和个性化设置。


## hook  wxheyper 自己编译的

> API文档： https://www.yuque.com/atorber/chatflow/dnq7miho2gkfnmvk#OMKN3 

> 开源地址： https://github.com/ttttupup/wxhelper/tree/dev-3.9.8.25?tab=readme-ov-file

>注入工具自己编译也行 https://github.com/nefarius/Injector  可以的话自己写一个， 有编译好的版本

>微信历史版本 https://github.com/tom-snow/wechat-windows-versions/releases


### 如何自己找 hook 点

todo

## ddddocr 训练验证码定制模型


# Flet app

A simple Flet app.

To run the app:

打包过程中使用过 flutter 会出现问题网络问题
使用管理员conda界面进去打包
打包后的地址：E:\workspace\flet\myapp\build\flutter\build\windows\x64\runner\Release\*

```bash
flet create wechat-qa
set HTTPS_PROXY=http://127.0.0.1:10809
set HTTP_PROXY=http://127.0.0.1:10809
flet build windows --module-name main --verbose
flet build windows --include libs/  # 添加第三方的外部包


```

启动
```
flet run 
```

## 采用 flet 写界面打包直接 cmake 的方式编译

界面快速生成

1. 居中显示，最左边是头像多开微信可点击按钮新增
2. 中间是点击头像后切换到不同的群聊。点击群聊针对群聊进行设置，最右边是设置界面
3. 每个群聊都有独立的设置


## 打包

> 使用 UPX 减少体积一定程度上加壳后去需要对关键的代码进行加密

```bash
 pyinstaller .\main.spec
```


### 微信图片解码   https://blog.csdn.net/qq_37673902/article/details/115128577
