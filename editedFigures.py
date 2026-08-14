import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================
# SETTINGS
# ============================================================

# Expand display to show all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 200)

# Define the period of interest
years = list(range(1990, 2001))
num_years = len(years)

# Create a folder called "figures" in the same directory
# as this Python file.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(SCRIPT_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)


# ============================================================
# CONSUMPTION (C)
# ============================================================

C_categories = [
    "Durable Goods: New Vehicles",
    "Durable Goods: Furniture & Appliances",
    "Durable Goods: Recreational Goods",
    "Nondurable Goods: Food & Beverages (at home)",
    "Nondurable Goods: Clothing & Footwear",
    "Nondurable Goods: Gasoline & Energy",
    "Services: Housing & Utilities",
    "Services: Healthcare (incl. medical services & drugs)",
    "Services: Transportation (fares, car rentals)",
    "Services: Food Services & Accommodation",
    "Services: Recreation & Culture",
    "Services: Financial & Insurance",
    "Services: Education"
]

C = np.array([
    np.random.randint(150, 200, num_years),
    np.random.randint(100, 140, num_years),
    np.random.randint(80, 120, num_years),
    np.random.randint(400, 500, num_years),
    np.random.randint(120, 180, num_years),
    np.random.randint(70, 100, num_years),
    np.random.randint(500, 600, num_years),
    np.random.randint(300, 400, num_years),
    np.random.randint(90, 130, num_years),
    np.random.randint(250, 350, num_years),
    np.random.randint(100, 150, num_years),
    np.random.randint(60, 90, num_years),
    np.random.randint(80, 110, num_years)
])


# ============================================================
# INVESTMENT (I)
# ============================================================

I_categories = [
    "Expat remitances: Social ROI",
    "Nonresidential Structures: Commercial Buildings",
    "Nonresidential Structures: Industrial Buildings",
    "Nonresidential Structures: Other (e.g., oil & gas)",
    "Nonresidential Equipment: Industrial Machinery",
    "Nonresidential Equipment: Information Processing Equip.",
    "Nonresidential Equipment: Transportation Equipment",
    "Intellectual Property Products: Software",
    "Intellectual Property Products: Research & Development",
    "Residential Investment: Single-Family Housing",
    "Residential Investment: Multi-Family Housing",
    "Residential Investment: Improvements",
    "Change in Private Inventories: Manufacturing",
    "Change in Private Inventories: Wholesale/Retail Trade"
]

I = np.array([
    np.random.randint(8, 9, num_years),
    np.random.randint(50, 80, num_years),
    np.random.randint(40, 70, num_years),
    np.random.randint(20, 50, num_years),
    np.random.randint(100, 150, num_years),
    np.random.randint(120, 180, num_years),
    np.random.randint(60, 90, num_years),
    np.random.randint(30, 60, num_years),
    np.random.randint(40, 70, num_years),
    np.random.randint(150, 200, num_years),
    np.random.randint(50, 80, num_years),
    np.random.randint(30, 60, num_years),
    np.random.randint(-10, 30, num_years),
    np.random.randint(-5, 20, num_years)
])


# ============================================================
# GOVERNMENT SPENDING (G)
# ============================================================

G_categories = [
    "Defense: Military Personnel Compensation",
    "Defense: Weapons & Equipment",
    "Defense: Operations & Maintenance",
    "Nondefense: Government Administration (Salaries)",
    "Nondefense: Healthcare Administration",
    "Nondefense: Education Spending (public schools)",
    "Nondefense: Public Safety (Police, Fire)",
    "Nondefense: Transportation Infrastructure",
    "Nondefense: Environmental Protection",
    "Nondefense: Scientific Research",
    "Nondefense: Public Hospitals & Health Programs"
]

G = np.array([
    np.random.randint(100, 150, num_years),
    np.random.randint(80, 120, num_years),
    np.random.randint(70, 110, num_years),
    np.random.randint(120, 180, num_years),
    np.random.randint(40, 70, num_years),
    np.random.randint(150, 200, num_years),
    np.random.randint(90, 130, num_years),
    np.random.randint(60, 100, num_years),
    np.random.randint(20, 40, num_years),
    np.random.randint(30, 60, num_years),
    np.random.randint(50, 90, num_years)
])


# ============================================================
# EXPORTS (X)
# ============================================================

X_categories = [
    "Goods Exports: Agricultural Products",
    "Goods Exports: Machinery & Equipment",
    "Goods Exports: Automotive Products",
    "Goods Exports: Chemicals",
    "Goods Exports: Electronics",
    "Services Exports: Travel (Tourism)",
    "Services Exports: Transportation",
    "Services Exports: Financial Services",
    "Services Exports: Intellectual Property Charges",
    "Services Exports: Computer & Information Services",
    "Services Exports: Other Business Services"
]

