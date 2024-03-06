# # 1
# word = input("Enter a word: ")

# letter_indexes = {}

# for index, letter in enumerate(word):
#     if letter not in letter_indexes:
#         letter_indexes[letter] = []
    
#     letter_indexes[letter].append(index)

# print(letter_indexes)

# 2

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
# wallet = "$300"

# wallet_amount = int(wallet.replace("$", "").replace(",", ""))

# affordable_items = []

# for item, price in items_purchase.items():
#     item_price = int(price.replace("$", "").replace(",", ""))
#     if item_price <= wallet_amount:
#         affordable_items.append(item)

# affordable_items.sort()

# if affordable_items:
#     print(affordable_items)
# else:
#     print("Nothing")
