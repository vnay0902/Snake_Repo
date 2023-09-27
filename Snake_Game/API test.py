import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=" + API_KEY

def get_weather_data():
    date = input("Enter the date (yyyy-mm-dd): ")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        for forecast in data['list']:
            if date in forecast['dt_txt']:
                print(f"Temperature on {forecast['dt_txt']}: {forecast['main']['temp']} °C")
                return
        print("No data found for the given date.")
    else:
        print("Error fetching data from the API.")

def get_wind_speed_data():
    date = input("Enter the date (yyyy-mm-dd): ")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        for forecast in data['list']:
            if date in forecast['dt_txt']:
                print(f"Wind Speed on {forecast['dt_txt']}: {forecast['wind']['speed']} m/s")
                return
        print("No data found for the given date.")
    else:
        print("Error fetching data from the API.")

def get_pressure_data():
    date = input("Enter the date (yyyy-mm-dd): ")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        for forecast in data['list']:
            if date in forecast['dt_txt']:
                print(f"Pressure on {forecast['dt_txt']}: {forecast['main']['pressure']} hPa")
                return
        print("No data found for the given date.")
    else:
        print("Error fetching data from the API.")

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            get_weather_data()
        elif choice == 2:
            get_wind_speed_data()
        elif choice == 3:
            get_pressure_data()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#push to github repository
#git add .
#git commit -m "message"
#git push origin master

#pull from github repository
#git pull origin master

#clone from github repository