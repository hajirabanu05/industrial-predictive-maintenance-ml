from pydantic import BaseModel


class MachineResponse(BaseModel):

    machine_id: int

    sensor: dict

    class Config:

        from_attributes = True