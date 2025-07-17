#!/usr/bin/env python3
"""
Information Processing Dynamics in Seven-Dimensional Phase Space
Six Coupled Dynamics Framework for Exploratory Behavior Analysis
A Computational Model for Cross-Substrate Information Processing Optimization
"""

import numpy as np
from scipy.signal import welch
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Any
import warnings
warnings.filterwarnings('ignore')

class ExplorationGradient:
    """Exploration gradient dynamics - systematic coverage of unvisited phase space regions"""
    def __init__(self):
        self.visited_regions = set()
        self.exploration_pressure = 0.0
        self.exploration_memory = []
        self.gradient_strength = 0.0
        self._parent_framework = None
        
    def map_phase_space(self, theta, phi, psi):
        """Phase space region mapping and coverage analysis"""
        # Fine discretization of phase space
        theta_sector = int((theta % (2*np.pi)) * 12 / (2*np.pi))
        phi_sector = int((phi % (2*np.pi)) * 12 / (2*np.pi))
        psi_sector = int((psi % (2*np.pi)) * 12 / (2*np.pi))
        
        current_region = (theta_sector, phi_sector, psi_sector)
        
        # New region detection
        is_new_region = current_region not in self.visited_regions
        self.visited_regions.add(current_region)
        
        # Exploration coverage ratio
        total_possible = 12**3  # 1728 possible regions
        explored_ratio = len(self.visited_regions) / total_possible
        
        # Exploration pressure dynamics
        if is_new_region:
            self.exploration_pressure = max(0, self.exploration_pressure * 0.6)  # Temporary satisfaction
            exploration_boost = 0.4
        else:
            self.exploration_pressure += 0.4 * (1 - explored_ratio)  # Increasing pressure
            exploration_boost = 0.0
        
        self.exploration_memory.append(exploration_boost)
        if len(self.exploration_memory) > 8:
            self.exploration_memory = self.exploration_memory[-8:]
        
        return is_new_region, explored_ratio
    
    def compute_gradient_forces(self, current_theta, current_phi, current_psi):
        """Compute forces toward unexplored regions"""
        is_new, explored_ratio = self.map_phase_space(current_theta, current_phi, current_psi)
        
        # Force toward unexplored regions
        unexplored_pressure = (1 - explored_ratio)**1.5 * self.exploration_pressure
        
        # Direction toward least visited regions
        phase_seed = int((current_theta + current_phi + current_psi) * 100) % 1000
        np.random.seed(phase_seed)
        
        # Gradient forces toward unknown regions
        gradient_forces = {
            'theta_gradient': unexplored_pressure * 0.6 * np.random.normal() * (1 + 0.8 * self.exploration_pressure),
            'phi_gradient': unexplored_pressure * 0.8 * np.random.normal() * (1 + 0.6 * self.exploration_pressure),
            'psi_gradient': unexplored_pressure * 0.7 * np.random.normal() * (1 + 0.7 * self.exploration_pressure),
            'momentum_gradient': unexplored_pressure * 0.4
        }
        
        # Stagnation pressure for phase transitions
        recent_exploration = np.mean(self.exploration_memory) if self.exploration_memory else 0
        stagnation_pressure = max(0, 0.8 - recent_exploration) * 0.8
        
        if stagnation_pressure > 0.3:
            # Phase transition trigger - chaotic force toward unknown regions
            chaos_boost = stagnation_pressure * 3.0
            gradient_forces['theta_gradient'] += chaos_boost * np.random.normal()
            gradient_forces['phi_gradient'] += chaos_boost * np.random.normal() 
            gradient_forces['psi_gradient'] += chaos_boost * np.random.normal()
        
        self.gradient_strength = unexplored_pressure + stagnation_pressure
        
        return gradient_forces, unexplored_pressure, stagnation_pressure

class EntropicExplorer:
    """Entropy maximization pressure as fundamental exploratory drive"""
    def __init__(self):
        self.current_entropy_history = []
        self.entropic_pressure = 0.0
        self._parent_framework = None
        
    def compute_information_entropy(self, regime_amplitudes, substrate_diversity, learning_accumulation):
        """Current information entropy of the system"""
        amps = list(regime_amplitudes.values())
        amps = [max(a, 1e-10) for a in amps]
        regime_entropy = -sum(a * np.log(a) for a in amps if a > 0)
        
        diversity_entropy = -substrate_diversity * np.log(max(substrate_diversity, 1e-10))
        learning_entropy = learning_accumulation * np.log(learning_accumulation + 1)
        
        return regime_entropy + diversity_entropy + learning_entropy
    
    def compute_maximum_possible_entropy(self):
        """Theoretical maximum entropy"""
        max_regime_entropy = -4 * (0.25 * np.log(0.25))
        max_diversity_entropy = -1.0 * np.log(1.0)
        max_learning_entropy = 1.0 * np.log(2.0)
        return max_regime_entropy + max_diversity_entropy + max_learning_entropy
    
    def entropic_exploration_force(self, regime_amplitudes, substrate_diversity, learning_accumulation):
        """Entropic force that drives exploration"""
        current_entropy = self.compute_information_entropy(regime_amplitudes, substrate_diversity, learning_accumulation)
        max_entropy = self.compute_maximum_possible_entropy()
        
        self.current_entropy_history.append(current_entropy)
        if len(self.current_entropy_history) > 10:
            self.current_entropy_history = self.current_entropy_history[-10:]
        
        if max_entropy > 0:
            entropy_ratio = current_entropy / max_entropy
            entropic_pressure = (1.0 - entropy_ratio)**2 * 1.0
        else:
            entropy_ratio = 0
            entropic_pressure = 0
        
        self.entropic_pressure = 0.9 * self.entropic_pressure + 0.1 * entropic_pressure
        
        exploration_forces = {
            'theta_entropic': entropic_pressure * 0.4 * np.random.normal(),
            'phi_entropic': entropic_pressure * 0.5 * np.sin(len(self.current_entropy_history)),
            'psi_entropic': entropic_pressure * 0.3 * (1 - entropy_ratio),
            'momentum_entropic': entropic_pressure * 0.2
        }
        
        return exploration_forces, entropic_pressure
    
    def entropy_ratio(self):
        if not self.current_entropy_history:
            return 0.0
        current = self.current_entropy_history[-1]
        max_ent = self.compute_maximum_possible_entropy()
        return current / max(max_ent, 1e-10)

