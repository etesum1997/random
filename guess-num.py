# 產生一個隨機整數 1~100 不要印出來
# 讓使用者重複輸入數字去猜
# 猜對的話 印出'終於猜對了！'
# 猜錯的話 要告訴他 比答案大/小
import random
r = random.randint(1, 100)
while True:
    num = input('請猜一個1-100之間的整數：')
    num = int(num)
    if num == r:
        print('終於猜對了！')
        break
    else:
        print('不對喔嗚嗚')
        if num > r:
            print('比答案大！')
        else:
            print('比答案小！')