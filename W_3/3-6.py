import random

def generate_average_rainfall(year_start, year_end):
    rainfall_dict = {}
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    for year in range(year_start, year_end + 1):
        for month in months:
            key = f"{month}_{year}"
            rainfall_dict[key] = round(random.uniform(50, 200), 2)  # Tạo giá trị ngẫu nhiên từ 50 đến 200 mm
            
    return rainfall_dict

rainfall = generate_average_rainfall(2000, 2019)
print("Từ điển lưu lượng mưa trung bình là:", rainfall)
