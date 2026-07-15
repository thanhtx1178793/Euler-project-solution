from datetime import datetime

# Base solution
start = datetime.now()
ans = 0
for i in range(100, 999):
    for j in range(i, 999):
        n = i * j
        if str(n) == str(n)[::-1]:
            ans = max(ans, n)
end = datetime.now()
print(ans, "Time: {}".format(end-start))



"""
    Tối ưu:
    - Cần tìm số lớn nhất là palindrome và là tích của 2 số có 3 chữ số. Dễ thấy 111111 = 143 * 777, do đó số cần tìm là số có 6 chữ số. Ta có:
    abccba = a*100001 + b*10010+c*1100 = 11*(a*9091 + b*910 + c*100)

    như vậy có thể thấy trong 2 số luôn có 1 số chia hết cho 11, ta có thể giả sử là số đầu tiên để check nhanh hơn 
""" 
# Optimization
import math
start = datetime.now()
ans = 0
for i in range(math.ceil(100/11), int(999/11)+1):
    x = i * 11
    for y in range(x+1, 999):
        n = x* y
        if str(n) == str(n)[::-1]:
            ans = max(ans, n)
end = datetime.now()
print(ans, "Time: {}".format(end-start))