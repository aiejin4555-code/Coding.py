#LA1
#Write a Python script that takes a numerical input representing years.
#Convert the years to seconds.
#Assume 1 year = 365 days.

years = float(input("Enter number of year: "))

years_seconds = years * 365 * 24 * 60 * 60

print (f"Output: {years_seconds}")
