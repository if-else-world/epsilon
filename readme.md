# Information Processing Dynamics Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15916410.svg)](https://doi.org/10.5281/zenodo.15916410)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Research Status](https://img.shields.io/badge/status-preprint-orange.svg)](https://zenodo.org/record/15916410)

A computational framework for analyzing exploratory behavior in seven-dimensional phase space using six coupled differential equations.

## Overview

This repository implements the mathematical framework described in "Information Processing Dynamics in Seven-Dimensional Phase Space: A Mathematical Framework for Exploratory Behavior Analysis" (de La Fourniere, 2025).

The framework models information processing through six coupled dynamics: kinetic flow, thermal noise, predictive bias, entropy maximization, curiosity accumulation, and exploration gradient.

## Installation

```bash
pip install numpy scipy matplotlib seaborn pandas
git clone https://github.com/if-else-world/epsilon.git
cd epsilon
```

## Quick Start

```python
from information_dynamics_framework import InformationDynamicsFramework

# Initialize framework
framework = InformationDynamicsFramework(duration=60, sample_rate=50)

# Run single cycle
result = framework.evolution_cycle(seed=42)
print(f"Coherence: {result['coherence']:.3f}")

# Run full experiment
experiment = framework.run_experiment(num_cycles=25)
print(f"Validation Score: {experiment['validation_score']:.3f}")
```

## Generate Figures

```python
from visualization_suite import InformationDynamicsVisualizationSuite

viz = InformationDynamicsVisualizationSuite()
viz.generate_all_figures()  # Creates figures/ directory
```

## Files

- `information_dynamics_framework.py` - Core framework implementation
- `visualization_suite.py` - Academic figure generation
- `validation_experiments.py` - Computational validation scripts
- `figures/` - Generated publication-ready figures

## Citation

```bibtex
@misc{lafourniere2025information,
  title={Information Processing Dynamics in Seven-Dimensional Phase Space}, 
  author={de La Fourniere, Brieuc},
  year={2025},
  publisher={Zenodo},
  doi={10.5281/zenodo.15916410}
}
```

## License

CC-BY 4.0 International

## Note

Disclaimer: This research explores speculative theoretical frameworks and should not be considered established science. All claims require extensive peer review and experimental validation.
This repository is part of a broader exploration of information geometry, coherence, and emergence.

## Warning

⚠ Experimental build: Runs on 4D spacetime (emulated) | Native Ψ7 support coming in v2.0

