# 1. Modify numbers tuple
numbers = (10, 20, 30, 40, 50)
numbers_list = list(numbers)
numbers_list[2] = 35  # Replace 30 with 35
numbers_list.append(60)  # Add 60 to the end
numbers = tuple(numbers_list)
print("1. Modified numbers:", numbers)

# 2. Arrange values in ascending order
values = (15, 5, 30, 25, 10)
values_sorted = tuple(sorted(values))
print("2. Sorted values:", values_sorted)

# 3. Count and remove "banana"
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
banana_count = fruits.count("banana")
fruits_filtered = tuple(fruit for fruit in fruits if fruit != "banana")
print("3. Count of 'banana':", banana_count)
print("   Fruits without 'banana':", fruits_filtered)

# 4. Reverse names using sort (not ideal but doable)
names = ("Alice", "Bob", "Charlie", "David")
names_list = list(names)
names_list.sort(reverse=True)  # Sort descending (reverse alphabetical order)
names = tuple(names_list)
print("4. Reversed names (using sort):", names)

# 5. Add "yellow" at index 1 and extend
colors = ("red", "blue", "green")
colors_list = list(colors)
colors_list.insert(1, "yellow")  # Add at index 1
colors_list.extend(["purple", "orange"])
colors = tuple(colors_list)
print("5. Updated colors:", colors)
