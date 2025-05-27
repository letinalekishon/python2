# mydstask.py

my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency": "KES"}], 987, (76, "John")]

# 1. Print KES
print("1:", my_ds[3][2]["currency"])

# 2. Print 560
print("2:", my_ds[2])

# 3. Print Maths
print("3:", my_ds[3][1])

# 4. Add another key “amount” with value 90
my_ds[3][2]["amount"] = 90
print("4:", my_ds[3][2])

# 5. Reverse 987 to 789 without using an inbuilt method or assigning manually
num = my_ds[4]
reversed_num = int(str(num)[::-1])
print("5:", reversed_num)

# 6. Change the name “John” to “Jane”
my_ds[5] = (my_ds[5][0], "Jane")
print("6:", my_ds[5])



x=(560)
print(type(x))