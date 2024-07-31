from datetime import datetime, timedelta

def get_next_day(day, month, year):
    current_date = datetime(year, month, day)
    next_day = current_date + timedelta(days=1)
    return next_day.day, next_day.month, next_day.year

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

next_day, next_month, next_year = get_next_day(day, month, year)
print(f"Ngày tiếp theo là: {next_day}/{next_month}/{next_year}")
