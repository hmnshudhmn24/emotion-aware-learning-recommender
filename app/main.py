from app.ingestion.text_input import get_text_input
from app.emotion_detection.text_emotion_model import detect_text_emotion
from app.learning_engine.content_recommender import recommend_content
from app.output.recommendation_report import generate_report

def run():
    text=get_text_input()
    emotion=detect_text_emotion(text)
    plan=recommend_content(emotion)
    generate_report(emotion,plan)

if __name__=='__main__': run()
