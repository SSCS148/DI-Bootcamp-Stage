# Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# result = dict(zip(keys, values))
# print(result)

# # Exercise 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total_cost = 0
# for member, age in family.items():
#     if age < 3:
#         ticket_price = 0
#     elif 3 <= age <= 12:
#         ticket_price = 10
#     else:
#         ticket_price = 15
    
#     print(f"{member.capitalize()} has to pay ${ticket_price} for the movie.")
    
#     total_cost += ticket_price

# print(f"\nThe total cost for the family is ${total_cost}.")

# Exercise 3
# Step 2
# brand_info = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": {"primary": "pink", "secondary": "green"}
#     }
# }

# # Step 3
# brand_info["number_stores"] = 2

# # Step 4
# print("Zara's clients are men, women, children, and home decorators.")

# # Step 5
# brand_info["country_creation"] = "Spain"

# # Step 6
# if "international_competitors" in brand_info:
#     brand_info["international_competitors"].append("Desigual")

# # Step 7
# del brand_info["creation_date"]

# # Step 8
# print("The last international competitor is:", brand_info["international_competitors"][-1])

# # Step 9
# print("The major clothes colors in the US are:", brand_info["major_color"]["US"])

# # Step 10
# print("The amount of key-value pairs in the dictionary is:", len(brand_info))

# # Step 11
# print("The keys of the dictionary are:", list(brand_info.keys()))

# # Step 12
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }

# # Step 13
# brand_info.update(more_on_zara)

# # Step 14
# print("The value of the key number_stores is:", brand_info["number_stores"])

#Exercise 4
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# disney_users_A = {}
# for user in users:
#     disney_users_A[user] = users.index(user)
# print("Result 1:", disney_users_A)

# disney_users_B = {}
# for i, user in enumerate(users):
#     disney_users_B[i] = user
# print("Result 2:", disney_users_B)

# disney_users_C = {user: i for i, user in enumerate(sorted(users))}
# print("Result 3:", disney_users_C)

# disney_users_i = {}
# for user in users:
#     if 'i' in user:
#         disney_users_i[user] = users.index(user)
# print("Result 1 for names containing 'i':", disney_users_i)

# disney_users_m_or_p = {}
# for user in users:
#     if user[0].lower() in ['m', 'p']:
#         disney_users_m_or_p[user] = users.index(user)
# print("Result 1 for names starting with 'm' or 'p':", disney_users_m_or_p)
