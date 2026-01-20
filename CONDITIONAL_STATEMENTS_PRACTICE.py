
def positive_negative():
  num = int(input("enter the number : "))

  if num >=1 :
      print("number is positive")
  elif num == 0:
      print("num is zero")

  else:
      print("this num is neg")





def odd_even():
  num = int(input("enter num :"))
  if num%2==0:
    print("this is even")

  else:
    print("odd")





def 2num_larger():
  num1 = int(input("enter num 1:"))
  num2 = int(input("enter num 2:"))

  if num1>num2:
    print(f"num 1 is larger then num 2 {num1} ")

  else:
    print(f"num 2 is the larger then num1 {num2}")





def divisible_by_3_and_5():
  num = int(input("enter the num: "))
  if num % 3 ==0 and num % 5==0 :
    print("yes it is divisible by 3 and 5")

  else:
    print("its not diviseble")








def largest_num():
  num1 =int(input("Enter the number1"))

  num2 = int(input("Enter the number2"))
  num3 =int(input("Enter the number2"))


  if num1 > num2 and num1>num3:
    print("num 1 is largest")

  elif num2>num1 and num2>num3:
    print("num2 is largest")

  else:
    print("num3 is largest")






def vowels():
  char1 = 'a','i','e','o','u'
  en = input("enter char")
  if en in char1:
    print("this is vowels char")

  else:
    print("this is not") 






def single_digit_2ble_digit_3ble_digit_4th_digit():
  num= int(input("enter the number : "))
  if num>0 and num<=9:
    print("num is single digit")

  elif num>=10 and num<=99:
    print("two digit num")

  elif num>=100 and num<=999:
    print("num is 3 digit")

  elif num>=1000 and num<9999:
    print("numis 4 digit")

  else:
    print("pls enter 1 or 2 or 3 or 4")






def large_num_in_3_num():
  a = int(input("enter the 1st angle num :"))
  b = int(input("enter the 2nd angle num :"))
  c = int(input("enter the 3rd angle num :"))

  if a==b==c:
    print("equlatral triangle")

  elif a == b or b==c or a==c:
    print("isosceles")

  elif a!=b or b!=c or a!=c:
    print("scalene")








def divisible_by_4_not_by_8():
  num =int(input("enter num :"))

  if num%4==0 and num%8 ==0:
    print("it is divisible by 4 not by 8")

  else:
    print("Enter valid num")








def marks():
    marks = int(input("enter the marks: "))
    if marks >= 90:
      print("grade A")

    elif marks >=75:
      print("grade B")

    elif marks >=60:
      print("grade c")

    elif marks < 50:
      print("fail")

    else:
      print("enter valid marks")

marks()





def divisible_7_and_last_digit_7():
    num= int(input("enter the num : "))

    if num%7 == 0:
      print(f"num is divisible by 7 ")
    else:
      print("enter valid num")

    strnum = str(num)

    if strnum[-1]=='7':
      print("last digit is 7 pass")
    else:
      print("last digit is not 7")

divisible_7_and_last_digit_7()
