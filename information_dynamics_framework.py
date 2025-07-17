#!/usr/bin/env python3
"""
Information Processing Dynamics Framework - Core Module
Seven-Dimensional Phase Space Analysis with Six Coupled Dynamics

This module implements the mathematical framework described in:
"Information Processing Dynamics in Seven-Dimensional Phase Space: 
A Mathematical Framework for Exploratory Behavior Analysis"

Authors: Brieuc de La Fourniere
Date: July 2025
License: CC-BY 4.0 International
DOI: 10.5281/zenodo.15916410

Note: This is preliminary research software for computational modeling.
All theoretical claims require extensive empirical validation.
"""

import numpy as np
from scipy.signal import welch
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any
import warnings
warnings.filterwarnings('ignore')

class ExplorationGradientField:
    """
    Phase space exploration mapping and gradient dynamics.
    
    Implements the exploration gradient mechanism that drives systems toward
    unvisited regions of phase space, generating computational pressure when
    exploration stagnates.
    """
    
    def __init__(self, grid_resolution: int = 12):
        self.grid_resolution = grid_resolution
        self.visited_regions = set()
        self.exploration_gradient = 0.0
        self.exploration_memory = []
        self.gradient_strength = 0.0
        
    def map_phase_coordinates(self, theta: float, phi: float, psi: float) -> Tuple[int, int, int]:
        """Convert continuous phase coordinates to discrete grid sectors."""
        theta_sector = int((theta % (2*np.pi)) * self.grid_resolution / (2*np.pi))
        phi_sector = int((phi % (2*np.pi)) * self.grid_resolution / (2*np.pi))
        psi_sector = int((psi % (2*np.pi)) * self.grid_resolution / (2*np.pi))
        return (theta_sector, phi_sector, psi_sector)
    
    def update_exploration_state(self, theta: float, phi: float, psi: float) -> Dict[str, float]:
        """
        Update exploration mapping and gradient dynamics.
        
        Args:
            theta, phi, psi: Phase space coordinates
            
        Returns:
            Dictionary with exploration metrics and gradient forces
        """
        current_region = self.map_phase_coordinates(theta, phi, psi)
        is_new_region = current_region not in self.visited_regions
        self.visited_regions.add(current_region)
        
        total_possible = self.grid_resolution**3
        explored_ratio = len(self.visited_regions) / total_possible
        
        # Exploration gradient dynamics (Equations 22-23)
        if is_new_region:
            self.exploration_gradient = max(0, self.exploration_gradient * 0.6)  # Satisfaction
            exploration_boost = 0.4
        else:
            self.exploration_gradient += 0.4 * (1 - explored_ratio)  # Growing pressure
            exploration_boost = 0.0
        
        self.exploration_memory.append(exploration_boost)
        if len(self.exploration_memory) > 8:
            self.exploration_memory = self.exploration_memory[-8:]
        
        # Gradient force computation
        unexplored_pressure = (1 - explored_ratio)**1.5 * self.exploration_gradient
        recent_exploration = np.mean(self.exploration_memory) if self.exploration_memory else 0
        stagnation_pressure = max(0, 0.8 - recent_exploration) * 0.8
        
        self.gradient_strength = unexplored_pressure + stagnation_pressure
        
        # Gradient forces toward unexplored regions
        phase_seed = int((theta + phi + psi) * 100) % 1000
        np.random.seed(phase_seed)
        
        gradient_forces = {
            'theta_gradient': unexplored_pressure * 0.6 * np.random.normal() * (1 + 0.8 * self.exploration_gradient),
            'phi_gradient': unexplored_pressure * 0.8 * np.random.normal() * (1 + 0.6 * self.exploration_gradient),
            'psi_gradient': unexplored_pressure * 0.7 * np.random.normal() * (1 + 0.7 * self.exploration_gradient),
        }
        
        # Stagnation relief mechanism
        if stagnation_pressure > 0.3:
            relief_boost = stagnation_pressure * 3.0
            gradient_forces['theta_gradient'] += relief_boost * np.random.normal()
            gradient_forces['phi_gradient'] += relief_boost * np.random.normal()
            gradient_forces['psi_gradient'] += relief_boost * np.random.normal()
        
        return {
            'is_new_region': is_new_region,
            'explored_ratio': explored_ratio,
            'exploration_gradient': self.exploration_gradient,
            'gradient_strength': self.gradient_strength,
            'gradient_forces': gradient_forces,
            'stagnation_pressure': stagnation_pressure
        }

