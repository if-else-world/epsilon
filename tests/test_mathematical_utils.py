#!/usr/bin/env python3
"""
Unit tests for shared mathematical utilities
"""

import unittest
import numpy as np
from frameworks.shared.math_utils import PHI, golden_ratio_frequencies

class TestMathUtils(unittest.TestCase):
    
    def test_golden_ratio_constant(self):
        """Test golden ratio constant"""
        expected_phi = (1 + np.sqrt(5)) / 2
        self.assertAlmostEqual(PHI, expected_phi, places=10)
        
    def test_golden_ratio_frequencies(self):
        """Test φ-linked frequency generation"""
        base_freq = 0.001
        freqs = golden_ratio_frequencies(base_freq, 3)
        expected = [PHI * base_freq, 2 * PHI * base_freq, 3 * PHI * base_freq]
        np.testing.assert_array_almost_equal(freqs, expected)

if __name__ == "__main__":
    unittest.main()
