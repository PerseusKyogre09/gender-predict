# models/fuzzy_gender.py
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

def setup_fuzzy_system():
    # Create fuzzy variables
    pitch = ctrl.Antecedent(np.arange(50, 500, 1), 'pitch')  # Adjusted for typical human voice range
    volume = ctrl.Antecedent(np.arange(0, 1, 0.01), 'volume')
    gender = ctrl.Consequent(np.arange(0, 2, 1), 'gender')  # 0 for female, 1 for male

    # Define refined fuzzy sets for pitch
    pitch['low'] = fuzz.trimf(pitch.universe, [50, 85, 165])  # Male voices typically in this range
    pitch['medium'] = fuzz.trimf(pitch.universe, [150, 200, 255])  # Female voices typically in this range
    pitch['high'] = fuzz.trimf(pitch.universe, [220, 300, 500])  # Very high-pitched voices

    # Define fuzzy sets for volume (tuned for sensitivity)
    volume['quiet'] = fuzz.trimf(volume.universe, [0, 0.2, 0.4])
    volume['normal'] = fuzz.trimf(volume.universe, [0.3, 0.5, 0.7])
    volume['loud'] = fuzz.trimf(volume.universe, [0.6, 0.8, 1])

    # Define fuzzy sets for gender
    gender['female'] = fuzz.trimf(gender.universe, [0, 0, 1])
    gender['male'] = fuzz.trimf(gender.universe, [1, 1, 1])

    # Define improved rules
    rule1 = ctrl.Rule(pitch['low'] & volume['quiet'], gender['male'])  # Low pitch + quiet volume -> male
    rule2 = ctrl.Rule(pitch['medium'] & volume['normal'], gender['female'])  # Medium pitch + normal volume -> female
    rule3 = ctrl.Rule(pitch['low'] & volume['loud'], gender['male'])  # Low pitch + loud volume -> male
    rule4 = ctrl.Rule(pitch['high'] & volume['quiet'], gender['female'])  # High pitch + quiet volume -> female

    # Debug the rules
    print(f"Rules: {rule1}, {rule2}, {rule3}, {rule4}")

    # Create the control system
    gender_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    return ctrl.ControlSystemSimulation(gender_control)

def predict_gender(pitch_value, volume_value):
    gender_simulation = setup_fuzzy_system()
    
    print(f"Predicting gender with pitch: {pitch_value}, volume: {volume_value}")
    
    gender_simulation.input['pitch'] = pitch_value
    gender_simulation.input['volume'] = volume_value
    
    # Compute the result
    try:
        gender_simulation.compute()
        result = gender_simulation.output['gender']
        print(f"Fuzzy logic output: {result}")
        return result
    except Exception as e:
        print(f"Error during fuzzy logic computation: {e}")
        return None
