import lab6_01 as test
def is_leapyear(year):
  test_year = test.is_numeric(year)
  if (test_year == False):
    return False
  elif(year%4 == 0):
    if (year%100 != 0 or year%400 != 0):
      return False
    else:
      return True
  else:
    return False

print(is_leapyear(2000))