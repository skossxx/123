import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("倒计时:", timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("时间到！")

# 设置专注时长为25分钟（可以根据需要自行调整）
focus_timer(25)
