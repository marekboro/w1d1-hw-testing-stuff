# As I have attempted some work on the list, dictonaries and For loops I will attempt both homeworks.
#
#Ask user which code will be used.
#
#
#

print("1: List")
user_list = []
print("2: Dictionarty")
user_dictionary={}
print("3: For loop")

input1 = input("Choose 1,2 or 3: ")

#starting with #4 as this is the actual homework.

if input1 == "1":
    print("You chose #1:")
    input_a = input("To exit type quit otherwise type a word: ")
    user_list.append(input_a)
    if input_a == "quit":
        print("quit typed, your list: ")
        print(user_list)
    else:
        input_b = input("type another word: ")
        user_list.append(input_b)
        print("your list: ")
        print(user_list)
      
elif input1 == "2":
    print("You chose #2:")
    input_x = input("Type in your faviourite colour: ")
    user_dictionary["favourite colour"] = input_x
    input_y = input("Type in your name: ")
    user_dictionary["name"] = input_y
    print("Your superhero name : " + user_dictionary["favourite colour"] + " " + user_dictionary["name"][::-1])
elif input1 == "3":
    print("You chose #3:")
    
    input_for_loop = input("type in a long word: ")
    for x in input_for_loop:
        print (x)

print("The end of the program")