X = np.array([
    np.random.randint(50, 80, num_years),
    np.random.randint(90, 130, num_years),
    np.random.randint(70, 100, num_years),
    np.random.randint(60, 90, num_years),
    np.random.randint(80, 120, num_years),
    np.random.randint(40, 70, num_years),
    np.random.randint(30, 50, num_years),
    np.random.randint(20, 40, num_years),
    np.random.randint(15, 30, num_years),
    np.random.randint(25, 45, num_years),
    np.random.randint(35, 60, num_years)
])


# ============================================================
# IMPORTS (M)
# ============================================================

M_categories = [
    "Goods Imports: Crude Oil & Petroleum Products",
    "Goods Imports: Manufactured Consumer Goods",
    "Goods Imports: Industrial Supplies & Materials",
    "Goods Imports: Automotive Products",
    "Goods Imports: Capital Goods (Machinery)",
    "Services Imports: Travel (Domestic residents abroad)",
    "Services Imports: Transportation",
    "Services Imports: Financial Services",
    "Services Imports: Intellectual Property Charges",
    "Services Imports: Computer & Information Services",
    "Services Imports: Other Business Services"
]

M = np.array([
    np.random.randint(80, 120, num_years),
    np.random.randint(150, 200, num_years),
    np.random.randint(100, 140, num_years),
    np.random.randint(90, 130, num_years),
    np.random.randint(70, 110, num_years),
    np.random.randint(50, 80, num_years),
    np.random.randint(35, 60, num_years),
    np.random.randint(25, 45, num_years),
    np.random.randint(20, 35, num_years),
    np.random.randint(30, 50, num_years),
    np.random.randint(40, 70, num_years)
])


# ============================================================
# NET EXPORTS & GDP
# ============================================================

NX = X.sum(axis=0) - M.sum(axis=0)

GDP = (
    C.sum(axis=0)
    + I.sum(axis=0)
    + G.sum(axis=0)
    + NX
)


# ============================================================
# DATAFRAMES
# ============================================================

df_C_detail = pd.DataFrame(
    C,
    index=C_categories,
    columns=years
)

df_I_detail = pd.DataFrame(
    I,
    index=I_categories,
    columns=years
)

df_G_detail = pd.DataFrame(
    G,
    index=G_categories,
    columns=years
)

df_X_detail = pd.DataFrame(
    X,
    index=X_categories,
    columns=years
)

df_M_detail = pd.DataFrame(
    M,
    index=M_categories,
    columns=years
)


gdp_summary_df = pd.DataFrame({
    'Year': years,
    'Consumption (C)': C.sum(axis=0),
    'Investment (I)': I.sum(axis=0),
    'Government Spending (G)': G.sum(axis=0),
    'Exports (X)': X.sum(axis=0),
    'Imports (M)': M.sum(axis=0),
    'Net Exports (X-M)': NX,
    'GDP': GDP
}).set_index('Year')


# ============================================================
# TERMINAL OUTPUT
# ============================================================

print("--- GDP Summary (Values in Hypothetical Units) ---")
print(gdp_summary_df)

print("\n--- Detailed Consumption (C) Data ---")
print(df_C_detail)

print("\n--- Detailed Investment (I) Data ---")
print(df_I_detail)

print("\n--- Detailed Government Spending (G) Data ---")
print(df_G_detail)

print("\n--- Detailed Exports (X) Data ---")
print(df_X_detail)

print("\n--- Detailed Imports (M) Data ---")
print(df_M_detail)


# ============================================================
# FIGURE 1 — GDP COMPONENTS AND TOTAL GDP
# ============================================================

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(
    years,
    gdp_summary_df['Consumption (C)'],
    gdp_summary_df['Investment (I)'],
    gdp_summary_df['Government Spending (G)'],
    gdp_summary_df['Net Exports (X-M)'],
    labels=[
        'Consumption (C)',
        'Investment (I)',
        'Government Spending (G)',
        'Net Exports (X-M)'
    ],
    colors=[
        '#1f77b4',
        '#ff7f0e',
        '#9467bd',
        '#2ca02c'
    ],
    alpha=0.8
)

ax.plot(
    years,
    gdp_summary_df['GDP'],
    color='black',
    linewidth=2.5,
    marker='o',
    label='Total GDP'
)

ax.set_title("GDP Components and Total GDP (1990–2000)")
ax.set_xlabel("Year")
ax.set_ylabel("Value (Hypothetical Units)")
ax.legend(
    loc='upper left',
    bbox_to_anchor=(1.02, 1),
    title="Components"
)
ax.grid(alpha=0.3)

fig.tight_layout()

