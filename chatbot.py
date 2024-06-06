import requests
import random

print("#### ChatBot by Amey ####")

def greet_name(name):
    return "Hello " + name + ", how are you!?"

name = input("What's your name? ")
print(greet_name(name))

def greet_age(age):
    return "Okay you are " + str(age) + " years old"

age = input("How old are you? ")
print(greet_age(age))

def bye(name):
    return "Bye " + name + ", Have a great day! "

def func_joke():
    jokes = [
        "Did you hear they arrested the devil? Yeah, they got him on possession.",
        "What did one DNA say to the other DNA? Do these genes make me look fat?",
        "My IQ test results came back. They were negative.",
        "What do you get when you cross a polar bear with a seal? A polar bear.",
        "Why can’t you trust an atom? Because they make up literally everything.",
        "Why was six afraid of seven? Because seven eight nine.",
        "What do you call a hippie’s wife? Mississippi."
    ]
    return random.choice(jokes)

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The weather in {city} is currently {weather_description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't fetch the weather for you."

api_key = '5667d6b863b2e1ad42bf8bb8df708846'

def func_calculator(x, y, operator):
    if operator.lower() == 'add':
        return x + y
    elif operator.lower() == 'subtract':
        return x - y
    elif operator.lower() == 'multiply':
        return x * y
    elif operator.lower() == 'divide':
        if y == 0:
            return "Cannot divide by 0!"
        else:
            return x / y
def func_quotes():
    quotes = [
           "The only way to do great work is to love what you do. – Steve Jobs",
           "The best time to plant a tree was 20 years ago. The second best time is now.",
           "It’s hard to beat a person who never gives up. – Babe Ruth",
           "I am not a product of my circumstances. I am a product of my decisions. – Stephen Covey",
           "Don’t watch the clock; do what it does. Keep going."
    ]
    return random.choice(quotes)

while True:
    choice = input("Do you want to continue with our App?\nPress Yes/No: ").lower()
    if choice == "no":
        print(bye(name))
        break
    elif choice != "yes":
        print("Enter a valid input")
        continue

    print("Okay " + name + ", how can I assist you today? ")
    print("You can press 1 to hear a Joke, 2 for Weather Updates, 3 to open the Calculator app and 4 for Motivational "
          "Quotes")

    user_choice = input("Enter your request: ").lower()
    if user_choice in ["1", "tell me a joke"]:
        print(func_joke())
    elif user_choice in ["2", "weather report"]:
        city = input("Please enter the city: ")
        print(get_weather(city, api_key))
    elif user_choice in ["3", "calculator"]:
        print("Calculator App started")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print("Select from one of the following Operations: Add, Subtract, Multiply or Divide")
        operator = input("Enter operation to do: ")
        print("Result is:", func_calculator(x, y, operator))
    elif user_choice in ["4", "quote"]:
        print(func_quotes())
    else:
        print("Invalid Option")
