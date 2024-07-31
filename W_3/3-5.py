prices = {
    'apple': 2,
    'banana': 1,
    'cherry': 3
}

stock = {
    'apple': 50,
    'banana': 30,
    'cherry': 20
}

total_value = {key: prices[key] * stock[key] for key in stock}
sorted_fruits = sorted(total_value.items(), key=lambda x: x[1], reverse=True)

print("Thứ tự các loại trái cây giảm dần theo tổng giá trị là:")
for fruit, value in sorted_fruits:
    print(f"{fruit}: {value}")
    