# Lists
a = [1,23,"abc",4,5];

# List + List
b = [1,2,3];
c = a + b;
print(c);

# remove last index from the list
a.pop();
# remove element by index
a.pop(2)
print (a);

# append to the list
a.append("abc");
print(a);

# Insert into index
a.insert(1,"def");
print(a);

# Array or string length
print(len(c));

# Slice from:to
d = c[3:6];
print(c);
print(d);

# Slice from start
d = c[:3];
print(d);

# slice to end
d = c[3:];
print(d);

# Copy an array
e = c[:];
print(e);

# sort array
f = [23,4,2,1,55,223]
f.sort();
print(f)

# make a sorted copy
g = sorted(f);
print(g);

# append n times an arrays
h = g * 2
print(h);

# === Tuples ===
# tuple is immutable
# typle is almost as the lists
j = (1,2,3,4);
j = (2,) + j[2:]


# Set in alphabetical order
basket = ['oranges','bananas','apple','kiwi','pear'];
print(sorted(set(basket)));
print( sorted(list(set(basket))));