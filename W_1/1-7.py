def classify_gpa(gpa):
    if gpa < 3.5:
        return "Yếu"
    elif 3.5 <= gpa < 5:
        return "Kém"
    elif 5 <= gpa < 6.5:
        return "Trung bình"
    elif 6.5 <= gpa < 8:
        return "Khá"
    elif 8 <= gpa < 9:
        return "Giỏi"
    else:
        return "Xuất sắc"

gpa = float(input("Nhập điểm trung bình học tập của sinh viên: "))
classification = classify_gpa(gpa)
print("Điểm trung bình học tập của sinh viên là:", gpa)
print("Xếp loại:", classification)
