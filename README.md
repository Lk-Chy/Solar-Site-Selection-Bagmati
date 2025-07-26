# ☀️ GIS-Based AHP for Optimal Solar Plant Site Selection in Bagmati Province, Nepal

This project applies a GIS-based **Analytical Hierarchy Process (AHP)** to identify optimal locations for **solar power plant installation** in **Bagmati Province, Nepal**. It integrates multiple spatial and climatic datasets to produce a **solar site suitability map** through **multi-criteria decision analysis (MCDA)**.

---

## 📌 Abstract

With the rising demand for energy and the need for clean, renewable sources, this study explores **solar photovoltaic (PV)** potential using **GIS** and **AHP**. It classifies the province's land based on environmental, economic, and climatic suitability. Out of the total area, **10.41%** was found to be ‘most suitable’ and **49.33%** as ‘suitable’ for solar plant development.

---

## 📍 Study Area

- **Region:** Bagmati Province, Nepal  
- **Coordinates:** ~83°55′E to 86°34′E and 26°55′N to 28°23′N  
- **Topography:** Terai to High Himalayas  
- **Sunshine Availability:** ~300 sunny days/year

---

## 🧪 Methodology Overview

The suitability analysis was conducted using:

1. **Data Preprocessing:** All layers were projected to UTM 45N and resampled to 30m resolution.
2. **Reclassification:** Raster layers reclassified based on suitability (1 = Most Suitable, 4 = Unsuitable).
3. **AHP Analysis:** Pairwise comparisons to assign weights to each criterion.
4. **Weighted Overlay:** Final suitability map computed using raster algebra in GIS.
5. **Exclusion Zones:** Removed areas like forests, water bodies, high slopes, and national parks.
6. **Sensitivity Analysis:** Checked model robustness by altering weights.

---

## 🎯 Criteria Used

| Category     | Criteria                             |
|--------------|--------------------------------------|
| Climatic     | Solar Irradiance (GHI), Temperature  |
| Economic     | Distance to Roads, Substations       |
| Environmental| Elevation, Slope, Aspect, LULC       |

> Weighting based on AHP matrix (highest: GHI – 28.02%)

---

## 📊 Results Summary

- **Most Suitable:** 2,111 km² (10.41%)
- **Suitable:** 10,004 km² (49.33%)
- **Validation:** 83% of existing solar farms fall in "most suitable" or "suitable" zones.
- **Sensitivity:** Model stable under ±5% weight variation

---

## 🧠 Tools & Technologies

- **GIS Software:** QGIS / ArcGIS
- **Programming:** Python (RasterIO, NumPy)
- **Data Analysis:** AHP (Saaty’s method), Sensitivity Analysis
- **Raster Data Processing:** DEM, LULC, GHI, etc.

---

## 📂 Project Structure

```
SOLAR-SITE-SELECTION-BAGMATI/
│
├── data/ # Contains raw and processed data files
│ ├── Data sources table.pdf # A table of the data sources used in the project
│ └── Landcover Datas.jpg # Landcover data image
│
├── figures/ # Contains generated figures and maps
│ ├── Change in Area per change in Weight.jpg # Visualization of area change vs. weight
│ ├── Methodology.png # Methodology flowchart or image
│ ├── Most Suitable Area.jpg # Most suitable area map for solar energy installation
│ ├── Restricted Area.jpg # Map showing restricted areas
│ ├── Study Area Map.jpg # Study area map of Bagmati
│ └── Suitability_map.png # Final suitability map for solar site selection
│
├── report/ # Contains project reports and documentation
│ └── GIS-Based-Analytical-Hierarchy-Process-for-Optimal-Solar-Site-Selection.pdf # Detailed report on methodology and results
│
├── Scripts/ # Contains Python scripts for analysis and processing
│ ├── ahp_weights.py # AHP weights calculation script
│ ├── criteria_reclassification.py # Criteria reclassification script for data preprocessing
│ ├── sensitivity_analysis.py # Sensitivity analysis script
│ └── suitability_overlay.py # Script for overlaying suitability maps
│
├── LICENSE # Project license file
└── README.md # Project documentation
```


---

## 📥 Data Sources

| Dataset               | Source                                    |
|------------------------|-------------------------------------------|
| Solar Irradiance       | [Global Solar Atlas](https://globalsolaratlas.info/)  
| Elevation & Slope      | [ASTER GDEM](https://search.earthdata.nasa.gov)  
| Temperature            | [Global Solar Atlas](https://globalsolaratlas.info/)  
| LULC                  | [ICIMOD NLCMS](https://rds.icimod.org)  
| Roads                 | [OpenStreetMap](https://www.openstreetmap.org)  
| Substations           | [Nepal Electricity Authority](https://nea.org.np)

---

## 📸 Sample Outputs

- 🗺️ Suitability Map (Most Suitable Zones in Red)
- 📈 Sensitivity Analysis Charts
- ✅ Overlay of Solar Farms on Model Output

---

## 👨‍💻 Authors

- Aadarsha Acharya  
- Dipesh Chaulagain  
- **Lokesh Chaudhary**  
- Nabin Shrestha  
- Rajesh Bajgain  

> **Supervisor:** Asst. Prof. Er. Saurav Gautam  
> Department of Geomatics Engineering, IOE, Pashchimanchal Campus

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 💡 Acknowledgments

We are grateful to the **Department of Geomatics Engineering, IOE** for support, and to all mentors and peers who contributed directly or indirectly to this project.

---

## ⭐️ If you find this helpful...

Please consider giving this repo a ⭐️ on GitHub to support academic open-source sharing!

