import librosa
import numpy as np

def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=22050)

    # Data Augmentation
    noise = np.random.randn(len(audio))
    audio = audio + 0.005 * noise
    audio = np.roll(audio, sr // 10)

    # MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)

    # Chroma
    chroma = librosa.feature.chroma_stft(y=audio, sr=sr)

    # Spectral Contrast
    contrast = librosa.feature.spectral_contrast(y=audio, sr=sr)

    # ZCR
    zcr = librosa.feature.zero_crossing_rate(audio)

    # Combine
    features = np.hstack([
        np.mean(mfcc.T, axis=0),
        np.mean(chroma.T, axis=0),
        np.mean(contrast.T, axis=0),
        np.mean(zcr.T, axis=0)
    ])

    return features