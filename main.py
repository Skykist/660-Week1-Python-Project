from colorama import init, Fore, Back
import random
import random_name

init()

print(Back.CYAN + Fore.YELLOW +"Hello, my name is",random_name.generate_name())
print(Back.BLACK+"Choose a number between 0 and a 100 and I'll try to guess it:")
choice = input()
x = random.randint(0, 101)
print("I guessed ", x)

if choice == x:
    print(Back.GREEN + "Hey, I got it!")
else:
    print(Back.RED + "Darn, I'll get it next time.")