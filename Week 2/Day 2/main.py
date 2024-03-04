# user_name = 'Sacha'
# user_email = 'sacha.02.cohen.04@gmail.com'
# user_age = 25 
# user_info = [user_name,user_email,user_age]
# print(user_info[1])

# user_name_list = [user_name]
# print(user_name_list)

# user_name_list2 = list(user_name)
# print(user_name_list2)

# user_name_list3 = user_name.split()
# print(user_name_list)

# user_info2 = input('Give me your name, email and age separated by ,:').split(',')

# user_info2.append("betsalel")
# print(user_info2)
# print(user_info2[-2])

# fav_color_list = ['blue', 'red','yellow',"green"]

# fav_color_list[1] = 'green'
# fav_color_list[0] = fav_color_list[1]
# fav_color_list[0] = fav_color_list[1]
# print(fav_color_list)


# fav_color_list.sort()
# print(fav_color_list)

# new_list = sorted(fav_color_list)
# print(fav_color_list)
# print(new_list)

# Option1
# list1 = [5,10,15,20,25,30,35,20]
# list1[list1.index(20)] = 200
# print(list)

# Option2

# list1 = [5,10,15,20,25,30,35,20]
# for i in list1:
#     if (i == 20):
#         index = list1.index(i)
#         list1[index] = 200
#         break
# print(list1)
    
# some_tuple = (1,2,3,4)
# fav_colors_tuple = tuple(fav_colors_list)
# print(some_tuple)
# print(fav_colors_tuple)

# a,b,c,d = (10,20,30,40)
# print(a)
# print(b)
# print(c)
# print(d)

# list = ['sa','ch','aa','sasachcha']
# list2 = ["fezf","efze","fregt"]
# list3 = [2,4,7,23,56]
# list.extend(['nenz', 'haha'])
# # print((list))

# list3[list3.index(23)] = 200
# print(list3)

# my_tuple = (5,6,7,'a')
# a,b,c,d = my_tuple
# print(a)
# print(b)
# print(c)
# print(d)

# students = ["mordekhai","shimon","mathitiahou","moshe"]
# for each_student in students:
#     if each_student == 'shimon':
#         print('sacha')
#     else:
#         print(each_student)

# cities = ('Tel Aviv',"Paris","Jerusalem","New york")
# for city in cities:
#     print(f'I\'ve been to {city}')
    
# user_num = int(input('Give me a number\n'))
# for i in range(1, 10):
#     print(user_num * i)
    
# counter = 0
# while counter < 8:
#     counter += 1
#     print("ghelo")

# password = ''
# while password != '12345':
#     password = input('Insert your password')
#     if password == 'sacha':
#         break
# print("nice")

# print(basket)
# 'orange' in basket
# 'crabgrass' in basket

basket = {'apple','orange','apple' , 'pear' , 'orange','banana'} 
list = {1,2,6,2,9,7}
first = set(list)
second = {1,5}
print(first | second)
print(first & second)
print(second - first)
print(second ^ first)

