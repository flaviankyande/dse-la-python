# Objective: Using nested if to check leap year and century

# input the year
year = int(input("Enter a year: "))

# condition to check whether the year is a leap year or leap century
if year % 4 == 0:
  if year % 400 == 0:
    print(f"{year} is a leap century")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")
