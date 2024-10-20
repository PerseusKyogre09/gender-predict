# features/extract_features.py
import librosa
import numpy as np

def extract_features(audio_path):
    try:
        # Load the audio file
        y, sr = librosa.load(audio_path, sr=None)
        print(f"Audio file loaded. Sample rate: {sr}, Length: {len(y)}")
        
        # Extract MFCCs
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_mean = np.mean(mfccs.T, axis=0)
        
        # Calculate pitch
        pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
        pitch = np.mean(pitches[np.nonzero(pitches)])  # Take the mean of non-zero pitches
        
        # Calculate volume
        volume = np.mean(librosa.feature.rms(y=y))  # Root mean square for volume
        
        # Print the features for debugging
        print(f"MFCCs mean: {mfccs_mean}")
        print(f"Pitch: {pitch}")
        print(f"Volume: {volume}")
        
        return {
            'mfccs': mfccs_mean,
            'pitch': pitch,
            'volume': volume
        }
    except Exception as e:
        print(f"Error extracting features: {e}")
        return {}
