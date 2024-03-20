# class Pagination:
#     def __init__(self, items=None, pageSize=10):
#         self.items = items or []
#         self.pageSize = int(pageSize)
#         self.currentPage = 1
#         self.totalPages = -(-len(self.items) // self.pageSize)  # Ceiling division to get total pages

#     def getVisibleItems(self):
#         start_index = (self.currentPage - 1) * self.pageSize
#         end_index = min(start_index + self.pageSize, len(self.items))
#         return self.items[start_index:end_index]

#     def prevPage(self):
#         self.currentPage = max(self.currentPage - 1, 1)
#         return self

#     def nextPage(self):
#         self.currentPage = min(self.currentPage + 1, self.totalPages)
#         return self

#     def firstPage(self):
#         self.currentPage = 1
#         return self

#     def lastPage(self):
#         self.currentPage = self.totalPages
#         return self

#     def goToPage(self, pageNum):
#         self.currentPage = min(max(int(pageNum), 1), self.totalPages)
#         return self


# # Example usage:
# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)

# print(p.getVisibleItems())  # ["a", "b", "c", "d"]

# p.nextPage().getVisibleItems()  # ["e", "f", "g", "h"]

# p.lastPage().getVisibleItems()  # ["y", "z"]

# p.goToPage(10).getVisibleItems()  # Goes to last page: ["y", "z"]

# p.goToPage(0).getVisibleItems()  # Goes to first page: ["a", "b", "c", "d"]

# p.goToPage(-5).getVisibleItems()  # Goes to first page: ["a", "b", "c", "d"]
