from datetime import date
f_date = date(2022, 3, 19)
l_date = date(2022, 3, 31)
delta = l_date - f_date
print(delta.days)