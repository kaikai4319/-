import PyInstaller.__main__
import sys
import os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 定义打包参数
options = [
    os.path.join(current_dir, 'main.py'),  # 使用完整路径
    '--name=英语练习程序',  # 生成的exe名称
    '--noconsole',  # 不显示控制台窗口
    '--windowed',  # 使用窗口模式
    '--onefile',  # 打包成单个文件
    '--clean',  # 清理临时文件
    '--noconfirm',  # 不确认覆盖
    f'--distpath={os.path.dirname(current_dir)}',  # 指定输出目录为项目根目录
    f'--workpath={os.path.join(current_dir, "build")}',  # 指定工作目录
    f'--specpath={current_dir}'  # 指定spec文件目录
]

# 添加所需的依赖
hidden_imports = [
    '--hidden-import=customtkinter',
    '--hidden-import=pandas',
    '--hidden-import=pyttsx3',
]
options.extend(hidden_imports)

# 运行打包命令
PyInstaller.__main__.run(options) 