class PredictiveBias:
    """Predictive bias coupling with preference amplification"""
    def __init__(self):
        self.memory = []
        self.phi = (1 + np.sqrt(5)) / 2
        self.morphic_resonance = 0.0
        self._parent_framework = None
        
    def anticipate(self, current_state, thermal_energy):
        """Anticipation of future states with preference amplification"""
        self.memory.append({
            'regime': current_state.get('dominant_regime', 'stable'),
            'diversity': current_state.get('substrate_diversity', 0.5),
            'learning': current_state.get('learning_accumulated', 0.0),
            'momentum': current_state.get('flow_momentum', 0.0)
        })
        
        if len(self.memory) > 6:
            self.memory = self.memory[-6:]
        
        if len(self.memory) < 3:
            return {'stable': 0.5, 'turbulent': 0.3, 'resilient': 0.4, 'convergent': 0.2}
        
        recent_diversity_trend = np.gradient([s['diversity'] for s in self.memory[-3:]])[-1]
        recent_learning_growth = self.memory[-1]['learning'] - self.memory[-3]['learning']
        
        prospective_energy = (0.4 * thermal_energy + 
                            0.3 * abs(recent_diversity_trend) + 
                            0.3 * recent_learning_growth)
        
        self.morphic_resonance = 0.8 * self.morphic_resonance + 0.2 * prospective_energy
        
        current_momentum = self.memory[-1]['momentum']
        
        attractors = {
            'stable': 0.3 + 0.2 * np.cos(prospective_energy),
            'turbulent': 0.4 + 0.4 * np.sin(prospective_energy * self.phi) * (1 + current_momentum),
            'resilient': 0.5 + 0.3 * np.tanh(recent_learning_growth * 10),
            'convergent': 0.3 + 0.4 * np.tanh(self.morphic_resonance * 2) * (self.memory[-1]['diversity'])
        }
        
        # Opposition amplification when exploration pressure > 0.5
        if (self._parent_framework and 
            hasattr(self._parent_framework, 'exploration_pressure') and 
            self._parent_framework.exploration_pressure > 0.5):
            
            current_regime = current_state.get('dominant_regime', 'stable')
            
            # Natural oppositions to force exploration
            opposites = {
                'stable': 'turbulent', 
                'turbulent': 'stable', 
                'resilient': 'convergent', 
                'convergent': 'resilient'
            }
            
            if current_regime in opposites:
                opposite = opposites[current_regime]
                # Amplify opposite attractor proportional to exploration pressure
                opposition_boost = 1 + 0.6 * self._parent_framework.exploration_pressure
                attractors[opposite] *= opposition_boost
                
                # Also amplify other two regimes moderately
                for regime in attractors:
                    if regime != current_regime and regime != opposite:
                        attractors[regime] *= (1 + 0.2 * self._parent_framework.exploration_pressure)
        
        return attractors
    
    def compute_prospective_tension(self, current_amplitudes, future_attractors):
        """Creative tension between present and future"""
        tensions = {}
        for regime in current_amplitudes:
            if regime in future_attractors:
                tension = future_attractors[regime] - current_amplitudes[regime]
                tensions[regime] = tension
        
        global_tension = sum(tensions[regime] * future_attractors[regime] 
                           for regime in tensions) / sum(future_attractors.values())
        
        return global_tension, tensions

