# Air Quality & Public Health Risk Forecasting

![Ozone Time Series](results/figures/ozone_time_series.png)

## Overview
Air pollution is one of the most critical environmental determinants of public health. Exposure to elevated ozone levels has been consistently linked to respiratory and cardiovascular diseases. This project develops a **research-oriented forecasting framework** to analyze air quality dynamics and identify **early-warning signals** for high-risk regions.

The repository is intentionally structured as an **academic research baseline**, suitable for collaboration with faculty members and further extension into peer-reviewed work.

---

## Research Motivation
Most air quality monitoring systems are reactive, detecting harmful pollution levels only after they occur. This project aims to move toward a **predictive and interpretable framework** by:

- Forecasting air quality risk using historical pollution data  
- Identifying counties with persistent high-risk exposure  
- Supporting early-warning indicators for preventive policy actions  
- Providing a foundation for linking pollution dynamics with health outcomes  

---

## Key Research Questions
1. Can counties with persistent high pollution risk be predicted years in advance?  
2. How do temporal pollution patterns differ between urban and rural regions?  
3. Are regulatory effects uniformly distributed across U.S. states?  
4. Can rolling statistics define effective early-warning thresholds?  
5. How does air quality volatility relate to long-term public health outcomes?  

---

## Data Source
- **Primary dataset:** EPA Air Quality System (AQS)  
- **Spatial resolution:** County-level  
- **Temporal resolution:** Annual  
- **Primary focus:** Ozone-related air quality indicators  

Raw EPA data are not included in this repository due to size and reproducibility constraints.  
The project instead emphasizes **processed datasets, feature engineering logic, and modeling pipelines** to ensure transparency and reproducibility.

---

## Methodological Framework
The project follows a structured and reproducible research pipeline:

### 1. Exploratory Data Analysis
- Long-term national pollution trends  
- Geographic variability across states and counties  
- Identification of high-risk regions and temporal persistence  

### 2. Feature Engineering
- Lagged pollution indicators  
- Rolling statistics as early-warning signals  
- Normalized temporal representations  

### 3. Baseline Modeling
- Interpretable regression-based approaches  
- Tree-based ensemble models for nonlinear patterns  
- Emphasis on transparency and analytical clarity  

### 4. Spatiotemporal Foundations
- Analysis of temporal dependence  
- Preparation for spatial and policy-oriented extensions  

---

## Urban vs Rural Pollution Patterns
![Urban vs Rural Comparison](results/figures/urban_rural_comparison.png)

Preliminary exploratory analysis suggests systematic differences in ozone dynamics between urban and rural counties, motivating further stratified modeling and causal investigation.

---

## Baseline Forecasting Performance
![Predicted vs Observed](results/figures/predicted_vs_observed.png)

Baseline forecasting results indicate that lagged values and rolling statistics capture strong temporal dependencies in ozone exceedance, supporting their use in early-warning systems without excessive model complexity.

---

## Project Structure
air-quality-health-risk-forecasting/
│
├── data/ # raw, processed, external (future)
├── notebooks/ # EDA, feature engineering, baseline models
├── src/ # reusable data, feature, and modeling code
├── results/
│ └── figures/ # research visualizations
├── experiments/ # experiment logs (future extensions)
├── research/ # abstract drafts and literature notes
└── README.md


---

## Research Status
This repository represents a **research-ready baseline**, designed to:

- Support academic collaboration  
- Enable integration with health and meteorological datasets  
- Serve as a foundation for journal or conference submissions  

The emphasis is placed on **methodological rigor, interpretability, and reproducibility**, rather than premature optimization.

---

## Future Work
- Integration with health outcome datasets (e.g., hospital admissions, mortality)  
- Causal evaluation of environmental and regulatory interventions  
- Advanced spatiotemporal modeling (Bayesian, hierarchical, or graph-based approaches)  
- Validation of early-warning thresholds for public health decision-making  

---

## Reproducibility Note
Raw and processed datasets are excluded from this repository due to size constraints.
All data preprocessing steps, feature engineering logic, and modeling pipelines
are fully documented and reproducible.

## Author
**Mariam Zakaria**  
Machine Learning & Data Science  

Research interests:
- Interpretable machine learning  
- Environmental risk modeling  
- Public health analytics  
