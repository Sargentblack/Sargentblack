First = int(input("Value 1: "))
sign = input("Sign: ")
Second = int(input("Value 2: "))
if sign =='×':
  Answer = First * Second
  print(Answer)
if sign =='÷':
  Answer = First / Second
  print(Answer)
if sign =='+':
  Answer = First + Second
  print(Answer)
if sign =='-':
  Answer = First - Second
  print(Answer)
else :
  print("incorrect input")