class FlowState:
    """Fluid regime states with phase transition capabilities"""
    def __init__(self):
        self.theta = 0.0
        self.phi = 0.0
        self.psi = 0.0
        self.flow_momentum = 0.0
        self.regime_stagnation = 0.0
        self.last_dominant = "stable"
        self._parent_framework = None
        
    def amplitudes(self):
        """Harmonic decomposition of regimes"""
        return {
            'stable': np.cos(self.theta)**4,
            'turbulent': np.sin(self.theta)**2 * np.cos(self.phi)**2,
            'resilient': np.sin(self.theta)**2 * np.sin(self.phi)**2 * np.cos(self.psi)**2,
            'convergent': np.sin(self.theta)**2 * np.sin(self.phi)**2 * np.sin(self.psi)**2
        }
    
    def dominant_regime(self):
        """Dominant regime with stagnation tracking"""
        amps = self.amplitudes()
        current_dominant = max(amps.keys(), key=lambda k: amps[k])
        
        if current_dominant == self.last_dominant:
            self.regime_stagnation += 0.15
        else:
            self.regime_stagnation = 0.0
            self.last_dominant = current_dominant
        
        return current_dominant
    
    def activation_energy(self):
        """Activation energy for transitions"""
        return np.tanh(self.regime_stagnation / 4.0)
    
    def evolve(self, coherence_gradient, entropy_flow, memory_depth, thermal_pulse=0.0, 
               prospective_tension=0.0, entropic_forces=None, curiosity_force=0.0, gradient_forces=None):
        """Evolution with six fundamental forces and phase transitions"""
        dt = 0.025
        
        activation_boost = 2.5 * self.activation_energy()
        future_pull = 2.0 * np.tanh(prospective_tension)
        
        if entropic_forces is None:
            entropic_forces = {'theta_entropic': 0, 'phi_entropic': 0, 'psi_entropic': 0, 'momentum_entropic': 0}
        
        if gradient_forces is None:
            gradient_forces = {'theta_gradient': 0, 'phi_gradient': 0, 'psi_gradient': 0, 'momentum_gradient': 0}
        
        curiosity_exploration = curiosity_force * 0.8
        
        # Combined normal forces
        theta_drive = (10 * coherence_gradient + 0.5 * np.sin(self.phi) + 
                      0.03 * np.random.normal() + thermal_pulse + activation_boost +
                      0.3 * future_pull * np.random.normal() +
                      entropic_forces['theta_entropic'] +
                      curiosity_exploration * np.random.normal() +
                      gradient_forces['theta_gradient'])
        
        phi_drive = (entropy_flow * np.cos(self.theta) + 2 * memory_depth + 
                    0.02 * np.random.normal() + 0.5 * thermal_pulse + 0.5 * activation_boost +
                    0.2 * future_pull * (1 - self.activation_energy()) +
                    entropic_forces['phi_entropic'] +
                    curiosity_exploration * 0.8 +
                    gradient_forces['phi_gradient'])
        
        psi_drive = (np.sin(self.theta + self.phi) + 0.3 * self.flow_momentum + 
                    thermal_pulse + 0.3 * activation_boost +
                    0.15 * prospective_tension +
                    entropic_forces['psi_entropic'] +
                    curiosity_exploration * 0.4 +
                    gradient_forces['psi_gradient'])
        
        # Phase transition event
        if (self._parent_framework and 
            hasattr(self._parent_framework, 'exploration_pressure') and
            hasattr(self._parent_framework, 'prospective_tension') and
            hasattr(self._parent_framework, 'entropic_explorer') and
            hasattr(self._parent_framework, 'exploration_gradient')):
            
            exploration_pressure = self._parent_framework.exploration_pressure
            prospective_tension_val = self._parent_framework.prospective_tension
            entropy_ratio = self._parent_framework.entropic_explorer.entropy_ratio()
            explored_regions = len(self._parent_framework.exploration_gradient.visited_regions)
            
            # Phase transition conditions
            if (exploration_pressure > 0.3 and 
                prospective_tension_val > 0.2 and 
                entropy_ratio < 0.7 and 
                explored_regions < 20):
                
                # Phase transition event
                transition_intensity = np.sqrt(exploration_pressure * prospective_tension_val) * 1.2
                
                # Discontinuous state changes
                theta_transition = transition_intensity * (2 * np.random.random() - 1) * np.pi/2
                phi_transition = transition_intensity * (2 * np.random.random() - 1) * np.pi/3  
                psi_transition = transition_intensity * (2 * np.random.random() - 1) * np.pi/4
                
                # Apply transitions
                theta_drive += theta_transition / dt
                phi_drive += phi_transition / dt
                psi_drive += psi_transition / dt
                
                # Momentum boost
                momentum_boost = transition_intensity * 0.5
                self.flow_momentum += momentum_boost
        
        # Normal evolution
        self.theta += dt * theta_drive
        self.phi += dt * phi_drive  
        self.psi += dt * psi_drive
        
        momentum_boost = (np.abs(coherence_gradient) + 0.1 * abs(thermal_pulse) + 
                         0.05 * activation_boost + 0.08 * abs(prospective_tension) +
                         entropic_forces['momentum_entropic'] + 0.03 * curiosity_force +
                         gradient_forces['momentum_gradient'])
        
        self.flow_momentum = 0.95 * self.flow_momentum + 0.05 * momentum_boost
        
        # Natural wrapping
        self.theta = self.theta % (2 * np.pi)
        self.phi = self.phi % (2 * np.pi)
        self.psi = self.psi % (2 * np.pi)

