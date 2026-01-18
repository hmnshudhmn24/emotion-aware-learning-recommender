def detect_text_emotion(t): t=t.lower();
    return 'happy' if 'happy' in t or 'good' in t else 'sad' if 'sad' in t or 'tired' in t else 'angry' if 'angry' in t else 'neutral'
