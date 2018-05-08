def device_time_parse(time_string):
    week_day = ''
    month = ''
    day = ''
    hours = ''
    time_zone = ''
    year = ''

# not implemented for day == 2char and month == 4char
    for x in time_string:
        if x != ' ':
            if (len(week_day) < 3 and month and day and hours and time and year) == '':
                week_day += x
            elif len(week_day) == 3 and len(month) < 3 and day == '' and hours == '' and time_zone == '' and year == '':
                month += x
            elif len(week_day) == 3 and len(
                    month) == 3 and day == '' and hours == '' and time_zone == '' and year == '':
                day += x
            elif len(week_day) == 3 and len(month) == 3 and day != '' and len(
                    hours) < 8 and time_zone == '' and year == '':
                hours += x
            elif len(week_day) == 3 and len(month) == 3 and day != '' and len(hours) == 8 and len(
                    time_zone) < 3 and year == '':
                time_zone += x
            elif len(week_day) == 3 and len(month) == 3 and day != '' and len(hours) == 8 and len(
                    time_zone) == 3 and len(year) < 4:
                year += x

    return week_day, month, day, hours, time_zone, year


def month_string_to_num(month):
    months = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "July": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    for x in months:
        if x == month:
            return months[x]


def month_select_direction_click_count(current_month):
    if current_month < 7:
        count = 7 - current_month
        direction = 'right'
        return count, direction
    elif current_month > 7:
        count = current_month - 7
        direction = 'left'
        return count, direction
    else:
        count = 0
        direction = 'none'
        return count, direction


def prev_or_next_month(count_direction):
    if count_direction[1] == 'left':
        return 'android:id/prev'
    else:
        return 'android:id/next'


time = 'Sun Aug  8 20:04:17 GMT 2018'
time_parsed = device_time_parse(time)
month_num = month_string_to_num(time_parsed[1])
count_direction = month_select_direction_click_count(month_num)
print(count_direction[0])
print(count_direction[1])
print("week_day: ", time_parsed[0])
print("month: ", time_parsed[1])
print("day: ", time_parsed[2])
print("hours: ", time_parsed[3])
print("time_zone: ", time_parsed[4])
print("year: ", time_parsed[5])
