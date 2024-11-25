import os
import random

os.system("cls")

while True:
    try:
        num = int(input("input any number: "))
        break
    except:
        print("use numbers")

os.system("cls")

print("do you think the next number will be higer or lower than \"x\"\n")
while True:
    random_number = random.randint(1, 12)
    hig_low = input(f"higher \"h\" / lower \"l\" than {random_number} ").lower()
    new_number = random.randint(1, 12)
    while True:
        if new_number == random_number:
            new_number = random.randint(1, 12)
        else:
            break
    if random_number > new_number and hig_low == "l":
        print(f"correct, {new_number} is lower than {random_number}\n")
    elif random_number < new_number and hig_low == "h":
        print(f"correct, {new_number} is higher than {random_number}\n")
    else:
        if hig_low == "q":
            print("you quit")
            break
        elif random_number > new_number and hig_low != "l":
            print(f"your wrong, {new_number} is lower then {random_number}\n")
        elif random_number < new_number and hig_low != "h":
            print(f"your wrong, {new_number} is higher then {random_number}\n")
        elif random_number == new_number:
            print("random_number is = new_number")

word = input("word: ")
print(word[:10])

word_2 = input("word_2: ")
if len(word_2) > 10:
    print(word_2[:10] + "...")
else:
    print(word_2)