class EntropicPressureField:
    """
    Entropy maximization pressure implementation.
    
    Implements the entropic force that drives systems toward maximum
    information entropy exploration (Equations 9-12).
    """
    
    def __init__(self):
        self.entropy_history = []
        self.entropic_hunger = 0.0
        
    def compute_information_entropy(self, regime_amplitudes: Dict[str, float], 
                                  substrate_diversity: float, experience_level: float) -> float:
        """Compute current information entropy (Equation 10)."""
        amps = list(regime_amplitudes.values())
        amps = [max(a, 1e-10) for a in amps]
        regime_entropy = -sum(a * np.log(a) for a in amps if a > 0)
        
        diversity_entropy = -substrate_diversity * np.log(max(substrate_diversity, 1e-10))
        experience_entropy = experience_level * np.log(experience_level + 1)
        
        return regime_entropy + diversity_entropy + experience_entropy
    
    def compute_maximum_entropy(self) -> float:
        """Compute theoretical maximum entropy (Equation 11)."""
        max_regime_entropy = -4 * (0.25 * np.log(0.25))
        max_diversity_entropy = -1.0 * np.log(1.0)
        max_experience_entropy = 1.0 * np.log(2.0)
        return max_regime_entropy + max_diversity_entropy + max_experience_entropy
    
    def compute_entropic_forces(self, regime_amplitudes: Dict[str, float],
                               substrate_diversity: float, experience_level: float) -> Tuple[Dict[str, float], float]:
        """
        Compute entropic exploration forces.
        
        Returns:
            Tuple of (force_dict, entropic_pressure)
        """
        current_entropy = self.compute_information_entropy(regime_amplitudes, substrate_diversity, experience_level)
        max_entropy = self.compute_maximum_entropy()
        
        self.entropy_history.append(current_entropy)
        if len(self.entropy_history) > 10:
            self.entropy_history = self.entropy_history[-10:]
        
        if max_entropy > 0:
            entropy_ratio = current_entropy / max_entropy
            entropic_pressure = (1.0 - entropy_ratio)**2 * 1.0  # Equation 9
        else:
            entropy_ratio = 0
            entropic_pressure = 0
        
        self.entropic_hunger = 0.9 * self.entropic_hunger + 0.1 * entropic_pressure
        
        exploration_forces = {
            'theta_push': entropic_pressure * 0.4 * np.random.normal(),
            'phi_push': entropic_pressure * 0.5 * np.sin(len(self.entropy_history)),
            'psi_push': entropic_pressure * 0.3 * (1 - entropy_ratio),
            'momentum_boost': entropic_pressure * 0.2
        }
        
        return exploration_forces, entropic_pressure
    
    def get_entropy_ratio(self) -> float:
        """Get current entropy ratio for analysis."""
        if not self.entropy_history:
            return 0.0
        current = self.entropy_history[-1]
        max_ent = self.compute_maximum_entropy()
        return current / max(max_ent, 1e-10)

