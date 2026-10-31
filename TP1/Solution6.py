def is_leapyear(year):
    return (year%4==0 and year%100!=0) or (year%400==0)
def day_in_month(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month==2:
        return 29 if is_leapyear(year) else 28
    else:
        return "Invalid month!"
years=[1900,2000,2024,2026]
for year in years:
    print(f"year:{year}->LeapYear:{is_leapyear(year)}\n")
for year in years:
    print(f"Days in February {year}->{day_in_month(2, year)}\n")
    print(f"Day in April 2026->{day_in_month(4,year)}")
    #print(f"Day in Febuary 2024->{day_in_month(2,2024)}")
    #print(f"Day in Febuary 2024->{day_in_month(2,2024)}")
    count_leap=0
for y in range(2000,2100):
    if is_leapyear(year):
        count_leap+=1
print(f"The total leap year from 2000 to 2100:{count_leap}")
    
    
