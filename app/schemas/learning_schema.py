from pydantic import BaseModel
class LearningPlan(BaseModel): difficulty:str; pacing:str; content:str