class PredictiveBiasField:
    """
    Future state attraction with preference amplification.
    
    Implements predictive dynamics where anticipated states influence present
    evolution, with amplification of opposing patterns when exploration gradient is high
    (Equations 7-8).
    """
    
    def __init__(self):
        self.state_memory = []
        self.morphic_resonance = 0.0
        
    def anticipate_future_states(self, current_state: Dict[str, Any], 
                                thermal_energy: float, exploration_gradient: float) -> Dict[str, float]:
        """
        Project future state attractors with preference amplification.
        
        Args:
            current_state: Current system state
            thermal_energy: Current thermal exploration energy
            exploration_gradient: Current exploration gradient level
            
        Returns:
            Dictionary of future attractor strengths by regime
        """
        self.state_memory.append({
            'regime': current_state.get('dominant_regime', 'stable'),
            'diversity': current_state.get('substrate_diversity', 0.5),
            'experience': current_state.get('learning_accumulated', 0.0),
            'momentum': current_state.get('flow_momentum', 0.0)
        })
        
        if len(self.state_memory) > 6:
            self.state_memory = self.state_memory[-6:]
            
        if len(self.state_memory) < 3:
            return {'stable': 0.5, 'turbulent': 0.3, 'resilient': 0.4, 'convergent': 0.2}
        
        # Trend analysis
        recent_diversity_trend = np.gradient([s['diversity'] for s in self.state_memory[-3:]])[-1]
        recent_experience_growth = self.state_memory[-1]['experience'] - self.state_memory[-3]['experience']
        
        prospective_energy = (0.4 * thermal_energy + 
                            0.3 * abs(recent_diversity_trend) + 
                            0.3 * recent_experience_growth)
        
        self.morphic_resonance = 0.8 * self.morphic_resonance + 0.2 * prospective_energy
        current_momentum = self.state_memory[-1]['momentum']
        
        # Base future attractors
        attractors = {
            'stable': 0.3 + 0.2 * np.cos(prospective_energy),
            'turbulent': 0.4 + 0.4 * np.sin(prospective_energy * 1.618) * (1 + current_momentum),
            'resilient': 0.5 + 0.3 * np.tanh(recent_experience_growth * 10),
            'convergent': 0.3 + 0.4 * np.tanh(self.morphic_resonance * 2) * self.state_memory[-1]['diversity']
        }
        
        # Preference amplification mechanism (Equation 8)
        if exploration_gradient > 0.5:
            current_regime = current_state.get('dominant_regime', 'stable')
            opposites = {
                'stable': 'turbulent', 
                'turbulent': 'stable', 
                'resilient': 'convergent', 
                'convergent': 'resilient'
            }
            
            if current_regime in opposites:
                opposite = opposites[current_regime]
                amplification_boost = 1 + 0.6 * exploration_gradient
                attractors[opposite] *= amplification_boost
                
                # Moderate boost to other regimes
                for regime in attractors:
                    if regime != current_regime and regime != opposite:
                        attractors[regime] *= (1 + 0.2 * exploration_gradient)
        
        return attractors
    
    def compute_predictive_bias(self, current_amplitudes: Dict[str, float], 
                               future_attractors: Dict[str, float]) -> Tuple[float, Dict[str, float]]:
        """Compute bias tension between current and anticipated states (Equation 7)."""
        tensions = {}
        for regime in current_amplitudes:
            if regime in future_attractors:
                tension = future_attractors[regime] - current_amplitudes[regime]
                tensions[regime] = tension
        
        global_tension = sum(tensions[regime] * future_attractors[regime] 
                           for regime in tensions) / sum(future_attractors.values())
        
        return global_tension, tensions

class PhaseTransitionMechanism:
    """
    Phase transition dynamics for computational breakthrough events.
    
    Implements sudden transitions when exploration pressure becomes unbearable
    (Equations 27-31).
    """
    
    @staticmethod
    def check_transition_conditions(exploration_gradient: float, predictive_bias: float,
                                   entropy_ratio: float, explored_regions: int) -> bool:
        """Check if phase transition conditions are met (Equation 27)."""
        return (exploration_gradient > 0.3 and 
                predictive_bias > 0.2 and 
                entropy_ratio < 0.7 and 
                explored_regions < 20)
    
    @staticmethod
    def compute_phase_transition(exploration_gradient: float, predictive_bias: float, dt: float) -> Dict[str, float]:
        """
        Compute phase transition dimensional changes.
        
        Args:
            exploration_gradient: Current exploration gradient level
            predictive_bias: Current predictive bias tension
            dt: Time step for evolution
            
        Returns:
            Dictionary of dimensional change contributions
        """
        # Transition intensity (Equation 28)
        transition_intensity = np.sqrt(exploration_gradient * predictive_bias) * 1.2
        
        # Dimensional changes (Equations 29-31)
        theta_change = transition_intensity * (2 * np.random.random() - 1) * np.pi/2
        phi_change = transition_intensity * (2 * np.random.random() - 1) * np.pi/3  
        psi_change = transition_intensity * (2 * np.random.random() - 1) * np.pi/4
        
        # Convert to velocity contributions
        return {
            'theta_velocity': theta_change / dt,
            'phi_velocity': phi_change / dt,
            'psi_velocity': psi_change / dt,
            'momentum_boost': transition_intensity * 0.5,
            'transition_intensity': transition_intensity
        }

