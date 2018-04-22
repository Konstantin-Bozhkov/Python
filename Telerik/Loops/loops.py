# While loop - run until the condition turn to false 
money = 12;
while money > 0:
    print("Go shopping");
    money -=1;

# For loops
items = ["pear","orange", "banana","kiwi",1,2,3,"car","house","holiday"];
for i in items:
    print(i);

print("------");

# For loops with range
# PHP version: for($i = 0; $i < 10; $i++)
for i in range(len(items)):
    print(items[i]);

# Enumarates - returns the item and its index
print(list(enumerate(items)));

# List comprehensions
# Instead of using this like most of the languages:
nums = [1,2,3,4]
for i in nums:
    print(i**2)
# In Python you can use some shortcuts
print( [i**2 for i in nums] );

#you can even add some conditions
print( [i**2 for i in nums if i % 2] );
print( [i**2 for i in nums if i > 2] );