import datetime
print('ONLY D.O.B AFTER 1900 WILL BE COMPUTED')
#Finding the date of birth of person and the current date and year
day_birth = int(input('Enter the date born on between(1-31): '))
month_birth = int(input('Enter the month born on between(1-12): '))
year_birth = int(input('Enter the year born on between(4 digit): '))
current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year
#determining number of seconds in a day, year, average year, average month
numsec_day = 24*3600
numsec_year = 365*numsec_day
avg_numsec_year = ((4 * numsec_year) + numsec_day)//4
avg_numsec_month = avg_numsec_year//12
#Calculate age in seconds
numsecs_1900_dob = ((year_birth - 1900) * avg_numsec_year)+(month_birth - 1 * avg_numsec_month)+(day_birth * numsec_day)
numsecs_1900_current = ((current_year - 1900) * avg_numsec_year)+(current_month - 1 * avg_numsec_month)+(current_day * numsec_day)
age_in_sec = numsecs_1900_current - numsecs_1900_dob
print('Your age in seconds is approx. ',age_in_sec)