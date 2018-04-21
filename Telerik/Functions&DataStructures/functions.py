def say(message1,message2 = "World"):
    print(message1);
    print(message2);
    return "Ok";

# normal call
say("hello","kosio");

# call with exact variable replacements
say(message2="hello",message1 = "Kosio");
