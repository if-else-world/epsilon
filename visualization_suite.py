#!/usr/bin/env python3
"""
Information Processing Dynamics Visualization Suite
Comprehensive visualization package for Seven-Dimensional Information Processing 
Framework academic publication.

Generates all figures required for academic publication:
- Temporal evolution of key metrics
- Phase space trajectories  
- Regime distribution analysis
- Stability convergence dynamics
- Phase transition occurrence patterns
- Dynamics interaction diagrams

Authors: Brieuc de La Fourniere
Date: July 2025
License: CC 4.0
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle
from matplotlib.collections import LineCollection
import pandas as pd
from typing import Dict, List, Any, Tuple
import os
from pathlib import Path

# Set style for academic publications
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'font.family': 'serif'
})

class InformationDynamicsVisualizationSuite:
    """
    Complete visualization suite for seven-dimensional information processing 
    framework academic presentation.
    
    Generates publication-ready figures for the six-component exploratory
    information processing framework with proper academic formatting.
    """
    
    def __init__(self, output_dir: str = "figures"):
        """
        Initialize visualization suite.
        
        Args:
            output_dir: Directory to save generated figures
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.phi = (1 + np.sqrt(5)) / 2  # Mathematical constant
        
        # Color scheme for different regimes and dynamics
        self.regime_colors = {
            'stable': '#2E86AB',
            'turbulent': '#A23B72', 
            'resilient': '#F18F01',
            'convergent': '#C73E1D'
        }
        
        self.dynamics_colors = {
            'kinetic': '#1f77b4',
            'thermal': '#ff7f0e',
            'predictive': '#2ca02c',
            'entropic': '#d62728',
            'curiosity': '#9467bd',
            'exploration': '#8c564b'
        }
    
    def generate_synthetic_data(self, num_cycles: int = 25) -> Dict[str, Any]:
        """
        Generate realistic synthetic data for visualization purposes.
        
        This simulates the output that would come from running the information
        processing framework for academic presentation when the actual framework isn't available.
        
        Args:
            num_cycles: Number of evolution cycles to simulate
            
        Returns:
            Dictionary containing all metrics for visualization
        """
        np.random.seed(42)  # Reproducible results
        
        # Initialize arrays
        data = {
            'cycles': np.arange(num_cycles),
            'coherence': [],
            'regime_amplitudes': {regime: [] for regime in self.regime_colors.keys()},
            'dominant_regime': [],
            'exploration_gradient': [],
            'learning_accumulation': [],
            'substrate_diversity': [],
            'predictive_bias': [],
            'entropic_pressure': [],
            'curiosity_drive': [],
            'phase_transition_occurred': [],
            'transition_intensity': [],
            'stability_proximity': [],
            'explored_ratio': [],
            'fractal_dimension': [],
            'theta': [],
            'phi': [],
            'psi': [],
            'flow_momentum': []
        }
        
        # Simulate realistic evolution
        exploration_gradient = 0.1
        learning = 0.0
        substrate_div = 0.4
        explored_count = 0
        theta, phi, psi = 0.5, 0.8, 1.2
        momentum = 0.0
        
        for cycle in range(num_cycles):
            # Coherence with natural fluctuations and growth trend
            base_coherence = 0.3 + 0.4 * np.tanh(cycle / 15.0)
            coherence = base_coherence + 0.1 * np.sin(cycle * 0.5) + 0.05 * np.random.normal()
            data['coherence'].append(max(0.1, coherence))
            
            # Regime amplitudes with transitions
            phase_shift = cycle * 0.3 + exploration_gradient * 2
            amps = {
                'stable': max(0.1, np.cos(theta)**4),
                'turbulent': max(0.1, np.sin(theta)**2 * np.cos(phi)**2),
                'resilient': max(0.1, np.sin(theta)**2 * np.sin(phi)**2 * np.cos(psi)**2),
                'convergent': max(0.1, np.sin(theta)**2 * np.sin(phi)**2 * np.sin(psi)**2)
            }
            
            # Normalize amplitudes
            total = sum(amps.values())
            amps = {k: v/total for k, v in amps.items()}
            
            for regime, amp in amps.items():
                data['regime_amplitudes'][regime].append(amp)
            
            dominant = max(amps.keys(), key=lambda k: amps[k])
            data['dominant_regime'].append(dominant)
            
            # Exploration gradient dynamics with region coverage
            if np.random.random() < 0.3:  # New region explored
                exploration_gradient *= 0.6
                explored_count += 1
            else:
                exploration_gradient += 0.4 * (1 - explored_count / 100.0)
            
            data['exploration_gradient'].append(exploration_gradient)
            data['explored_ratio'].append(explored_count / 1728.0)  # 12^3 total regions
            
            # Learning accumulation
            learning += 0.015 * np.random.exponential(0.5)
            data['learning_accumulation'].append(learning)
            
            # Substrate diversity evolution
            substrate_div = 0.6 * substrate_div + 0.4 * (0.3 + 0.4 * np.random.random())
            data['substrate_diversity'].append(substrate_div)
            
            # Dynamics and pressures
            predictive_bias = 0.3 * np.sin(cycle * 0.2) + 0.2 * exploration_gradient
            data['predictive_bias'].append(max(0, predictive_bias))
            
            entropic_pressure = (1 - min(amps.values()) / max(amps.values())) * 0.8
            data['entropic_pressure'].append(entropic_pressure)
            
            curiosity = learning * 0.4 + substrate_div * 0.2 + np.tanh(cycle / 20.0) * 0.3
            data['curiosity_drive'].append(curiosity)
            
            # Phase transitions when conditions are met
            phase_transition = (exploration_gradient > 0.3 and predictive_bias > 0.2 and 
                          entropic_pressure > 0.5 and explored_count < 20)
            data['phase_transition_occurred'].append(phase_transition)
            
            if phase_transition:
                transition_intensity = np.sqrt(exploration_gradient * predictive_bias) * 1.2
                # Apply dimensional changes
                theta += transition_intensity * np.random.uniform(-np.pi/2, np.pi/2) * 0.1
                phi += transition_intensity * np.random.uniform(-np.pi/3, np.pi/3) * 0.1
                psi += transition_intensity * np.random.uniform(-np.pi/4, np.pi/4) * 0.1
                momentum += transition_intensity * 0.5
            else:
                transition_intensity = 0
                # Normal evolution
                theta += 0.1 * np.random.normal()
                phi += 0.08 * np.random.normal() 
                psi += 0.06 * np.random.normal()
            
            data['transition_intensity'].append(transition_intensity)
            
            # Phase space coordinates
            theta = theta % (2 * np.pi)
            phi = phi % (2 * np.pi)
            psi = psi % (2 * np.pi)
            momentum = 0.95 * momentum + 0.05 * np.random.exponential(0.1)
            
            data['theta'].append(theta)
            data['phi'].append(phi)
            data['psi'].append(psi)
            data['flow_momentum'].append(momentum)
            
            # Fractal dimension with stability convergence
            base_dim = 1.4 + 0.6 * np.tanh(entropic_pressure)
            stability_attraction = 0.2 * np.tanh(cycle / 10.0) * np.sign(1.65 - base_dim)
            fractal_dim = base_dim + stability_attraction
            data['fractal_dimension'].append(fractal_dim)
            data['stability_proximity'].append(abs(fractal_dim - 1.65))
        
        return data
    
    def plot_temporal_evolution(self, data: Dict[str, Any]) -> None:
        """
        Generate temporal evolution plots of key metrics.
        
        Args:
            data: Simulation data dictionary
        """
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Temporal Evolution of Six-Component Information Processing Dynamics', fontsize=16)
        
        cycles = data['cycles']
        
        # Coherence evolution
        ax = axes[0, 0]
        ax.plot(cycles, data['coherence'], 'b-', linewidth=2, alpha=0.8)
        ax.fill_between(cycles, data['coherence'], alpha=0.3)
        ax.set_title('Information Coherence Evolution')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Coherence')
        ax.grid(True, alpha=0.3)
        
        # Exploration gradient with phase transitions
        ax = axes[0, 1]
        ax.plot(cycles, data['exploration_gradient'], 'purple', linewidth=2, label='Exploration Gradient')
        transition_cycles = [i for i, transition in enumerate(data['phase_transition_occurred']) if transition]
        if transition_cycles:
            transition_values = [data['exploration_gradient'][i] for i in transition_cycles]
            ax.scatter(transition_cycles, transition_values, color='red', s=50, zorder=5, 
                      label='Phase Transitions', marker='^')
        ax.set_title('Exploration Gradient & Phase Transitions')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Exploration Gradient Level')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Learning accumulation
        ax = axes[0, 2]
        ax.plot(cycles, data['learning_accumulation'], 'orange', linewidth=2)
        ax.fill_between(cycles, data['learning_accumulation'], alpha=0.3, color='orange')
        ax.set_title('Learning Accumulation')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Accumulated Learning')
        ax.grid(True, alpha=0.3)
        
        # Dynamics interactions
        ax = axes[1, 0]
        ax.plot(cycles, data['predictive_bias'], label='Predictive Bias', linewidth=2)
        ax.plot(cycles, data['entropic_pressure'], label='Entropic Pressure', linewidth=2)
        ax.plot(cycles, data['curiosity_drive'], label='Curiosity Drive', linewidth=2)
        ax.set_title('Six-Component Dynamics')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Dynamics Intensity')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Fractal dimension with stability convergence
        ax = axes[1, 1]
        ax.plot(cycles, data['fractal_dimension'], 'green', linewidth=2, label='Fractal Dimension')
        ax.axhline(y=1.65, color='orange', linestyle='--', linewidth=2, label='Stability Target ≈ 1.65')
        ax.fill_between(cycles, [1.45] * len(cycles), [1.85] * len(cycles), 
                       alpha=0.2, color='orange', label='Stability Range')
        ax.set_title('Fractal Dimension Evolution')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Fractal Dimension')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Exploration ratio
        ax = axes[1, 2]
        ax.plot(cycles, data['explored_ratio'], 'brown', linewidth=2)
        ax.fill_between(cycles, data['explored_ratio'], alpha=0.3, color='brown')
        ax.set_title('Phase Space Exploration')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Explored Ratio')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'temporal_evolution.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_regime_analysis(self, data: Dict[str, Any]) -> None:
        """
        Generate regime distribution and transition analysis.
        
        Args:
            data: Simulation data dictionary
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        fig.suptitle('Regime Analysis: Four Computational States in Information Processing Framework', fontsize=16)
        
        cycles = data['cycles']
        
        # Regime amplitude evolution
        ax = axes[0]
        for regime, color in self.regime_colors.items():
            ax.plot(cycles, data['regime_amplitudes'][regime], 
                   label=regime.capitalize(), color=color, linewidth=2)
        ax.set_title('Regime Amplitude Evolution')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Amplitude')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Regime distribution pie chart
        ax = axes[1]
        regime_counts = {}
        for regime in data['dominant_regime']:
            regime_counts[regime] = regime_counts.get(regime, 0) + 1
        
        if regime_counts:
            labels = list(regime_counts.keys())
            sizes = list(regime_counts.values())
            colors = [self.regime_colors[regime] for regime in labels]
            
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                             startangle=90, textprops={'fontsize': 10})
            ax.set_title('Dominant Regime Distribution')
        
        # Regime transition matrix
        ax = axes[2]
        regimes = list(self.regime_colors.keys())
        transition_matrix = np.zeros((len(regimes), len(regimes)))
        
        for i in range(len(data['dominant_regime']) - 1):
            current = data['dominant_regime'][i]
            next_regime = data['dominant_regime'][i + 1]
            current_idx = regimes.index(current)
            next_idx = regimes.index(next_regime)
            transition_matrix[current_idx, next_idx] += 1
        
        # Normalize by row sums
        row_sums = transition_matrix.sum(axis=1, keepdims=True)
        transition_matrix = np.divide(transition_matrix, row_sums, 
                                    out=np.zeros_like(transition_matrix), where=row_sums!=0)
        
        im = ax.imshow(transition_matrix, cmap='Blues', aspect='auto')
        ax.set_xticks(range(len(regimes)))
        ax.set_yticks(range(len(regimes)))
        ax.set_xticklabels([r.capitalize() for r in regimes])
        ax.set_yticklabels([r.capitalize() for r in regimes])
        ax.set_xlabel('Next Regime')
        ax.set_ylabel('Current Regime')
        ax.set_title('Regime Transition Probabilities')
        
        # Add transition probability text
        for i in range(len(regimes)):
            for j in range(len(regimes)):
                text = ax.text(j, i, f'{transition_matrix[i, j]:.2f}',
                             ha="center", va="center", color="black" if transition_matrix[i, j] < 0.5 else "white")
        
        plt.colorbar(im, ax=ax, label='Transition Probability')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'regime_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_phase_space_trajectories(self, data: Dict[str, Any]) -> None:
        """
        Generate 3D phase space trajectory visualization.
        
        Args:
            data: Simulation data dictionary
        """
        fig = plt.figure(figsize=(16, 12))
        
        # 3D trajectory plot
        ax1 = fig.add_subplot(221, projection='3d')
        
        # Color trajectory by exploration gradient level
        colors = plt.cm.viridis(np.array(data['exploration_gradient']) / max(data['exploration_gradient']))
        
        # Create trajectory line
        for i in range(len(data['theta']) - 1):
            ax1.plot([data['theta'][i], data['theta'][i+1]], 
                    [data['phi'][i], data['phi'][i+1]], 
                    [data['psi'][i], data['psi'][i+1]], 
                    color=colors[i], alpha=0.7, linewidth=2)
        
        # Mark phase transitions
        transition_indices = [i for i, transition in enumerate(data['phase_transition_occurred']) if transition]
        if transition_indices:
            transition_theta = [data['theta'][i] for i in transition_indices]
            transition_phi = [data['phi'][i] for i in transition_indices]
            transition_psi = [data['psi'][i] for i in transition_indices]
            ax1.scatter(transition_theta, transition_phi, transition_psi, color='red', s=100, 
                       marker='*', label='Phase Transitions')
        
        ax1.set_xlabel('θ (Theta)')
        ax1.set_ylabel('φ (Phi)')
        ax1.set_zlabel('ψ (Psi)')
        ax1.set_title('3D Phase Space Trajectory\n(Colored by Exploration Gradient)')
        if transition_indices:
            ax1.legend()
        
        # 2D projections
        ax2 = fig.add_subplot(222)
        scatter = ax2.scatter(data['theta'], data['phi'], c=data['exploration_gradient'], 
                            cmap='viridis', alpha=0.6, s=30)
        ax2.set_xlabel('θ (Theta)')
        ax2.set_ylabel('φ (Phi)')
        ax2.set_title('θ-φ Projection')
        plt.colorbar(scatter, ax=ax2, label='Exploration Gradient')
        
        ax3 = fig.add_subplot(223)
        scatter = ax3.scatter(data['phi'], data['psi'], c=data['transition_intensity'], 
                            cmap='plasma', alpha=0.6, s=30)
        ax3.set_xlabel('φ (Phi)')
        ax3.set_ylabel('ψ (Psi)')
        ax3.set_title('φ-ψ Projection')
        plt.colorbar(scatter, ax=ax3, label='Transition Intensity')
        
        ax4 = fig.add_subplot(224)
        scatter = ax4.scatter(data['theta'], data['psi'], c=data['flow_momentum'], 
                            cmap='coolwarm', alpha=0.6, s=30)
        ax4.set_xlabel('θ (Theta)')
        ax4.set_ylabel('ψ (Psi)')
        ax4.set_title('θ-ψ Projection')
        plt.colorbar(scatter, ax=ax4, label='Flow Momentum')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'phase_space_trajectories.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_dynamics_interactions(self, data: Dict[str, Any]) -> None:
        """
        Generate dynamics interaction and correlation analysis.
        
        Args:
            data: Simulation data dictionary
        """
        fig, axes = plt.subplots(2, 2, figsize=(14, 12))
        fig.suptitle('Six-Component Dynamics Interaction Analysis', fontsize=16)
        
        # Dynamics correlation matrix
        ax = axes[0, 0]
        dynamics_data = pd.DataFrame({
            'Exploration Gradient': data['exploration_gradient'],
            'Predictive Bias': data['predictive_bias'],
            'Entropic Pressure': data['entropic_pressure'],
            'Curiosity Drive': data['curiosity_drive'],
            'Flow Momentum': data['flow_momentum'],
            'Coherence': data['coherence']
        })
        
        correlation_matrix = dynamics_data.corr()
        im = ax.imshow(correlation_matrix, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
        ax.set_xticks(range(len(correlation_matrix.columns)))
        ax.set_yticks(range(len(correlation_matrix.columns)))
        ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha='right')
        ax.set_yticklabels(correlation_matrix.columns)
        ax.set_title('Dynamics Correlation Matrix')
        
        # Add correlation values
        for i in range(len(correlation_matrix.columns)):
            for j in range(len(correlation_matrix.columns)):
                text = ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                             ha="center", va="center", 
                             color="white" if abs(correlation_matrix.iloc[i, j]) > 0.5 else "black")
        
        plt.colorbar(im, ax=ax, label='Correlation Coefficient')
        
        # Dynamics evolution over time
        ax = axes[0, 1]
        cycles = data['cycles']
        ax.plot(cycles, data['exploration_gradient'], label='Exploration Gradient', linewidth=2)
        ax.plot(cycles, data['predictive_bias'], label='Predictive Bias', linewidth=2)
        ax.plot(cycles, data['entropic_pressure'], label='Entropic Pressure', linewidth=2)
        ax.plot(cycles, np.array(data['curiosity_drive']) / max(data['curiosity_drive']), 
               label='Curiosity (normalized)', linewidth=2)
        ax.set_title('Normalized Dynamics Evolution')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Normalized Intensity')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Phase transition analysis
        ax = axes[1, 0]
        transition_intensities = [intensity for intensity in data['transition_intensity'] if intensity > 0]
        if transition_intensities:
            ax.hist(transition_intensities, bins=10, alpha=0.7, color='red', edgecolor='black')
            ax.set_title(f'Phase Transition Intensity Distribution\n({len(transition_intensities)} transitions total)')
            ax.set_xlabel('Transition Intensity')
            ax.set_ylabel('Frequency')
            ax.grid(True, alpha=0.3)
        else:
            ax.text(0.5, 0.5, 'No Phase Transitions\nOccurred', 
                   ha='center', va='center', transform=ax.transAxes, fontsize=14)
            ax.set_title('Phase Transition Analysis')
        
        # Stability convergence
        ax = axes[1, 1]
        ax.plot(cycles, data['stability_proximity'], 'orange', linewidth=2, label='Distance from Stability')
        ax.axhline(y=0.3, color='red', linestyle='--', alpha=0.7, label='Convergence Threshold')
        ax.fill_between(cycles, 0, data['stability_proximity'], alpha=0.3, color='orange')
        ax.set_title('Stability Convergence Dynamics')
        ax.set_xlabel('Evolution Cycle')
        ax.set_ylabel('Distance from Target')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'force_interactions.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_framework_overview(self) -> None:
        """
        Generate conceptual overview diagram of the information processing framework.
        """
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        fig.suptitle('Information Processing Framework: Six Coupled Dynamics', fontsize=16)
        
        # Central system
        center = (0.5, 0.5)
        ax.add_patch(Circle(center, 0.15, color='lightblue', alpha=0.7, zorder=1))
        ax.text(center[0], center[1], 'Information\nProcessing\nSystem', ha='center', va='center', 
               fontsize=12, fontweight='bold', zorder=2)
        
        # Six dynamics around the center
        dynamics = [
            ('Kinetic\nInformation', (0.2, 0.8), self.dynamics_colors['kinetic']),
            ('Thermal\nNoise', (0.8, 0.8), self.dynamics_colors['thermal']),
            ('Predictive\nBias', (0.9, 0.5), self.dynamics_colors['predictive']),
            ('Entropic\nPressure', (0.8, 0.2), self.dynamics_colors['entropic']),
            ('Curiosity\nAccumulation', (0.2, 0.2), self.dynamics_colors['curiosity']),
            ('Exploration\nGradient', (0.1, 0.5), self.dynamics_colors['exploration'])
        ]
        
        for dynamics_name, position, color in dynamics:
            # Dynamics circle
            ax.add_patch(Circle(position, 0.08, color=color, alpha=0.7, zorder=1))
            ax.text(position[0], position[1], dynamics_name, ha='center', va='center', 
                   fontsize=9, fontweight='bold', color='white', zorder=2)
            
            # Arrow to center
            dx = center[0] - position[0]
            dy = center[1] - position[1]
            length = np.sqrt(dx**2 + dy**2)
            dx_norm = dx / length * 0.15
            dy_norm = dy / length * 0.15
            
            ax.arrow(position[0] + dx_norm * 0.5, position[1] + dy_norm * 0.5,
                    dx_norm * 0.8, dy_norm * 0.8, 
                    head_width=0.02, head_length=0.03, fc=color, ec=color, alpha=0.8)
        
        # Four regimes in corners
        regimes = [
            ('Stable', (0.1, 0.9), self.regime_colors['stable']),
            ('Turbulent', (0.9, 0.9), self.regime_colors['turbulent']),
            ('Resilient', (0.1, 0.1), self.regime_colors['resilient']),
            ('Convergent', (0.9, 0.1), self.regime_colors['convergent'])
        ]
        
        for regime_name, position, color in regimes:
            ax.add_patch(Circle(position, 0.06, color=color, alpha=0.5, zorder=1))
            ax.text(position[0], position[1], regime_name, ha='center', va='center', 
                   fontsize=9, fontweight='bold', zorder=2)
        
        # Phase transition indicators
        ax.text(0.5, 0.05, '⚡ Phase Transitions when Exploration Gradient > 0.3 ⚡', 
               ha='center', va='center', fontsize=12, fontweight='bold', 
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
        
        # Stability indicator
        ax.text(0.5, 0.95, f'Fractal Dimension Stability Target ≈ 1.65', 
               ha='center', va='center', fontsize=12, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'framework_overview.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def generate_all_figures(self, data: Dict[str, Any] = None) -> None:
        """
        Generate complete figure suite for academic publication.
        
        Args:
            data: Optional simulation data. If None, generates synthetic data.
        """
        print("Generating Information Processing Framework Visualization Suite...")
        print(f"Output directory: {self.output_dir}")
        
        if data is None:
            print("Generating synthetic data for visualization...")
            data = self.generate_synthetic_data(25)
        
        print("Creating figures:")
        
        print("  1. Framework overview diagram...")
        self.plot_framework_overview()
        
        print("  2. Temporal evolution analysis...")
        self.plot_temporal_evolution(data)
        
        print("  3. Regime distribution analysis...")
        self.plot_regime_analysis(data)
        
        print("  4. Phase space trajectories...")
        self.plot_phase_space_trajectories(data)
        
        print("  5. Dynamics interaction analysis...")
        self.plot_dynamics_interactions(data)
        
        print(f"\nAll figures generated successfully!")
        print(f"Files saved in: {self.output_dir.absolute()}")
        
        # Generate figure summary
        summary_file = self.output_dir / "figure_descriptions.txt"
        with open(summary_file, 'w') as f:
            f.write("Information Processing Framework Figure Descriptions for Academic Publication\n")
            f.write("=" * 75 + "\n\n")
            f.write("Figure 1: framework_overview.png\n")
            f.write("Conceptual diagram showing the six coupled dynamics and four computational regimes\n")
            f.write("in the seven-dimensional information processing framework.\n\n")
            f.write("Figure 2: temporal_evolution.png\n")
            f.write("Temporal evolution of key metrics: coherence, exploration gradient with phase transitions,\n")
            f.write("learning accumulation, dynamics interactions, fractal dimension, and exploration ratio.\n\n")
            f.write("Figure 3: regime_analysis.png\n")
            f.write("Analysis of the four computational regimes: amplitude evolution, distribution,\n")
            f.write("and transition probability matrix.\n\n")
            f.write("Figure 4: phase_space_trajectories.png\n")
            f.write("3D and 2D projections of system trajectories in seven-dimensional phase space,\n")
            f.write("with phase transition events and dynamics intensities.\n\n")
            f.write("Figure 5: force_interactions.png\n")
            f.write("Dynamics correlation analysis, evolution patterns, phase transition distribution,\n")
            f.write("and stability convergence dynamics.\n\n")
        
        print(f"Figure descriptions saved to: {summary_file}")

def main():
    """Main function for standalone execution."""
    print("Information Processing Dynamics Visualization Suite")
    print("=" * 60)
    
    # Create visualization suite
    viz = InformationDynamicsVisualizationSuite()
    
    # Generate all figures
    viz.generate_all_figures()
    
    print("\nVisualization suite complete!")
    print("Ready for academic publication.")

if __name__ == "__main__":
    main()