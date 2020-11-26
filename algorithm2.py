# Cho x,y (y>x)
# 2 cách để tthay đổi x:
#     x * 2 => y luôn chẵn 
#     x - 1 => y luôn lẻ 
# tìm số bước nhỏ nhất để x = y
bad = "x phải nhỏ hơn y"
no = "x ko thế lớn hơn y"
def Compare(x, y):
#     times = 0
    if(x == y): 
        return 0

    if(x > y): 
        return 0

    if(x <= 0 and y > 0): 
        return 0
    
    # y lẻ 
    if(y % 2 == 1): 
        #-1 y 
        #+1 x 
        return 1 + Compare(x, y + 1)

    # y chẵn 
    else: 
        #*2 ở x
        #y/2 ở y 
        return 1 + Compare(x, y / 2) 

if __name__ == '__main__':
    x = 2
    y = 4294967295
    print("Cần tổng cộng",Compare(x, y), "bước để x = y") 