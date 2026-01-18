from app.learning_engine.difficulty_adapter import adapt_difficulty
from app.learning_engine.pacing_controller import control_pacing

def recommend_content(e): return {'difficulty':adapt_difficulty(e),'pacing':control_pacing(e),'content':'Personalized learning module'}
