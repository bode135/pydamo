import sys

if __name__ == "__main__":
    # 测试系统参数用
    if len(sys.argv)>1:
        print(sys.argv[0], '哈哈哈哈')
        #输入图像
        print(sys.argv[0])
        print(sys.argv[1])
    else:
        print("Usage: python contours.py image")
input()