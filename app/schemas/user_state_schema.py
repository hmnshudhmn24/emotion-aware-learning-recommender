from pydantic import BaseModel
class UserState(BaseModel): emotion:str; engagement:float
