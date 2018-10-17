"""
Task:
You are given a date. Your task is to find what the day is on that date.

Input Format:
A single line of input containing the space separated month, day and year, respectively, in    format.

Constraints:
2000 < year < 3000

Output Format:
Output the correct day in capital letters.

"""
import calendar


def get_day_in_caps(input):
    month, day, year = [int(x) for x in input.split()]
    if year in xrange(2000, 3001):
        return calendar.day_name[calendar.weekday(year, month, day)].upper()


if __name__ == '__main__':
    month_day_year = str(raw_input('Enter date in the format "MM DD YYYY": '))
    print get_day_in_caps(month_day_year)