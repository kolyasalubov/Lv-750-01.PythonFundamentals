while True:
  dict={'login':'First'}
  a=input("Enter your login: ")
  if dict.get('login')==a:
    print("Greetings")
    break
  elif  dict.get('login')!=a:
    print("Error")
