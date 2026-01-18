import librosa, numpy as np
def extract_mfcc(y,sr): return np.mean(librosa.feature.mfcc(y=y,sr=sr),axis=1)
