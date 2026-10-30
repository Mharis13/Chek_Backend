from pydantic import BaseModel, Field


class HealthOutput(BaseModel):
    api: str = Field()
    database: str = Field()
