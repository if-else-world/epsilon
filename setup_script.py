#!/usr/bin/env python3
"""
Script pour créer automatiquement la structure du repository epsilon
"""

import os
import subprocess

def create_directory_structure():
    """Crée l'arborescence complète du projet"""
    
    # Structure des dossiers
    directories = [
        "src/field_equations",
        "src/galaxy_analysis", 
        "src/quantum_coherence",
        "src/cosmological",
        "data/galaxy_fits",
        "data/coherence_pred",
        "data/constraints",
        "docs/api_reference",
        "visualization"
    ]
    
    # Créer tous les dossiers
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Créé: {directory}/")
    
    # Fichiers README pour chaque section principale
    readme_contents = {
        "src/README.md": """# Source Code

Ce dossier contient les modules de calcul pour le framework epsilon.

## Modules

- `field_equations/` : Solveurs pour les équations d'Einstein 5D
- `galaxy_analysis/` : Analyse des courbes de rotation galactiques
- `quantum_coherence/` : Calculs de cohérence quantique modifiée
- `cosmological/` : Analyses CMB et structure à grande échelle
""",
        
        "src/field_equations/README.md": """# Field Equations Solvers

Solveurs numériques pour les équations de champ 5D.

## Fichiers attendus

- `einstein_5d.py` : Solveur principal des équations d'Einstein 5D
- `metric_utils.py` : Utilitaires pour les calculs métriques
- `boundary_conditions.py` : Conditions aux limites
""",

        "src/galaxy_analysis/README.md": """# Galaxy Analysis

Analyse des courbes de rotation galactiques avec le framework 5D.

## Fichiers attendus

- `sparc_fitting.py` : Ajustement sur les données SPARC
- `rotation_curves.py` : Calculs des courbes de rotation modifiées
- `statistical_analysis.py` : Analyses statistiques et comparaisons de modèles
""",

        "src/quantum_coherence/README.md": """# Quantum Coherence

Calculs des effets quantiques dans le framework 5D.

## Fichiers attendus

- `lifetime_enhancement.py` : Prédictions d'amélioration des temps de cohérence
- `decoherence_modified.py` : Modèles de décohérence modifiée
- `experimental_protocols.py` : Protocoles expérimentaux suggérés
""",

        "src/cosmological/README.md": """# Cosmological Analysis

Analyses cosmologiques et contraintes observationnelles.

## Fichiers attendus

- `cmb_analysis.py` : Analyse du fond diffus cosmologique
- `large_scale_structure.py` : Structure à grande échelle
- `observational_constraints.py` : Contraintes observationnelles
""",

        "data/README.md": """# Data

Datasets numériques et résultats computationnels.

## Structure

- `galaxy_fits/` : Résultats d'ajustement des galaxies
- `coherence_pred/` : Prédictions de cohérence quantique
- `constraints/` : Limites observationnelles et contraintes paramétriques

## Formats

- CSV pour les données tabulaires
- HDF5 pour les datasets volumineux
- JSON pour les métadonnées et paramètres
""",

        "docs/README.md": """# Documentation

Documentation technique du framework.

## Fichiers

- `mathematical_framework.pdf` : Fondements mathématiques détaillés
- `computational_methods.pdf` : Méthodes numériques et algorithmes
- `api_reference/` : Documentation des APIs de code
""",

        "visualization/README.md": """# Visualization

Scripts de visualisation et génération de figures.

## Fichiers attendus

- `plot_galaxy_fits.py` : Graphiques des ajustements galactiques
- `plot_coherence_predictions.py` : Visualisation des prédictions quantiques
- `plot_parameter_space.py` : Exploration de l'espace des paramètres
- `figure_generation.py` : Génération automatique des figures pour publications
""",

        "requirements.txt": """# Dépendances Python pour le projet epsilon
numpy>=1.20.0
scipy>=1.7.0
matplotlib>=3.3.0
astropy>=4.0
pandas>=1.3.0
h5py>=3.1.0
jupyter>=1.0.0
sympy>=1.8
""",

        ".gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# Data files
*.h5
*.hdf5
large_datasets/

# Temporary files
*.tmp
*.log
.DS_Store

# IDE
.vscode/
.idea/
*.swp
*.swo
"""
    }
    
    # Créer tous les fichiers README
    for filepath, content in readme_contents.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Créé: {filepath}")

def create_placeholder_files():
    """Crée quelques fichiers placeholder pour maintenir la structure git"""
    
    placeholders = [
        "src/field_equations/.gitkeep",
        "src/galaxy_analysis/.gitkeep", 
        "src/quantum_coherence/.gitkeep",
        "src/cosmological/.gitkeep",
        "data/galaxy_fits/.gitkeep",
        "data/coherence_pred/.gitkeep",
        "data/constraints/.gitkeep",
        "docs/api_reference/.gitkeep",
        "visualization/.gitkeep"
    ]
    
    for placeholder in placeholders:
        with open(placeholder, 'w') as f:
            f.write("# Placeholder file to maintain directory structure in git\n")
        print(f"✓ Créé: {placeholder}")

def main():
    print("🚀 Création de la structure du repository epsilon...")
    print()
    
    create_directory_structure()
    print()
    
    create_placeholder_files()
    print()
    
    print("✅ Structure créée avec succès !")
    print()
    print("Prochaines étapes :")
    print("1. git add .")
    print("2. git commit -m 'Initialize repository structure'")
    print("3. git push")
    print()
    print("La structure est maintenant prête pour le développement !")

if __name__ == "__main__":
    main()
