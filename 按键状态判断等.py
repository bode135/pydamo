'''
尝试用python对大漠插件进行初步的封装
基本的按键和鼠标功能已经能够满足

按键状态判断
'''

from my_time import Time, vk
#初始化
tt = Time() # 该模块支持64位python

if(1):
    # 5秒内判断鼠标右键是否处于按下状态       *右键虚拟按键码 vk_code = 2
    tt.__init__()
    while(tt.during(5)):
        tt.sleep(0.1)
        print(tt.get_key_state(vk.mouse_right))  # from win32api import GetKeyState

if(1):
    '''
    暂停功能： 按下[Alt + a]暂停循环。
    通过控制输入可以选择是否继续循环。
    
    tt.stop_alt(ch): 按下[Alt+ch]暂停循环，通过输入来控制是否继续循环。
    tt.stop(ch)：    按下[ch]暂停循环，通过输入来控制是否继续循环。
    tt.stop_0(ch):   按下[ch]暂停循环，通过弹窗控制是否继续循环。（有BUG，不推荐）
    '''

    ch = 'a'                    # ch ∈ ['A', 'a', 65]

    # ch = vk.conv_ord(ch)  # 转换为虚拟键盘码：多花一步统一下数据类型，买不了吃亏买不了上当

    tt = Time()
    while (tt.during(100)):
        tt.sleep(0.1)
        if (tt.stop_alt(ch)):
            print('~~~')
            if input('continue: ') != '':  break        # 通过输入来控制是否继续循环。
        else:
            print('--- press_ch: ', tt.get_key_state(ch))

    print('End: ', tt.now().__round__(1), '\bs')    # 打印程序运行时间

if(1):
    # 按下's'跳出双重循环
    tt.__init__()
    for i in range(10):

        try:
            if (break_flag):
                break_flag = 0
                break
        except:
            break_flag = 0

        for j in range(5):
            tt.sleep(0.1)

            print('press_key: ', tt.get_key_state('s'))
            if (tt.stop('s')):  # 确认后再跳出
                break_flag = 1
                print('break')
                break
            else:
                break_flag = 0

    print('End: ', tt.now().__round__(1), '\bs')    # 打印程序运行时间