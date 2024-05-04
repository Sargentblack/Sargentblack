name = input("what is your name? ")
print("Hello " + name)
birth = input("When is your birth year? ")
age = 2023 -  int(birth)
print("you are " + str(age) + " years old!")
if age < 18:
  print("oh you are still a teenager")
  school = input("Where do you go to school? ")
  print("I'm sure " + school + " is a good school")
  grade = input("Did you pass?(true or false) ")
  result = bool(grade.lower() == 'true')
  if result:
    print("That's great, congrats!")
  else:
    print("I'm sorry to hear that but you'll do better next year ")
  print("the end")
if age > 18:
  print("You are an adult")
  job = input("Do you have a job?(true or false) ")
  work = bool(job.lower() == 'true')
  if work:
    job_location=input("Where do you work? ")
    print ("I'm sure working at " + job_location + " is great")
  else:
    input("Im sure you'll get one soon")
  print("the end")
