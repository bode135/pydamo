echo off
chcp 65001


: 新建环境名称
set env_name="win32_py36"


: 查看conda的平台位数
conda info | findstr platform

: 设置为32位(临时生效, 重新打开cmd将失效)
set CONDA_FORCE_32BIT=1

: 一起运行
conda create -n %env_name% python=3.6 -y && activate %env_name% && python -c "import sys;print('*** Python interpreter path: ', sys.executable)"


: --- pycharm启用conda创建的虚拟环境略, 请看下面的参考链接 --- pycharm use python interpreter which created by conda
: anaconda3下64位python和32位python共存
: https://blog.csdn.net/weixin_41710606/article/details/86747877?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_antiscanv2&utm_relevant_index=3


: --- 笔记 ---


: 创建32位的python3.6
: conda create -n %env_name% python=3.6 -y

: 查看是否成功
: conda info -e

: 删除一个已有的环境
: conda remove --name %env_name% --all -y

: 激活并查看执行路径
: activate %env_name% && python -c "import sys;print('*** Python interpreter path: ', sys.executable)"

