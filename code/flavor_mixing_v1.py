#!/usr/bin/env python3
"""
================================================================================
FLAVOR MIXING PARAMETERS FROM GENERATION HIERARCHY
================================================================================

Paper: "Flavor Mixing Parameters from Generation Hierarchy"
Version: 1.0
Date: January 2026
Author: Erick Francisco Pérez Eugenio

DESCRIPTION:
    This code verifies the empirical observation that flavor mixing parameters
    in the Standard Model can be expressed using a simple generation hierarchy
    rule: p_i = 3^(i-1) for generation i, combined with the cluster number 13.
    
    The code reproduces all calculations in the paper and compares predictions
    with PDG 2024 experimental values.

EMPIRICAL RULES:
    - Generation hierarchy: p_1 = 1, p_2 = 3, p_3 = 9
    - Cluster gauge number: 13 (= 1 + 12 gauge bosons)
    - Secondary cluster: 11 = 13 - 2

USAGE:
    python kaelion_flavor_v1.py
    
LICENSE:
    MIT License - Free to use, modify, and distribute with attribution.

REPOSITORY:
    https://github.com/AsesorErick/kaelion-flavor
    DOI: 10.5281/zenodo.XXXXXXX (pending)

================================================================================
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Dict, List
import json

# ============================================================================
# CONSTANTS AND PDG 2024 VALUES
# ============================================================================

@dataclass
class PDGValues:
    """
    Particle Data Group 2024 experimental values.
    Reference: https://pdg.lbl.gov/
    
    All values are central values with symmetric uncertainties where applicable.
    """
    
    # CKM Matrix elements (magnitudes)
    # Source: PDG 2024, CKM Quark-Mixing Matrix
    Vus: float = 0.2243      # |V_us| = sin(θ_12)
    Vus_err: float = 0.0005
    
    Vcb: float = 0.0422      # |V_cb| = sin(θ_23) * cos(θ_13) ≈ sin(θ_23)
    Vcb_err: float = 0.0008
    
    Vub: float = 0.00369     # |V_ub| = sin(θ_13) - updated value
    Vub_err: float = 0.00011
    
    # CKM CP phase
    delta_CKM_deg: float = 65.4  # degrees (from Jarlskog invariant fit)
    delta_CKM_err: float = 3.0
    
    # PMNS Matrix elements (sin² values)
    # Source: PDG 2024, Neutrino Mixing
    sin2_theta12_PMNS: float = 0.307   # sin²(θ_12)
    sin2_theta12_PMNS_err: float = 0.013
    
    sin2_theta23_PMNS: float = 0.546   # sin²(θ_23) - Normal ordering
    sin2_theta23_PMNS_err: float = 0.021
    
    sin2_theta13_PMNS: float = 0.0220  # sin²(θ_13)
    sin2_theta13_PMNS_err: float = 0.0007
    
    # PMNS CP phase
    delta_PMNS_deg: float = -130.0  # degrees (best fit, large uncertainty)
    delta_PMNS_err: float = 40.0
    
    # Weinberg angle
    sin2_theta_W: float = 0.23121  # sin²(θ_W) at M_Z scale (MS-bar)
    sin2_theta_W_err: float = 0.00004
    
    # Lepton mass ratios
    m_tau: float = 1776.86   # MeV
    m_muon: float = 105.6584 # MeV  
    m_electron: float = 0.51100 # MeV
    
    # Coupling constants (at M_Z scale)
    alpha_s: float = 0.1179
    alpha_s_err: float = 0.0009
    
    alpha_EM_inverse: float = 137.036  # 1/α_EM
    
    alpha_W: float = 0.0338  # α_W = g²/(4π) at M_Z
    alpha_W_err: float = 0.0001
    
    # Higgs sector
    m_H: float = 125.25  # GeV
    v_higgs: float = 246.22  # GeV (VEV)
    
    # Neutrino mass squared differences
    Delta_m2_21: float = 7.53e-5  # eV² (solar)
    Delta_m2_32: float = 2.453e-3  # eV² (atmospheric, normal ordering)


# ============================================================================
# GENERATION HIERARCHY MODEL
# ============================================================================

class GenerationHierarchy:
    """
    Implements the empirical generation hierarchy rule.
    
    The observed regularity suggests that flavor mixing parameters
    can be expressed in terms of:
    - p_i = 3^(i-1) for generation i = 1, 2, 3
    - Cluster number 13 (possibly related to 1 + 12 gauge bosons)
    - Secondary number 11 = 13 - 2
    """
    
    def __init__(self):
        # Generation powers
        self.p = {1: 1, 2: 3, 3: 9}  # p_i = 3^(i-1)
        
        # Cluster numbers
        self.cluster = 13
        self.cluster_secondary = 11  # = 13 - 2
        
    def get_p(self, gen: int) -> int:
        """Get power for generation i."""
        if gen not in [1, 2, 3]:
            raise ValueError(f"Generation must be 1, 2, or 3, got {gen}")
        return self.p[gen]
    
    # ========================================================================
    # CKM MATRIX PREDICTIONS
    # ========================================================================
    
    def sin_theta12_CKM(self) -> Tuple[float, str]:
        """
        CKM θ_12 (Cabibbo angle).
        
        Empirical formula: sin(θ_12) = (p_2 × 13 - p_1) / 13²
                                     = (3 × 13 - 1) / 169
                                     = 38 / 169
        """
        num = self.p[2] * self.cluster - self.p[1]
        denom = self.cluster ** 2
        value = num / denom
        formula = f"(p₂×13 - p₁)/13² = ({self.p[2]}×13 - {self.p[1]})/169 = {num}/{denom}"
        return value, formula
    
    def sin_theta23_CKM(self) -> Tuple[float, str]:
        """
        CKM θ_23.
        
        Empirical formula: sin(θ_23) = [13 - (p_3 - p_2)] / 13²
                                     = (13 - 6) / 169
                                     = 7 / 169
        """
        num = self.cluster - (self.p[3] - self.p[2])
        denom = self.cluster ** 2
        value = num / denom
        formula = f"[13 - (p₃-p₂)]/13² = [13 - ({self.p[3]}-{self.p[2]})]/169 = {num}/{denom}"
        return value, formula
    
    def sin_theta13_CKM(self) -> Tuple[float, str]:
        """
        CKM θ_13.
        
        Empirical formula: sin(θ_13) = (p_3 - p_1) / 13³
                                     = 8 / 2197
        """
        num = self.p[3] - self.p[1]
        denom = self.cluster ** 3
        value = num / denom
        formula = f"(p₃ - p₁)/13³ = ({self.p[3]} - {self.p[1]})/2197 = {num}/{denom}"
        return value, formula
    
    def sin_delta_CKM(self) -> Tuple[float, str]:
        """
        CKM CP phase δ.
        
        Empirical formula: sin(δ) = (13 - p_2) / (13 - 2)
                                  = 10 / 11
        """
        num = self.cluster - self.p[2]
        denom = self.cluster - 2
        value = num / denom
        formula = f"(13 - p₂)/(13 - 2) = (13 - {self.p[2]})/11 = {num}/{denom}"
        return value, formula
    
    def delta_CKM_degrees(self) -> float:
        """Return CKM δ in degrees."""
        sin_delta, _ = self.sin_delta_CKM()
        return np.degrees(np.arcsin(sin_delta))
    
    # ========================================================================
    # PMNS MATRIX PREDICTIONS
    # ========================================================================
    
    def sin2_theta12_PMNS(self) -> Tuple[float, str]:
        """
        PMNS θ_12 (solar angle).
        
        Empirical formula: sin²(θ_12) = (p_1 + p_2) / 13
                                      = 4 / 13
        """
        num = self.p[1] + self.p[2]
        denom = self.cluster
        value = num / denom
        formula = f"(p₁ + p₂)/13 = ({self.p[1]} + {self.p[2]})/13 = {num}/{denom}"
        return value, formula
    
    def sin2_theta23_PMNS(self) -> Tuple[float, str]:
        """
        PMNS θ_23 (atmospheric angle).
        
        Empirical formula: sin²(θ_23) = (p_3 - p_2) / (13 - 2)
                                      = 6 / 11
        """
        num = self.p[3] - self.p[2]
        denom = self.cluster - 2
        value = num / denom
        formula = f"(p₃ - p₂)/(13 - 2) = ({self.p[3]} - {self.p[2]})/11 = {num}/{denom}"
        return value, formula
    
    def sin2_theta13_PMNS(self) -> Tuple[float, str]:
        """
        PMNS θ_13 (reactor angle).
        
        Empirical formula: sin²(θ_13) = (13 - p_3)(13 - p_1) / 13³
                                      = 4 × 12 / 2197
                                      = 48 / 2197
        """
        num = (self.cluster - self.p[3]) * (self.cluster - self.p[1])
        denom = self.cluster ** 3
        value = num / denom
        formula = f"(13-p₃)(13-p₁)/13³ = (13-{self.p[3]})(13-{self.p[1]})/2197 = {num}/{denom}"
        return value, formula
    
    def sin_delta_PMNS(self) -> Tuple[float, str]:
        """
        PMNS CP phase δ.
        
        Empirical formula: sin(δ) = -(13 - p_2) / 13
                                  = -10 / 13
        
        Note: Negative sign distinguishes leptons from quarks.
        """
        num = self.cluster - self.p[2]
        denom = self.cluster
        value = -num / denom  # Negative for leptons
        formula = f"-(13 - p₂)/13 = -(13 - {self.p[2]})/13 = -{num}/{denom}"
        return value, formula
    
    def delta_PMNS_degrees(self) -> float:
        """
        Return PMNS δ in degrees.
        
        Note: arcsin(-10/13) gives -50.28°, but the physical angle
        is in the second/third quadrant: δ = -180° - arcsin(10/13) = -129.72°
        
        sin(δ) = -10/13 has two solutions in [-180°, 180°]:
        - δ = -50.28° (principal value)
        - δ = -180° + 50.28° = -129.72° (physical value)
        """
        # sin(δ) = -10/13, so |sin(δ)| = 10/13
        principal = np.degrees(np.arcsin(10/13))  # +50.28°
        # Physical angle is in third quadrant
        return -180 + principal  # -129.72°
    
    # ========================================================================
    # WEINBERG ANGLE
    # ========================================================================
    
    def sin2_theta_W(self) -> Tuple[float, str]:
        """
        Weinberg angle (weak mixing angle).
        
        Empirical formula: sin²(θ_W) = p_2 / 13
                                     = 3 / 13
        """
        num = self.p[2]
        denom = self.cluster
        value = num / denom
        formula = f"p₂/13 = {self.p[2]}/13 = {num}/{denom}"
        return value, formula
    
    # ========================================================================
    # CROSS-RELATIONS
    # ========================================================================
    
    def cross_relation_theta13(self) -> Tuple[float, float, str]:
        """
        Cross-relation between CKM and PMNS θ_13.
        
        Observation: sin²(θ_13)_PMNS = 6 × sin(θ_13)_CKM
        
        Derivation:
        - sin(θ_13)_CKM = 8/13³
        - sin²(θ_13)_PMNS = 48/13³
        - Ratio = 48/8 = 6
        """
        sin_ckm, _ = self.sin_theta13_CKM()
        sin2_pmns, _ = self.sin2_theta13_PMNS()
        ratio = sin2_pmns / sin_ckm
        explanation = "sin²(θ₁₃)_PMNS / sin(θ₁₃)_CKM = (48/13³) / (8/13³) = 48/8 = 6"
        return ratio, 6.0, explanation
    
    def phase_structure(self) -> str:
        """
        Explain the structure of CP phases.
        
        Both CKM and PMNS phases share numerator 10 = 13 - p_2.
        - CKM: +10/11 (positive, denominator 11)
        - PMNS: -10/13 (negative, denominator 13)
        """
        explanation = """
