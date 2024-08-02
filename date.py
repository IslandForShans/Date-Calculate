def dateConvert(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    
    K = year % 100
    J = year // 100
    
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    
    dayFinal = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    return dayFinal[h]

print("Please enter a date to find the day of the week it happened on.")

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

print(dateConvert(year, month, day))
