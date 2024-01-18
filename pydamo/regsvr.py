from bdtime import tt
import os
from random import randint
from win32com.client import Dispatch
import ctypes


def run_in_bat(cmd, echo=0):
    f_id = str(tt.now())[-6:] + '_' + str(randint(0, 10)) + str(randint(0, 10))  # 随机id避免混淆
    bat_name = 'cmd' + f_id + '.bat'

    cmd_head = 'chcp 65001\n'
    if echo == 0:
        cmd_head = '@echo off\n' + cmd_head

    bat_text = cmd_head + cmd
    with open(bat_name, 'w') as f:
        f.write(bat_text)

    os.system(bat_name)
    os.remove(bat_name)

    return 1


def success_regsvr(desc='--- 调用dm.dll失败! ---', T=0.5):
    try:
        dm = Dispatch('dm.dmsoft')  # 调用大漠插件
        print('调用dm.dll成功!')
        return dm
    except:
        print(desc)
        # tt.tqdm_sleep(desc, T)
        return 0


def get_regsvr_cmd():
    dirpath_0 = os.getcwd()
    dirpath = __file__.replace('/', '\\')
    dirpath = os.path.dirname(dirpath)
    path_dll = os.path.join(dirpath, 'dm.dll')
    cmd_dll_0 = 'regsvr32 \"' + path_dll + '\" /s'
    return cmd_dll_0


class RegDM():
    def __init__(self, dirpath=''):
        cwd_0 = os.getcwd()

        if (not dirpath):
            # 没指定dm.dll就用默认的dm.dll
            dirpath = __file__.replace('/', '\\')
            dirpath = os.path.dirname(dirpath)

        if (dirpath.endswith('.dll')):
            path_dll = dirpath
        else:
            path_dll = os.path.join(dirpath, 'dm.dll')
        print('dm.dll注册路径:', path_dll)
        cmd_dll_0 = 'regsvr32 \"' + path_dll + '\" /s'

        self.dirpath_0 = cwd_0
        self.dirpath = dirpath
        self.path_dll = path_dll
        self.cmd_dll_0 = cmd_dll_0
        # print(self.cmd_dll_0)

        self.dm = 0
        pass

    def reg(self):
        dm = success_regsvr()
        if not dm:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if is_admin:
                print('--------- self.reg_dm() -------------')
                self.reg_dm()
                dm = success_regsvr()
            else:
                print('--------- self.reg_as_admin() -------------')
                dm = self.reg_as_admin()
                dm = success_regsvr()  # 调用大漠插件
        self.dm = dm
        return dm

    def unreg_dm(self):
        # os.system(self.cmd_dll_0 + ' /u')
        cmd = f'regsvr32 /u /s "{self.path_dll}"'
        run_in_bat(cmd)
        print('已移除dm.dll')

    def reg_dm(self):
        os.system(self.cmd_dll_0)

    def reg_as_admin(self):
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/C %s" % self.cmd_dll_0, None, 1)
        tt.sleep(3)
        dm = success_regsvr()  # 调用大漠插件
        return dm

    @property
    def is_reg(self):
        ret = success_regsvr()
        if (ret):
            return 1
        else:
            return 0
        1

    def __repr__(self):
        ret = 'dm.dll注册状态: ' + str(self.dm)
        return ret


if __name__ == '__main__':
    reg_dm = RegDM()

    reg_dm.unreg_dm()

    reg_dm.reg_as_admin()

    success_regsvr()

    reg_dm.reg()

    print(reg_dm.dm)
    print(1)
