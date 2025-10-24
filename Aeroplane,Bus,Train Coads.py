try:
    print("Welcome To Bhiravnath Tours And Travels\n\n")
    imp=str(input("Do you want to see the previous reservation made by people yes or no?"))
    #for bus
    if 'yes' in imp:
        imp2=str.capitalize(input("Which one do you want to see Bus,Aeroplan,Railway?"))
        if imp2=="Bus":
            f=open("bus.txt","r")
            print(f.read())
            with open("bus.txt", "r") as f:
                a = (len(f.readlines()))  # This would give length of files.
                if a<4:
                    print(f"Reservations left={4-a}")
                else:
                    print("no more reservations today")

        elif imp2=="aeroplane":
            f = open("aeroplane.txt", "r")
            print(f.read())
            with open("aeroplane.txt", "r") as f:
                a = (len(f.readlines()))  # This would give length of files.
                if a<280:
                    print(f"Reservations left={280-a}")
                else:
                    print("no more reservations today")
                    breakpoint()
        elif imp2=="railway":
            f = open("railway.txt", "r")
            print(f.read())
            with open("railway.txt", "r") as f:
                a = (len(f.readlines()))  # This would give length of files.
                if a<400:
                    print(f"Reservations left={400-a}")
                else:
                    print("no more reservations today")
    in1=int(input("Means of transportatinon to travel are as followes\nPress 1 To travel via Bus\nPress 2 to travel via Aeroplane\nPress 3 To travel via Railway"))
    #for bus
    if in1==1:
       in2=int(input("Destinations are availablem are as followes\n1]Pune\n2]Dhule\n3]Nashik\n4]A.nagar\n5]Mumbai\n6]Goa\n6]Ganpatipule\nSelect one of the destination mentioned above to travel"))
       print("Thankyou for your responce!")
       if in2<7:
           in3=int(input("Which Class:-\nPress 1 for First class Prise of one ticket[500]\nPress 2 for Second class Prise of one ticket[250]\nPress 3 for Third class Prise of one ticket[100]"))
           if in3==1:
               in4=str(input("Do you want to confirm your tickets Yes or No ?"))
               if in4=='yes':
                   n=1
                   in5=int(input("How many tickets do you want to book?"))
                   while n<=in5:
                       with open("bus.txt", "r") as f:
                           a=(len(f.readlines()))  # This would give length of files.
                           if a<10:
                               ou1 = str(input(f"Enter your name no"))
                               n = n + 1
                               print(f"Reservations left={10-a}")
                               f = open("bus.txt", "a")
                               f.write(f"\n{a}]{ou1}")
                               f.close()
                           elif a==10:
                               print(f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10-a}")
                               break

                           else:
                               print("no more reservations today")
                           if n>in5:
                               print(f"Total Payable amount=",in5*500,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")

           if in3==2:
               in4=str(input("Do you want to confirm your tickets Yes or No ?"))
               if in4=='yes':
                   no=1
                   in5=int(input("How many tickets do you want to book?"))
                   while no<=in5:
                       with open("bus.txt", "r") as f:
                           a=(len(f.readlines()))  # This would give length of files.
                           if a<10:
                               ou1 = str(input(f"Enter your name no"))
                               no= no + 1
                               print(f"Reservations left={10-a}")
                               f = open("bus.txt", "a")
                               f.write(f"\n{a}]{ou1}")
                               f.close()
                           elif a==4:
                               print(f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10-a}")
                               break
                           else:
                               print("no more reservations today")
                           if no>in5:
                               print(f"Total Payable amount=",in5*250,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")

           if in3==3:
               in4=str(input("Do you want to confirm your tickets Yes or No ?"))
               if in4=='yes':
                   no=1
                   in5=int(input("How many tickets do you want to book?"))
                   while no<=in5:
                       with open("bus.txt", "r") as f:
                           a=(len(f.readlines()))  # This would give length of files.
                           if a<10:
                               ou1 = str(input(f"Enter your name no"))
                               no= no + 1
                               print(f"Reservations left={10-a}")
                               f = open("bus.txt", "a")
                               f.write(f"\n{a}]{ou1}")
                               f.close()
                           elif a==10:
                               print(f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10-a}")
                               break

                           else:
                               print("no more reservations today")
                           if no>in5:
                               print(f"Total Payable amount=",in5*100,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")

    #for aerolpane
    elif in1==2:
        in6= int(input(
            "Destinations are availablem are as followes\n1]Honkong\n2]Paris\n3]U.S.A\n4]Londan\n5]Brazil\n6]Russia\n6]China\nSelect one of the destination mentioned above to travel"))
        print("Thankyou for your responce!")
        if in6<7:
            in7 = int(input(
                "Which Class:-\nPress 1 for First class Prise of one ticket[18000]\nPress 2 for Second class Prise of one ticket[9000]\nPress 3 for Third class Prise of one ticket[5000]"))
            if in7==1:
                in8= str(input("Do you want to confirm your tickets Yes or No ?"))
                if in8 == 'yes':
                    no = 1
                    in9=int(input("How many tickets do you want to book?"))
                    while no<=in9:
                        with open("aeroplane.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a <10:
                                ou1 = str(input(f"Enter your name no"))
                                no = no + 1
                                print(f"Reservations left={10- a}")
                                f = open("bus.txt", "a")
                                f.write(f"\n{a}]{ou1}")
                                f.close()
                            elif a ==10:
                                print(
                                    f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10- a}")
                                break

                            else:
                                print("no more reservations today")
                            if no > in9:
                                print(f"Total Payable amount=",in9*18000,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
            elif in7==2:
                in8= str(input("Do you want to confirm your tickets Yes or No ?"))
                if in8 == 'yes':
                    no = 1
                    in9 = int(input("How many tickets do you want to book?"))
                    while no <= in9:
                        with open("aeroplane.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 10:
                                ou1 = str(input(f"Enter your name no"))
                                no= no + 1
                                print(f"Reservations left={10 - a}")
                                f = open("bus.txt", "a")
                                f.write(f"\n{a}]{ou1}")
                                f.close()
                            elif a == 10:
                                print(
                                    f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                break

                            else:
                                print("no more reservations today")

                            if no > in9:
                                print(f"Total Payable amount=", in9*9000,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
            elif in7==3:
                in8= str(input("Do you want to confirm your tickets Yes or No ?"))
                if in8 == 'yes':
                    no = 1
                    in9 = int(input("How many tickets do you want to book?"))
                    while no <= in9:
                        with open("aeroplane.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 10:
                                ou1 = str(input(f"Enter your name no"))
                                no = no + 1
                                print(f"Reservations left={10 - a}")
                                f = open("bus.txt", "a")
                                f.write(f"\n{a}]{ou1}")
                                f.close()
                            elif a == 10:
                                print(
                                    f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                break

                            else:
                                print("no more reservations today")

                            if no>in9:
                                print(f"Total Payable amount=", in9*5000,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
    #for railway
    elif in1==3:
        in10= int(input(
            "Destinations are availablem are as followes\n1]Pune\n2]Dhule\n3]Nashik\n4]A.nagar\n5]Mumbai\n6]Goa\n6]Ganpatipule\nSelect one of the destination mentioned above to travel"))
        print("Thankyou for your responce!")
        if in10 < 7:
            in11= int(input("Which Class:-\nPress 1 for First class Prise of one ticket[750]\nPress 2 for Second class Prise of one ticket[500]\nPress 3 for Third class Prise of one ticket[300]"))
            if in11==1:
                in12 = str(input("Do you want to confirm your tickets Yes or No ?"))
                if in12 == 'yes':
                    no = 1
                    in13 = int(input("How many tickets do you want to book?"))
                    while no<=in13:
                        with open("railway.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 20:
                                ou1 = str(input(f"Enter your name no"))
                                no = no + 1
                                print(f"Reservations left={20 - a}")
                                f = open("railway.txt", "a")
                                f.write(f"\n{a}]{ou1}")
                                f.close()
                            elif a ==20:
                                print(
                                    f"no more reservations today\nTotal reservations={a}\nRemaining reservations={20- a}")
                                break

                            else:
                                print("no more reservations today")

                            if no > in13:
                                print(f"Total Payable amount=", in13 *750,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
            elif in11 == 2:
                in12 = str(input("Do you want to confirm your tickets Yes or No ?"))
                if in12 == 'yes':
                    no = 1
                    in13 = int(input("How many tickets do you want to book?"))
                    while no <= in13:
                        with open("railway.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 20:
                                ou1 = str(input(f"Enter your name no"))
                                no = no + 1
                                print(f"Reservations left={20 - a}")
                                f = open("railway.txt", "a")
                                f.write(f"\n{a}]{ou1}")
                                f.close()
                            elif a ==20:
                                print(f"no more reservations today\nTotal reservations={a}\nRemaining reservations={20- a}")
                                break

                            else:
                                print("no more reservations today")

                            if no > in13:
                                print(f"Total Payable amount=", in13 * 500,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
            elif in11==3:
                in12 = str(input("Do you want to confirm your tickets Yes or No ?"))
                if in12 == 'yes':
                    no = 1
                    in13 = int(input("How many tickets do you want to book?"))
                    while no<=in13:
                        with open("railway.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 20:
                                ou1 = str(input(f"Enter your name no"))
                                no = no + 1
                                print(f"Reservations left={20 - a}")
                                f = open("railway.txt", "a")
                                f.write(f"\n{a}]{ou1}")
                                f.close()
                            elif a ==20:
                                print(
                                    f"no more reservations today\nTotal reservations={a}\nRemaining reservations={20- a}")
                                break

                            else:
                                print("no more reservations today")
                        if no > in13:
                            print(f"Total Payable amount=", in13 * 300,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
except Exception as e:
    print("something went wrong")

