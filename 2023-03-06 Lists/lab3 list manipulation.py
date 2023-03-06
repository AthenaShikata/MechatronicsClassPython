# Python Manipulating Lists
# Change the title/name of this Replit, so it is in your named Replit Directory

print('''
Manipulating Lists by slicing them

Change the title/name of this Replit, so it is in your 
named Replit Directory

Challenge #1
      ''')
# Add a Comment Here to describe what you are doing
my_string = 'Babylon_5'
my_list = ['B','a','b','y','l','o','n','_','5']
print(my_string)
print(my_list)

print('''Print some index ranges 
Remember that you start index at '0', so you 
have the 0th, 1st, 2nd, 3rd... index values

Print the following:
# 3rd to 5th (not including the 6th)
# beginning up to but not including the 4th
# 6th to end
# beginning to end      
      
# Enter Your Code Here:
      ''')
# Enter Your Code Here:
# 3rd to 5th (not including the 6th)
print(my_list[3:6])
# beginning up to but not including the 4th
print(my_list[:-5])
# 6th to end
print(my_list[5:])
# beginning to end
print(my_list[:])
# elements beginning up to but not including the 4th
print(my_list[:4])

print('''Challenge #2
Slice some index ranges 

# from my_list, slice elements beginning with 0th, up to but not including the 4th, and assign it to a new_list, then print the new list

# from my_list, slice elements from -4 to -2 and assign it to a new_list2, then print the new list2  
      
# Enter Your Code Here:
      ''')
# elements beginning with 0th, up to but not including the 4th
new_list=my_list[:4]
print(new_list)
# elements from -4 up to -2
new_list2 = my_list[-4:-2]
print(new_list2)
print('''Challenge #3
replace indexed values 

# change index[1] to 'pinapple'
      
# Enter Your Code Here:
      ''')
my_list = ["apple", "orange", "pomegranate"]
my_list[1] = "pinapple"
print(my_list)
# change index[1] to 'pinapple'