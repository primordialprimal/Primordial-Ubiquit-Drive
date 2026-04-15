import numpy as np

class PhaseLock:
    def __init__(self, target_phase=0.0):
        self.target_phase = target_phase
        self.current_phase = 0.0
        self.locked = False
        self.lock_tolerance = 0.01
        
    def phase_detection(self, signal):
        """Detect phase of input signal"""
        fft = np.fft.fft(signal)
        phase = np.angle(fft[1])
        self.current_phase = phase
        return phase
    
    def synchronize(self, error):
        """Synchronize phase using proportional control"""
        correction = error * 0.1
        self.current_phase += correction
        return self.current_phase
    
    def check_lock(self):
        """Check if phase is locked within tolerance"""
        phase_error = abs(self.target_phase - self.current_phase)
        if phase_error < self.lock_tolerance:
            self.locked = True
        else:
            self.locked = False
        return self.locked
    
    def lock_phase(self):
        """Engage phase lock"""
        self.locked = True
    
    def unlock_phase(self):
        """Disengage phase lock"""
        self.locked = False
    
    def get_phase_error(self):
        """Get current phase error"""
        return self.target_phase - self.current_phase

if __name__ == "__main__":
    phase_lock = PhaseLock(target_phase=np.pi/2)
    signal = np.sin(np.linspace(0, 2*np.pi, 1000))
    detected_phase = phase_lock.phase_detection(signal)
    print(f"Detected phase: {detected_phase:.4f}")
    print(f"Target phase: {phase_lock.target_phase:.4f}")
    print(f"Phase locked: {phase_lock.check_lock()}")