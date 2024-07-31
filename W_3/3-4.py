from collections import Counter

S = input("Nhập chuỗi: ")
D = dict(Counter(S))
print("Từ điển đếm số lần xuất hiện của các chữ trong chuỗi là:", D)
