
Made a Chat bot using Python with some predefined questions and integrated a bunch of Functions in it to make it more interactive and useful.
First we created a bunch of functions in the program to take Name and Age as input from the user.
             def greet_name(name):
   		 return "Hello " + name + ", how are you!?"

	name = input("What's your name? ")
  print(greet_name(name))

We also wrote a function which prints  “Bye” after we choose to exit the loop.
def bye(name):
    return "Bye " + name + ", Have a great day! "

Then we move on to create our App’s main functionalities like:
•	Jokes
•	Weather Report
•	Calculator
•	Motivational Quotes
Jokes Function: 
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

We import the module “random” for this function to work the way we intended it to.
Inside the function, we created a list of Strings and called it Jokes.
Inside the list we stored some jokes we got from the internet.
We close this function with “return random.choices(jokes)” where The choices() method returns multiple or a single random element from the list.


Weather Function:
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

In this function we integrated an API called OpenWeatherMap API with our software that takes the name of any city as input and tells us the Weather of that city and also the temperature.
In order for this to work we have to connect our App to the API with an API Key which we got from creating a free account on the OpenWeather Map website.
Let’s break the code down:
def get_weather(city, api_key):
•	This line defines a function named get_weather that takes two parameters: city (the name of the city for which we want to fetch weather data) and api_key (the API key required for accessing the OpenWeatherMap API).
base_url :
•	 This line sets the base URL for the OpenWeatherMap API. We will append query parameters to this URL to specify the city and other details.
Params:
params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'
}
Here, we define a dictionary params containing the query parameters required for the API request.
•	'q': city specifies the city for which we want to fetch weather data.
•	'appid': api_key provides the API key required for authentication.
•	'units': 'metric' specifies that we want temperature data in Celsius.

response = requests.get(base_url, params=params)

•	This line makes an HTTP GET request to the OpenWeatherMap API using the requests.get() function. It combines the base_url with the query parameters specified in the params dictionary.
if response.status_code == 200:

•	Here, we check if the response status code is 200, which indicates a successful response from the API.

data = response.json()

•	If the response is successful, we extract the JSON data from the response object using the .json() method and store it in the variable data.

weather_description = data['weather'][0]['description']
temperature = data['main']['temp']

•	We extract the weather description and temperature from the JSON data. The weather description is located at data['weather'][0]['description'], and the temperature is at data['main']['temp']
Finally we return a formatted string which contains the temperature and the description of the weather for the specified city.
api_key = '5667d6b863b2e1ad42bf8bb8df708846'

•	This key is necessary for authenticating your requests to the API and is typically obtained by registering for an account on the OpenWeatherMap website and generating an API key there. This key allows you to access weather data for various locations using the OpenWeatherMap API.






Calculator Function:
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

In this section of our code, we write a function and pass the following three parameters through it:
•	x, y, operator
Where x and y denote any integer we input in the app and operator denotes what operation we want to perform on the integers.
We put the whole function in an if-else condition so that exceptions in the “division” part of the code can be handled	.

Quotes Function:
def func_quotes():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "It’s hard to beat a person who never gives up. – Babe Ruth",
        "I am not a product of my circumstances. I am a product of my decisions. – Stephen Covey",
        "Don’t watch the clock; do what it does. Keep going."
    ]
    return random.choice(quotes)

•	This function is similar to the “Jokes” function as it is implemented in the same way.

We have defined all our functions and now it is time start the loop and implement all these functions inside the loop.




We use a while loop and the syntax is
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

We take the input from the user whether he chooses to continue with our App or not.
If the answer is No, we break the loop and exit out of it and print our Bye function.
If the answer is Yes then we continue with our App and print some messages to tell the user about the functions the App can do.




















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
 
This is the final part of the code where we take input from the user for the function he wants to use and run it.
If he presses 1 or writes “tell me a joke”, the function for jokes will execute and it will print any random joke from our list of jokes.
If the user presses 2 or writes “Weather report”, the function for the weather report will execute and it will ask the user to enter the name of the city for which he wants the report for and then print the report and the temperature.
If the user presses 3, the Calculator function will execute and it will ask the user for two numbers as inputs and then ask for what operation to perform on them.
If the user presses 4, the Quotes function will execute and a random quotes will be printed on the user’s screen. 




