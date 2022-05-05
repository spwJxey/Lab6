import lab6_01 as test
import math

def hypotenuse(a, b):
  """
  Returns length of hypotenuse given two parameters, if value is none numeric or less than 1 returns an AssertionError
  """
  test_a = test.is_numeric(a)
  test_b = test.is_numeric(b)
  if test_a == False or test_b == False:
    raise AssertionError("Both values must be numeric")
  elif a <= 0 or b <= 0:
    raise AssertionError("Both values must be greater than 0")
  else:
    l_hypotenuse = math.sqrt(a**2 + b**2)
    return l_hypotenuse

print(hypotenuse(5, 5))