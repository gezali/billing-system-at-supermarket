while True:
    name = input("Enter your name : ")
    num = (int(input("Enter your number : ")))
    email = (input("Enter your email : "))
    total = 0

    while True:
        print("Enter the amount and quantity")
        amount = (float(input("Enter the amount : ")))
        quantity = (float(input("Enter the quantity : ")))
        total += amount * quantity
        repeat = (input("Do you want to add more items ? (yes/no): "))
        if repeat == "no" or repeat =="No":
            break
    print("-"*40)
    print("Name :" ,name)
    print("Number : ", num)
    print("Email : ", email)
    print("The total amount to be paid : ", total)
    print("-" * 40)
    print("**** Happy shopping ****")

    repeat1 = input("Do you want to go to the next customer ? Yes / no : ")
    if repeat1 == "no" or repeat1== "No":
        break