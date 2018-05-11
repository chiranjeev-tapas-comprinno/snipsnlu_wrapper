"""
Flask based api to get the input from the user as a post request in the json
format asking about some data like "What will be the weather in Mumbai next
week?" and the application will return a process data in a json format.

Input:
{"sentence": "What will be the weather in Mumbai next week?"}

Output:
{
   "intent": {
      "intentName": "searchWeatherForecast",
      "probability": 0.95
   },
   "slots": [
      {
         "value": "mumbai",
         "entity": "locality",
         "slotName": "forecast_locality"
      },
      {
         "value": {
            "kind": "InstantTime",
            "value": "2018-02-08 20:00:00 +00:00"
         },
         "entity": "snips/datetime",
         "slotName": "forecast_start_datetime"
      }
   ]
}
"""

from app import create_app

# Get our app setup and running.
# The create app will instantiates the Flask object, load config and call
# necessary methods to train out NLP engine.
app = create_app()
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
