from fastapi import FastAPI
import pandas as pd
import requests

app = FastAPI()

@app.get("/")
def read_root():
    data = requests.get("https://24f1001980.github.io/q5-static-JSON/data.json").json()
    data = pd.DataFrame(data["products"])
    median_price = data["price"].median()
    return "Median price of all products is: " + str(median_price)
