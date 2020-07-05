from datetime import datetime,date


date_string="2030-07-05"
old_date = datetime.strptime(date_string,"%Y-%m-%d").date()
current_date = datetime.today().date()

print("Current date",current_date)
print("Old date", old_date)

difference_in_date = (current_date - old_date)
print("Difference in date", difference_in_date)
