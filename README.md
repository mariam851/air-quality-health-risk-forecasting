# Air Quality & Public Health Risk Forecasting 
**An Interpretable Research Framework for Early-Warning Pollution Signals**

![National Trends](results/figures/National%20Average%20Ozone%20Exceedance%20Over%20Time.png)

## Overview
Air pollution is one of the most critical environmental determinants of public health. Exposure to elevated ozone levels has been consistently linked to respiratory and cardiovascular diseases. This project develops a **research-oriented forecasting framework** to analyze air quality dynamics and identify **early-warning signals** for high-risk regions.

The repository is structured as an **academic research baseline**, emphasizing methodological rigor, interpretability, and reproducibility.

---

## Key Research Questions
1. **Predictive Persistence:** Can counties with chronic high-pollution risk be forecasted years in advance?
2. **Geographic Heterogeneity:** How do temporal pollution patterns differ between industrial urban centers and rural regions?
3. **Policy Evaluation:** Are regulatory effects (e.g., Clean Air Act) uniformly distributed across U.S. states?
4. **Threshold Identification:** Can rolling statistics define effective early-warning thresholds for public health?
5. **Health Linkage:** How does air quality volatility relate to long-term public health outcomes?

---

## Exploratory Insights & Trends
Our analysis reveals significant geographic variability. While national averages show general trends, specific "hotspots" require localized attention.

![State Trends](results/figures/Air%20Quaility%20Trends%20Over%20Time%20(Selected%20States).png)
*Figure 1: Comparative analysis of ozone trends across high-impact states.*

![High Risk States](results/figures/Top%2010%20States%20by%20High-Risk%20Frequency.png)
*Figure 2: Statistical frequency of counties exceeding safety thresholds per state.*

---

## Methodological Framework
### 1. Feature Engineering (Signal Extraction)
We focus on extracting temporal signals that act as early-warning indicators:
- **Lagged Indicators:** Capturing historical pollution "memory".
- **Rolling Statistics:** Using 3-year windows to smooth volatility and detect emerging trends.
- **Normalized Temporal Representations:** Accounting for long-term shifts.

![Rolling Mean](results/figures/3-Year%20Rolling%20Mean%20vs%20Actual%20Value.png)
*Figure 3: 3-year rolling average vs. actual fluctuations.*

### 2. Modeling Strategy
We employ a tiered modeling approach to ensure analytical clarity:
* **Baseline Forecasting:** A persistence model ($Value_{t} = Value_{t-1}$) to establish a reference point.
* **Machine Learning:** Using Random Forest to capture non-linear spatiotemporal patterns.

---

## Performance Benchmarking
Our Machine Learning approach significantly outperforms the baseline, proving the value of engineered features.

| Model | MAE (Error in Days) | R² Score | Status |
| :--- | :--- | :--- | :--- |
| **Baseline (Naive)** | **8.47 Days** | -0.1593 | Reference |
| **Random Forest** | **2.17 Days** | **0.6098** | **Best Performer** |

![Persistence Comparison](results/figures/Actual%20vs.%20Persistence.png)
*Figure 4: Visualizing the baseline model's limitations.*

![Final Prediction](results/figures/Predicted%20vs.%20Observed%20(Ozone%20Days).png)
*Figure 5: High correlation achieved by the Random Forest model.*

---

Future Work
Health Integration: Linking pollution forecasts with hospital admission rates.

Causal Evaluation: Analyzing the impact of specific regulatory interventions.

Advanced Modeling: Exploring spatiotemporal Graph Neural Networks (GNNs).

Author
Mariam Zakaria Machine Learning & Data Science Researcher Research interests: Interpretable ML, Environmental Risk Modeling, Public Health Analytics.

## Project Structure
```text
air-quality-health-risk-forecasting/
├── data/                 # Data documentation (Raw data excluded for size)
├── notebooks/           # EDA, Feature Engineering, and Modeling logic
├── src/                 # Reusable Python scripts for the pipeline
├── results/figures/     # Research visualizations
├── research/            # Literature notes and abstract drafts
└── README.md            # Research documentation
