# Flavor Mixing Parameters from Generation Hierarchy

## An Empirical Observation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18347004.svg)](https://doi.org/10.5281/zenodo.18347004)
[![OSF](https://img.shields.io/badge/OSF-Pre--registered-blue)](https://doi.org/10.17605/OSF.IO/ZAHBN)

---

## IMPORTANT DISCLAIMER

**This repository documents an empirical observation, NOT a fundamental theory.**

The patterns described here are **phenomenological regularities** that may or may not reflect deeper physics. No claim is made that these formulas are derived from first principles.

**If future precision measurements (JUNO, DUNE, or others) significantly deviate from these predictions, this hypothesis must be discarded.**

---

## Summary

We observe that the flavor mixing parameters of the Standard Model (CKM and PMNS matrices, plus the Weinberg angle) can be expressed using simple fractions involving only three numbers:

- **3** = number of generations
- **11** = 13 - 2
- **13** = 1 + 12 (number of gauge bosons in the Standard Model)

The generation hierarchy follows the rule: **p_i = 3^(i-1)** for generation i = 1, 2, 3.

| Generation | Value |
|------------|-------|
| p1 | 3^0 = 1 |
| p2 | 3^1 = 3 |
| p3 | 3^2 = 9 |

---

## Results

### CKM Matrix (Quarks)

| Parameter | Formula | Predicted | Observed (PDG 2024) | Error |
|-----------|---------|-----------|---------------------|-------|
| sin theta_12 | 38/169 | 0.2249 | 0.2243 ± 0.0005 | 0.25% |
| sin theta_23 | 7/169 | 0.0414 | 0.0422 ± 0.0008 | 1.85% |
| sin theta_13 | 8/2197 | 0.00364 | 0.00369 ± 0.00011 | 1.32% |
| sin delta | 10/11 | 0.9091 | 0.909 ± 0.02 | 0.03% |

### PMNS Matrix (Leptons)

| Parameter | Formula | Predicted | Observed (PDG 2024) | Error |
|-----------|---------|-----------|---------------------|-------|
| sin^2 theta_12 | 4/13 | 0.3077 | 0.307 ± 0.013 | 0.23% |
| sin^2 theta_23 | 6/11 | 0.5455 | 0.546 ± 0.021 | 0.10% |
| sin^2 theta_13 | 48/2197 | 0.0218 | 0.0220 ± 0.0007 | 0.69% |
| sin delta | -10/13 | -0.7692 | -0.766 ± 0.05 | 0.42% |

### Weinberg Angle

| Parameter | Formula | Predicted | Observed | Error |
|-----------|---------|-----------|----------|-------|
| sin^2 theta_W | 3/13 | 0.2308 | 0.23121 ± 0.00004 | 0.19% |

**Note:** The Weinberg angle prediction deviates by ~11σ from the measured value at M_Z. This tension requires explanation; one possibility is that 3/13 corresponds to a high-energy value before RG running.

---

## Cross-Relations

A striking relationship between the quark and lepton sectors:

```
sin^2(theta_13)_PMNS = 6 × sin(theta_13)_CKM

48/13^3 = 6 × 8/13^3
```

Both CP-violating phases share the numerator **10 = 13 - 3**:
- CKM: sin delta = +10/11
- PMNS: sin delta = -10/13

---

## Falsifiability

This hypothesis makes specific, testable predictions:

### JUNO Experiment (~2027)
- **Prediction:** sin^2(theta_12) = 4/13 = 0.30769...
- **Current:** 0.307 ± 0.013
- **JUNO precision:** ±0.003
- **Falsifiable if:** JUNO measures value outside 0.298 – 0.317 at 3σ

### DUNE Experiment (~2029+)
- **Prediction:** sin(delta_PMNS) = -10/13 = -0.7692...
- **Current:** -0.766 ± 0.05
- **DUNE precision:** ±0.02
- **Falsifiable if:** DUNE measures sin(delta) outside -0.83 to -0.71 at 3σ

### Pre-registration
These predictions are pre-registered at OSF: [10.17605/OSF.IO/ZAHBN](https://doi.org/10.17605/OSF.IO/ZAHBN)

---

## What This Is NOT

1. **NOT a derivation from first principles** — We observe patterns, we don't explain them
2. **NOT a complete theory** — No mechanism is proposed for WHY these patterns exist
3. **NOT numerology-proof** — While we use only 3, 11, 13 (numbers with gauge significance), the risk of overfitting remains
4. **NOT a claim of new physics** — These are Standard Model parameters expressed differently

---

## What This IS

1. **An empirical observation** of regularities in flavor mixing parameters
2. **A falsifiable hypothesis** testable by upcoming experiments
3. **An invitation** for theorists to find (or disprove) an underlying mechanism
4. **Reproducible** — All code and data are provided

---

## Repository Structure

```
generation-hierarchy-flavor/
├── README.md
├── LICENSE
├── CITATION.cff
├── OSF_PREREGISTRATION.md
├── code/
│   ├── flavor_mixing_v1.py
│   └── generate_figures.py
├── data/
│   └── results.json
└── figures/
    ├── fig1_generation_hierarchy.png
    ├── fig2_ckm_comparison.png
    ├── fig3_pmns_comparison.png
    ├── fig4_summary.png
    └── fig5_cross_relations.png
```

---

## Usage

```bash
git clone https://github.com/AsesorErick/generation-hierarchy-flavor.git
cd generation-hierarchy-flavor

python code/flavor_mixing_v1.py
python code/generate_figures.py
```

Requirements: Python 3.8+, NumPy, Matplotlib

---

## Author

**Erick Francisco Pérez Eugenio**
- ORCID: [0009-0006-3228-4847](https://orcid.org/0009-0006-3228-4847)

---

## License

MIT License

---

## Citation

```bibtex
@software{perez_flavor_2026,
  author = {Pérez Eugenio, Erick Francisco},
  title = {Flavor Mixing Parameters from Generation Hierarchy: An Empirical Observation},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18347004}
}
```
