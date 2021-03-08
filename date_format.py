from datetime import date

# Read the current date
current_date = date.today()

# Print the formatted date
print("Today is :%d-%d-%d" % (current_date.day,current_date.month,current_date.year))

# Set the custom date
custom_date = date(2021, 05, 20)
print("The date is:",custom_date)