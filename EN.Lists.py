name = "Edward"

subjects = ["English","Math","Science","History","Mandarin"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)

tennisplayers = ["Djokovic","Kyrgios","Sock","Tiafoe","Edmund","Murray"]

for i in tennisplayers:
    if i == "Murray":
        print(i + " is my least favorite tennis player.")
    elif i == "Sock":
        print(i + " is the best tennis player in the country. ")
    else:
        print("One of my favorite tennis players is " + i)


sports = []

while True:
    print("What sport do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break

    else:
        sports.append(answer)


for i in sports:
    print("One of your favorite sports is " +i)
        