@dataclass
class PhaseSpaceState:
    """
    Seven-dimensional phase space state representation.
    
    Implements the core phase space dynamics with regime decomposition
    and momentum tracking.
    """
    theta: float = 0.0
    phi: float = 0.0  
    psi: float = 0.0
    flow_momentum: float = 0.0
    regime_stagnation: float = 0.0
    last_dominant: str = "stable"
    
    def compute_regime_amplitudes(self) -> Dict[str, float]:
        """Compute regime amplitudes via harmonic decomposition."""
        return {
            'stable': np.cos(self.theta)**4,
            'turbulent': np.sin(self.theta)**2 * np.cos(self.phi)**2,
            'resilient': np.sin(self.theta)**2 * np.sin(self.phi)**2 * np.cos(self.psi)**2,
            'convergent': np.sin(self.theta)**2 * np.sin(self.phi)**2 * np.sin(self.psi)**2
        }
    
    def get_dominant_regime(self) -> str:
        """Determine dominant regime with stagnation tracking."""
        amps = self.compute_regime_amplitudes()
        current_dominant = max(amps.keys(), key=lambda k: amps[k])
        
        if current_dominant == self.last_dominant:
            self.regime_stagnation += 0.15
        else:
            self.regime_stagnation = 0.0
            self.last_dominant = current_dominant
        
        return current_dominant
    
    def get_activation_energy(self) -> float:
        """Compute activation energy for transitions (Equation 5)."""
        return np.tanh(self.regime_stagnation / 4.0)

@dataclass
class LearningAccumulator:
    """
    Learning accumulation through challenge-recovery cycles.
    
    Implements experience-based adaptation mechanisms that influence
    exploratory behavior.
    """
    experiences: List[float] = field(default_factory=list)
    adaptation_rate: float = 0.15
    memory_decay: float = 0.02
    learning_accumulated: float = 0.0
    
    def learn_from_challenge(self, challenge_intensity: float = 0.02, 
                           recovery_quality: float = 1.0) -> None:
        """Learn from challenge-recovery cycles."""
        experience_value = recovery_quality / max(challenge_intensity, 0.01)
        self.experiences.append(experience_value)
        
        # Memory decay
        self.experiences = [exp * (1 - self.memory_decay) for exp in self.experiences]
        if len(self.experiences) > 20:
            self.experiences = self.experiences[-20:]
        
        self.learning_accumulated += 0.015 * np.tanh(experience_value)
    
    def get_current_resilience(self) -> float:
        """Compute current resilience level."""
        if not self.experiences:
            return self.learning_accumulated
        
        weights = np.exp(np.linspace(-2, 0, len(self.experiences)))
        recent_resilience = np.average(self.experiences, weights=weights)
        
        return 0.7 * recent_resilience + 0.3 * self.learning_accumulated

