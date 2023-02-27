while True:
  print("Give me a four-digit natural number, please (press 0000 for quit):")
  n=str(input())
  if len(n) > 4:
    print("Not four-digit natural number")
  elif len(n) < 4:
    print("Not four-digit natural number")
  elif n == "0000":
      print("The end")
      break
  else:
    m=int(n[0])*int(n[1])*int(n[2])*int(n[3])
    print("Multiplying: ",m)
    r=n[::-1]
    print("Reverse: ",r)
    s=sorted(n)
    j=''.join(s)
    print("Sorting in ascending order ",j)