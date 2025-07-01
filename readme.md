# Mathematical Extension of Spacetime to Five Dimensions

## Geometric Framework and Empirical Consequences

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15741958.svg)](https://doi.org/10.5281/zenodo.15741958)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Author:** Brieuc de La Fournière  
**Email:** ael@ifelse.world  
**ORCID:** [0009-0000-0641-9740](https://orcid.org/0009-0000-0641-9740)

## Abstract

This repository contains the computational implementation and numerical datasets supporting the theoretical framework presented in "Mathematical Extension of Spacetime to Five Dimensions: Geometric Framework and Empirical Consequences" ([Zenodo record](https://zenodo.org/records/15741958)).

The work presents a mathematical extension of General Relativity to a 5-dimensional manifold **M = ℝ⁴ × ℰ**, generating modified field equations and testable predictions for quantum coherence, gravitational phenomena, and astrophysical observations.

## ⚠️ Important Disclaimers

- **Theoretical Status:** This represents speculative mathematical exploration, not established physics
- **Independent Research:** Conducted outside institutional frameworks without formal peer review
- **Computational Results:** All numerical results are theoretical predictions requiring experimental validation
- **Extraordinary Claims:** Any implications for fundamental physics should be viewed with appropriate scientific skepticism

## Repository Structure

```
├── src/                     # Simulation codes and computational modules
│   ├── field_equations/     # 5D Einstein equation solvers
│   ├── galaxy_analysis/     # SPARC galaxy rotation curve fitting
│   ├── quantum_coherence/   # Modified decoherence calculations
│   └── cosmological/        # CMB and large-scale structure analysis
├── data/                    # Numerical datasets and results
│   ├── galaxy_fits/         # Galaxy rotation curve analysis results
│   ├── coherence_pred/      # Quantum coherence lifetime predictions
│   └── constraints/         # Observational limits and parameter bounds
├── docs/                    # Technical documentation
│   ├── mathematical_framework.pdf
│   ├── computational_methods.pdf
│   └── api_reference/
└── visualization/           # Plotting scripts and figure generation
```

## Mathematical Framework

The theoretical foundation extends spacetime geometry through:

- **5D Manifold Structure:** M = ℝ⁴ × ℰ with metric signature (-,+,+,+,+)
- **Modified Einstein Equations:** G_AB = 8πT_AB + Λ₅g_AB
- **Scalar Field Dynamics:** □₅Φ_ε = ∂V/∂Φ_ε
- **Matter Coupling:** L_int = -κρ_matter Φ_ε

## Key Computational Results

### Astrophysical Applications
- **Galaxy Sample:** 120 SPARC survey galaxies analyzed
- **Best-fit Parameter:** κ = (2.3 ± 0.4) × 10⁻⁶
- **Model Performance:** χ²/dof = 1.08 (cf. 1.34 for ΛCDM)
- **Information Criterion:** ΔAIC = -47

### Laboratory Predictions
- **Quantum Coherence Enhancement:** τ_modified = 68 ± 4 μs (vs. 47 ± 3 μs standard)
- **Equivalence Principle:** η ~ 5 × 10⁻¹⁴ (within current experimental bounds)

## Installation and Usage

### Requirements
```bash
python >= 3.8
numpy >= 1.20.0
scipy >= 1.7.0
matplotlib >= 3.3.0
astropy >= 4.0
```

### Quick Start
```bash
git clone https://github.com/if-else-world/epsilon.git
cd epsilon
pip install -r requirements.txt

# Run galaxy rotation curve analysis
python src/galaxy_analysis/sparc_fitting.py

# Calculate quantum coherence predictions
python src/quantum_coherence/lifetime_enhancement.py
```

## Reproducibility Statement

All computational results can be independently reproduced using the provided codes and documented parameters. We strongly encourage independent validation and welcome collaborative efforts for experimental testing.

**Version Control:** All results are tagged to specific code versions for reproducibility  
**Documentation:** Comprehensive technical documentation provided in `/docs/`  
**Data Availability:** Complete numerical datasets available in standardized formats

## Scientific Context

### Relationship to Established Physics
- **Conservative Foundation:** Built on standard differential geometry and General Relativity
- **Speculative Extensions:** Novel 5D manifold structure and field coupling mechanisms
- **Falsifiable Predictions:** Specific numerical predictions for laboratory and astrophysical tests

### Model Comparison
| Framework | Dark Matter | Dark Energy | Quantum Effects | Status |
|-----------|-------------|-------------|-----------------|---------|
| ΛCDM | CDM particles | Cosmological constant | Standard QM | Established |
| Modified Gravity | Geometric effect | f(R) dynamics | Standard QM | Alternative |
| **5D Framework** | **ε-field configurations** | **ε-field pressure** | **Modified coherence** | **Speculative** |

## Future Directions

### Critical Validation Needs
1. **Peer Review:** Submission to established physics journals
2. **Independent Reproduction:** Computational validation by other groups  
3. **Experimental Testing:** Laboratory verification of quantum predictions
4. **Theoretical Development:** Mathematical refinement and consistency checks

### Realistic Timeline
Meaningful experimental validation would require 5-10 years of concentrated effort by multiple research groups.

## Contributing

This repository welcomes:
- Independent computational reproduction
- Code improvements and optimization
- Bug reports and documentation enhancement
- Theoretical extensions and mathematical refinements

Please submit issues or pull requests following standard scientific collaboration practices.

## Citation

If you use this code or data in your research, please cite:

```bibtex
@article{delafourniere2025epsilon,
  title={Mathematical Extension of Spacetime to Five Dimensions: Geometric Framework and Empirical Consequences},
  author={de La Fourni{\`e}re, Brieuc},
  journal={Zenodo},
  year={2025},
  doi={10.5281/zenodo.15741958}
}
```

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Contact

**Brieuc de La Fournière**  
Email: ael@ifelse.world  
ORCID: [0009-0000-0641-9740](https://orcid.org/0009-0000-0641-9740)

---

**Final Disclaimer:** This repository contains speculative theoretical development requiring extensive empirical validation. Readers should maintain appropriate scientific skepticism and avoid drawing definitive conclusions about physical reality based on these preliminary theoretical explorations.
