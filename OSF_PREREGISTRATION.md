# PRE-REGISTRATION: Flavor Mixing Parameters from Generation Hierarchy

## Study Information

**Title:** Flavor Mixing Parameters from Generation Hierarchy: An Empirical Observation

**Author:** Erick Francisco Pérez Eugenio  
**ORCID:** 0009-0006-3228-4847  
**Date of Pre-registration:** January 23, 2026  
**Institution:** Independent Researcher

---

## 1. Hypotheses

### Primary Hypothesis

The flavor mixing parameters of the Standard Model can be expressed using simple fractions involving the numbers 3, 11, and 13, based on a generation hierarchy rule pᵢ = 3^(i-1).

### Specific Predictions

#### CKM Matrix (Quarks)

| Parameter | Predicted Value | Formula |
|-----------|-----------------|---------|
| sin(θ₁₂)_CKM | 0.224852071 | 38/169 = 38/13² |
| sin(θ₂₃)_CKM | 0.041420118 | 7/169 = 7/13² |
| sin(θ₁₃)_CKM | 0.003641329 | 8/2197 = 8/13³ |
| sin(δ)_CKM | 0.909090909 | 10/11 |

#### PMNS Matrix (Leptons)

| Parameter | Predicted Value | Formula |
|-----------|-----------------|---------|
| sin²(θ₁₂)_PMNS | 0.307692308 | 4/13 |
| sin²(θ₂₃)_PMNS | 0.545454545 | 6/11 |
| sin²(θ₁₃)_PMNS | 0.021847975 | 48/2197 = 48/13³ |
| sin(δ)_PMNS | -0.769230769 | -10/13 |

#### Weinberg Angle

| Parameter | Predicted Value | Formula |
|-----------|-----------------|---------|
| sin²(θ_W) | 0.230769231 | 3/13 |

---

## 2. Falsification Criteria

### For JUNO Experiment (~2027)

**Parameter:** sin²(θ₁₂)_PMNS

- **Prediction:** 4/13 = 0.30769...
- **Current PDG 2024:** 0.307 ± 0.013
- **Expected JUNO precision:** ±0.003

**Falsification threshold:** 
If JUNO measures sin²(θ₁₂) < 0.301 or sin²(θ₁₂) > 0.314 (3σ from prediction), the hypothesis is falsified for this parameter.

### For DUNE Experiment (~2029)

**Parameter:** sin(δ)_PMNS

- **Prediction:** -10/13 = -0.76923...
- **Current PDG 2024:** -0.766 ± 0.05
- **Expected DUNE precision:** ±0.02

**Falsification threshold:**
If DUNE measures sin(δ) < -0.83 or sin(δ) > -0.71 (3σ from prediction), the hypothesis is falsified for this parameter.

### Global Falsification

If **two or more** of the nine predictions deviate by more than 3σ from experimental values, the entire hypothesis should be considered falsified.

---

## 3. Current Experimental Values (PDG 2024)

These are the values used for comparison at the time of pre-registration:

### CKM Matrix
- |V_us| = 0.2243 ± 0.0005 → sin(θ₁₂) = 0.2243
- |V_cb| = 0.0422 ± 0.0008 → sin(θ₂₃) = 0.0422
- |V_ub| = 0.00369 ± 0.00011 → sin(θ₁₃) = 0.00369
- δ_CKM = 65.4° ± 3.0° → sin(δ) = 0.909

### PMNS Matrix
- sin²(θ₁₂) = 0.307 ± 0.013
- sin²(θ₂₃) = 0.546 ± 0.021 (normal ordering)
- sin²(θ₁₃) = 0.0220 ± 0.0007
- δ_PMNS = -130° ± 40° → sin(δ) = -0.766

### Electroweak
- sin²(θ_W) = 0.23121 ± 0.00004

---

## 4. Analysis Plan

### 4.1 Comparison Method

For each parameter:
1. Calculate predicted value from formula
2. Compare to experimental central value
3. Calculate percentage deviation: |pred - obs| / |obs| × 100%
4. Calculate sigma deviation: |pred - obs| / σ_obs

### 4.2 Success Criteria

The hypothesis is considered **supported** (not proven) if:
- All 9 parameters have deviations < 3σ
- Average percentage deviation < 2%
- No systematic bias (over/under-prediction pattern)

### 4.3 Code Availability

All analysis code is available at:
- GitHub: https://github.com/AsesorErick/kaelion-flavor
- Zenodo: DOI pending

---

## 5. Theoretical Framework

### 5.1 Generation Hierarchy Rule

For generation i = 1, 2, 3:
```
pᵢ = 3^(i-1)

p₁ = 3⁰ = 1
p₂ = 3¹ = 3
p₃ = 3² = 9
```

### 5.2 Cluster Numbers

- Primary cluster: 13 = 1 + 12 (one observer + 12 gauge bosons)
- Secondary cluster: 11 = 13 - 2

### 5.3 Formula Construction

The formulas are constructed using combinations of pᵢ and cluster numbers:

**CKM:**
- θ₁₂: (p₂×13 - p₁)/13² = (39-1)/169 = 38/169
- θ₂₃: [13 - (p₃-p₂)]/13² = [13-6]/169 = 7/169
- θ₁₃: (p₃ - p₁)/13³ = 8/2197
- δ: (13 - p₂)/(13-2) = 10/11

**PMNS:**
- θ₁₂: (p₁ + p₂)/13 = 4/13
- θ₂₃: (p₃ - p₂)/(13-2) = 6/11
- θ₁₃: (13-p₃)(13-p₁)/13³ = 4×12/2197 = 48/2197
- δ: -(13 - p₂)/13 = -10/13

**Weinberg:**
- θ_W: p₂/13 = 3/13

---

## 6. Limitations and Caveats

### 6.1 This is NOT a derivation

These formulas are **observed patterns**, not derived from first principles. No mechanism is proposed for WHY these patterns exist.

### 6.2 Numerology risk

While the formulas use only numbers with physical significance (3, 11, 13), the possibility of coincidental agreement cannot be excluded.

### 6.3 Post-hoc construction

The formulas were constructed to match known experimental values. This pre-registration freezes the predictions for future comparison.

---

## 7. Declaration

I, Erick Francisco Pérez Eugenio, declare that:

1. These predictions are made BEFORE the publication of JUNO and DUNE precision results
2. The formulas will NOT be modified to match future experimental values
3. If the predictions are falsified, I will publicly acknowledge this
4. All code and data are openly available for verification

---

## 8. References

1. Particle Data Group (2024). Review of Particle Physics. Prog. Theor. Exp. Phys.
2. JUNO Collaboration (2022). JUNO Physics and Detector. Prog. Part. Nucl. Phys. 123, 103927.
3. DUNE Collaboration (2020). Deep Underground Neutrino Experiment Far Detector Technical Design Report.

---

**Date:** January 23, 2026  
**Signature:** Erick Francisco Pérez Eugenio  
**ORCID:** 0009-0006-3228-4847
