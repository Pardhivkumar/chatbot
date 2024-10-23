import pyttsx3
import requests
import phonenumbers
from phonenumbers import geocoder
import wikipedia
from pprint import pprint
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import speech_recognition as sr
from random import choice
from datetime import datetime
import os
import subprocess as sp
user='pardhv'
bot='siri'
username='pardhiv'
botname='siri'
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',190)
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]
paths = {
    'notepad': "C:\\Windows\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greet_user():
    hour=datetime.now().hour
    if(hour>6 and hour<12):
        print(f"good morning {username}    sir")
    elif(hour>12 and hour<16):
        print(f"good afternoon {username}   sir")
    elif(hour>16 and hour<19):
        print(f"good evening {username}   sir")
    speak(f"hi    sir i'm {botname} ! how may help you")

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("sir i'm waiting for your message")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("sir   i'm recognizing")
        query = r.recognize_google(audio, language="en-in")
        if 'exit' in query or 'stop' in query:
            hour = datetime.now().hour
            if hour > 21 or hour < 6:
                speak("sir time ayyindhi paduko vacchu ga")
            else:
                speak("sir nuvvu handsome ga unttav")
            exit()
        else:
            speak(choice(opening_text))
    except Exception:
        speak("sir konchem fluent ga cheppava nakosam")
        query = None
    return query

#opening camera
def open_camera():
    sp.run('start microsoft.windows.camera',shell=True)
#opening calculator
def open_calculator():
    os.startfile(paths['calculator'])
#opening command prompt
def open_cmd():
    os.system('start cmd')
{
    "ip": "117.214.111.199"
}
#finding ip address
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
#searching wikipedia
def search_on_wikipedia(query):
    results=wikipedia.summary(query,sentence=2)
    return results
#playing youtube video
def play_on_youtube(video):
    kit.playonyt(video)
#searching in google
def search_on_google(query):
    kit.search(query)
#tracing location
def get_location(phone_number):
    try:
        parsed_number=phonenumbers.parse(phone_number,None)
        if not phonenumbers.is_valid_number(parsed_number):
            return "invalid number sir"
        else:
            region=geocoder.description_for_number(parsed_number,"en")
            return region
    except Exception as e:
        return f"error {str(e)}"
# calling a phone number
def call_phone_number(number):
    try:
        sp.call(["start","tell"+number],shell=True)
        return True
    except Exception as e:
        print("error :",e)
        return False
#sending whatsapp message
def send_whatsapp_message(number,message):
    kit.sendwhatmsg_instantly(f"+91{number}",message)
EMAIL ='pardhivkumarchippada@gmail.com'
PASSWORD ='Pardhiv@@1234'
#sending email

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
#getting weather report
OPENWEATHER_APP_ID ="https://www.weatherapi.com/weather/"


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
#getting random advices
def get_random_advice():
    res=requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()


        if 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        
        elif 'location' in query:
            phone_number = '6304532197'  # Replace this with the phone number you want to trace
            location = get_location(phone_number)
            print(f"Location for given phone number {phone_number}: {location}")
        
        elif "call" in query:
            number="9618296103"
            speak(f"given number is {number}")
            speak(f"calling :{number}")
            if(call_phone_number(number)):
                speak("call initated")
            else:
                speak("unable to call")
        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")