import calendar

def get_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    a = []
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += " &nbsp;"
            else:
                week_str += f"{day:02}"
            week_str += " "
        a.append(week_str.strip())
    
    a = [week.replace("  ", " ") for week in a]
    return a


calendar.setfirstweekday(calendar.SUNDAY)