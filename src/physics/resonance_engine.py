import numpy as np

class ResonanceEngine:
    def __init__(self, min_freq, max_freq):
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.current_freq = min_freq
        
    def calculate_resonance_frequency(self, mass, spring_constant):
        omega = np.sqrt(spring_constant / mass)
        return omega / (2 * np.pi)
    
    def frequency_sweep(self, num_points):
        return np.linspace(self.min_freq, self.max_freq, num_points)
    
    def detect_constructive_interference(self, impedance, threshold=0.05):
        impedance_drop = abs(impedance - self.current_freq)
        if impedance_drop < threshold:
            return True, self.current_freq
        return False, None
    
    def set_frequency(self, freq):
        self.current_freq = freq

if __name__ == "__main__":
    engine = ResonanceEngine(min_freq=1e6, max_freq=1e9)
    sweep = engine.frequency_sweep(100)
    print(f"Frequency sweep range: {sweep[0]:.2e} to {sweep[-1]:.2e} Hz")
    resonance = engine.calculate_resonance_frequency(mass=1.0, spring_constant=1e6)
    print(f"Calculated resonance frequency: {resonance:.2e} Hz")
