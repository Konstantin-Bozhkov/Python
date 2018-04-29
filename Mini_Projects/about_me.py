def say(message):
    print(message)
    
def say_wellcome(user = "",age = 0, location = "" ,withAge = False):
    
    if withAge:
        return say("%s I see you are %s years old and you are from %s " % (user,age,location));
    return say("Hello %s , and wellcome to Python" % user)

username = "User"
location = "LA"
age = 18

def ask_user(q_type):
    global username;
    global age;
    global location;
    
    while True:
        if q_type == "name":
            say("What is your name?")
            username = input("My name is ")
            # Stop the current while loop and ask again with LOCATION question
            if username.isalpha():
                say_wellcome(username)
                ask_user("location")
                return;
            else: say("Invalid name, please try again")
        elif q_type == "location":
            say("Where are you from?");
            location = input("I am from ");
             # Stop the current while loop and ask again with AGE question
            if location.isalpha():
                ask_user("age")
                return
            else: say("Invalid location string, please try again!");
        elif q_type == "age":
            say("How old are you?")
            age = input("I am ")
             # Stop the current while loop and print the result
            if age.isdigit():
                say_wellcome(username,age,location,True);
                return
            else: say("Invalid age, please try again")
        
ask_user("location")