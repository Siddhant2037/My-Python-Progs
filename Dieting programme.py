try:
    def getdate():
        import datetime
        return datetime.datetime.now()
    t=getdate()
    num=int(input("Who are you?\nPress 1 for Siddhant\nPress 2 for Rupesh\nPress 3 for Sanjana"))
    #for siddhnat1
    if num==1:
        num2=str(input("Do you want to add or retrive?"))
        if num2=="add":
            num3 =str(input("exercise or food ?"))
            if num3=="exercise":
                f=open("siddhant.txt","a")
                f.write(str(t,))
                f.write(str(input("what do you Exercised today?")))
                print("Your data is added successfully")
                f.close()
            elif num3=="food":
                f=open("siddhant.txt", "a")
                f.write(str(t,))
                f.write(str(input("what do you eat today?")))
                print("Your data is added successfully")
                f.close()
            else:
                print("invalid syntes please check again")
        elif num2=="retrive":
            f=open("siddhant.txt","r")
            print(f.read())
            f.close()
            print("Thankyou for using our sooftwere")

    #for rupesh
    elif num==2:
        num5 = str(input("Do you want to add or retrive?"))
        if num5=="add":
            num4 =str(input("exercise or food ?"))
            if num4=="exercise":
                f=open("Rupesh.txt","a")
                f.write(str(t,))
                f.write(str(input("what do you Exercised today?")))
                f.close()
            elif num4=="food":
                f=open("Rupesh.txt", "a")
                f.write(str(t,))
                f.write(str(input("what do you eat today?")))
                print("Your data is added successfully")
                f.close()
            print("Thankyou for using our sooftwere")

            else:
                print("invalid syntes please check again")
        elif num5=="retrive":
            f=open("Rupesh.txt","r")
            print(f.read())
            f.close()

        # for Sanjan
    elif num==3:
        num6 = str(input("Do you want to add or retrive?"))
        if num6=="add":
            num7 =str(input("exercise or food ?"))
            if num7=="exercise":
                f=open("Sanjana.txt","a")
                f.write(str(t,))
                f.write(str(input("what do you Exercised today?")))
                print("Your data is added successfully")
                f.close()
            elif num7=="food":
                f=open("Sanjana.txt", "a")
                f.write(str(t,))
                f.write(str(input("what do you eat today?")))
                print("Your data is added successfully")
                f.close()
            else:
                print("invalid syntes please check again")
        elif num6=="retrive":
            f=open("Sanjana.txt","r")
            print(f.read())
            f.close()
            print("Thankyou for using our sooftwere")
else:
        print("thank")
except Exception as e:
    print("something went wrong")
