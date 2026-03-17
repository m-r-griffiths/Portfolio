# Detecting the anomalous activity of a ship’s engine

- **Context** This project was an assessed project that I completed as part of my course on Data Science, with Machine Learning and AI, at the University of Cambridgde
- **Problem**: Detect anomalous engine activity in order to reduce downtime and safety risk across a shipping fleet.
- **Data**: c.20_000 records, six feaures of engine status: `engine_rpm`, `oil_pressure`, `fuel_pressure`, `coolant_pressure`, `oil_temp`, `coolant_temp`.
- **Deliverables**: Collab notebook with analysis and figures, PDF report.

## Approach
- **EDA**: Missing data ID, distribution, boxplots.
- **Methods**: Inter-Quartile Range (IQR), One Class Support Vector Machine (OCSVM), Isolation Forest (IF)
- **Visualisation**: Principal Component Analysis (PCA)

## Key Results
- **OCSVM (best)**: `gamma=0.1`, `nu=0.03` → ~3% anomalies.
- **Isolation Forest (best)**: `contamination=0.03`, `n_estimators=20`, ~3.0% anomalies.
- **Insights**: A good overlap in the anomalies identified by the OCSVM and ISO methods - 306 records, or 1.57% of the total records. This could be reasonably treated as the priority anomalies to investigate.