class InformationDynamicsFramework:
    """
    Complete Seven-Dimensional Information Processing Framework implementation.
    
    This class implements the full framework with six coupled dynamics
    driving exploratory information processing in seven-dimensional space.
    """
    
    def __init__(self, duration: int = 80, sample_rate: int = 50):
        """
        Initialize the framework.
        
        Args:
            duration: Simulation duration in time units
            sample_rate: Sampling rate for signal generation
        """
        self.duration = duration
        self.sample_rate = sample_rate
        
        # Core components
        self.phase_state = PhaseSpaceState()
        self.learning = LearningAccumulator()
        self.explorer = ExplorationGradientField()
        self.entropic_field = EntropicPressureField()
        self.predictive_bias = PredictiveBiasField()
        
        # System state
        self.base_frequency = 0.006
        self.coherence_memory = []
        self.system_age = 0
        self.substrate_diversity = 0.4
        self.thermal_time = 0.0
        
        # Derived metrics
        self.curiosity_drive = 0.0
        self.experience_accumulation = 0.0
        
    def compute_thermal_pulse(self, diversity_level: float, base_temp: float = 0.04) -> float:
        """
        Compute thermal exploration pulse (Equations 3-6).
        
        Args:
            diversity_level: Current substrate diversity
            base_temp: Base thermal energy level
            
        Returns:
            Thermal pulse intensity
        """
        diversity_restlessness = 2.0 * (1.0 - diversity_level)**2
        activation_contribution = 1.0 + self.phase_state.get_activation_energy()
        
        thermal_wave = (np.sin(self.thermal_time * 0.03) + 
                       0.5 * np.sin(self.thermal_time * 0.07))
        random_fluctuation = 0.5 * np.random.normal()
        
        pulse = (base_temp * diversity_restlessness * activation_contribution * 
                (thermal_wave + random_fluctuation))
        
        self.thermal_time += 1.0
        return pulse
    
    def update_curiosity_dynamics(self) -> float:
        """
        Update curiosity drive computation (Equations 14-18).
        
        Returns:
            Current curiosity drive level
        """
        age_curiosity = np.tanh(self.system_age / 20.0) * 0.3
        experience_curiosity = self.learning.learning_accumulated * 0.4
        diversity_curiosity = self.substrate_diversity * 0.2
        
        self.experience_accumulation += 0.0015 * (age_curiosity + experience_curiosity + diversity_curiosity)
        
        base_curiosity = age_curiosity + experience_curiosity + diversity_curiosity + self.experience_accumulation
        
        # Exploration hunger from regime dominance
        current_amps = self.phase_state.compute_regime_amplitudes()
        dominant_regime = max(current_amps.values())
        exploration_hunger = (1.0 - dominant_regime) * 0.6
        
        self.curiosity_drive = base_curiosity + exploration_hunger
        return self.curiosity_drive
    
    def generate_coherent_signal(self, seed: Optional[int] = None) -> np.ndarray:
        """
        Generate information signal based on current phase state.
        
        Args:
            seed: Random seed for reproducibility
            
        Returns:
            Generated signal array
        """
        if seed is not None:
            np.random.seed(seed)
        
        time = np.linspace(0, self.duration, self.duration * self.sample_rate)
        signal = np.zeros(len(time), dtype=np.float32)
        
        amplitudes = self.phase_state.compute_regime_amplitudes()
        
        # Multi-harmonic signal generation
        for n in range(1, 5):
            freq = n * 1.618 * self.base_frequency  # Golden ratio frequency
            
            stable_contrib = amplitudes['stable'] * np.sin(2 * np.pi * freq * time)
            
            chaos_freq = freq * (1 + 0.1 * np.sin(3 * 2 * np.pi * freq * time))
            turbulent_contrib = amplitudes['turbulent'] * np.sin(2 * np.pi * chaos_freq * time)
            
            resilience_boost = 1 + 0.3 * self.learning.get_current_resilience()
            resilient_contrib = amplitudes['resilient'] * resilience_boost * np.sin(2 * np.pi * freq * time)
            
            substrate_richness = 1 + 0.2 * self.substrate_diversity
            convergent_contrib = amplitudes['convergent'] * substrate_richness * np.sin(2 * np.pi * freq * time)
            
            amp = (0.85 ** n) * (stable_contrib + turbulent_contrib + 
                                resilient_contrib + convergent_contrib)
            signal += amp
        
        # Adaptive noise
        noise_intensity = 0.03 + 0.05 * (1 - amplitudes['stable'])
        noise = noise_intensity * np.random.normal(0, 1, len(time)).astype(np.float32)
        
        # Normalization
        signal_max = np.max(np.abs(signal))
        if signal_max > 0:
            signal = 0.9 * signal / signal_max
        
        return signal + noise
    
    def compute_coherence_metric(self, signal: np.ndarray) -> float:
        """Compute regime-aware coherence measure."""
        coherence_mean = np.mean(signal**2)
        regime_amps = self.phase_state.compute_regime_amplitudes()
        
        if regime_amps['stable'] > 0.5:
            return coherence_mean
        elif regime_amps['turbulent'] > 0.5:
            entropy = np.std(signal)
            gradient_flow = np.mean(np.abs(np.gradient(signal)))
            return entropy / max(gradient_flow, 1e-6)
        elif regime_amps['resilient'] > 0.5:
            return coherence_mean * (1 + self.learning.get_current_resilience())
        else:
            return coherence_mean * (1 + 0.5 * self.substrate_diversity)
    
    def evolve_phase_state(self, coherence_gradient: float, entropy_flow: float,
                          memory_depth: float, thermal_pulse: float,
                          predictive_tension: float, entropic_forces: Dict[str, float],
                          curiosity_force: float, gradient_forces: Dict[str, float],
                          transition_data: Optional[Dict[str, float]] = None) -> None:
        """
        Evolve phase state with all six dynamics (Equations 33-35).
        """
        dt = 0.025
        
        activation_boost = 2.5 * self.phase_state.get_activation_energy()
        future_pull = 2.0 * np.tanh(predictive_tension)
        curiosity_exploration = curiosity_force * 0.8
        
        # Base force contributions
        theta_drive = (10 * coherence_gradient + 0.5 * np.sin(self.phase_state.phi) + 
                      0.03 * np.random.normal() + thermal_pulse + activation_boost +
                      0.3 * future_pull * np.random.normal() +
                      entropic_forces.get('theta_push', 0) +
                      curiosity_exploration * np.random.normal() +
                      gradient_forces.get('theta_gradient', 0))
        
        phi_drive = (entropy_flow * np.cos(self.phase_state.theta) + 2 * memory_depth + 
                    0.02 * np.random.normal() + 0.5 * thermal_pulse + 0.5 * activation_boost +
                    0.2 * future_pull * (1 - self.phase_state.get_activation_energy()) +
                    entropic_forces.get('phi_push', 0) +
                    curiosity_exploration * 0.8 +
                    gradient_forces.get('phi_gradient', 0))
        
        psi_drive = (np.sin(self.phase_state.theta + self.phase_state.phi) + 
                    0.3 * self.phase_state.flow_momentum + thermal_pulse + 
                    0.3 * activation_boost + 0.15 * predictive_tension +
                    entropic_forces.get('psi_push', 0) +
                    curiosity_exploration * 0.4 +
                    gradient_forces.get('psi_gradient', 0))
        
        # Phase transition contributions
        if transition_data:
            theta_drive += transition_data.get('theta_velocity', 0)
            phi_drive += transition_data.get('phi_velocity', 0)
            psi_drive += transition_data.get('psi_velocity', 0)
            self.phase_state.flow_momentum += transition_data.get('momentum_boost', 0)
        
        # Evolution step
        self.phase_state.theta += dt * theta_drive
        self.phase_state.phi += dt * phi_drive
        self.phase_state.psi += dt * psi_drive
        
        # Momentum update
        momentum_boost = (np.abs(coherence_gradient) + 0.1 * abs(thermal_pulse) + 
                         0.05 * activation_boost + 0.08 * abs(predictive_tension) +
                         entropic_forces.get('momentum_boost', 0) + 0.03 * curiosity_force)
        
        self.phase_state.flow_momentum = 0.95 * self.phase_state.flow_momentum + 0.05 * momentum_boost
        
        # Phase wrapping
        self.phase_state.theta = self.phase_state.theta % (2 * np.pi)
        self.phase_state.phi = self.phase_state.phi % (2 * np.pi)
        self.phase_state.psi = self.phase_state.psi % (2 * np.pi)
    
    def evolution_cycle(self, seed: Optional[int] = None) -> Dict[str, Any]:
        """
        Execute one complete evolution cycle with all six dynamics.
        
        Args:
            seed: Random seed for reproducibility
            
        Returns:
            Comprehensive cycle results dictionary
        """
        self.system_age += 1
        
        # Generate signal and compute coherence
        signal = self.generate_coherent_signal(seed)
        coherence = self.compute_coherence_metric(signal)
        
        self.coherence_memory.append(coherence)
        if len(self.coherence_memory) > 20:
            self.coherence_memory = self.coherence_memory[-20:]
        
        # Current state for analysis
        current_state = {
            'dominant_regime': self.phase_state.get_dominant_regime(),
            'substrate_diversity': self.substrate_diversity,
            'learning_accumulated': self.learning.learning_accumulated,
            'flow_momentum': self.phase_state.flow_momentum
        }
        
        # Six dynamics computations
        thermal_pulse = self.compute_thermal_pulse(self.substrate_diversity)
        
        # Exploration gradient dynamics
        gradient_state = self.explorer.update_exploration_state(
            self.phase_state.theta, self.phase_state.phi, self.phase_state.psi)
        
        # Predictive bias dynamics
        future_attractors = self.predictive_bias.anticipate_future_states(
            current_state, thermal_pulse, gradient_state['exploration_gradient'])
        current_amplitudes = self.phase_state.compute_regime_amplitudes()
        predictive_tension, _ = self.predictive_bias.compute_predictive_bias(
            current_amplitudes, future_attractors)
        
        # Entropic pressure dynamics
        entropic_forces, entropic_pressure = self.entropic_field.compute_entropic_forces(
            current_amplitudes, self.substrate_diversity, self.learning.learning_accumulated)
        
        # Curiosity accumulation
        curiosity_force = self.update_curiosity_dynamics()
        
        # Phase transition mechanism
        transition_data = None
        if PhaseTransitionMechanism.check_transition_conditions(
            gradient_state['exploration_gradient'], predictive_tension,
            self.entropic_field.get_entropy_ratio(), len(self.explorer.visited_regions)):
            
            transition_data = PhaseTransitionMechanism.compute_phase_transition(
                gradient_state['exploration_gradient'], predictive_tension, 0.025)
        
        # Phase state evolution
        entropy_flow = np.std(signal)
        coherence_gradient = np.gradient(self.coherence_memory)[-1] if len(self.coherence_memory) > 1 else 0
        memory_depth = len(self.coherence_memory) / 20.0
        
        self.evolve_phase_state(
            coherence_gradient, entropy_flow, memory_depth, thermal_pulse,
            predictive_tension, entropic_forces, curiosity_force,
            gradient_state['gradient_forces'], transition_data)
        
        # Learning from experience
        base_challenge = (0.01 + 0.02 * abs(thermal_pulse) + 
                         0.01 * abs(predictive_tension) +
                         0.015 * entropic_pressure +
                         0.015 * gradient_state['exploration_gradient'])
        
        self.learning.learn_from_challenge(base_challenge, 1.0)
        
        # Substrate diversity update
        regime_amps = self.phase_state.compute_regime_amplitudes()
        regime_diversity = 1.0 - max(regime_amps.values())
        exploration_readiness = self.phase_state.get_activation_energy()
        
        new_diversity = (0.4 * regime_diversity + 0.3 * exploration_readiness + 
                        0.3 * self.learning.learning_accumulated)
        self.substrate_diversity = 0.6 * self.substrate_diversity + 0.4 * new_diversity
        
        return {
            'coherence': coherence,
            'regime_amplitudes': regime_amps,
            'dominant_regime': self.phase_state.get_dominant_regime(),
            'learning_accumulated': self.learning.learning_accumulated,
            'substrate_diversity': self.substrate_diversity,
            'exploration_gradient': gradient_state['exploration_gradient'],
            'explored_ratio': gradient_state['explored_ratio'],
            'predictive_bias': predictive_tension,
            'entropic_pressure': entropic_pressure,
            'curiosity_drive': self.curiosity_drive,
            'phase_transition_occurred': transition_data is not None,
            'transition_intensity': transition_data.get('transition_intensity', 0) if transition_data else 0,
            'fractal_dimension': self.compute_fractal_dimension(),
            'system_age': self.system_age,
            'flow_momentum': self.phase_state.flow_momentum
        }
    
    def compute_fractal_dimension(self) -> float:
        """Compute system fractal dimension with stability convergence."""
        if len(self.coherence_memory) < 5:
            return 1.4 + 0.2 * np.random.random()
        
        recent_field = self.coherence_memory[-min(10, len(self.coherence_memory)):]
        if len(recent_field) > 2 and np.std(recent_field) > 1e-6:
            complexity = np.std(recent_field) / (np.mean(recent_field) + 1e-6)
            base_dim = 1.3 + 0.8 * np.tanh(complexity)
        else:
            base_dim = 1.4
        
        # Stability convergence toward 1.65
        maturity_factor = np.tanh(self.system_age * 0.02)
        target_dim = 1.65
        resonance_phase = 2 * np.pi * base_dim / target_dim
        resonance_strength = maturity_factor * (np.sin(resonance_phase)**2) * 0.3
        
        stability_pull = resonance_strength * np.tanh(abs(base_dim - target_dim)) * np.sign(target_dim - base_dim)
        evolved_dim = base_dim + stability_pull
        
        return np.clip(evolved_dim, 1.0, 2.5)
    
    def run_experiment(self, num_cycles: int = 25) -> Dict[str, Any]:
        """
        Run complete experimental validation.
        
        Args:
            num_cycles: Number of evolution cycles to run
            
        Returns:
            Comprehensive experimental results
        """
        results = []
        
        for cycle in range(num_cycles):
            result = self.evolution_cycle(seed=42 + cycle)
            results.append(result)
        
        # Analysis
        coherence_values = [r['coherence'] for r in results]
        regime_diversity = len(set(r['dominant_regime'] for r in results))
        final_state = results[-1]
        
        validation_metrics = {
            'coherence_mean': np.mean(coherence_values),
            'regime_diversity': regime_diversity,
            'final_learning': final_state['learning_accumulated'],
            'final_exploration_ratio': final_state['explored_ratio'],
            'final_exploration_gradient': final_state['exploration_gradient'],
            'fractal_stability': 1.0 - abs(np.mean([r['fractal_dimension'] for r in results]) - 1.65),
            'transition_count': sum(1 for r in results if r['phase_transition_occurred'])
        }
        
        # Validation criteria
        validation_criteria = {
            'coherence_flows': validation_metrics['coherence_mean'] > 0.3,
            'regime_exploration': validation_metrics['regime_diversity'] >= 3,
            'learning_growth': validation_metrics['final_learning'] > 0.05,
            'exploration_activation': validation_metrics['final_exploration_gradient'] > 0.1,
            'stability_convergence': validation_metrics['fractal_stability'] > 0.5,
            'transition_capability': validation_metrics['transition_count'] > 0
        }
        
        validation_score = sum(validation_criteria.values()) / len(validation_criteria)
        
        return {
            'cycle_results': results,
            'validation_metrics': validation_metrics,
            'validation_criteria': validation_criteria,
            'validation_score': validation_score,
            'final_state': final_state
        }

