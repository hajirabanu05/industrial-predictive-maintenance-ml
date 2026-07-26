from pydantic import BaseModel


class PredictionResponse(BaseModel):

    machine_id: int

    prediction: str

    probability: float

    class Config:

        from_attributes = True