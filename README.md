# GDP Macroeconomic Decomposition & Time-Series Analytics Engine

A production-ready Python framework for modeling, aggregating, and analyzing macroeconomic Expenditure-Approach GDP datasets ($GDP = C + I + G + (X - M)$).

This project demonstrates core **Data Analysis**, **Economic Modeling**, and **Automated Data Visualization** capabilities built with Python's data science stack (`pandas`, `numpy`, `seaborn`, `matplotlib`).

---

## Key Analytical Skills Demonstrated

* **Multi-Dimensional Matrix Aggregation:** Transforming multi-category sub-component arrays into time-series DataFrames using `numpy.sum(axis=0)` and index mapping.
* **Economic Time-Series Analytics:** Calculating percentage shares of baseline metrics, YoY percentage growth rates (`pct_change()`), and component correlation matrices (`corr()`).
* **Automated Publication-Quality Data Visualization:** Dynamically generating 6 distinct statistical and analytical plots (Stackplots, Normalized Component Bars, YoY Rate Curves, Heatmaps, Trade Balance Fill Plots) and auto-exporting 300 DPI high-resolution PNGs.
* **Robust Automated Workflow:** Programmatic directory routing (`os.makedirs`), dynamic file paths, headless rendering (`plt.close()`), and formatted terminal logging.

---

## Project Structure & Visualization Output

When executed, the engine automatically populates a `/figures` directory with six analytical visual assets:

```
├── gdp_analysis.py          # Core processing script
└── figures/
    ├── 01_gdp_components_and_total_gdp.png   # Stacked area breakdown vs Total GDP line
    ├── 02_gdp_component_shares.png          # Normalized % share bar chart
    ├── 03_year_over_year_growth_rates.png  # YoY growth percentage trend lines
    ├── 04_gdp_correlation_heatmap.png       # Seaborn Pearson correlation matrix
    ├── 05_balance_of_trade.png              # Trade balance (X vs M) with net fill
    └── 06_gdp_component_comparison.png      # Clustered bar comparison across years

```

---

## Technical Stack

* **Language:** Python 3.x
* **Data Manipulation:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`
* **File & Environment Management:** `os`

---

## Scalability & Live Data Production Roadmap

While this module uses a localized dynamic array generation pipeline for simulation, the framework is architected to seamlessly interface with **live REST APIs and real-time data feeds**.

**Enterprise Integration Potential:**

1. **Live Macro Data API Pipelines:** Replace mock arrays with live automated queries fetching real data from APIs like **World Bank API (`wbgapi`)**, **FRED (Federal Reserve Economic Data)**, or **IMF Data Services**.
2. **Database Connectors:** Connect directly to PostgreSQL or BigQuery warehouses storing streaming market or trade data using `SQLAlchemy`.
3. **Automated BI Dashboards:** Modularize functions to power interactive Web Dashboards (Streamlit, Plotly Dash) or automated periodic PDF report generation.
