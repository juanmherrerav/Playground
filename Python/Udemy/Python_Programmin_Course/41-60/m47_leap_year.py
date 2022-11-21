def is_leap_year(year:int)->bool:
    if year < 1583 :
        return False
    is_divisible_by_4 = year % 4 == 0
    is_divisible_by_100 = year % 100 == 0
    is_divisible_by_400 = year % 400 == 0
    return is_divisible_by_4 and (not is_divisible_by_100 or is_divisible_by_400)



print(is_leap_year(2019))
print(is_leap_year(2020))
print(is_leap_year(2100))
print(is_leap_year(2025))
