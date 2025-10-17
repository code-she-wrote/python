def is_leap_year(year):
    if year % 4 == 0:  # if year div by 4
        if year % 100 == 0:  # and div by  100
            if year % 400 == 0:  # and also div 400
                return True  # it is a leap year

            else:  # if div by 4 and 100 but not by 400
                return False  # its not leap
        else:  # if div by 4 and not div by 100
            return True  # it is leap year
    else:
        return False  # otherwise not leap


print(is_leap_year(2000))  # run function with hardcoded value