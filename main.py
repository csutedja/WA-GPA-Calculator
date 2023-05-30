# WA-GPA-Calculator
# Easy-to-use program written in Python to calculate the weighted GPA of a student, based on the Westford Academy GPA system.
# Have any problems? Make an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator

from statistics import mean # used to calculate the average GPA

def main():
  cp_count = 0
  ap_count = 0 #defining class counts
  honors_count = 0


  def error_check():
    if int(cp_count) < 0 or int(honors_count) < 0 or int(ap_count) < 0:
      print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
      raise SystemExit
  cp_count = str(input("How many CP classses do you take at WA? If you take none, just enter '0'."))
  error_check()
  honors_count = str(input("How many honors classses do you take? If you take none, just enter '0'. "))
  error_check()
  ap_count = str(input("How many AP classses do you take? If you take none, just enter '0'. "))
  error_check()
  gpa = []

  
  for i in range(0, int(cp_count)):
    try:
      grade_input = int(input("Please input a CP course grade from 0 to 100 "))
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
      elif grade_input <=0 or grade_input > 100:
       print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
       raise SystemExit
        
        
    except ValueError:
      print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
      raise SystemExit
  print("\n")
  for i in range(0, int(honors_count)):
    try:
      grade_input = int(input("Please input a honors course grade from 0 to 100 "))
      if grade_input <= 64 and grade_input >= 0:
        gpa.append(float(0))
      elif grade_input <= 69 and grade_input >= 65:
        gpa.append(float(1.5))  
      elif grade_input <= 72 and grade_input >= 70:
        gpa.append(float(2.2))  
      elif grade_input <= 76 and grade_input >= 73:
        gpa.append(float(2.5))  
      elif grade_input <= 79 and grade_input >= 77:
        gpa.append(float(2.9))  
      elif grade_input <= 82 and grade_input >= 80:
        gpa.append(float(3.2))  
      elif grade_input <= 86 and grade_input >= 83:
        gpa.append(float(3.5))  
      elif grade_input <= 89 and grade_input >= 87:
        gpa.append(float(3.8))  
      elif grade_input <= 92 and grade_input >= 90:
        gpa.append(float(4.0))  
      elif grade_input <= 97 and grade_input >= 93:
        gpa.append(float(4.2))  
      elif grade_input <= 100 and grade_input >= 98:
        gpa.append(float(4.5))  
      elif grade_input <=0 or grade_input > 100:
        print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
      raise SystemExit  
    except ValueError:
      print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
      raise SystemExit
  print("\n")  
  for i in range(0, int(ap_count)):
    try:
      grade_input = int(input("Please input an AP course grade from 0 to 100 "))
      if grade_input <= 64 and grade_input >= 0:
        gpa.append(float(0))
      elif grade_input <= 69 and grade_input >= 65:
        gpa.append(float(2))  
      elif grade_input <= 72 and grade_input >= 70:
        gpa.append(float(2.7))  
      elif grade_input <= 76 and grade_input >= 73:
        gpa.append(float(3))  
      elif grade_input <= 79 and grade_input >= 77:
        gpa.append(float(3.4))  
      elif grade_input <= 82 and grade_input >= 80:
        gpa.append(float(3.7))  
      elif grade_input <= 86 and grade_input >= 83:
        gpa.append(float(4))  
      elif grade_input <= 89 and grade_input >= 87:
        gpa.append(float(4.3))  
      elif grade_input <= 92 and grade_input >= 90:
        gpa.append(float(4.5))  
      elif grade_input <= 97 and grade_input >= 93:
        gpa.append(float(4.7))  
      elif grade_input <= 100 and grade_input >= 98:
        gpa.append(float(5))  
      elif grade_input <=0 or grade_input > 100:
       print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
       raise SystemExit        
    except ValueError:
      print("\nInvalid input! This program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
      raise SystemExit
  average_gpa = mean(gpa)
  print("Your weighted GPA is",round(average_gpa, 3) + '.')
 
  
  
def repeat():
  try:
    question = str(input("Would you like to repeat this program?\n1) If so, please enter '1' or 'y'.\n2) If not, please enter '2' or 'y'.\n"))
    if question == str(1) or question == str(y):
      main()
    if question == str(2) or question == str(n):
      print("\nThis program will now exit.\nThank you for using this program.\nIf you have any problems, please create an issue at this project's GitHub page: https://github.com/csutedja/WA-GPA-Calculator")
      raise SystemExit
    else: 
      print("\nInvalid input!")
      repeat()
  except ValueError:
    print("\nInvalid input!")
    repeat()

main()
repeat()
