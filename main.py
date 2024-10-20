# main.py
import os
from features.extract_features import extract_features
from models.fuzzy_gender import predict_gender

def main():
    audio_files = os.listdir('data/voice_samples/')
    
    # Check if files are being detected
    if not audio_files:
        print("No audio files found in the 'data/voice_samples/' directory.")
        return

    for file in audio_files:
        if file.endswith('.wav') or file.endswith('.mp3'):  # Allow both .wav and .mp3 files
            audio_path = os.path.join('data/voice_samples/', file)
            print(f"Processing file: {file}")
            
            # Extract features and check the values
            features = extract_features(audio_path)
            print(f"Extracted features from {file}: {features}")

            # Check if pitch and volume were extracted properly
            if 'pitch' not in features or 'volume' not in features:
                print(f"Error: Pitch or volume not extracted correctly for {file}")
                continue

            # Use the extracted features for prediction
            predicted_gender = predict_gender(features['pitch'], features['volume'])
            gender_label = 'Male' if predicted_gender >= 1 else 'Female'
            
            print(f"File: {file}, Predicted Gender: {gender_label}")
        else:
            print(f"Skipping file {file} as it's not a supported audio format (.wav or .mp3)")

if __name__ == '__main__':
    main()
