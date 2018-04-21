def say(msg):
    print(msg);

def say_welcome(player = "Player"):
    say("Hello %s and Welcome to our Casino" % player);


# If not main file dont run;
# Main function similar to C#
if __name__ == "__main":
    say_welcome();