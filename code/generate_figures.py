#!/usr/bin/env python3
"""
================================================================================
FIGURES FOR PAPER 5: Flavor Mixing from Generation Hierarchy
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['figure.figsize'] = (10, 8)

# ============================================================================
# DATA
# ============================================================================

# Generation hierarchy
p = {1: 1, 2: 3, 3: 9}

# CKM predictions and observations
ckm_data = {
    'labels': [r'$\sin\theta_{12}$', r'$\sin\theta_{23}$', r'$\sin\theta_{13}$', r'$\sin\delta$'],
    'predicted': [38/169, 7/169, 8/2197, 10/11],
    'observed': [0.2243, 0.0422, 0.00369, 0.909],
    'errors': [0.0005, 0.0008, 0.00011, 0.02]
}

# PMNS predictions and observations
pmns_data = {
    'labels': [r'$\sin^2\theta_{12}$', r'$\sin^2\theta_{23}$', r'$\sin^2\theta_{13}$', r'$\sin\delta$'],
    'predicted': [4/13, 6/11, 48/2197, -10/13],
    'observed': [0.307, 0.546, 0.0220, -0.766],
    'errors': [0.013, 0.021, 0.0007, 0.05]
}

# ============================================================================
# FIGURE 1: Generation Hierarchy Diagram
# ============================================================================

def fig1_generation_hierarchy():
    """Diagram showing the generation rule p_i = 3^(i-1)."""
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Generation boxes
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    
    for i, (gen, power) in enumerate([(1, 1), (2, 3), (3, 9)]):
        x = i * 3
        
        # Box
        rect = mpatches.FancyBboxPatch((x, 2), 2, 2, 
                                        boxstyle="round,pad=0.1",
                                        facecolor=colors[i], 
                                        edgecolor='black',
                                        linewidth=2,
                                        alpha=0.8)
        ax.add_patch(rect)
        
        # Generation label
        ax.text(x + 1, 3.5, f'Gen {gen}', ha='center', va='center', 
                fontsize=14, fontweight='bold', color='white')
        
        # Power value
        ax.text(x + 1, 2.5, f'$p_{gen} = 3^{{{gen-1}}} = {power}$', 
                ha='center', va='center', fontsize=12, color='white')
    
    # Arrows between generations
    for i in range(2):
        ax.annotate('', xy=(i*3 + 2.2, 3), xytext=(i*3 + 2.8, 3),
                   arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    
    # Title and cluster info
    ax.text(3, 5.5, 'Generation Hierarchy Rule', ha='center', va='center',
            fontsize=16, fontweight='bold')
    ax.text(3, 4.8, r'$p_i = 3^{i-1}$ for generation $i = 1, 2, 3$', 
            ha='center', va='center', fontsize=13)
    
    # Cluster number box
    rect_cluster = mpatches.FancyBboxPatch((2, 0), 2, 1.2,
                                           boxstyle="round,pad=0.1",
                                           facecolor='#9b59b6',
                                           edgecolor='black',
                                           linewidth=2,
                                           alpha=0.8)
    ax.add_patch(rect_cluster)
    ax.text(3, 0.6, 'Cluster = 13', ha='center', va='center',
            fontsize=13, fontweight='bold', color='white')
    
    # Secondary cluster
    ax.text(3, -0.3, r'Secondary: $11 = 13 - 2$', ha='center', va='center',
            fontsize=11, style='italic')
    
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-1, 6.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig1_generation_hierarchy.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig1_generation_hierarchy.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Figure 1 saved: fig1_generation_hierarchy.png/pdf")


# ============================================================================
# FIGURE 2: CKM Comparison
# ============================================================================

def fig2_ckm_comparison():
    """Bar chart comparing CKM predictions vs observations."""
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    params = [
        (r'$\sin\theta_{12}$ (Cabibbo)', 38/169, 0.2243, 0.0005, '38/169'),
        (r'$\sin\theta_{23}$', 7/169, 0.0422, 0.0008, '7/169'),
        (r'$\sin\theta_{13}$', 8/2197, 0.00369, 0.00011, '8/2197'),
        (r'$\sin\delta$ (CP phase)', 10/11, 0.909, 0.02, '10/11')
    ]
    
    for idx, (ax, (name, pred, obs, err, formula)) in enumerate(zip(axes.flat, params)):
        x = [0, 1]
        values = [pred, obs]
        colors = ['#3498db', '#e74c3c']
        labels = ['Predicted', 'Observed']
        
        bars = ax.bar(x, values, color=colors, width=0.6, edgecolor='black', linewidth=1.5)
        
        # Error bar on observed
        ax.errorbar(1, obs, yerr=err, fmt='none', color='black', capsize=5, capthick=2, linewidth=2)
        
        # Percentage difference
        pct_diff = abs(pred - obs) / obs * 100
        
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.set_title(f'{name}\nFormula: {formula}', fontsize=13, fontweight='bold')
        
        # Add value annotations
        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax.annotate(f'{val:.4f}' if val > 0.01 else f'{val:.5f}',
                       xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, 3), textcoords='offset points',
                       ha='center', va='bottom', fontsize=10)
        
        # Add error percentage
        ax.text(0.5, 0.95, f'Error: {pct_diff:.2f}%', transform=ax.transAxes,
               ha='center', va='top', fontsize=11, 
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    fig.suptitle('CKM Matrix: Predicted vs Observed', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('fig2_ckm_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig2_ckm_comparison.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Figure 2 saved: fig2_ckm_comparison.png/pdf")


# ============================================================================
# FIGURE 3: PMNS Comparison
# ============================================================================

def fig3_pmns_comparison():
    """Bar chart comparing PMNS predictions vs observations."""
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    params = [
        (r'$\sin^2\theta_{12}$ (Solar)', 4/13, 0.307, 0.013, '4/13'),
        (r'$\sin^2\theta_{23}$ (Atmospheric)', 6/11, 0.546, 0.021, '6/11'),
        (r'$\sin^2\theta_{13}$ (Reactor)', 48/2197, 0.0220, 0.0007, '48/2197'),
        (r'$\sin\delta$ (CP phase)', -10/13, -0.766, 0.05, '-10/13')
    ]
    
    for idx, (ax, (name, pred, obs, err, formula)) in enumerate(zip(axes.flat, params)):
        x = [0, 1]
        values = [pred, obs]
        colors = ['#3498db', '#e74c3c']
        labels = ['Predicted', 'Observed']
        
        bars = ax.bar(x, values, color=colors, width=0.6, edgecolor='black', linewidth=1.5)
        
        # Error bar on observed
        ax.errorbar(1, obs, yerr=err, fmt='none', color='black', capsize=5, capthick=2, linewidth=2)
        
        # Percentage difference
        pct_diff = abs(pred - obs) / abs(obs) * 100
        
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.set_title(f'{name}\nFormula: {formula}', fontsize=13, fontweight='bold')
        
        # Add value annotations
        for bar, val in zip(bars, values):
            height = bar.get_height()
            offset = 3 if height >= 0 else -12
            va = 'bottom' if height >= 0 else 'top'
            ax.annotate(f'{val:.4f}' if abs(val) > 0.01 else f'{val:.5f}',
                       xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, offset), textcoords='offset points',
                       ha='center', va=va, fontsize=10)
        
        # Add error percentage
        ax.text(0.5, 0.95, f'Error: {pct_diff:.2f}%', transform=ax.transAxes,
               ha='center', va='top', fontsize=11,
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    fig.suptitle('PMNS Matrix: Predicted vs Observed', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('fig3_pmns_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig3_pmns_comparison.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Figure 3 saved: fig3_pmns_comparison.png/pdf")


# ============================================================================
# FIGURE 4: Summary - All Parameters
# ============================================================================

def fig4_summary():
    """Summary plot showing all 9 parameters and their errors."""
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # All parameters
    parameters = [
        # CKM
        ('CKM θ₁₂', 38/169, 0.2243, 0.0005),
        ('CKM θ₂₃', 7/169, 0.0422, 0.0008),
        ('CKM θ₁₃', 8/2197, 0.00369, 0.00011),
        ('CKM δ', 10/11, 0.909, 0.02),
        # PMNS
        ('PMNS θ₁₂', 4/13, 0.307, 0.013),
        ('PMNS θ₂₃', 6/11, 0.546, 0.021),
        ('PMNS θ₁₃', 48/2197, 0.0220, 0.0007),
        ('PMNS δ', -10/13, -0.766, 0.05),
        # Weinberg
        ('Weinberg', 3/13, 0.23121, 0.00004),
    ]
    
    names = [p[0] for p in parameters]
    errors_pct = [abs(p[1] - p[2]) / abs(p[2]) * 100 for p in parameters]
    
    # Colors by category
    colors = ['#3498db']*4 + ['#e74c3c']*4 + ['#2ecc71']
    
    y_pos = np.arange(len(names))
    bars = ax.barh(y_pos, errors_pct, color=colors, edgecolor='black', linewidth=1.5, height=0.7)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=12)
    ax.set_xlabel('Deviation from Observed (%)', fontsize=13)
    ax.set_title('Generation Hierarchy Predictions vs PDG 2024 Values', 
                fontsize=15, fontweight='bold')
    
    # Add percentage labels
    for bar, pct in zip(bars, errors_pct):
        width = bar.get_width()
        ax.annotate(f'{pct:.2f}%',
                   xy=(width, bar.get_y() + bar.get_height()/2),
                   xytext=(5, 0), textcoords='offset points',
                   ha='left', va='center', fontsize=11, fontweight='bold')
    
    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#3498db', edgecolor='black', label='CKM (Quarks)'),
        mpatches.Patch(facecolor='#e74c3c', edgecolor='black', label='PMNS (Leptons)'),
        mpatches.Patch(facecolor='#2ecc71', edgecolor='black', label='Electroweak')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=11)
    
    # Add vertical line at 1% and 2%
    ax.axvline(x=1, color='gray', linestyle='--', alpha=0.7, label='1%')
    ax.axvline(x=2, color='gray', linestyle=':', alpha=0.7, label='2%')
    
    ax.set_xlim(0, max(errors_pct) * 1.3)
    ax.invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('fig4_summary.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig4_summary.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Figure 4 saved: fig4_summary.png/pdf")


# ============================================================================
# FIGURE 5: Cross-Relations
# ============================================================================

def fig5_cross_relations():
    """Diagram showing the cross-relations between CKM and PMNS."""
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # CKM box
    ckm_rect = mpatches.FancyBboxPatch((0.5, 4), 4, 3,
                                        boxstyle="round,pad=0.2",
                                        facecolor='#3498db',
                                        edgecolor='black',
                                        linewidth=2,
                                        alpha=0.3)
    ax.add_patch(ckm_rect)
    ax.text(2.5, 6.5, 'CKM (Quarks)', ha='center', va='center',
            fontsize=14, fontweight='bold')
    ax.text(2.5, 5.5, r'$\sin\theta_{13} = 8/13^3$', ha='center', va='center', fontsize=12)
    ax.text(2.5, 4.8, r'$\sin\delta = +10/11$', ha='center', va='center', fontsize=12)
    
    # PMNS box
    pmns_rect = mpatches.FancyBboxPatch((6.5, 4), 4, 3,
                                         boxstyle="round,pad=0.2",
                                         facecolor='#e74c3c',
                                         edgecolor='black',
                                         linewidth=2,
                                         alpha=0.3)
    ax.add_patch(pmns_rect)
    ax.text(8.5, 6.5, 'PMNS (Leptons)', ha='center', va='center',
            fontsize=14, fontweight='bold')
    ax.text(8.5, 5.5, r'$\sin^2\theta_{13} = 48/13^3$', ha='center', va='center', fontsize=12)
    ax.text(8.5, 4.8, r'$\sin\delta = -10/13$', ha='center', va='center', fontsize=12)
    
    # Arrow for θ₁₃ relation
    ax.annotate('', xy=(6.3, 5.5), xytext=(4.7, 5.5),
               arrowprops=dict(arrowstyle='<->', lw=2, color='purple'))
    ax.text(5.5, 5.8, r'$\times 6$', ha='center', va='center',
            fontsize=14, fontweight='bold', color='purple')
    ax.text(5.5, 5.2, r'$48/8 = 6$', ha='center', va='center',
            fontsize=11, color='purple')
    
    # Arrow for δ relation
    ax.annotate('', xy=(6.3, 4.8), xytext=(4.7, 4.8),
               arrowprops=dict(arrowstyle='<->', lw=2, color='darkgreen'))
    ax.text(5.5, 4.5, 'Same numerator: 10', ha='center', va='center',
            fontsize=11, color='darkgreen')
    ax.text(5.5, 4.1, 'Opposite signs', ha='center', va='center',
            fontsize=11, color='darkgreen', style='italic')
    
    # Common origin box
    origin_rect = mpatches.FancyBboxPatch((3, 0.5), 5, 2,
                                           boxstyle="round,pad=0.2",
                                           facecolor='#9b59b6',
                                           edgecolor='black',
                                           linewidth=2,
                                           alpha=0.3)
    ax.add_patch(origin_rect)
    ax.text(5.5, 2, 'Common Origin', ha='center', va='center',
            fontsize=14, fontweight='bold')
    ax.text(5.5, 1.3, r'$p_i = 3^{i-1}$, Cluster = 13', ha='center', va='center',
            fontsize=12)
    ax.text(5.5, 0.8, 'Numerator 10 = 13 - 3', ha='center', va='center',
            fontsize=11, style='italic')
    
    # Arrows from origin to matrices
    ax.annotate('', xy=(2.5, 3.9), xytext=(4.5, 2.6),
               arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    ax.annotate('', xy=(8.5, 3.9), xytext=(6.5, 2.6),
               arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Cross-Relations Between CKM and PMNS Matrices', 
                fontsize=16, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig('fig5_cross_relations.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig5_cross_relations.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Figure 5 saved: fig5_cross_relations.png/pdf")


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Generate all figures."""
    print("\n" + "="*60)
    print("Generating figures for Paper 5...")
    print("="*60 + "\n")
    
    fig1_generation_hierarchy()
    fig2_ckm_comparison()
    fig3_pmns_comparison()
    fig4_summary()
    fig5_cross_relations()
    
    print("\n" + "="*60)
    print("All figures generated successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
