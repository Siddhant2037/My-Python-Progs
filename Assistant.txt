import pywhatkit
import subprocess
import os
import webbrowser
import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import googletrans

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def takeCommand2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")
        imp3 = r.recognize_google(audio, language='en-in')
    except Exception as a:
        # print(e)
        print("Say that again please...")
        return "None"
    return imp3


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Iam an AI softwere mister siddhant has created me \n\n ")
        speak("Hellow sir Iam an AI softwere mister siddhant has created me")
        print("how can I help you?")
        speak("how can I help you?")
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")
        imp = r.recognize_google(audio, language='en-in')
        print(f"User said: {imp}\n")


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return imp

if __name__ == "__main__":
    wishMe()
    if 1:
        imp = takeCommand().lower()
        #if "youtube" in imp:
           # webbrowser.open("http://www.youtube.com")
        if "open youtube and search" in imp:
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.by import By
            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager
            import time

            imp=imp.replace("open youtube and search","")

            # Initialize the Chrome WebDriver
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

            # Open the ChatGPT website
            driver.get("https://www.youtube.com/")
            time.sleep(5)
            driver.maximize_window()
            time.sleep(3)
            # Add a wait to ensure the page loads (you might need to adjust the timing)
            # Locate the input field for typing the query
            # Note: Update the XPath if necessary
            input_field = driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')  # Update the XPath to match the actual input field ID or class
            input_field.send_keys(imp)
            input_field.send_keys(Keys.ENTER)
            time.sleep(100000000)
        elif "spotify" in imp:
            os.system("spotify setup(1)")
        elif "vlc" in imp:
            subprocess.call('C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe')
        elif "wikipedia" in imp:
            speak("Serching wikipedia.....")
            imp = imp.replace("wikipedia", "")
            result = wikipedia.summary(imp, sentences=4)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "calculator" in imp:
            subprocess.call("calc.exe")
        elif "google" in imp:
            webbrowser.open("Google.com")
        elif "pycharm " in imp:
            os.startfile("C:\\Users\\Siddhant Tak\\Download")
        elif "send" in imp:
            def takeCommand2():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold = 0.6
                    audio = r.listen(source)
                try:
                    print("Recognizing...")
                    imp3= r.recognize_google(audio, language='en-in')
                except Exception as a:
                    # print(e)
                    print("Say that again please...")
                    return "None"
                return imp3
            if __name__ == "__main__":
                contacts={'Suvarna Amale	': '+917721005385', '919689020112	': '+919689020112',
                            'Aditi Deshmukh': '+917350970379',
                            'Anil amale': '+918308793287',
                            'Anupama Kankrej': '+917588556840',
                            'Atharva Harale': '+919850517794',
                            'Athie': '+917710824169',
                            '918805595653	': '+918805595653',
                            '919284717640	': '+919284717640',
                            '919881366530	': '+919881366530',
                            '917066036640	': '+917066036640',
                            'Sonali Bhor': '+919730563370',
                            'sapnilpk9@gmail.com': '+917887742067',
                            'Yash Sanap': '+919529424520',
                            'Chaitanya Shete': '+919420339631',
                            'Chaitanya': '+917020963739',
                            'Charu Katyare': '+919766946145',
                            'Chinmay': '+917378991117',
                            'aditya': '+919309404633',
                            'ganesh katyare': '+919421525864',
                            'Ganesh Bidve': '+919702013057',
                            'Hemant Mandlik': '+917798032827',
                            '918888141111	': '+918888141111',
                            '918778665718	': '+918778665718',
                            'MySeetFamily': '+919158476816',
                            'Jitendraade': '+919422945442',
                            'Krupesh Khambekar': '+919922419484',
                            '917972563316': '+917972563316',
                            '𝐊𝐮𝐥𝐝𝐢𝐩': '+919370770874',
                            'Maya Sonawane': '+917745854320',
                            'Mayur Katyare': '+918446597430',
                            'Nakul Dawkhar': '+919623522513',
                            'Santosh Dawkhar': '+919922400760',
                            'Kumudini Tak': '+917028232330',
                            '919404527074': '+919404527074',
                            '919921521681': '+919921521681',
                            'Mayur Tak': '+919850114367',
                            '919356183390': '+919356183390',
                            'Parth unde': '+919049923204',
                            'Rajendra Kankrej': '+919423017515',
                            'Ritesh Goyal': '+919021250661',
                            'Rohanade': '+919765354550',
                            '919527227776': '+919527227776',
                            'Rupesh Kankrej': '+919172148840',
                            '919766187781': '+919766187781',
                            'Sahil Patil': '+918788469075',
                            'Manisha Vaidya': '+919673762301',
                            'Sanjana Katyare': '+919309116408',
                            'Omkar Dhoot': '+919421151821',
                            'Shrutika wakchaure': '+919970376715',
                            'Soham Gaikad': '+919423276006',
                            'Satiade': '+919423971842',
                            'Tushar': '+917620886825',
                            'Vinod.agh': '+918605929816',
                            'tanavi daware': '+918177990053',
                            'SangitaDaware': '+917420805607',
                            'Sanika Jadhav': '+918999031789',
                            'Yash Sahane': '+918446186825',
                            'Aaditey Choudhary': '+918263029469',
                            'Ananya Jadhav': '+917758053092',
                            'Anuj': '+918468992349',
                            'Arif Mansuri': '+918087304502',
                            'Ashutosh': '+917498285132',
                            'Bandu Dhayapule': '+919448293316',
                            'Bhavesh Ugale22': '+917276288020',
                            'Bhavishyaare': '+918625813720',
                            'chandrashekhar': '+919860884836',
                            'Chaudhari Bajrang': '+919423388383',
                            'Chhaya Vijay Aher': '+919284475873',
                            'dattatraysupekar88': '+919921122416',
                            'dhamalelalita68': '+919960979266',
                            'dhatrakbhagvati': '+918975012240',
                            'haneef': '+919948676875',
                            'Javed Kagdi': '+919503827872',
                            'Jayesh Nemade': '+919860726264',
                            'Mahendra Pande': '+918275278914',
                            'Manoj Soni': '+919844548881',
                            'MinalPaar': '+918888832272',
                            'Mohit Jadhav': '+917066567063',
                            'najimtamboli2019': '+919890707866',
                            'Pooja Bedre': '+919730127277',
                            'Pranav Badgujar': '+91920934538',
                            'prarabdha Shelke': '+919860099972',
                            'rajeshkhambekar084': '+918805232345',
                            'Samrat': '+919579392626',
                            'sandeep shinde29010': '+919657251909',
                            'Sanjay Ambekar': '+919881623260',
                            'Sanjay Gujar': '+919890379531',
                            'Sarika Paar': '+917350002844',
                            'Shanthilal': '+918123549733',
                            'Sharad Kshatriya': '+919765165178',
                            'Siddhant Tak': '+919730134254',
                            'Smita Mate': '+917057899091',
                            'TejasShivajiGodase': '+919657644751',
                            'Tushar Chavan': '+918830153254',
                            'Vikrant Kaade': '+919921759059',
                            'Vilasak chaure': '+919822113184',
                            'yogeshchavanke145': '+917709404514',
                            'yogeshnikam2210': '+919890162795',
                            'YuvrajPaar': '+919172010334','mummy':'+917028232330','pappa':'+919850114367'}
                speak("To whom you want to send the message")
                print("To whom you want to send the message")
                s1= takeCommand2()
                print(f"user saif:{s1}")
                speak("What message do you want to send")
                print("What message do you want to send")
                s2=takeCommand2()
                print(f"user saif:{s2}")

                result=contacts.get(s1)
                print(f"sending to{result}")
                pywhatkit.sendwhatmsg_instantly(f"{result}",f"{s2}")



        elif "ticket booking" in imp:
            import pyttsx3
            import speech_recognition as sr
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
                if hour >= 0 and hour < 12:
                    speak("Good Morning!")

                elif hour >= 12 and hour < 18:
                    speak("Good Afternoon!")

                else:
                    speak("Good Evening!")


            def takeCommand():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Welcome To Bhiravnath Tours And Travels \n\n ")
                    speak(
                        "Welcome To Bhiravnath Tours And Travels\n\nIam an AI softwere mister siddhant has created me")
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
                                imp2 = r.recognize_google(audio, language='en-in')
                                print(f"User said: {imp2}\n")
                                if 'bus' in imp2:
                                    f = open("bus.txt", "r")
                                    print(f.read())
                                    with open("bus.txt", "r") as f:
                                        a = (len(f.readlines()))  # This would give length of files.
                                        if a < 4:
                                            speak(f"Reservations left are{4 - a}")
                                            print(f"Reservations left are={4 - a}")
                                        else:
                                            speak("no more reservations today")
                                            print("no more reservations today")

                                elif 'aeroplane' in imp2:
                                    f = open("aeroplane.txt", "r")
                                    print(f.read())
                                    with open("aeroplane.txt", "r") as f:
                                        a = (len(f.readlines()))  # This would give length of files.
                                        if a < 280:
                                            speak(f"Reservations left are{280 - a}")
                                            print(f"Reservations left are={280 - a}")
                                        else:
                                            speak("no more reservations today")
                                            print("no more reservations today")
                                            breakpoint()
                                elif 'railway' or 'Railway' in imp2:
                                    f = open("railway.txt", "r")
                                    print(f.read())
                                    with open("railway.txt", "r") as f:
                                        a = (len(f.readlines()))  # This would give length of files.
                                        if a < 400:
                                            speak(f"Reservations left are {400 - a}")
                                            print(f"Reservations left are= {400 - a}")
                                        else:
                                            speak("no more reservations today")
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
                                in1 = r.recognize_google(audio, language='en-in')
                                print(f"User said: {in1}\n")
                                # for bus
                                if 'bus' in in1:
                                    def takeCommand4():
                                        r = sr.Recognizer()
                                        with sr.Microphone() as source:
                                            print(
                                                "On which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
                                            speak(
                                                "on which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
                                            print("Listening...")
                                            r.pause_threshold = 1
                                            audio = r.listen(source)

                                        try:
                                            print("Recognizing...")
                                            in2 = r.recognize_google(audio, language='en-in')
                                            print(f"User said: {in2}\n")
                                            if 'Pune' or 'Dhule' or 'Nashik' or 'A.nagar' or 'Mumbai' or 'Goa' or 'Ganpatipule' in in2:
                                                speak(
                                                    "Which Class:-\nPress 1 for First class Prise of one ticket[500]\nPress 2 for Second class Prise of one ticket[250]\nPress 3 for Third class Prise of one ticket[100]")
                                                in3 = int(input(
                                                    "Which Class:-\nPress 1 for First class Prise of one ticket[500]\nPress 2 for Second class Prise of one ticket[250]\nPress 3 for Third class Prise of one ticket[100]"))
                                                if in3 == 1:
                                                    speak("do you want to confirm your tickets type yes or no")
                                                    in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                                    if in4 == 'yes':
                                                        n = 1
                                                        speak("enter the number of tickets you want to buy")
                                                        in5 = int(input("How many tickets do you want to book?"))
                                                        while n <= in5:
                                                            with open("bus.txt", "r") as f:
                                                                a = (
                                                                    len(f.readlines()))  # This would give length of files.
                                                                if a < 10:
                                                                    speak("enter names of passengars")
                                                                    ou1 = str(input(f"Enter your name no"))
                                                                    n = n + 1
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
                                                                    speak("no more reservations today")

                                                                    print("no more reservations today")
                                                                    break
                                                                if n > in5:
                                                                    speak(
                                                                        f"Total Payable amount is\t={in5 * 500}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
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
                                            print(
                                                "On which Destination do you want to visti \tHonkong\nParis\nU.S.A\nLondan\nBrazil\nRussia\nChina\n")
                                            speak(
                                                "on which Destination do you want to visit  \tHonkong\nParis\nU.S.A\nLondan\nBrazil\nRussia\nChina\n")
                                            print("Listening...")
                                            r.pause_threshold = 1
                                            audio = r.listen(source)

                                        try:
                                            print("Recognizing...")
                                            in2 = r.recognize_google(audio, language='en-in')
                                            print(f"User said: {in2}\n")
                                            if 'Honkong' or 'paris' or 'USA' or 'londan' or 'brazil' or 'russia' or 'China' in in2:
                                                speak(
                                                    "Which Class:-\nPress 1 for First class Prise of one ticket[18000]\nPress 2 for Second class Prise of one ticket[9000]\nPress 3 for Third class Prise of one ticket[5000]")
                                                in3 = int(input(
                                                    "Which Class:-\nPress 1 for First class Prise of one ticket[18000]\nPress 2 for Second class Prise of one ticket[9000]\nPress 3 for Third class Prise of one ticket[5000]"))
                                                if in3 == 1:
                                                    speak("do you want to confirm your tickets type yes or no")
                                                    in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                                    if in4 == 'yes':
                                                        n = 1
                                                        speak("enter the number of tickets you want to buy")
                                                        in5 = int(input("How many tickets do you want to book?"))
                                                        while n <= in5:
                                                            with open("aeroplane.txt", "r") as f:
                                                                a = (
                                                                    len(f.readlines()))  # This would give length of files.
                                                                if a < 10:
                                                                    speak("enter names of passengars")
                                                                    ou1 = str(input(f"Enter your name no"))
                                                                    n = n + 1
                                                                    print(f"Reservations left={10 - a}")
                                                                    f = open("aeroplane.txt", "a")
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
                                                                    speak(
                                                                        f"Total Payable amount is\t={in5 * 18000}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
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
                                                                a = (
                                                                    len(f.readlines()))  # This would give length of files.
                                                                if a < 10:
                                                                    speak("enter names of passengars")
                                                                    ou1 = str(input(f"Enter your name no"))
                                                                    n = n + 1
                                                                    print(f"Reservations left={10 - a}")
                                                                    f = open("aeroplane.txt", "a")
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
                                                                    speak(
                                                                        f"Total Payable amount is\t= {in5 * 9000}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
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
                                                                a = (
                                                                    len(f.readlines()))  # This would give length of files.
                                                                if a < 10:
                                                                    speak("enter names of passengars")
                                                                    ou1 = str(input(f"Enter your name no"))
                                                                    n = n + 1
                                                                    print(f"Reservations left={10 - a}")
                                                                    f = open("aeroplane.txt", "a")
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
                                                                    speak(f"Total Payable amount is\t={in5 * 5000}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                                    print(f"Total Payable amount=", in5 * 5000,
                                                                          "\nYour seats are reserved successfully\n\nThankyou for choosing our platform")










                                        except Exception as e:
                                            # print(e)
                                            print("Say that again please...")
                                            return "None"
                                        return in2

                                    if __name__ == "__main__":
                                        takeCommand5()



                                # for railways

                                elif 'railway' in in1:
                                    def takeCommand6():
                                        r = sr.Recognizer()
                                        with sr.Microphone() as source:
                                            print(
                                                "On which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
                                            speak(
                                                "on which Destination do you want to visit .Pune .Dhule .Nashik .A.nagar .Mumbai .Goa .Ganpatipule. ")
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
                                                                a = (
                                                                    len(f.readlines()))  # This would give length of files.
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
                                                                    speak(
                                                                        f"Total Payable amount is\t={in5 * 750}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                                    print(
                                                                        f"Total Payable amount={in5 * 750}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                if in3 == 2:
                                                    speak("do you want to confirm your tickets type yes or no")
                                                    in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                                    if in4 == 'yes':
                                                        n = 1
                                                        speak("enter the number of tickets you want to buy")
                                                        in5 = int(input("How many tickets do you want to book?"))
                                                        while n <= in5:
                                                            with open("railway.txt", "r") as f:
                                                                a = (
                                                                    len(f.readlines()))  # This would give length of files.
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
                                                                    speak(
                                                                        f"Total Payable amount is\t={in5 * 500}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                                    print(
                                                                        f"Total Payable amount={in5 * 500}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                if in3 == 3:
                                                    speak("do you want to confirm your tickets type yes or no")
                                                    in4 = str(input("Do you want to confirm your tickets Yes or No ?"))
                                                    if in4 == 'yes':
                                                        n = 1
                                                        speak("enter the number of tickets you want to buy")
                                                        in5 = int(input("How many tickets do you want to book?"))
                                                        while n <= in5:
                                                            with open("railway.txt", "r") as f:
                                                                a = (
                                                                    len(f.readlines()))  # This would give length of files.
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
                                                                    speak(
                                                                        f"Total Payable amount is\t={in5 * 300}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")
                                                                    print(
                                                                        f"Total Payable amount={in5 * 300}\nYour seats are reserved successfully\n\nThankyou for choosing our platform")









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

        elif "dieting programme" in imp:
            try:
                def getdate():
                    import datetime
                    return datetime.datetime.now()


                t = getdate()
                speak("Press 1 for Siddhant\nPress 2 for rupesh\nPress 3 for Sanjana\nPress 4 for Mayur\nPress 5 for Riddhi\n")
                num = int(input("Press 1 for Siddhant\nPress 2 for rupesh\nPress 3 for Sanjana\nPress 4 for Mayur\nPress 5 for Riddhi\n"))
                # for siddhant
                if num == 1:
                    speak("Do you want to add or retrive data in your daily rutine?")
                    num2 = str(input("Do you want to add or retrive?"))
                    if num2 == "add":
                        speak("Which daily activity ditals you want to add exercise done or food eaten type below")
                        num3 = str(input("exercise or food ?"))
                        if num3 == "exercise":
                            f = open("siddhant.txt", "a")
                            speak("what do you exercised?")
                            a6 = str(input("what do you exercised?"))
                            f.write(f"\n[{t}]\t[{a6}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")
                            f.close()
                        elif num3 == "food":
                            f = open("siddhant.txt", "a")
                            speak("what do you eat today?")
                            a = str(input("what do you eat today?"))
                            f.write(f"\n[{t}]\t[{a}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")
                            f.close()
                        else:
                            print("invalid syntex please check again")
                    elif num2 == "retrive":
                        f = open("siddhant.txt", "r")
                        print(f.read())
                        f.close()
                        print("Thankyou for using our sooftwere")
                        speak("Thankyou for using our sooftwere")

                # for rupesh
                elif num == 2:
                    speak("Do you want to add or retrive data in your daily rutine?")
                    num5 = str(input("Do you want to add or retrive?"))

                    if num5 == "add":
                        speak("Which daily activity ditals you want to add exercise done or food eaten type below")
                        num4 = str(input("exercise or food ?"))

                        if num4 == "exercise":
                            f = open("rupesh.txt", "a")
                            speak("what do you exercised?")
                            a3 = str(input("what do you exercised?"))

                            f.write(f"\n[{t}]\t[{a3}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")

                            f.close()
                        elif num4 == "food":
                            f = open("rupesh.txt", "a")
                            speak("what do you eat today?")
                            a5 = str(input("what do you eat today?"))

                            f.write(f"\n[{t}]\t[{a5}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")

                            f.close()
                            print("Thankyou for using our sooftwere")
                            speak("Thankyou for using our sooftwere")

                        else:
                            print("invalid syntex please check again")
                    elif num5 == "retrive":
                        f = open("rupesh.txt", "r")
                        print(f.read())
                        f.close()

                    # for Sanjana
                elif num == 3:
                    speak("Do you want to add or retrive data in your daily rutine?")
                    num6 = str(input("Do you want to add or retrive?"))

                    if num6 == "add":
                        speak("Which daily activity ditals you want to add exercise done or food eaten type below")
                        num7 = str(input("exercise or food ?"))

                        if num7 == "exercise":
                            f = open("sanjana.txt", "a")
                            speak("what do you exercised?")
                            a3 = str(input("what do you exercised?"))

                            f.write(f"\n[{t}]\t[{a3}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")

                            f.close()
                        elif num7 == "food":
                            f = open("sanjana.txt", "a")
                            speak("what do you eat today?")
                            a4 = str(input("what do you eat?"))

                            f.write(f"\n[{t}]\t[{a4}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")

                            f.close()
                        else:
                            print("invalid syntes please check again")
                    elif num6 == "retrive":
                        f = open("sanjana.txt", "r")
                        print(f.read())
                        f.close()
                        print("Thankyou for using our sooftwere")
                        speak("Thankyou for using our sooftwere")



                # for Mayur

                elif num == 4:
                    speak("Do you want to add or retrive data in your daily rutine?")
                    num6 = str(input("Do you want to add or retrive?"))

                    if num6 == "add":
                        speak("Which daily activity ditals you want to add exercise done or food eaten type below")
                        num7 = str(input("exercise or food ?"))

                        if num7 == "exercise":
                            f = open("mayur.txt", "a")
                            speak("what do you exercised?")
                            a3 = str(input("what do you exercised?"))

                            f.write(f"\n[{t}]\t[{a3}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")


                            f.close()
                        elif num7 == "food":
                            f = open("mayur.txt", "a")
                            speak("what do you eat today?")
                            a4 = str(input("what do you eat?"))

                            f.write(f"\n[{t}]\t[{a4}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")

                            f.close()
                        else:
                            print("invalid syntes please check again")
                    elif num6 == "retrive":
                        f = open("mayur.txt", "r")
                        print(f.read())
                        f.close()
                        print("Thankyou for using our sooftwere")
                        speak("Thankyou for using our sooftwere")



                # for riddhi

                elif num == 5:
                    speak("Do you want to add or retrive data in your daily rutine?")
                    num6 = str(input("Do you want to add or retrive?"))

                    if num6 == "add":
                        speak("Which daily activity ditals you want to add exercise done or food eaten type below")
                        num7 = str(input("exercise or food ?"))

                        if num7 == "exercise":
                            f = open("riddhi.txt", "a")
                            speak("what do you exercised?")
                            a3 = str(input("what do you exercised?"))

                            f.write(f"\n[{t}]\t[{a3}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")

                            f.close()
                        elif num7 == "food":
                            f = open("riddhi.txt", "a")
                            speak("what do you eat today?")
                            a4 = str(input("what do you eat?"))

                            f.write(f"\n[{t}]\t[{a4}]")
                            print("Your data is added successfully")
                            speak("Your data is added successfully")

                            f.close()
                        else:
                            print("invalid syntes please check again")
                    elif num6 == "retrive":
                        f = open("riddhi.txt", "r")
                        print(f.read())
                        f.close()
                        print("Thankyou for using our sooftwere")
                        speak("Thankyou for using our sooftwere")




                else:
                    print("thank")
            except Exception as e:
                print("Invalid Syntex")
        elif "stone paper scissor" in imp:
            speak("Welcome to stone paper ceaser Arena")
            list = ['s', 'p', 'c']
            import random

            t = random.choice(list)
            a = 0
            b = 0
            c = 0
            while a < 11:
                num = str(input("Press s for stone\nPress c for ceaser\nPress p for paper"))
                if num == "s" and t == "s":
                    print(
                        f"Its a tie!!!\nyour choice={num}\ncomputers choice={t}\nYour points={b}\ncomputers points={c}\nyou have taken{str(a + 1)}attempts")
                    b = b + 0
                    c = c + 0
                    a = a + 1
                elif num == "s" and t == "p":
                    print(
                        f"You lost this match computer will get a point\nyour choice={num}\ncomputers choice={t}\nYour points={str(b + 0)}\ncomputers points={str(c + 1)}\nyou have taken{str(a + 1)}attempts")
                    b = b + 0
                    c = c + 1
                    a = a + 1
                elif num == "s" and t == "c":
                    print(
                        f"You won this match you will get a point\nyour choice={num}\ncomputers choice={t}\nyour choice={num}\ncomputers choice{t} \nYour points={str(b + 1)}\ncomputers points={str(c + 0)}\nyou have taken{str(a + 1)}attempts")

                    b = b + 1
                    c = c + 0
                    a = a + 1
                elif num == "c" and t == "s":
                    print(
                        f"You lost this match computer will get a point\nyour choice={num}\ncomputers choice={t}\nYour points={str(b + 0)}\ncomputers points={str(c + 1)}\nyou have taken{str(a + 1)}attempts")
                    b = b + 0
                    c = c + 1
                    a = a + 1
                elif num == "c" and t == "p":
                    print(
                        f"You won this match you will get a point\nyour choice={num}\ncomputers choice={t}\nYour points={str(b + 1)}\ncomputers points={str(c + 0)}\nyou have taken{str(a + 1)}attempts")
                    b = b + 1
                    c = c + 0
                    a = a + 1
                elif num == "c" and t == "c":
                    print(
                        f"Its a tie!!!\nyour choice={num}\ncomputers choice={t}\nYour points={b}\ncomputers points={c}\nyou have taken{str(a + 1)} attempts")
                    b = b + 0
                    c = c + 0
                    a = a + 1
                elif num == "p" and t == "c":
                    print(
                        f"You lost this match computer will get a point\nyour choice={num}\ncomputers choice={t}\nYour points={str(b + 0)}\ncomputers points={str(c + 1)}\nyou have taken{str(a + 1)}attempts")
                    b = b + 0
                    c = c + 1
                    a = a + 1
                elif num == "p" and t == "s":
                    print(
                        f"You won this match you will get a point\nyour choice={num}\ncomputers choice={t}\nYour points={str(b + 1)}\ncomputers points={str(c + 0)}\nyou have taken{str(a + 1)}attempts")
                    b = b + 1
                    c = c + 0
                    a = a + 1
                elif num == "p" and t == "p":
                    print(
                        f"Its a tie!!!\nyour choice={num}\ncomputers choice={t}\nYour points={b}\ncomputers points={c}\nyou have taken{str(a + 1)} attempts")
                    b = b + 0
                    c = c + 0
                    a = a + 1
                else:
                    print("Incorrect input")
            if a == 11:
                if c == b:
                    print(
                        f"Match Tie\nyour choice={num}\ncomputers choice={t}\n your points={b}\nComputers points={c}\ntotal attempts taken={a}")
                elif c < b:
                    print(f"you won the game!!!\n your points={b}\nComputers points={c}\ntotal attempts taken={a}")
                else:
                    print(f"computer won the game\n your points={b}\nComputers points={c}\ntotal attempts taken={a}")
            else:
                print("Something went wrong")


        elif "translate" in imp:
            languages = {'Afrikaans': 'af',
                'Albanian': 'sq',
                'Amharic': 'am',
                'Arabic': 'ar',
                'Armenian': 'hy',
                'Azerbaijani': 'az',
                'Basque': 'eu',
                'Belarusian': 'be',
                'Bengali': 'bn',
                'Bosnian': 'bs',
                'Bulgarian': 'bg',
                'Catalan': 'ca',
                'Cebuano': 'ceb',
                'Chichewa': 'ny',
                'Chinese (Simplified)': 'zh-cn',
                'Chinese (Traditional)': 'zh-tw',
                'Corsican': 'co',
                'Croatian': 'hr',
                'Czech': 'cs',
                'Danish': 'da',
                'Dutch': 'nl',
                'English': 'en',
                'Esperanto': 'eo',
                'Estonian': 'et',
                'Filipino': 'tl',
                'Finnish': 'fi',
                'French': 'fr',
                'Frisian': 'fy',
                'Galician': 'gl',
                'Georgian': 'ka',
                'German': 'de',
                'Greek': 'el',
                'Gujarati': 'gu',
                'Haitian Creole': 'ht',
                'Hausa': 'ha',
                'Hawaiian': 'haw',
                'Hebrew': 'he',
                'Hindi': 'hi',
                'Hmong': 'hmn',
                'Hungarian': 'hu',
                'Icelandic': 'is',
                'Igbo': 'ig',
                'Indonesian': 'id',
                'Irish': 'ga',
                'Italian': 'it',
                'Japanese': 'ja',
                'Javanese': 'jw',
                'Kannada': 'kn',
                'Kazakh': 'kk',
                'Khmer': 'km',
                'Korean': 'ko',
                'Kurdish (Kurmanji)': 'ku',
                'Kyrgyz': 'ky',
                'Lao': 'lo',
                'Latin': 'la',
                'Latvian': 'lv',
                'Lithuanian': 'lt',
                'Luxembourgish': 'lb',
                'Macedonian': 'mk',
                'Malagasy': 'mg',
                'Malay': 'ms',
                'Malayalam': 'ml',
                'Maltese': 'mt',
                'Maori': 'mi',
                'Marathi': 'mr',
                'Mongolian': 'mn',
                'Myanmar (Burmese)': 'my',
                'Nepali': 'ne',
                'Norwegian': 'no',
                'Odia': 'or',
                'Pashto': 'ps',
                'Persian': 'fa',
                'Polish': 'pl',
                'Portuguese': 'pt',
                'Punjabi': 'pa',
                'Romanian': 'ro',
                'Russian': 'ru',
                'Samoan': 'sm',
                'Scots Gaelic': 'gd',
                'Serbian': 'sr',
                'Sesotho': 'st',
                'Shona': 'sn',
                'Sindhi': 'sd',
                'Sinhala': 'si',
                'Slovak': 'sk',
                'Slovenian': 'sl',
                'Somali': 'so',
                'Spanish': 'es',
                'Sundanese': 'su',
                'Swahili': 'sw',
                'Swedish': 'sv',
                'Tajik': 'tg',
                'Tamil': 'ta',
                'Telugu': 'te',
                'Thai': 'th',
                'Turkish': 'tr',
                'Ukrainian': 'uk',
                'Urdu': 'ur',
                'Uyghur': 'ug',
                'Uzbek': 'uz',
                'Vietnamese': 'vi',
                'Welsh': 'cy',
                'Xhosa': 'xh',
                'Yiddish': 'yi',
                'Yoruba': 'yo',
                'Zulu': 'zu',}
            from googletrans import Translator

            speak(f"speak the sentance you want to translate")
            i1=takeCommand2()
            print(f"{i1}")
            speak("in which language you want to Translate")
            i2=takeCommand2()
            print(f"{i2}")

            def translate_sentence(sentence, dest_language):

                translator = Translator()
                translation = translator.translate(sentence, dest=dest_language)
                return translation.text

            result1=languages.get('i2')
            # Example usage
            input_sentence = f"{i1}"
            target_language = f"{i2}"
            result= translate_sentence(input_sentence, target_language)

            print(f"Original: {input_sentence}")
            print(f"Translated: {result}")
            from gtts import gTTS
            import os

            tts = gTTS(text=f"{i1}", lang='hi')
            tts.save("pcvoice.mp3")
            # to start the file from python
            os.system("start pcvoice.mp3")

        else:
            speak("Taking Help og Google to Fulfill your demand")
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.by import By
            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager
            import time

            # Initialize the Chrome WebDriver
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

            # Open the ChatGPT website
            driver.get("https://google.com/")
            driver.maximize_window()
            # Add a wait to ensure the page loads (you might need to adjust the timing)
            time.sleep(2)
            # Locate the input field for typing the query
            # Note: Update the XPath if necessary
            input_field = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')  # Update the XPath to match the actual input field ID or class
            # Type the query
            input_field.send_keys(imp)
            # Press Enter to submit the query
            input_field.send_keys(Keys.ENTER)
            # Add a wait to observe the result (you might need to adjust the timing)
            time.sleep(50)
            # Close the WebDriver
            driver.quit()





