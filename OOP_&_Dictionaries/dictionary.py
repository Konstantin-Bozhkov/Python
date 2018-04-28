# Init dictionary
d = {
    "name":"Chuck",
    "age":"50",
    "nationality":"Amerikan",
    "drink":"water",
    True:False
};
print(d["name"]);

# Add elements
d["last_name"] = "Noris";

#Delete element
del d[True];
d.pop("drink");

print(d);

# Set a default value if the key is missing
drink = d.get("drink", "Beer");
print(drink)

# If there is no default value it will return None (null)
print(d.get("eat"))
print(d.get("eat") is None)


d2 = {
    "name":"Rambo",
    "age":70,
    "eat":"rice"
      };

# Update d with d2
# if there are key confilicts, the updating dictionary wins
d.update(d2);
print(d)


# Generate a dictionary from an array
basket = ["banana","apple","kiwi","orange"];
dict_basket = dict( [ (a,b) for a,b in enumerate(basket) ] );
print(dict_basket)

# Populate dictionaries
# Set a default value (0) for dictionary key if it doesn't exists and then increase it with one 
fruit_basket = ["banana","apple","apple","pear","banana","kiwi","apple"];
fruitcount = {};
for fruit in fruit_basket:
    fruitcount[fruit] = fruitcount.setdefault(fruit,0) + 1;
print(fruitcount);