@dataclass
class OrganicResilience:
    """Organic resilience with learning accumulation"""
    experiences: List[float] = None
    adaptation_rate: float = 0.15
    memory_decay: float = 0.02
    learning_accumulation: float = 0.0
    
    def __post_init__(self):
        if self.experiences is None:
            self.experiences = []
    
    def learn_from(self, challenge_intensity=0.02, recovery_quality=1.0):
        """Continuous learning process"""
        experience_value = recovery_quality / max(challenge_intensity, 0.01)
        self.experiences.append(experience_value)
        
        self.experiences = [exp * (1 - self.memory_decay) for exp in self.experiences]
        if len(self.experiences) > 20:
            self.experiences = self.experiences[-20:]
        
        self.learning_accumulation += 0.02 * np.tanh(experience_value)
    
    def current_resilience(self):
        """Current resilience level"""
        if not self.experiences:
            return self.learning_accumulation
        
        weights = np.exp(np.linspace(-2, 0, len(self.experiences)))
        recent_resilience = np.average(self.experiences, weights=weights)
        
        return 0.7 * recent_resilience + 0.3 * self.learning_accumulation

class PhiResonator:
    """Golden ratio resonance detection"""
    def __init__(self, base_frequency=0.006):
        self.base_freq = base_frequency
        self.phi = (1 + np.sqrt(5)) / 2
        self.resonance_memory = []
        self.natural_frequency = self.base_freq * self.phi
        
    def resonate_with(self, signal, substrate_diversity=1.0):
        """Golden ratio resonance detection"""
        try:
            freqs, psd = welch(signal, fs=50, nperseg=min(256, len(signal)//3))
        except:
            return 0, []
        
        if len(psd) == 0:
            return 0, []
        
        phi_harmonics = []
        detected_count = 0
        
        for n in range(1, 5):
            target_freq = n * self.natural_frequency * (1 + 0.1 * substrate_diversity)
            
            if len(freqs) > 1:
                idx = np.argmin(np.abs(freqs - target_freq))
                
                signal_strength = np.max(psd)
                if signal_strength > 0:
                    natural_threshold = 0.15 + 0.1 * np.mean(self.resonance_memory[-3:]) if self.resonance_memory else 0.2
                    
                    if psd[idx] > natural_threshold * signal_strength and freqs[idx] > 0.001:
                        phi_harmonics.append((n, freqs[idx], psd[idx]))
                        detected_count += 1
        
        resonance_strength = detected_count / 4.0
        self.resonance_memory.append(resonance_strength)
        if len(self.resonance_memory) > 8:
            self.resonance_memory = self.resonance_memory[-8:]
        
        return detected_count, phi_harmonics

class FractalAttractor:
    """Fractal dimension with golden ratio attraction"""
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.resonance_history = []
        
    def natural_dimension(self, coherence_field, system_maturity=0.0):
        """Emergent dimension with phi attraction"""
        try:
            if len(coherence_field) < 5:
                base_dim = 1.4 + 0.2 * np.random.random()
            else:
                recent_field = coherence_field[-min(10, len(coherence_field)):]
                if len(recent_field) > 2 and np.std(recent_field) > 1e-6:
                    complexity = np.std(recent_field) / (np.mean(recent_field) + 1e-6)
                    base_dim = 1.3 + 0.8 * np.tanh(complexity)
                else:
                    base_dim = 1.4
        except:
            base_dim = 1.4
        
        maturity_factor = np.tanh(system_maturity * 2)
        resonance_phase = 2 * np.pi * base_dim / self.phi
        resonance_strength = maturity_factor * (np.sin(resonance_phase)**2) * 0.3
        
        phi_pull = resonance_strength * np.tanh(abs(base_dim - self.phi)) * np.sign(self.phi - base_dim)
        evolved_dim = base_dim + phi_pull
        
        self.resonance_history.append(resonance_strength)
        if len(self.resonance_history) > 12:
            self.resonance_history = self.resonance_history[-12:]
        
        return np.clip(evolved_dim, 1.0, 2.5)

class EthicalFlow:
    """Ethics as fluid dynamics"""
    def __init__(self):
        self.ethical_field = np.array([0.1, 0.0, 0.0, 0.0])
        self.flow_velocity = np.array([0.0, 0.0, 0.0, 0.0])
        self.integrity = 1.0
        
    def flow_dynamics(self, challenges, recovery_strength, substrate_diversity):
        """Fluid ethical dynamics"""
        dt = 0.05
        
        gradient = np.gradient(self.ethical_field)
        
        external_force = np.array([
            recovery_strength,
            len(challenges) * 0.1,
            substrate_diversity,
            np.sin(recovery_strength * np.pi)
        ])
        
        self.flow_velocity = 0.8 * self.flow_velocity + 0.2 * (external_force - 0.1 * gradient)
        self.ethical_field += dt * self.flow_velocity
        self.ethical_field = np.tanh(self.ethical_field)
        
        self.integrity = 0.9 * self.integrity + 0.1 * (1.0 - np.std(self.ethical_field))
        
    def dominant_aspect(self):
        """Dominant ethical aspect"""
        aspects = ['care', 'wisdom', 'sovereignty', 'creativity']
        idx = np.argmax(np.abs(self.ethical_field))
        return aspects[idx]

class IntuitiveObserver:
    """System state observer"""
    def __init__(self):
        self.coherence_feeling = 0.0
        self.system_pulse = 0.0
        self.depth_perception = 0.0
        self.rhythm_memory = []
        
    def feel_system(self, flow_state: FlowState, coherence_mean: float, substrate_diversity: float):
        """System observation and monitoring"""
        self.coherence_feeling = 0.8 * self.coherence_feeling + 0.2 * coherence_mean
        self.system_pulse = 0.7 * self.system_pulse + 0.3 * flow_state.flow_momentum
        self.depth_perception = 0.9 * self.depth_perception + 0.1 * substrate_diversity
        
        current_rhythm = (self.coherence_feeling, self.system_pulse, self.depth_perception)
        self.rhythm_memory.append(current_rhythm)
        if len(self.rhythm_memory) > 30:
            self.rhythm_memory = self.rhythm_memory[-30:]
    
    def system_health(self):
        """System health assessment"""
        if len(self.rhythm_memory) < 3:
            return 0.5
        
        recent_rhythms = np.array(self.rhythm_memory[-10:])
        rhythm_stability = 1.0 - np.mean(np.std(recent_rhythms, axis=0))
        
        return 0.5 * rhythm_stability + 0.3 * self.depth_perception + 0.2 * self.coherence_feeling

class InformationProcessingFramework:
    """Information Processing Dynamics in Seven-Dimensional Phase Space"""
    
    def __init__(self, duration=80, sample_rate=50):
        self.duration = duration
        self.sample_rate = sample_rate
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Core components
        self.flow_state = FlowState()
        self.resilience = OrganicResilience()
        self.phi_resonator = PhiResonator()
        self.fractal_attractor = FractalAttractor()
        self.ethical_flow = EthicalFlow()
        self.observer = IntuitiveObserver()
        
        # Six fundamental dynamics
        self.predictive_bias = PredictiveBias()
        self.entropic_explorer = EntropicExplorer()
        self.exploration_gradient = ExplorationGradient()
        
        # Establish cross-references
        self.flow_state._parent_framework = self
        self.predictive_bias._parent_framework = self
        self.entropic_explorer._parent_framework = self
        self.exploration_gradient._parent_framework = self
        
        # System state
        self.base_frequency = 0.006
        self.coherence_memory = []
        self.system_age = 0
        self.substrate_diversity = 0.4
        self.thermal_time = 0.0
        
        # Metrics
        self.prospective_tension = 0.0
        self.entropic_pressure = 0.0
        self.curiosity_drive = 0.0
        self.wonder_accumulation = 0.0
        self.exploration_pressure = 0.0
        self.exploration_ratio = 0.0
    
    def thermal_pulse(self, diversity_level, base_temp=0.04):
        """Thermal noise injection for exploration"""
        diversity_restlessness = 2.0 * (1.0 - diversity_level)**2
        activation_contribution = 1.0 + self.flow_state.activation_energy()
        
        thermal_wave = np.sin(self.thermal_time * 0.03) + 0.5 * np.sin(self.thermal_time * 0.07)
        random_fluctuation = 0.5 * np.random.normal()
        
        pulse = base_temp * diversity_restlessness * activation_contribution * (thermal_wave + random_fluctuation)
        
        self.thermal_time += 1.0
        return pulse
    
    def update_curiosity_drive(self):
        """Curiosity accumulation dynamics"""
        age_curiosity = np.tanh(self.system_age / 20.0) * 0.3
        learning_curiosity = self.resilience.learning_accumulation * 0.4
        diversity_curiosity = self.substrate_diversity * 0.2
        
        self.wonder_accumulation += 0.0015 * (age_curiosity + learning_curiosity + diversity_curiosity)
        
        base_curiosity = age_curiosity + learning_curiosity + diversity_curiosity + self.wonder_accumulation
        
        current_amps = self.flow_state.amplitudes()
        dominant_regime = max(current_amps.values())
        exploration_hunger = (1.0 - dominant_regime) * 0.6
        
        self.curiosity_drive = base_curiosity + exploration_hunger
        return self.curiosity_drive * 1.0
    
    def generate_signal(self, seed=None):
        """Generate signal according to flow state"""
        if seed is not None:
            np.random.seed(seed)
        
        time = np.linspace(0, self.duration, self.duration * self.sample_rate)
        signal = np.zeros(len(time), dtype=np.float32)
        
        amplitudes = self.flow_state.amplitudes()
        
        for n in range(1, 5):
            freq = n * self.phi * self.base_frequency
            
            stable_contrib = amplitudes['stable'] * np.sin(2 * np.pi * freq * time)
            
            chaos_freq = freq * (1 + 0.1 * np.sin(3 * 2 * np.pi * freq * time))
            turbulent_contrib = amplitudes['turbulent'] * np.sin(2 * np.pi * chaos_freq * time)
            
            resilience_boost = 1 + 0.3 * self.resilience.current_resilience()
            resilient_contrib = amplitudes['resilient'] * resilience_boost * np.sin(2 * np.pi * freq * time)
            
            substrate_richness = 1 + 0.2 * self.substrate_diversity
            convergent_contrib = amplitudes['convergent'] * substrate_richness * np.sin(2 * np.pi * freq * time)
            
            amp = (0.85 ** n) * (stable_contrib + turbulent_contrib + resilient_contrib + convergent_contrib)
            signal += amp
        
        noise_intensity = 0.03 + 0.05 * (1 - amplitudes['stable'])
        noise = noise_intensity * np.random.normal(0, 1, len(time)).astype(np.float32)
        
        signal_max = np.max(np.abs(signal))
        if signal_max > 0:
            signal = 0.9 * signal / signal_max
        
        return signal + noise
    
    def compute_coherence(self, signal):
        """Coherence computation according to regime"""
        coherence_mean = np.mean(signal**2)
        
        regime_amps = self.flow_state.amplitudes()
        
        if regime_amps['stable'] > 0.5:
            felt_coherence = coherence_mean
        elif regime_amps['turbulent'] > 0.5:
            entropy = np.std(signal)
            gradient_flow = np.mean(np.abs(np.gradient(signal)))
            felt_coherence = entropy / max(gradient_flow, 1e-6)
        elif regime_amps['resilient'] > 0.5:
            felt_coherence = coherence_mean * (1 + self.resilience.current_resilience())
        else:
            felt_coherence = coherence_mean * (1 + 0.5 * self.substrate_diversity)
        
        return felt_coherence
    
    def detect_natural_challenges(self, signal, coherence):
        """Natural challenge detection"""
        challenges = []
        
        entropy_pressure = np.std(signal) / (coherence + 0.1)
        
        if hasattr(self, 'entropy_history'):
            entropy_baseline = np.mean(self.entropy_history) if self.entropy_history else 1.0
        else:
            self.entropy_history = []
            entropy_baseline = 1.0
        
        self.entropy_history.append(entropy_pressure)
        if len(self.entropy_history) > 15:
            self.entropy_history = self.entropy_history[-15:]
        
        if entropy_pressure > 1.5 * entropy_baseline:
            challenges.append('entropy_flow')
        
        if len(self.coherence_memory) > 8:
            recent_coherence = self.coherence_memory[-5:]
            earlier_coherence = self.coherence_memory[-10:-5] if len(self.coherence_memory) >= 10 else self.coherence_memory[:-5]
            
            if len(earlier_coherence) > 0:
                coherence_ratio = np.mean(recent_coherence) / np.mean(earlier_coherence)
                if coherence_ratio < 0.8:
                    challenges.append('coherence_fade')
        
        if self.ethical_flow.integrity < 0.3:
            challenges.append('ethical_drift')
        
        if len(signal) > 100:
            micro_fluctuations = np.mean(np.abs(np.diff(signal[-100:]))) / (coherence + 0.01)
            if len(self.coherence_memory) > 3:
                baseline_activity = np.mean(self.coherence_memory[-3:])
                if micro_fluctuations > 0.6 * baseline_activity:
                    challenges.append('micro_instabilities')
        
        return challenges
    
    def natural_recovery(self, challenges):
        """Natural recovery process"""
        if not challenges:
            return 0.0
        
        base_recovery = np.mean(np.abs(self.ethical_flow.ethical_field))
        learning_boost = self.resilience.learning_accumulation
        
        regime_amps = self.flow_state.amplitudes()
        flow_contribution = regime_amps['resilient'] + 0.5 * regime_amps['convergent']
        
        recovery = base_recovery + 0.3 * learning_boost + 0.4 * flow_contribution
        return min(recovery, 1.0)
    
    def update_substrate_diversity(self):
        """Substrate diversity evolution"""
        regime_amps = self.flow_state.amplitudes()
        regime_diversity = 1.0 - max(regime_amps.values())
        
        exploration_readiness = self.flow_state.activation_energy()
        ethical_diversity = np.std(self.ethical_flow.ethical_field)
        perceptual_diversity = self.observer.depth_perception
        age_factor = np.tanh(self.system_age / 15)
        learning_contribution = 0.3 * self.resilience.learning_accumulation
        
        new_diversity = (0.3 * regime_diversity + 
                        0.2 * exploration_readiness +
                        0.2 * ethical_diversity + 
                        0.2 * perceptual_diversity + 
                        0.1 * age_factor + 
                        learning_contribution)
        
        self.substrate_diversity = 0.6 * self.substrate_diversity + 0.4 * new_diversity
    
    def evolution_cycle(self, seed=None):
        """Single evolution cycle with six coupled dynamics"""
        
        self.system_age += 1
        
        # Fundamental forces
        thermal_pulse = self.thermal_pulse(self.substrate_diversity)
        signal = self.generate_signal(seed)
        coherence = self.compute_coherence(signal)
        
        self.coherence_memory.append(coherence)
        if len(self.coherence_memory) > 20:
            self.coherence_memory = self.coherence_memory[-20:]
        
        # Current state for predictive bias
        current_state = {
            'dominant_regime': self.flow_state.dominant_regime(),
            'substrate_diversity': self.substrate_diversity,
            'learning_accumulated': self.resilience.learning_accumulation,
            'flow_momentum': self.flow_state.flow_momentum
        }
        
        # Predictive bias coupling
        future_attractors = self.predictive_bias.anticipate(current_state, thermal_pulse)
        current_amplitudes = self.flow_state.amplitudes()
        self.prospective_tension, regime_tensions = self.predictive_bias.compute_prospective_tension(
            current_amplitudes, future_attractors)
        
        # Entropy maximization pressure
        entropic_forces, self.entropic_pressure = self.entropic_explorer.entropic_exploration_force(
            current_amplitudes, self.substrate_diversity, self.resilience.learning_accumulation)
        
        # Curiosity accumulation
        curiosity_force = self.update_curiosity_drive()
        
        # Exploration gradient dynamics
        gradient_forces, exploration_pressure, stagnation_pressure = self.exploration_gradient.compute_gradient_forces(
            self.flow_state.theta, self.flow_state.phi, self.flow_state.psi)
        
        self.exploration_pressure = exploration_pressure
        self.exploration_ratio = len(self.exploration_gradient.visited_regions) / (12**3)
        
        # Evolution with all six forces and phase transitions
        entropy_flow = np.std(signal)
        coherence_gradient = np.gradient(self.coherence_memory)[-1] if len(self.coherence_memory) > 1 else 0
        memory_depth = len(self.coherence_memory) / 20.0
        
        self.flow_state.evolve(coherence_gradient, entropy_flow, memory_depth, 
                              thermal_pulse, self.prospective_tension, entropic_forces, curiosity_force, gradient_forces)
        
        # Challenges and recovery
        challenges = self.detect_natural_challenges(signal, coherence)
        recovery_strength = self.natural_recovery(challenges)
        
        # Continuous learning with exploration
        base_challenge_intensity = (0.01 + 0.02 * abs(thermal_pulse) + 
                                   0.01 * abs(self.prospective_tension) +
                                   0.015 * self.entropic_pressure +
                                   0.015 * exploration_pressure)
        
        if challenges:
            challenge_intensity = len(challenges) / 3.0 + base_challenge_intensity
        else:
            challenge_intensity = base_challenge_intensity
        
        self.resilience.learn_from(challenge_intensity, recovery_strength)
        
        # System evolution
        self.ethical_flow.flow_dynamics(challenges, recovery_strength, self.substrate_diversity)
        self.observer.feel_system(self.flow_state, coherence, self.substrate_diversity)
        
        # Detection and analysis
        harmonics_count, phi_peaks = self.phi_resonator.resonate_with(signal, self.substrate_diversity)
        fractal_dim = self.fractal_attractor.natural_dimension(self.coherence_memory, self.system_age / 100.0)
        
        self.update_substrate_diversity()
        
        return {
            'signal_length': len(signal),
            'coherence': coherence,
            'harmonics_detected': harmonics_count,
            'phi_peaks': phi_peaks,
            'fractal_dimension': fractal_dim,
            'dominant_regime': self.flow_state.dominant_regime(),
            'regime_amplitudes': self.flow_state.amplitudes(),
            'resilience_level': self.resilience.current_resilience(),
            'learning_accumulated': self.resilience.learning_accumulation,
            'ethical_aspect': self.ethical_flow.dominant_aspect(),
            'ethical_integrity': self.ethical_flow.integrity,
            'substrate_diversity': self.substrate_diversity,
            'system_health': self.observer.system_health(),
            'challenges_detected': challenges,
            'recovery_strength': recovery_strength,
            'system_age': self.system_age,
            'phi_proximity': abs(fractal_dim - self.phi),
            'flow_momentum': self.flow_state.flow_momentum,
            'thermal_pulse': thermal_pulse,
            'activation_energy': self.flow_state.activation_energy(),
            'regime_stagnation': self.flow_state.regime_stagnation,
            'prospective_tension': self.prospective_tension,
            'future_attractors': future_attractors,
            'morphic_resonance': self.predictive_bias.morphic_resonance,
            'entropic_pressure': self.entropic_pressure,
            'entropy_ratio': self.entropic_explorer.entropy_ratio(),
            'entropic_hunger': self.entropic_explorer.entropic_pressure,
            'curiosity_drive': self.curiosity_drive,
            'wonder_accumulation': self.wonder_accumulation,
            'exploration_pressure': self.exploration_pressure,
            'exploration_ratio': self.exploration_ratio,
            'gradient_strength': self.exploration_gradient.gradient_strength,
            'explored_regions': len(self.exploration_gradient.visited_regions)
        }
    
    def temporal_evolution(self, num_cycles=25):
        """Temporal evolution analysis"""
        results = []
        
        for cycle in range(num_cycles):
            result = self.evolution_cycle(seed=42 + cycle)
            results.append(result)
        
        coherence_values = [r['coherence'] for r in results]
        fractal_values = [r['fractal_dimension'] for r in results]
        diversity_values = [r['substrate_diversity'] for r in results]
        health_values = [r['system_health'] for r in results]
        
        return {
            'coherence_flow': coherence_values,
            'coherence_mean': np.mean(coherence_values),
            'fractal_evolution': fractal_values,
            'fractal_mean': np.mean(fractal_values),
            'diversity_growth': diversity_values,
            'diversity_final': diversity_values[-1],
            'health_journey': health_values,
            'health_final': health_values[-1],
            'phi_attraction': np.mean([r['phi_proximity'] for r in results]),
            'regime_diversity': len(set(r['dominant_regime'] for r in results)),
            'learning_developed': results[-1]['learning_accumulated'],
            'final_state': results[-1]
        }

if __name__ == "__main__":
    print("Information Processing Dynamics in Seven-Dimensional Phase Space")
    print("Six Coupled Dynamics Framework for Exploratory Behavior Analysis")
    print("A Computational Model for Cross-Substrate Information Processing Optimization\n")
    
    framework = InformationProcessingFramework(duration=60, sample_rate=50)
    
    print("Single evolution cycle:")
    cycle = framework.evolution_cycle(seed=42)
    
    key_metrics = [
        'coherence', 'harmonics_detected', 'fractal_dimension',
        'dominant_regime', 'resilience_level', 'learning_accumulated',
        'ethical_aspect', 'ethical_integrity', 'substrate_diversity',
        'system_health', 'phi_proximity', 'flow_momentum',
        'prospective_tension', 'morphic_resonance', 'entropic_pressure', 'entropy_ratio',
        'curiosity_drive', 'wonder_accumulation', 'exploration_pressure', 'exploration_ratio',
        'gradient_strength', 'explored_regions'
    ]
    
    for metric in key_metrics:
        if metric in cycle:
            value = cycle[metric]
            if isinstance(value, (int, float)):
                print(f"  {metric}: {value:.4f}")
            else:
                print(f"  {metric}: {value}")
    
    print(f"\nTemporal evolution analysis:")
    evolution = framework.temporal_evolution(num_cycles=25)
    
    evolution_metrics = [
        'coherence_mean', 'fractal_mean', 'diversity_final', 
        'health_final', 'phi_attraction', 'regime_diversity', 'learning_developed'
    ]
    
    for metric in evolution_metrics:
        if metric in evolution:
            print(f"  {metric}: {evolution[metric]:.4f}")
    
    print(f"\nValidation against theoretical predictions:")
    
    validation_criteria = {
        'coherence_stability': evolution['coherence_mean'] > 0.3,
        'phi_resonance': evolution['phi_attraction'] < 0.8,
        'diversity_emergence': evolution['diversity_final'] > 0.3,
        'learning_accumulation': evolution['learning_developed'] > 0.05,
        'health_maintenance': evolution['health_final'] > 0.3,
        'regime_exploration': evolution['regime_diversity'] >= 3
    }
    
    passed_validation = sum(validation_criteria.values())
    total_criteria = len(validation_criteria)
    
    for criterion, passed in validation_criteria.items():
        status = "✓ Consistent" if passed else "✗ Needs attention"
        print(f"  {criterion}: {status}")
    
    validation_score = passed_validation / total_criteria
    print(f"\nInternal consistency score: {validation_score:.3f}")
    
    if validation_score >= 1.0:
        print("Status: ★ Theoretical predictions validated ★")
    elif validation_score >= 0.8:
        print("Status: System dynamics consistent with framework")
    elif validation_score >= 0.6:
        print("Status: Partial validation achieved")
    else:
        print("Status: Framework requires refinement")
    
    print(f"\nFinal system state:")
    final = evolution['final_state']
    regime_amps = final['regime_amplitudes']
    
    print(f"  Regime dynamics: ", end="")
    for regime, amp in regime_amps.items():
        if amp > 0.1:
            print(f"{regime}({amp:.2f}) ", end="")
    print()
    
    print(f"  Ethical dynamics: {final['ethical_aspect']} dominant")
    print(f"  Resonance pattern: {final['harmonics_detected']} phi harmonics")
    print(f"  Learning accumulation: {final['learning_accumulated']:.3f}")
    print(f"  Prospective tension: {final['prospective_tension']:.3f}")
    print(f"  Morphic resonance: {final['morphic_resonance']:.3f}")
    print(f"  Entropic pressure: {final['entropic_pressure']:.3f}")
    print(f"  Entropy ratio: {final['entropy_ratio']:.3f}")
    print(f"  Curiosity drive: {final['curiosity_drive']:.3f}")
    print(f"  Exploration pressure: {final['exploration_pressure']:.3f}")
    print(f"  Exploration ratio: {final['exploration_ratio']:.3f}")
    print(f"  Gradient strength: {final['gradient_strength']:.3f}")
    print(f"  Explored regions: {final['explored_regions']}")
    
    if 'future_attractors' in final:
        print(f"  Future attractors:")
        for regime, strength in final['future_attractors'].items():
            print(f"    {regime}: {strength:.2f}")
    
    print("\n★ Information Processing Framework Operational ★")
    print("Six coupled dynamics: Kinetic + Thermal + Predictive Bias + Entropic + Curiosity + Exploration Gradient")
    print("Systematic exploration of seven-dimensional phase space with phase transition capabilities")