CP Phase Structure:
    Common numerator: 10 = 13 - p₂ = 13 - 3
    
    CKM:  sin(δ) = +10/11 = +(13-p₂)/(13-2)  →  δ = +65.4°
    PMNS: sin(δ) = -10/13 = -(13-p₂)/13      →  δ = -129.7°
    
    Interpretation:
    - Numerator 10 = cluster - generation_2
    - CKM denominator 11 = cluster - 2
    - PMNS denominator 13 = cluster
    - Sign: positive for quarks, negative for leptons
"""
        return explanation


# ============================================================================
# ADDITIONAL PREDICTIONS (for extended analysis)
# ============================================================================

class ExtendedPredictions(GenerationHierarchy):
    """
    Extended predictions beyond flavor mixing.
    These are more speculative and included for completeness.
    """
    
    def alpha_strong(self) -> Tuple[float, str]:
        """
        Strong coupling constant.
        
        Empirical formula: α_s = 1/p_3 = 1/9
        """
        value = 1 / self.p[3]
        formula = f"1/p₃ = 1/{self.p[3]}"
        return value, formula
    
    def alpha_EM_inverse(self) -> Tuple[int, str]:
        """
        Inverse of electromagnetic coupling constant.
        
        Empirical formula: 1/α_EM = 11×13 - (p_3 - p_2)
                                  = 143 - 6
                                  = 137
        """
        value = 11 * 13 - (self.p[3] - self.p[2])
        formula = f"11×13 - (p₃-p₂) = 143 - ({self.p[3]}-{self.p[2]}) = 143 - 6 = {value}"
        return value, formula
    
    def lepton_mass_ratio_tau_muon(self) -> Tuple[int, str]:
        """
        Tau to muon mass ratio.
        
        Empirical formula: m_τ/m_μ = 13 + p_2 + p_1 = 17
        """
        value = self.cluster + self.p[2] + self.p[1]
        formula = f"13 + p₂ + p₁ = 13 + {self.p[2]} + {self.p[1]} = {value}"
        return value, formula
    
    def lepton_mass_ratio_muon_electron(self) -> Tuple[int, str]:
        """
        Muon to electron mass ratio.
        
        Empirical formula: m_μ/m_e = 13×(13 + p_2) - p_1 = 207
        """
        value = self.cluster * (self.cluster + self.p[2]) - self.p[1]
        formula = f"13×(13+p₂) - p₁ = 13×(13+{self.p[2]}) - {self.p[1]} = 13×16 - 1 = {value}"
        return value, formula
    
    def neutrino_mass_ratio(self) -> Tuple[int, str]:
        """
        Ratio of neutrino mass squared differences.
        
        Empirical formula: Δm²_32/Δm²_21 = (p_3 - p_1)(p_2 + p_1) = 32
        """
        value = (self.p[3] - self.p[1]) * (self.p[2] + self.p[1])
        formula = f"(p₃-p₁)(p₂+p₁) = ({self.p[3]}-{self.p[1]})({self.p[2]}+{self.p[1]}) = 8×4 = {value}"
        return value, formula
    
    def higgs_vev_ratio(self) -> Tuple[float, str]:
        """
        Higgs mass to VEV ratio.
        
        Empirical formula: m_H/v = 1/2 + 1/(p_3 × 13) = 1/2 + 1/117
        """
        value = 0.5 + 1/(self.p[3] * self.cluster)
        formula = f"1/2 + 1/(p₃×13) = 1/2 + 1/({self.p[3]}×13) = 1/2 + 1/117"
        return value, formula


# ============================================================================
# VERIFICATION AND COMPARISON
# ============================================================================

def compare_with_experiment(model: GenerationHierarchy, pdg: PDGValues) -> Dict:
    """
    Compare model predictions with PDG experimental values.
    
    Returns a dictionary with all comparisons.
    """
    results = {}
    
    # CKM Matrix
    val, formula = model.sin_theta12_CKM()
    results['CKM_theta12'] = {
        'parameter': 'sin(θ₁₂)_CKM',
        'formula': formula,
        'predicted': val,
        'observed': pdg.Vus,
        'obs_error': pdg.Vus_err,
        'deviation_percent': abs(val - pdg.Vus) / pdg.Vus * 100,
        'sigma': abs(val - pdg.Vus) / pdg.Vus_err if pdg.Vus_err > 0 else None
    }
    
    val, formula = model.sin_theta23_CKM()
    results['CKM_theta23'] = {
        'parameter': 'sin(θ₂₃)_CKM',
        'formula': formula,
        'predicted': val,
        'observed': pdg.Vcb,
        'obs_error': pdg.Vcb_err,
        'deviation_percent': abs(val - pdg.Vcb) / pdg.Vcb * 100,
        'sigma': abs(val - pdg.Vcb) / pdg.Vcb_err if pdg.Vcb_err > 0 else None
    }
    
    val, formula = model.sin_theta13_CKM()
    results['CKM_theta13'] = {
        'parameter': 'sin(θ₁₃)_CKM',
        'formula': formula,
        'predicted': val,
        'observed': pdg.Vub,
        'obs_error': pdg.Vub_err,
        'deviation_percent': abs(val - pdg.Vub) / pdg.Vub * 100,
        'sigma': abs(val - pdg.Vub) / pdg.Vub_err if pdg.Vub_err > 0 else None
    }
    
    val, formula = model.sin_delta_CKM()
    delta_deg = model.delta_CKM_degrees()
    results['CKM_delta'] = {
        'parameter': 'sin(δ)_CKM',
        'formula': formula,
        'predicted': val,
        'predicted_deg': delta_deg,
        'observed_deg': pdg.delta_CKM_deg,
        'obs_error_deg': pdg.delta_CKM_err,
        'deviation_percent': abs(delta_deg - pdg.delta_CKM_deg) / pdg.delta_CKM_deg * 100
    }
    
    # PMNS Matrix
    val, formula = model.sin2_theta12_PMNS()
    results['PMNS_theta12'] = {
        'parameter': 'sin²(θ₁₂)_PMNS',
        'formula': formula,
        'predicted': val,
        'observed': pdg.sin2_theta12_PMNS,
        'obs_error': pdg.sin2_theta12_PMNS_err,
        'deviation_percent': abs(val - pdg.sin2_theta12_PMNS) / pdg.sin2_theta12_PMNS * 100,
        'sigma': abs(val - pdg.sin2_theta12_PMNS) / pdg.sin2_theta12_PMNS_err
    }
    
    val, formula = model.sin2_theta23_PMNS()
    results['PMNS_theta23'] = {
        'parameter': 'sin²(θ₂₃)_PMNS',
        'formula': formula,
        'predicted': val,
        'observed': pdg.sin2_theta23_PMNS,
        'obs_error': pdg.sin2_theta23_PMNS_err,
        'deviation_percent': abs(val - pdg.sin2_theta23_PMNS) / pdg.sin2_theta23_PMNS * 100,
        'sigma': abs(val - pdg.sin2_theta23_PMNS) / pdg.sin2_theta23_PMNS_err
    }
    
    val, formula = model.sin2_theta13_PMNS()
    results['PMNS_theta13'] = {
        'parameter': 'sin²(θ₁₃)_PMNS',
        'formula': formula,
        'predicted': val,
        'observed': pdg.sin2_theta13_PMNS,
        'obs_error': pdg.sin2_theta13_PMNS_err,
        'deviation_percent': abs(val - pdg.sin2_theta13_PMNS) / pdg.sin2_theta13_PMNS * 100,
        'sigma': abs(val - pdg.sin2_theta13_PMNS) / pdg.sin2_theta13_PMNS_err
    }
    
    val, formula = model.sin_delta_PMNS()
    delta_deg = model.delta_PMNS_degrees()
    results['PMNS_delta'] = {
        'parameter': 'sin(δ)_PMNS',
        'formula': formula,
        'predicted': val,
        'predicted_deg': delta_deg,
        'observed_deg': pdg.delta_PMNS_deg,
        'obs_error_deg': pdg.delta_PMNS_err,
        'deviation_percent': abs(delta_deg - pdg.delta_PMNS_deg) / abs(pdg.delta_PMNS_deg) * 100
    }
    
    # Weinberg angle
    val, formula = model.sin2_theta_W()
    results['Weinberg'] = {
        'parameter': 'sin²(θ_W)',
        'formula': formula,
        'predicted': val,
        'observed': pdg.sin2_theta_W,
        'obs_error': pdg.sin2_theta_W_err,
        'deviation_percent': abs(val - pdg.sin2_theta_W) / pdg.sin2_theta_W * 100,
        'sigma': abs(val - pdg.sin2_theta_W) / pdg.sin2_theta_W_err
    }
    
    return results


def print_results(results: Dict) -> None:
    """Print comparison results in a formatted table."""
    
    print("\n" + "=" * 80)
    print("FLAVOR MIXING PARAMETERS FROM GENERATION HIERARCHY")
    print("Comparison with PDG 2024 experimental values")
    print("=" * 80)
    
    print("\n" + "-" * 80)
    print("CKM MATRIX (Quarks)")
    print("-" * 80)
    print(f"{'Parameter':<20} {'Predicted':>12} {'Observed':>12} {'Error %':>10}")
    print("-" * 80)
    
    for key in ['CKM_theta12', 'CKM_theta23', 'CKM_theta13']:
        r = results[key]
        print(f"{r['parameter']:<20} {r['predicted']:>12.6f} {r['observed']:>12.6f} {r['deviation_percent']:>9.2f}%")
    
    r = results['CKM_delta']
    print(f"{'δ_CKM (degrees)':<20} {r['predicted_deg']:>12.2f}° {r['observed_deg']:>11.1f}° {r['deviation_percent']:>9.2f}%")
    
    print("\n" + "-" * 80)
    print("PMNS MATRIX (Leptons)")
    print("-" * 80)
    print(f"{'Parameter':<20} {'Predicted':>12} {'Observed':>12} {'Error %':>10}")
    print("-" * 80)
    
    for key in ['PMNS_theta12', 'PMNS_theta23', 'PMNS_theta13']:
        r = results[key]
        print(f"{r['parameter']:<20} {r['predicted']:>12.6f} {r['observed']:>12.6f} {r['deviation_percent']:>9.2f}%")
    
    r = results['PMNS_delta']
    print(f"{'δ_PMNS (degrees)':<20} {r['predicted_deg']:>12.2f}° {r['observed_deg']:>11.1f}° {r['deviation_percent']:>9.2f}%")
    
    print("\n" + "-" * 80)
    print("WEINBERG ANGLE")
    print("-" * 80)
    r = results['Weinberg']
    print(f"{r['parameter']:<20} {r['predicted']:>12.6f} {r['observed']:>12.6f} {r['deviation_percent']:>9.2f}%")
    
    print("\n" + "=" * 80)


def print_formulas(model: GenerationHierarchy) -> None:
    """Print all formulas used."""
    
    print("\n" + "=" * 80)
    print("EMPIRICAL FORMULAS")
    print("=" * 80)
    
    print("\nGeneration Hierarchy Rule:")
    print("  p_i = 3^(i-1) for generation i = 1, 2, 3")
    print(f"  p_1 = {model.p[1]}, p_2 = {model.p[2]}, p_3 = {model.p[3]}")
    print(f"  Cluster number = {model.cluster}")
    
    print("\n" + "-" * 80)
    print("CKM Matrix Formulas:")
    print("-" * 80)
    _, f = model.sin_theta12_CKM()
    print(f"  sin(θ₁₂) = {f}")
    _, f = model.sin_theta23_CKM()
    print(f"  sin(θ₂₃) = {f}")
    _, f = model.sin_theta13_CKM()
    print(f"  sin(θ₁₃) = {f}")
    _, f = model.sin_delta_CKM()
    print(f"  sin(δ)   = {f}")
    
    print("\n" + "-" * 80)
    print("PMNS Matrix Formulas:")
    print("-" * 80)
    _, f = model.sin2_theta12_PMNS()
    print(f"  sin²(θ₁₂) = {f}")
    _, f = model.sin2_theta23_PMNS()
    print(f"  sin²(θ₂₃) = {f}")
    _, f = model.sin2_theta13_PMNS()
    print(f"  sin²(θ₁₃) = {f}")
    _, f = model.sin_delta_PMNS()
    print(f"  sin(δ)    = {f}")
    
    print("\n" + "-" * 80)
    print("Weinberg Angle:")
    print("-" * 80)
    _, f = model.sin2_theta_W()
    print(f"  sin²(θ_W) = {f}")
    
    print("\n" + "-" * 80)
    print("Cross-Relations:")
    print("-" * 80)
    ratio, expected, explanation = model.cross_relation_theta13()
    print(f"  {explanation}")
    print(f"  Calculated ratio: {ratio:.1f} (expected: {expected})")
    
    print(model.phase_structure())


def print_extended_predictions(model: ExtendedPredictions, pdg: PDGValues) -> None:
    """Print extended predictions (more speculative)."""
    
    print("\n" + "=" * 80)
    print("EXTENDED PREDICTIONS (Exploratory)")
    print("=" * 80)
    print("Note: These predictions are more speculative and require further investigation.")
    
    print("\n" + "-" * 80)
    print("Coupling Constants:")
    print("-" * 80)
    
    val, formula = model.alpha_strong()
    obs = pdg.alpha_s
    err = abs(val - obs) / obs * 100
    print(f"  α_s = {formula} = {val:.4f}")
    print(f"        Observed: {obs:.4f}, Error: {err:.2f}%")
    
    val, formula = model.alpha_EM_inverse()
    obs = pdg.alpha_EM_inverse
    err = abs(val - obs) / obs * 100
    print(f"\n  1/α_EM = {formula}")
    print(f"           Observed: {obs:.3f}, Error: {err:.3f}%")
    
    print("\n" + "-" * 80)
    print("Lepton Mass Ratios:")
    print("-" * 80)
    
    val, formula = model.lepton_mass_ratio_tau_muon()
    obs = pdg.m_tau / pdg.m_muon
    err = abs(val - obs) / obs * 100
    print(f"  m_τ/m_μ = {formula} = {val}")
    print(f"            Observed: {obs:.3f}, Error: {err:.2f}%")
    
    val, formula = model.lepton_mass_ratio_muon_electron()
    obs = pdg.m_muon / pdg.m_electron
    err = abs(val - obs) / obs * 100
    print(f"\n  m_μ/m_e = {formula} = {val}")
    print(f"            Observed: {obs:.2f}, Error: {err:.2f}%")
    
    print("\n" + "-" * 80)
    print("Neutrino Mass Ratio:")
    print("-" * 80)
    
    val, formula = model.neutrino_mass_ratio()
    obs = pdg.Delta_m2_32 / pdg.Delta_m2_21
    err = abs(val - obs) / obs * 100
    print(f"  Δm²₃₂/Δm²₂₁ = {formula} = {val}")
    print(f"                Observed: {obs:.2f}, Error: {err:.2f}%")
    
    print("\n" + "-" * 80)
    print("Higgs Sector:")
    print("-" * 80)
    
    val, formula = model.higgs_vev_ratio()
    obs = pdg.m_H / pdg.v_higgs
    err = abs(val - obs) / obs * 100
    print(f"  m_H/v = {formula} = {val:.6f}")
    print(f"          Observed: {obs:.6f}, Error: {err:.3f}%")


def export_results_json(results: Dict, filename: str = "kaelion_flavor_results.json") -> None:
    """Export results to JSON for further analysis."""
    
    # Convert numpy types to Python native types
    def convert(obj):
        if isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        return obj
    
    results_clean = convert(results)
    
    with open(filename, 'w') as f:
        json.dump(results_clean, f, indent=2)
    
    print(f"\nResults exported to {filename}")


# ============================================================================
# FALSIFIABILITY STATEMENT
# ============================================================================

def print_falsifiability() -> None:
    """Print falsifiability criteria for the hypothesis."""
    
    print("\n" + "=" * 80)
    print("FALSIFIABILITY CRITERIA")
    print("=" * 80)
    
    print("""