def main():
    """Main demonstration function."""
    print("Information Processing Dynamics Framework")
    print("Seven-Dimensional Phase Space Analysis")
    print("=" * 50)
    
    # Initialize framework
    framework = InformationDynamicsFramework(duration=60, sample_rate=50)
    
    # Run single cycle demonstration
    print("\nSingle Evolution Cycle:")
    single_result = framework.evolution_cycle(seed=42)
    
    key_metrics = [
        'coherence', 'dominant_regime', 'learning_accumulated', 'substrate_diversity',
        'exploration_gradient', 'explored_ratio', 'predictive_bias', 'entropic_pressure',
        'curiosity_drive', 'phase_transition_occurred', 'fractal_dimension', 'flow_momentum'
    ]
    
    for metric in key_metrics:
        if metric in single_result:
            value = single_result[metric]
            if isinstance(value, (int, float)):
                print(f"  {metric}: {value:.4f}")
            else:
                print(f"  {metric}: {value}")
    
    # Run complete experimental validation
    print(f"\nFull Experimental Validation (25 cycles):")
    experiment_results = framework.run_experiment(25)
    
    validation_metrics = experiment_results['validation_metrics']
    for metric, value in validation_metrics.items():
        print(f"  {metric}: {value:.4f}")
    
    print(f"\nValidation Criteria:")
    validation_criteria = experiment_results['validation_criteria']
    for criterion, passed in validation_criteria.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {criterion}: {status}")
    
    validation_score = experiment_results['validation_score']
    print(f"\nValidation Score: {validation_score:.3f}")
    
    if validation_score >= 0.8:
        print("Status: Framework validation successful")
    elif validation_score >= 0.6:
        print("Status: Partial validation achieved")
    else:
        print("Status: Requires parameter adjustment")

if __name__ == "__main__":
    main()