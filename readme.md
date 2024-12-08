
# Solar Radiation Analysis - Benin Malanville

This project focuses on analyzing solar radiation data from Malanville, Benin, as part of the Week 0 Challenge for 10 Academy's training program. The analysis includes exploratory data analysis (EDA), insights generation, and dashboard development to identify high-potential regions for solar installations.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Dataset Description](#dataset-description)
3. [Project Structure](#project-structure)
4. [How to Run the Project](#how-to-run-the-project)
5. [Key Insights](#key-insights)
6. [Streamlit Dashboard](#streamlit-dashboard)
7. [Dependencies](#dependencies)
8. [Author](#author)

---

## **Project Overview**
MoonLight Energy Solutions aims to enhance operational efficiency by identifying optimal regions for solar installations. This project analyzes solar radiation data to provide actionable insights and supports decision-making through a dynamic Streamlit dashboard.

---

## **Dataset Description**
The dataset, `benin-malanville.csv`, contains solar radiation and environmental measurements:
- **Key Columns**:
  - `GHI`: Global Horizontal Irradiance (W/m²)
  - `DNI`: Direct Normal Irradiance (W/m²)
  - `DHI`: Diffuse Horizontal Irradiance (W/m²)
  - `Tamb`: Ambient Temperature (°C)
  - `RH`: Relative Humidity (%)
  - `WS`: Wind Speed (m/s)
  - `Cleaning`: Indicator for sensor cleaning events (1 = cleaned, 0 = not cleaned)
  - `Timestamp`: Observation time (yyyy-mm-dd hh:mm)

---

## **Project Structure**
```
solar-radioation-analysis/
├── app/
│   ├── main.py        # Streamlit dashboard
├── data/
│   ├── benin-malanville.csv        # Raw dataset
│   ├── benin-malanville-cleaned.csv # Cleaned dataset
├── notebooks/
│   ├── EDA_Benin_Malanville.ipynb  # EDA Jupyter Notebook
├── .github/
│   ├── workflows/
│       ├── unittests.yml           # CI/CD workflow
├── .gitignore                      # Excludes unnecessary files
├── README.md                       # Project documentation
├── requirements.txt                # Dependencies
```

---

## **How to Run the Project**

### **Prerequisites**
1. Python 3.8 or higher.
2. Required libraries installed via `requirements.txt`.

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/solar-radiation-analysis.git
   cd solar-radiation-analysis
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit Dashboard:
   ```bash
   streamlit run app/main.py
   ```

---

## **Key Insights**
- **High Solar Irradiance**: Midday hours show peak values for GHI and DNI, indicating optimal energy harvesting times.
- **Impact of Cleaning**: Regular cleaning significantly improves sensor readings, especially after precipitation events.
- **Correlation Trends**:
  - Strong positive correlation between GHI and DNI.
  - Moderate relationship between wind speed and irradiance.

---

## **Streamlit Dashboard**
The interactive dashboard visualizes key insights, allowing users to:
1. Upload their own datasets.
2. Explore solar radiation trends dynamically.
3. Visualize the impact of cleaning and environmental factors.

### **Live Link**:
[Access the Streamlit Dashboard](https://solar-radiation-analysis-gwebjksq589whnukxr9j3b.streamlit.app/)

---

## **Dependencies**
The following Python libraries are required:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `streamlit`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Author**
**Mulsew M. Tesfaye**  

---

## **Acknowledgments**
This project was developed as part of the 10 Academy Week 0 Challenge. Special thanks to the facilitators and mentors for their guidance and support.
