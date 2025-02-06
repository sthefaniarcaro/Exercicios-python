# if statement

def school_class(grade):
  if grade >= 55:
    print("You passed.")
  else:
    print("You failed.")

grade = float(input("enter your note:"))
school_class(grade)