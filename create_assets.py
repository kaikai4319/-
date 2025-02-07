import os

# 创建 assets 文件夹
assets_path = os.path.join('src', 'assets')
if not os.path.exists(assets_path):
    os.makedirs(assets_path)
    print(f"Created assets directory at: {assets_path}") 