fig.savefig(
    os.path.join(FIGURES_DIR, "01_gdp_components_and_total_gdp.png"),
    dpi=300,
    bbox_inches='tight'
)

plt.close(fig)


# ============================================================
# FIGURE 2 — PERCENTAGE CONTRIBUTION
# ============================================================

component_shares = (
    gdp_summary_df[
        [
            'Consumption (C)',
            'Investment (I)',
            'Government Spending (G)',
            'Net Exports (X-M)'
        ]
    ]
    .div(gdp_summary_df['GDP'], axis=0)
    * 100
)

fig, ax = plt.subplots(figsize=(12, 7))

component_shares.plot(
    kind='bar',
    stacked=True,
    colormap='tab20',
    alpha=0.85,
    ax=ax
)

ax.set_title("GDP Component Shares (% of GDP)")
ax.set_xlabel("Year")
ax.set_ylabel("Percentage Contribution")
ax.legend(
    loc='upper left',
    bbox_to_anchor=(1.02, 1),
    title="Components"
)

fig.tight_layout()

fig.savefig(
    os.path.join(FIGURES_DIR, "02_gdp_component_shares.png"),
    dpi=300,
    bbox_inches='tight'
)

plt.close(fig)


# ============================================================
# FIGURE 3 — GROWTH RATES
# ============================================================

growth_rates = gdp_summary_df.pct_change() * 100

fig, ax = plt.subplots(figsize=(12, 7))

for col in [
    'GDP',
    'Consumption (C)',
    'Investment (I)',
    'Government Spending (G)',
    'Net Exports (X-M)'
]:
    ax.plot(
        growth_rates.index,
        growth_rates[col],
        marker='o',
        label=col
    )

ax.set_title("Year-over-Year Growth Rates (%)")
ax.set_xlabel("Year")
ax.set_ylabel("Growth Rate (%)")
ax.legend(
    loc='upper left',
    bbox_to_anchor=(1.02, 1)
)
ax.grid(alpha=0.3)

fig.tight_layout()

fig.savefig(
    os.path.join(FIGURES_DIR, "03_year_over_year_growth_rates.png"),
    dpi=300,
    bbox_inches='tight'
)

plt.close(fig)


# ============================================================
# FIGURE 4 — CORRELATION HEATMAP
# ============================================================

fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(
    gdp_summary_df.corr(),
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    ax=ax
)

ax.set_title("Correlation Between GDP Components")

fig.tight_layout()

fig.savefig(
    os.path.join(FIGURES_DIR, "04_gdp_correlation_heatmap.png"),
    dpi=300,
    bbox_inches='tight'
)

plt.close(fig)


# ============================================================
# FIGURE 5 — BALANCE OF TRADE
# ============================================================

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(
    years,
    gdp_summary_df['Exports (X)'],
    label='Exports',
    color='green',
    marker='o'
)

ax.plot(
    years,
    gdp_summary_df['Imports (M)'],
    label='Imports',
    color='red',
    marker='o'
)

ax.fill_between(
    years,
    gdp_summary_df['Net Exports (X-M)'],
    0,
    alpha=0.2,
    color='blue',
    label='Net Exports'
)

ax.axhline(
    0,
    color='black',
    linewidth=0.8
)

ax.set_title("Balance of Trade (Exports vs Imports)")
ax.set_xlabel("Year")
ax.set_ylabel("Value (Hypothetical Units)")
ax.legend(loc='upper left')
ax.grid(alpha=0.3)

fig.tight_layout()

fig.savefig(
    os.path.join(FIGURES_DIR, "05_balance_of_trade.png"),
    dpi=300,
    bbox_inches='tight'
)

plt.close(fig)


# ============================================================
# FIGURE 6 — GDP COMPONENT COMPARISON
# ============================================================

fig, ax = plt.subplots(figsize=(12, 7))

gdp_summary_df[
    [
        'Consumption (C)',
        'Investment (I)',
        'Government Spending (G)',
        'Net Exports (X-M)'
    ]
].plot(
    kind='bar',
    ax=ax
)

ax.set_title("GDP Component Comparison by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Value (Hypothetical Units)")
ax.legend(
    loc='upper left',
    bbox_to_anchor=(1.02, 1),
    title="Components"
)

fig.tight_layout()

fig.savefig(
    os.path.join(FIGURES_DIR, "06_gdp_component_comparison.png"),
    dpi=300,
    bbox_inches='tight'
)

plt.close(fig)


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("ALL FIGURES HAVE BEEN SAVED SUCCESSFULLY.")
print("=" * 60)
print(f"Figure directory:")
print(FIGURES_DIR)

print("\nSaved files:")

for filename in sorted(os.listdir(FIGURES_DIR)):
    if filename.endswith(".png"):
        print(f"  - {filename}")

print("=" * 60)