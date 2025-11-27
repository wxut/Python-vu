# -*- coding: utf-8 -*-
"""
依赖包检查脚本
快速验证所有必需的依赖包是否已正确安装
"""

import sys
import io

# 设置标准输出为UTF-8编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_dependencies():
    """检查所有必需的依赖包"""
    required_packages = {
        'PySide6': 'PySide6',
        'numpy': 'numpy',
        'psutil': 'psutil',
        'keyboard': 'keyboard',
        'wmi': 'wmi',
        'pywin32': 'win32api'
    }
    
    missing = []
    installed = []
    
    print("=" * 60)
    print("依赖包检查")
    print("=" * 60)
    
    for package_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            installed.append(package_name)
            print(f"[OK] {package_name:15} - 已安装")
        except ImportError:
            missing.append(package_name)
            print(f"[X]  {package_name:15} - 未安装")
    
    print("=" * 60)
    
    if missing:
        print(f"\n缺少 {len(missing)} 个依赖包:")
        for pkg in missing:
            print(f"  - {pkg}")
        print(f"\n请运行以下命令安装:")
        print(f"pip install {' '.join(missing)}")
        return False
    else:
        print(f"\n所有 {len(installed)} 个依赖包已正确安装！")
        print("可以运行程序了: python wy/main.py")
        return True

if __name__ == '__main__':
    success = check_dependencies()
    sys.exit(0 if success else 1)