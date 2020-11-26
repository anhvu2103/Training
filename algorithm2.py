# Cho x,y (y>x)
# 2 cách để tthay đổi x:
#     x * 2
#     x - 1
# tìm số bước nhỏ nhất để x = y 
import queue

bad = "x phải nhỏ hơn y"
no = "x và y phải lớn hơn 0 và x phải nhỏ hơn y"
def Compare(x,y):
    times = 0
#     if x == y: 
#         print("Chỉ cần",times,"bước để x = y")
#   Không cần vì x phải nhỏ hơn ý 
    if x >= y:
        print(bad)
    if x <= 0 or y <= 0:
        print(no)
    while times >= 0:
        if x < y:
            x = x * 2
            times += 1
            if y == x - 1:
                times += 1
#                 print(times) check số lần lúc code 
                break
    return times 

if __name__ == '__main__':
    x = 2
    y = 4294967295
    print("Cần tổng cộng",Compare(x, y), "bước để x = y") 