The generation hierarchy hypothesis makes specific, testable predictions.
If future measurements significantly deviate from these relations, the
hypothesis must be discarded.

CRITICAL TESTS:

1. PMNS θ₁₂ (Solar angle):
   Prediction: sin²(θ₁₂) = 4/13 = 0.3077
   Current:    0.307 ± 0.013
   Future precision (JUNO): ±0.003
   
   → If JUNO measures sin²(θ₁₂) > 0.315 or < 0.300 at 3σ,
     the hypothesis is falsified.

2. PMNS θ₂₃ (Atmospheric angle):
   Prediction: sin²(θ₂₃) = 6/11 = 0.5455
   Current:    0.546 ± 0.021
   Future precision (DUNE): ±0.01
   
   → If DUNE measures sin²(θ₂₃) > 0.575 or < 0.515 at 3σ,
     the hypothesis is falsified.

3. PMNS δ_CP:
   Prediction: sin(δ) = -10/13 → δ = -129.7°
   Current:    -130° ± 40°
   Future precision (DUNE): ±10°
   
   → If DUNE measures δ_CP outside [-150°, -110°] at 3σ,
     the hypothesis is falsified.

4. Weinberg angle (high precision):
   Prediction: sin²(θ_W) = 3/13 = 0.2308
   Current:    0.23121 ± 0.00004
   
   → The prediction differs by 0.2%, which is 10σ from current value.
     This is already in tension and requires explanation.
     Possible interpretation: 3/13 is the "bare" value at unification scale.

SUMMARY:
The hypothesis is FALSIFIABLE. Upcoming experiments (JUNO 2025+, DUNE 2030+)
will provide definitive tests of the PMNS predictions.
""")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    
    print("\n" + "=" * 80)
    print("  KAELION FLAVOR v1.0 - Verification Code for Paper 5")
    print("=" * 80)
    
    # Initialize model and PDG values
    model = GenerationHierarchy()
    extended = ExtendedPredictions()
    pdg = PDGValues()
    
    # Print formulas
    print_formulas(model)
    
    # Compare with experiment
    results = compare_with_experiment(model, pdg)
    print_results(results)
    
    # Extended predictions
    print_extended_predictions(extended, pdg)
    
    # Falsifiability
    print_falsifiability()
    
    # Export results
    export_results_json(results)
    
    print("\n" + "=" * 80)
    print("  Execution complete. Results exported to kaelion_flavor_results.json")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
