import time
import random
import pyautogui
import pyperclip

shut_lan=[
    '牛逼',
    '6666',
    '雕塑',
    '你吗炸了',
    '逗比',
    '我去年买了一个表',
    '明年给你上文',
    '你牛逼呀',
    '来呀兄弟',
    '你女朋友呢',
    '逗死我了'
]

def cutdown():
    """用于4秒倒计时，便于移动窗口"""
    count_sleep = 4
    print('攻击即将开始。。。')
    while count_sleep>0:
        time.sleep(1)
        print(f'倒计时{count_sleep}秒',end='\r',flush=True)
        count_sleep -= 1
    print('fire! fire! fire!')


def worker(num1: int):
    """攻击函数,重复的输入和回车"""
    cutdown()
    start_time = time.time()

    # 只支持英文的的输入
    # fuck = 'i fuck your mather'
    # for _ in range(num1):
    #     pyautogui.typewrite(fuck)
    #     pyautogui.press('enter')
    #     time.sleep(0.1)

    # 中文模式尝试
    len_list = len(shut_lan)
    for _ in range(num1):
        num = random.randint(0,len_list)
        pyperclip.copy(shut_lan[num-1])
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
    print(f'花费{time.time()-start_time}s，攻击{num1}次')
    print('攻击结束！')

def main():
    print('攻击工具，请合法使用！ by LH！')
    num1 = int(input('请输入要发送的次数'))
    worker(num1)

if __name__ == "__main__":
    main()