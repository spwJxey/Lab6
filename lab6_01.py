def is_numeric(value):
  """
  Tests parameter type, if int or float returns true, otherwise returns false
  """
  test_int = isinstance(value, int)
  test_float = isinstance(value, float)
  if test_int == False and test_float == False:
    return False
  else:
    return True

a = is_numeric(4.33)
#print(a)
#i removed print statement so it doesnt print the bool when the function is called in other questions
