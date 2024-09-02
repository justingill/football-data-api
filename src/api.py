from fastapi import FastAPI
from src.client import FootballDataClient
import uvicorn
import os
from typing import Optional

app = FastAPI()
data_client = FootballDataClient(os.environ["API_KEY"])


@app.get("/")
def root():
    return {"message": "Football API"}


@app.get("/areas/")
def get_areas(area_id: Optional[str] = None):
    try:
        if area_id:
            return data_client.get_areas(area_id)
        else:
            return data_client.get_areas_list()
    except Exception as e:
        return e


@app.get("/competitions/")
def get_competitions(competition_id: Optional[str] = None):
    try:
        if competition_id:
            return data_client.get_competitions(competition_id)
        else:
            return data_client.get_competitions_list()
    except Exception as e:
        return e


@app.get("/teams/")
def get_teams(team_id: Optional[str] = None):
    try:
        if team_id:
            return data_client.get_teams(team_id)
        else:
            return data_client.get_teams_list()
    except Exception as e:
        return e


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
