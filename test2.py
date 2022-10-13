
def myfunction():
    print("function is running beep boop");



print("testing... beep boop")
# Lists


candy = input("what candy do you want?")
candylist = ["chocolate", "marshmallow", "m&m"] 
if candy == "chocolate":
    CT=input("choose dark or white")
    if CT="white":
        print "Okay, here is white chocolate"
    elif CT='dark':
        print "okay, here is dark chocolate"
    else:
        print"we do not have that"
elif candy == "m&m":
        MM=input("Do you want peanut butter or chocolate m&ms?") 
        if MM="peanut butter":
            print "Okay, here is the peanut butter m&m"
        elif MM="chocolate":
            print "Okay, here is the chocolate m&m"
elif candy == "marshmallow":
    print("okay, here are marshmallow")
else: 
    print("We do not have anything else")
    

myfunction()


