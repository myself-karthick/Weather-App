# Backend with Django and OpenWeatherMap API
The backend of this weather app is built using Django, a high-level Python web framework, and it relies on the OpenWeatherMap API to fetch weather data for various locations. Django is used to serve as the interface between the frontend and the OpenWeatherMap API.

* The backend is hosted seperately and accessed in frontend.
* render.com is used to host the backend with provides web services for deploy and easy maintainance the hosted link is 
https://openweathermap.org/weather-conditions

# Steps to Run:
* Ensure python is installed in the system.
* Install Django using,
  <pre>pip install django</pre>
* After installing django the server can be directly initialized using,
  <pre>python manage.py runserver</pre>
* Now the server will start to run in port 8000 in default.

# Request:
* The request is sent in POST method as the body should be in JSON format. For example 
  <pre>
    {
      "city" : "Chennai"
    }
  </pre>
# Response:
* The respons contains details as follows:
  <pre>
    {
      "country_code": "IN",
      "coordinate": "80.2785, 13.0878",
      "temp": "29.98",
      "temp_min": "29.98",
      "temp_max": "30.99",
      "wind_speed": "3.09",
      "pressure": "1009",
      "humidity": "85",
      "main": "Clouds",
      "description": "scattered clouds",
      "icon": "03n"
    }
  </pre>
This response can be used in frontend to display the weather conditions.
Thank You :)
