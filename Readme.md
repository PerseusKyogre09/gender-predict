# Gender Prediction from Voice Samples
This Python project uses fuzzy logic to predict gender based on voice samples. It extracts MFCCs, pitch, and volume from the audio and applies fuzzy rules to determine whether the speaker is male or female.

## Features
- Supports WAV and MP3 audio formats.
- Extracts key audio features like MFCCs, pitch, and volume.
- Uses fuzzy logic for gender prediction.
## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/gender-predict.git
```
2. Navigate to the project directory:
```bash
cd gender-predict
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. You will also need to install Microsoft C++ Build Tools for the fuzzy library. Download it here.

## Usage
1. Place your audio files (.wav or .mp3) in the data/voice_samples/ folder.
2. Run the script:
```bash
python main.py
```
3. The system will extract features from the audio sample and predict the gender.

## Example Output:
```
yaml
Processing file: male-what-6177.mp3
Audio file loaded. Sample rate: 44100, Length: 35712
MFCCs mean: [-222.50427, 109.97699, -23.271553, ...]
Pitch: 1370.9210205078125
Volume: 0.19457927346229553
Predicted gender: Male
```
## File Structure
```bash
├── data/
│   └── voice_samples/         # Folder to store voice samples
├── models/
│   └── fuzzy_gender.py        # Fuzzy logic model for gender prediction
├── main.py                    # Main script to process the audio files
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
```
### Dependencies
- NumPy
- SciPy
- skfuzzy
- librosa
- pydub
- ffmpeg (required for MP3 file processing)
You can install these dependencies using the requirements.txt file.

### How it Works
- Audio Feature Extraction: Extracts MFCCs, pitch, and volume from the audio sample.
- Fuzzy Logic: The fuzzy control system processes the pitch and volume using a set of predefined rules to predict the gender.
- Prediction: The result is displayed on the terminal as either Male or Female.

### Troubleshooting
- If you encounter any errors related to fuzzy installation, make sure you have installed the Microsoft C++ Build Tools as mentioned above.
- If .mp3 files are not being processed, ensure ffmpeg is installed and available in your system path.

### Future Enhancements
- Improve the accuracy of the model with more refined rules.
- Add a graphical interface for easier usage.
- Train a machine learning model for more accurate predictions.