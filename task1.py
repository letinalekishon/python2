# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57


temp = 56.8926
temp_int = round(temp)
print(temp_int)  


# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 

temp = 56.8926
rounded_temp = round(temp, 2)
print(rounded_temp)


# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 

temp = 56.8926
rounded_temp = round(temp, 3)
print(rounded_temp) 


# Convert the float below to give the results as follows
# temp=56.8926 to 8.926

temp = 56.8926
temp_str = str(temp)
# Remove the '5' and take from index 1 to 5 ('6.892')
new_str = temp_str[1:6] + temp_str[6]
result = float(new_str)
print(result)  


# temp = 111.0789 to 78.9

temp = 111.0789
temp = str(temp)
tenp=temp[5]
temp=temp[0:2]+"."
print(result)







