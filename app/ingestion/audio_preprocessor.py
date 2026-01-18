import librosa
def preprocess_audio(path): y,sr=librosa.load(path); return y,sr
