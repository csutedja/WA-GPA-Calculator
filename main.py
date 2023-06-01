# WA-GPA-Calculator
# Easy-to-use program written in Python to calculate the unweighted/weighted GPA of a student, based on the Westford Academy GPA system.
# Have any problems? Make an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator

from statistics import mean # used to calculate the average GPA
def invalid_input():
  print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
  raise SystemExit
def goodbye_message():
  print("\nThis program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
  raise SystemExit
def weighted_main():
  cp_count = 0
  ap_count = 0 #defining class counts
  honors_count = 0

  
  def error_check():
    if int(cp_count) < 0 or int(honors_count) < 0 or int(ap_count) < 0:
      invalid_input()
  print('\n')    
  cp_count = str(input("How many CP classses do you take? If you take none, just enter '0'. "))
  error_check()
  honors_count = str(input("How many honors classses do you take? If you take none, just enter '0'. "))
  error_check()
  ap_count = str(input("How many AP classses do you take? If you take none, just enter '0'. "))
  error_check()
  gpa = []
  def base_gpa_calc():
    if grade_input <= 64 and grade_input >= 0:
      gpa.append(float(0))
    elif grade_input <= 69 and grade_input >= 65:
      gpa.append(float(1))  
    elif grade_input <= 72 and grade_input >= 70:
      gpa.append(float(1.7))  
    elif grade_input <= 76 and grade_input >= 73:
      gpa.append(float(2))  
    elif grade_input <= 79 and grade_input >= 77:
      gpa.append(float(2.3))  
    elif grade_input <= 82 and grade_input >= 80:
      gpa.append(float(2.7))  
    elif grade_input <= 86 and grade_input >= 83:
      gpa.append(float(3))  
    elif grade_input <= 89 and grade_input >= 87:
      gpa.append(float(3.3))  
    elif grade_input <= 92 and grade_input >= 90:
      gpa.append(float(3.5))  
    elif grade_input <= 97 and grade_input >= 93:
      gpa.append(float(3.7))  
    elif grade_input <= 100 and grade_input >= 98:
      gpa.append(float(4))  


  for i in range(0, int(cp_count)):
    try:
      grade_input = int(input("Please input a CP course grade from 0 to 100 "))
      base_gpa_calc()
          
    except ValueError:
      invalid_input()
  for i in range(0, int(honors_count)):
    try:
      grade_input = int(input("Please input a honors course grade from 0 to 100 "))
      grade_input + 0.5
      base_gpa_calc()
    except ValueError:
      invalid_input()
 
  for i in range(0, int(ap_count)):
    try:
      grade_input = int(input("Please input an AP course grade from 0 to 100 "))
      grade_input + 1
      base_gpa_calc()
    except ValueError:
      invalid_input()
  average_gpa = mean(gpa)
  print("Your weighted GPA is", str(round(average_gpa, 3)) + '.')
  repeat()
def unweighted_main():
  count = 0

  def error_check():
    if int(count) < 0:
      invalid_input()
  count = str(input("How many classes do you take? "))
  gpa = []
 
  for i in range(0, int(count)):
    try:
      grade_input = int(input("Please input a course grade from 0 to 100 "))
      if grade_input <= 64 and grade_input >= 0:
        gpa.append(float(0))
      elif grade_input <= 69 and grade_input >= 65:
        gpa.append(float(1))  
      elif grade_input <= 72 and grade_input >= 70:
        gpa.append(float(1.7))  
      elif grade_input <= 76 and grade_input >= 73:
        gpa.append(float(2))  
      elif grade_input <= 79 and grade_input >= 77:
        gpa.append(float(2.3))  
      elif grade_input <= 82 and grade_input >= 80:
        gpa.append(float(2.7))  
      elif grade_input <= 86 and grade_input >= 83:
        gpa.append(float(3))  
      elif grade_input <= 89 and grade_input >= 87:
        gpa.append(float(3.3))  
      elif grade_input <= 92 and grade_input >= 90:
        gpa.append(float(3.5))  
      elif grade_input <= 97 and grade_input >= 93:
        gpa.append(float(3.7))  
      elif grade_input <= 100 and grade_input >= 98:
        gpa.append(float(4))  
      elif grade_input < 0 or grade_input > 100:
        invalid_input()
    except ValueError:
      invalid_input()
      raise SystemExit
  average_gpa = mean(gpa)
  print("Your unweighted GPA is", str(round(average_gpa, 3)) + '.')
  repeat()
 
  
  
def prompt():
  question = str(input("Westford Academy GPA Calculator\nWelcome! What would you like to do?\n\n1) Weighted GPA Calculation\n2) Unweighted GPA Calculation\n3) Exit this program\n"))
  try:
    if question == str(1):
      weighted_main()
    elif question == str(2):  
      unweighted_main()
    elif question == str(3):
      goodbye_message() 
    else:
      print("\nInvalid input!\n")
      prompt()
  except ValueError:
    print("\nInvalid input!\n")
    prompt()
def repeat():
  try:
    question = str(input("Would you like to repeat this program?\n1) If so, please enter '1' or 'y'.\n2) If not, please enter '2' or 'n'.\n"))
    if question == str(1) or question == str('y'):
      weighted_main()
    if question == str(2) or question == str('n'):
      goodbye_message()
    else: 
      print("\nInvalid input!")
      repeat()
  except ValueError:
    print("\nInvalid input!")
    repeat()

prompt()
