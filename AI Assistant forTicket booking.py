import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Welcome To Bhiravnath Tours And Travels \n\n ")
        speak("Welcome To Bhiravnath Tours And Travels\n\nIam an AI softwere mister siddhant has created me")
        print("Do you want to see the previous reservation made by people yes or no?")
        speak("Do you want to see the previous reservation made by people yes or no?")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        imp = r.recognize_google(audio, language='en-in')
        print(f"User said: {imp}\n")
        if 'yes' in imp:
            def takeCommand2():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Which reservations would you like to see. Aeroplane. railways.or Bus")
                    print("Listening...")
                    r.pause_threshold = 1
                    audio = r.listen(source)

                try:
                    print("Recognizing...")
                    imp2= r.recognize_google(audio, language='en-in')
                    print(f"User said: {imp2}\n")
                    if 'bus' in imp2 :
                        f = open("bus.txt", "r")
                        print(f.read())
                        with open("bus.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 4:
                                speak(f"Reservations left are={4 - a}")
                            else:
                                speak("no more reservations today")

                    elif 'aeroplane' in imp2:
                        f = open("aeroplane.txt", "r")
                        print(f.read())
                        with open("aeroplane.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 280:
                                speak(f"Reservations left are={280 - a}")
                            else:
                                speak("no more reservations today")
                                breakpoint()
                    elif 'railway' in imp2 :
                        f = open("railway.txt", "r")
                        print(f.read())
                        with open("railway.txt", "r") as f:
                            a = (len(f.readlines()))  # This would give length of files.
                            if a < 400:
                                speak(f"Reservations left are= {400 - a}")
                            else:
                                speak("no more reservations today")
                    speak("thank you")

                    speak("Thank you")
                except Exception as e:
                    print("Say that again please...")
                    return "None"
                return imp2

            if __name__ == "__main__":
                takeCommand2()
        else:
            def takeCommand3():
                r = sr.Recognizer()
                with sr.Microphone() as source:

                    speak(" which Means of transportatinon do you want to choose to travel  via Bus.  Aeroplane. or via Railway")
                    print("Listening...")
                    r.pause_threshold = 1
                    audio = r.listen(source)

                try:
                    print("Recognizing...")
                    in1= r.recognize_google(audio, language='en-in')
                    print(f"User said: {in1}\n")
                    # for bus
                    if 'bus' in in1:
                        def takeCommand4():
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print("On which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
                                speak("on which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
                                print("Listening...")
                                r.pause_threshold = 1
                                audio = r.listen(source)

                            try:
                                print("Recognizing...")
                                in2 = r.recognize_google(audio, language='en-in')
                                print(f"User said: {in2}\n")
                                if 'Pune'or'Dhule'or'Nashik'or'A.nagar'or'Mumbai'or'Goa'or'Ganpatipule' in in2:
                                    speak("Which Class:-\nPress 1 for First class Prise of one ticket[500]\nPress 2 for Second class Prise of one ticket[250]\nPress 3 for Third class Prise of one ticket[100]")
                                    in3 = int(input("Which Class:-\nPress 1 for First class Prise of one ticket[500]\nPress 2 for Second class Prise of one ticket[250]\nPress 3 for Third class Prise of one ticket[100]"))
                                    if in3 == 1:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            n = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while n <= in5:
                                                with open("bus.txt", "r") as f:
                                                    a = (len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        n = n + 1
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("bus.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        speak("no more reservations today")

                                                        print("no more reservations today")
                                                        break
                                                    if n > in5:
                                                        speak(f"Total Payable amount is\t={ in5 * 500}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                        print(f"Total Payable amount=", in5 * 500,
                                                              "\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                    elif in3 == 2:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(
                                            input("Do you want to conform your tickets yes or no?"))
                                        if in4 == 'yes':
                                            no = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while no <= in5:
                                                with open("bus.txt", "r") as f:
                                                    a = (
                                                        len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        no = no + 1
                                                        speak("Reservations left are={10 - a")
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("bus.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 4:
                                                        speak(
                                                            f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break
                                                    else:
                                                        print("no more reservations today")
                                                    if no > in5:
                                                        print(f"Total Payable amount=", in5 * 250,
                                                              "\nYour seats are reserved successfully\n\nThankyou for choosing our platform")

                                    elif in3 == 3:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(
                                            input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            no = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while no <= in5:
                                                with open("bus.txt", "r") as f:
                                                    a = (
                                                        len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        no = no + 1
                                                        speak("Reservations left are={10 - a")
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("bus.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(
                                                            f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        print("no more reservations today")
                                                    if no > in5:
                                                        print(f"Total Payable amount=", in5 * 100,
                                                              "\nYour seats are reserved successfully\n\nThankyou for choosing our platform")




                            except Exception as e:
                                # print(e)
                                print("Say that again please...")
                                return "None"
                            return in2

                        if __name__ == "__main__":
                            takeCommand4()


                    # for aerolpane
                    elif 'aeroplane' in in1:
                        def takeCommand5():
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print("On which Destination do you want to visti \tHonkong\nParis\nU.S.A\nLondan\nBrazil\nRussia\nChina\n")
                                speak("on which Destination do you want to visit  \tHonkong\nParis\nU.S.A\nLondan\nBrazil\nRussia\nChina\n")
                                print("Listening...")
                                r.pause_threshold = 1
                                audio = r.listen(source)

                            try:
                                print("Recognizing...")
                                in2 = r.recognize_google(audio, language='en-in')
                                print(f"User said: {in2}\n")
                                if 'Honkong'or'paris'or'USA'or'londan'or'brazil'or'russia'or'China' in in2:
                                    speak("Which Class:-\nPress 1 for First class Prise of one ticket[18000]\nPress 2 for Second class Prise of one ticket[9000]\nPress 3 for Third class Prise of one ticket[5000]")
                                    in3 = int(input("Which Class:-\nPress 1 for First class Prise of one ticket[18000]\nPress 2 for Second class Prise of one ticket[9000]\nPress 3 for Third class Prise of one ticket[5000]"))
                                    if in3 == 1:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            n = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while n <= in5:
                                                with open("aeroplane.txt", "r") as f:
                                                    a = (len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        n = n + 1
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("aeroplane.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        speak("no more reservations today")

                                                        print("no more reservations today")
                                                        break
                                                    if n > in5:
                                                        speak(f"Total Payable amount is\t=", in5 * 18000,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                        print(f"Total Payable amount=", in5 * 18000,
                                              "\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                    if in3 == 2:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            n = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while n <= in5:
                                                with open("aeroplane.txt", "r") as f:
                                                    a = (len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        n = n + 1
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("aeroplane.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        speak("no more reservations today")

                                                        print("no more reservations today")
                                                        break
                                                    if n > in5:
                                                        speak(f"Total Payable amount is\t= {in5 * 9000}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                        print(f"Total Payable amount=", in5 * 9000,
                                                              "\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                    if in3 == 3:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            n = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while n <= in5:
                                                with open("aeroplane.txt", "r") as f:
                                                    a = (len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        n = n + 1
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("aeroplane.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        speak("no more reservations today")

                                                        print("no more reservations today")
                                                        break
                                                    if n > in5:
                                                        speak(f"Total Payable amount is\t=", in5 * 5000,"\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                        print(f"Total Payable amount=", in5 * 5000,
                                                              "\nYour seats are reserved successfully\n\nThankyou for choosing our platform")










                            except Exception as e:
                                # print(e)
                                print("Say that again please...")
                                return "None"
                            return in2

                        if __name__ == "__main__":
                            takeCommand5()



 #for railways

                    elif 'Railway' in in1:
                        def takeCommand6():
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print("On which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
                                speak("on which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
                                print("Listening...")
                                r.pause_threshold = 1
                                audio = r.listen(source)

                            try:
                                print("Recognizing...")
                                in2 = r.recognize_google(audio, language='en-in')
                                print(f"User said: {in2}\n")
                                if 'Pune' or 'Dhule' or 'Nashik' or 'A.nagar' or 'Mumbai' or 'Goa' or 'Ganpatipule' in in2:
                                    speak(
                                        "Which Class:-\nPress 1 for First class Prise of one ticket[750]\nPress 2 for Second class Prise of one ticket[500]\nPress 3 for Third class Prise of one ticket[300]")
                                    in3 = int(input(
                                        "Which Class:-\nPress 1 for First class Prise of one ticket[750]\nPress 2 for Second class Prise of one ticket[500]\nPress 3 for Third class Prise of one ticket[300]"))
                                    if in3 == 1:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            n = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while n <= in5:
                                                with open("railway.txt", "r") as f:
                                                    a = (len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        n = n + 1
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("railway.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(
                                                            f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        speak("no more reservations today")

                                                        print("no more reservations today")
                                                        break

                                                    if n > in5:
                                                        speak(f"Total Payable amount is\t={in5 * 750}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                        print(f"Total Payable amount={in5 * 750}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                    if in3 == 2:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            n = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while n <= in5:
                                                with open("railway.txt", "r") as f:
                                                    a = (len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        n = n + 1
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("railway.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(
                                                            f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        speak("no more reservations today")

                                                        print("no more reservations today")
                                                        break

                                                    if n > in5:
                                                        speak(f"Total Payable amount is\t={in5 * 500}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                        print(f"Total Payable amount={in5 * 500}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                    if in3 == 3:
                                        speak("do you want to confirm your tickets type yes or no")
                                        in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                        if in4 == 'yes':
                                            n = 1
                                            speak("enter the number of tickets you want to buy")
                                            in5 = int(input("How many tickets do you want to book?"))
                                            while n <= in5:
                                                with open("railway.txt", "r") as f:
                                                    a = (len(f.readlines()))  # This would give length of files.
                                                    if a < 10:
                                                        speak("enter names of passengars")
                                                        ou1 = str(input(f"Enter your name no"))
                                                        n = n + 1
                                                        print(f"Reservations left={10 - a}")
                                                        f = open("railway.txt", "a")
                                                        f.write(f"\n{a}]{ou1}")
                                                        f.close()
                                                    elif a == 10:
                                                        speak(
                                                            f"opps so sorry sir no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        print(
                                                            f"no more reservations today\nTotal reservations={a}\nRemaining reservations={10 - a}")
                                                        break

                                                    else:
                                                        speak("no more reservations today")

                                                        print("no more reservations today")
                                                        break

                                                    if n > in5:
                                                        speak(f"Total Payable amount is\t={in5 * 300}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                        print(f"Total Payable amount={in5 * 300}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")









                            except Exception as e:
                                # print(e)
                                print("Say that again please...")
                                return "None"
                            return in2
                        if __name__ == "__main__":
                            takeCommand6()





                except Exception as e:
                    print("Say that again please...")
                    return "None"
                return in1

            if __name__ == "__main__":
                wishMe()
                takeCommand3()


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return imp
if __name__ == "__main__":
    wishMe()
    takeCommand()
