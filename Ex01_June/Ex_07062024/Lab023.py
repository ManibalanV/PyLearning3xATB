# List - Shopping List
# milk, bread, butter, grape
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit

shopping_List = ["milk", "bread", "butter", "grape"]
print(shopping_List)
print(len(shopping_List))
print(shopping_List[1])
print(shopping_List[-1])

shopping_List.append("curd") # Add item in the end
print(shopping_List)

shopping_List.insert(1,"jam") #Add item in the middle
print(shopping_List)

shopping_List.extend(["chips", 'salt']) #Add multiple items in the end
print(shopping_List)

shopping_List.remove("bread") #Remove item
print(shopping_List)

print(shopping_List.pop()) #Remove the last item in the list
print(shopping_List)

shopping_List.sort() #order it in ascending order
print(shopping_List)







my_list = [1, 2, 3, 4, True, 3.14, "Manibalan"]
print(type(my_list))
