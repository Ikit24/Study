name = input("Type your name: ")
print("welcome", name, "to this adventure!")

answer = input("""
You are on a dirt road, it has come to an end and you can go left or right.
Which way do you want to go?
               """).lower()

if answer == "left":
    answer = input("""
You come to a river, you can walk around it or swim across.
Type walk to walk around and swim to swim across: 
                   """)
    
    if answer == "swim":
        print("""
You swam across and were eaten by an alligator!
              """)

    elif answer == "walk":
        print("""
              You walked for many miles, ran out of water and died.
              """)

    else:
        print("Not a valid option. You loose.")
        quit()

elif answer == "right":
    answer = input("""
You come to a bridge, it looks woobly do you want to cross?
Do you want to corss it or head back?(cross/back)                   
                   """)
    
    if answer == "back":
        print("""
You go back and loose.
              """)

    elif answer == "cross":
        answer = input("""
You cross the bridge and meet a stranger. Do you talk to them?
(Yes/No)
                       """)
        if answer == "yes":
            print("""
You talk to the stranger and they give you a gold coin.
You WON!                  
                  """)
            quit()

        elif answer == "no":
            print("""
You ignore the stranger and as soon as you turn your back, he kills you.
You lost!
                    """)
            quit()

        else:
            print("Not a valid option. You loose.")

    else:
        print("Not a valid option. You loose.")
        quit()

else:
    print("Not a valid option. You loose.")

