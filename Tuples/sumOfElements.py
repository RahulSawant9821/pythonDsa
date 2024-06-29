

total =0
list_Of_Numbers=[]
while True:
    
    items = input("Enter the numbers or enter done to exit:")

    if items.lower() == "done":
        break
    else:
        try:
            list_Of_Numbers.append(int(items))
            tuple_ = tuple(list_Of_Numbers)
            print(tuple_)
            total+=int(items)
            print(total)
        except ValueError:
            print("Incorrect Value entered")
