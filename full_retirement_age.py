import datetime


def main(user_birthyear, user_birthmonth):
    if user_birthyear.isdigit():
        if int(user_birthyear) >= 1900 and int(user_birthyear) <= datetime.datetime.today().year:
            user_birthyear = int(user_birthyear)
        else: return "Invalid input. Please try again."
    else: return "Invalid input. Please try again."
    if user_birthmonth.isdigit():
        if int(user_birthmonth) >= 1 and int(user_birthmonth) <= 12:
            user_birthmonth = int(user_birthmonth)
        else: return "Invalid input. Please try again."
    else: return "Invalid input. Please try again."
    
    user_retirement_age = get_retirement_age(user_birthyear)
    user_retirement_time = get_retirement_time(user_birthyear, user_birthmonth)
    return_value = ""
    return_value += f"Your full retirement age is {user_retirement_age[0]} and {user_retirement_age[1]} months.\n"
    return_value += f"This will be in {user_retirement_time[1]} of {user_retirement_time[0]}.\n"
    return return_value


def get_retirement_age(year):
    if year >= 1943 and year <= 1954:
        return 66, 0
    elif year < 1943:
        diff = 1943 - year
        retire = 66 - (diff * 2/12)
        return int(retire // 1), round((retire - retire // 1) * 12)
    elif year > 1954:
        diff = year - 1954
        retire = 66 + (diff * 2/12)
        return int(retire // 1), round((retire - retire // 1) * 12)


def get_retirement_time(year, month):
    month_names = {1: "January", 2: "February", 3: "March", 4: "April", 
                   5: "May", 6: "June", 7: "July", 8: "August", 
                   9: "September", 10: "October", 11: "November", 12: "December"}
    user_age, user_month = get_retirement_age(year)
    retire_year = year + user_age + (month + user_month >= 13)
    retire_month = (month + user_month) - 12 if month + user_month >= 13 else month + user_month
    retire_monthname = month_names[retire_month]
    return int(retire_year), retire_monthname
