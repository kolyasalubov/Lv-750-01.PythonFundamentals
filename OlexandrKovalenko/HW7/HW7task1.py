def larg_num(num1, num2):
  """
  Function that returns the 
  largest number of two numbers
  """
  if num1 > num2:
    return num1
  elif num1 < num2:
    return num2
  elif num1==num2:
    return "Numbers are equal"

print(larg_num(12.5, 25))
print(larg_num.__doc__)
