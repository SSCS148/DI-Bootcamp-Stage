# my_name = 'Sacha Shimon'
# my_Last_name = 'Cohen Solal'
# my_age = 24
# futur_age = my_age + 123456789
# print(my_name, my_Last_name)
# print("I am ",my_age, "years old")
# print("In 123456789 years i'm gonna be",my_age + futur_age,"Thanks")

# print(4 < 1)

# birthday_day = 8
# birthday_month = 2
# birthday_year = 1979
# print("I was born the {}/{}/{}".format(birthday_day, birthday_month, birthday_year))

# input('How old are you ? ')
# # name = input('How old are you ?')
num = int(input('Choose a number between 1 and 100\n'))
print(f'You have choosen the number {num}')

if num % 3 == 0 and num % 5 == 0:
     print("FIZZBUZZ")
elif num % 3 == 0:
    print("FIZZ")
elif num % 5 == 0:
     print("BUZZ")
else: print(f"{num} is not a multpile of 3 or 5")

# if num % 3 == 0:
#     print("FIZZ")
# elif num % 5 == 0:
#      print("BUZZ")
# elif num % 3 == 0 and num % 5 == 0:
#      print("FIZZBUZZ")
# else: print(f"{num} is not a multpile of 3 or 5")


    
