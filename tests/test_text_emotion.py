from app.emotion_detection.text_emotion_model import detect_text_emotion
def test(): assert detect_text_emotion('I am happy')=='happy'
