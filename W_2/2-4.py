import re

def is_valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email) is not None

email = input("Nhập địa chỉ email: ")
if is_valid_gmail(email):
    print("Địa chỉ email là hợp lệ và là địa chỉ Gmail.")
else:
    print("Địa chỉ email không hợp lệ hoặc không phải Gmail.")
