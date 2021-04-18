from pydamo_0 import Time, vk, DM, Key, Mouse

dm = DM()           # 初始化
# dm.reg()           # 注册

ms = Mouse(dm)
kk = Key(dm)
tt = Time()

dm.Beep()    # 蜂鸣器

print('your mouse\'s position: ', ms.position)
tt.sleep(1)

x, y = (1000, 500)
ms.position = x, y
print('move your mouse\'s to: ', ms.position)
tt.sleep(1)


ms.click_right(10, 10)
print('clike mouse_right: ', ms.position)

