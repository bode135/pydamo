from pydamo_0 import Time, DM, Mouse, Key, vk

dm = DM()
ms = Mouse(dm)
kk = Key(dm)
tt = Time()

tmp = 0.5           # 按键间隔
xy1 = (1095, 1005)  # 第1格装备
xy2 = (1125, 1005)  # 第2格装备

# 将xy2的耀光移动到xy1， 然后鼠标移回xy0
def change_position(xy1=xy1, xy2=xy2, tmp = 0.1, ret_original_pos = 1):
    xy0 = ms.position
    ms.position = xy1
    dm.LeftDown()
    tt.sleep(tmp)
    ms.position = xy2
    dm.LeftUp()
    tt.sleep(tmp)

    # 返回原来的鼠标位置
    if(ret_original_pos):    ms.position = xy0

# 释放技能后按下vk.o键就可以自动刷新装备CD了，注意要把“快捷移动攻击指令”设置为字母“O”键。
def fresh_cd(ch = vk.o, xy1=xy1, xy2=xy2, tmp = 0.1, ret_original_pos = 1):
    change_position(xy1 = xy1, xy2 = xy2, tmp = tmp, ret_original_pos = ret_original_pos)
    kk.dp(ch)

# --- test ---
# tt.sleep(1)]
# change_position(xy1, xy2)

def main():
    T = 60 * 60 * 3  # 3小时

    print('run script!')
    tt.__init__()
    t1 = tt.now()
    run_times = 0
    while (tt.during(T)):
        if (tt.stop_0(vk.enter)):  break

        if (tt.get_key_state(vk.back)):
            # back退格键，我的鼠标宏快捷键。建议用T键或者3
            change_position()

        if (tt.get_key_state(vk.symbol[']'])):
            fresh_cd(vk.o)

        temp = tt.now() - t1
        if (temp >= 1):
            # print tt.now() every 5 seconds
            print('--- tt.now():', tt.now(0), '--- run_times:', run_times)
            t1 = tt.now()

        run_times += 1

    print('程序已退出, 总运行时间:', tt.now(1), '秒')

if __name__ == '__main__':
    main()