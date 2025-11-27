# Python 3.12 64位 安装指南

## 问题说明

当前系统使用的是 **Python 3.13 32位**,但 PySide6 要求:
- Python 版本: 3.7 - 3.12 (不支持 3.13)
- 架构: 仅支持 64位

## 安装步骤

### 1. 下载 Python 3.12 64位

访问 Python 官网下载页面:
```
https://www.python.org/downloads/release/python-31210/
```

在页面底部找到 "Files" 部分,下载:
```
Windows installer (64-bit)
```

文件名类似: `python-3.12.10-amd64.exe`

### 2. 卸载旧版本 (可选但推荐)

1. 打开 "设置" → "应用" → "已安装的应用"
2. 找到 "Python 3.13.9 (32-bit)"
3. 点击 "卸载"

### 3. 安装 Python 3.12

1. 运行下载的安装程序
2. **重要**: 勾选 "Add Python 3.12 to PATH"
3. 选择 "Customize installation"
4. 确保勾选:
   - pip
   - py launcher
   - for all users (optional)
5. 在 "Advanced Options" 中:
   - 勾选 "Install for all users"
   - 勾选 "Add Python to environment variables"
6. 点击 "Install"

### 4. 验证安装

打开**新的**命令提示符窗口,运行:

```cmd
python --version
```

应该显示:
```
Python 3.12.x
```

检查是否为 64位:
```cmd
python -c "import struct; print(struct.calcsize('P') * 8, 'bit')"
```

应该显示:
```
64 bit
```

### 5. 安装项目依赖

```cmd
cd C:\Users\x\Desktop\wy
pip install PySide6
```

或运行批处理文件:
```cmd
install_dependencies.bat
```

### 6. 验证依赖

```cmd
python check_dependencies.py
```

应该显示所有依赖都已安装。

### 7. 启动程序

```cmd
python main.py
```

## 常见问题

### Q: 安装后 python 命令仍然指向旧版本?

A: 
1. 关闭所有命令提示符窗口
2. 打开新的命令提示符
3. 如果仍然不行,重启电脑

### Q: 同时保留两个 Python 版本?

A: 可以使用 `py` 启动器:
```cmd
py -3.12 --version    # 使用 Python 3.12
py -3.13 --version    # 使用 Python 3.13
```

### Q: pip 安装速度慢?

A: 使用清华镜像源:
```cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PySide6
```

## 下一步

安装完成后,请运行:
```cmd
python check_dependencies.py
```

确认所有依赖都已安装,然后启动程序:
```cmd
python main.py