from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import json
from utils import known_location, known_rest_type, known_type

app = FastAPI()


def preprocess_data(df):
    col_to_OHE = ["online_order", "book_table"]
    for col in col_to_OHE:
        df[col] = df[col].map({True: 1, False: 0})
        df[col] = pd.to_numeric(df[col])

    location = pd.Categorical(df["location"], categories=known_location)
    location_dummies = pd.get_dummies(location)

    rest_type = pd.Categorical(df["rest_type"], categories=known_rest_type)
    rest_type_dummies = pd.get_dummies(rest_type)

    typ = pd.Categorical(df["type"], categories=known_type)
    type_dummies = pd.get_dummies(typ)

    df = pd.concat([df, location_dummies, rest_type_dummies, type_dummies], axis=1)
    df = df.drop(["location", "rest_type", "type"], axis=1)
    return df


class RatingItem(BaseModel):
    online_order: bool  # "Yes",
    book_table: bool  # "Yes",
    votes: float  # 775,
    cost: float  # 800.0,
    location: str  # "Banashankari",
    rest_type: str  # "Casual Dining",
    type: str  # "Buffet"


with open("random_forest.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/predict")
async def rating_endpoint(item: RatingItem):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    df = preprocess_data(df)
    # print(f"COLS OF DATAFRAME: {df.shape[1]}")
    # print("Prediction", model.predict(df))
    y_pred = round(model.predict(df)[0], 2)
    return json.dumps({"Rating": y_pred})
