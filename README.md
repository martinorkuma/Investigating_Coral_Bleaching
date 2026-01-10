![Coral Dashboard Snap](https://github.com/user-attachments/assets/f40b345c-9ece-41a3-824c-56f061cb0358)

## Project Overview ## 

Coral bleaching is a critical environmental challenge affecting reef ecosystems globally, with the Florida Keys among the most vulnerable and well-studied regions in the United States. Bleaching occurs when corals are exposed to prolonged thermal stress, primarily driven by elevated sea surface temperatures (SST), causing them to expel symbiotic algae that are essential for their nutrition and survival. Increasing ocean temperatures associated with climate change have intensified both the frequency and severity of bleaching events, threatening reef biodiversity, fisheries, and coastal protection.

This project applies exploratory data analysis and visualization techniques to quantify long-term SST trends in the Florida Keys and to examine how thermal stress metrics relate to coral bleaching alerts. The analysis is designed to be reproducible and interpretable, providing insight into environmental drivers of coral stress and supporting climate and conservation research.

## Objectives: ##

The primary objectives of this analysis are to:
- Quantify long-term trends in sea surface temperature in the Florida Keys (1985–2025)

- Examine seasonal patterns in SST and identify periods of elevated thermal stress

- Visualize geospatial hotspots associated with high SST values

- Evaluate statistical relationships between SST, Degree Heating Weeks (DHW), hotspots, and bleaching alert areas

- Assess how increasing temperatures and prolonged heat exposure contribute to coral bleaching risk

## Data Source: ##

The dataset used in this project was compiled by the [National Oceanic and Atmospheric Administration](https://www.noaa.gov/) from 1985 to 2025. <br>   

Download link: https://www.nnvl.noaa.gov/Portal/Output/NOAA_CRW_5km_Regional_Virtual_Stations/Florida_Keys.csv


Definitions of key variables and methodological details are available in the NOAA Coral Reef Watch documentation: https://coralreefwatch.noaa.gov/product/5km/methodology.php#ssttrend  
<br>

 
## Key Variables ## 
- Sea_Surface_Temperature (SST): Surface ocean temperature measured in degrees Celsius

- HotSpots: Areas where SST exceeds climatological thresholds

- Degree_Heating_Weeks (DHW): Cumulative thermal stress metric indicating prolonged exposure to elevated temperatures

- Bleaching_Alert_Area: Spatial extent of bleaching alerts based on thermal stress thresholds

- Date: Observation date

- Latitude / Longitude: Spatial coordinates for geospatial analysis    
  

## Analysis Workflow ##

The analysis follows a structured workflow:

1. Data ingestion and cleaning

    - Parsing and validating date fields

    - Ensuring numeric consistency across temperature and bleaching-related variables

    - Deriving temporal features such as year and month

2. Exploratory data analysis and visualization

    - Time series analysis of SST

    - Seasonal (monthly) SST distributions

    - Geospatial visualization of SST patterns

    - Correlation analysis among SST, DHW, hotspots, and bleaching alerts

3. Impact assessment

    - Relationship between Degree Heating Weeks and bleaching alert areas

    - Relationship between elevated SST and bleaching severity  

All visual outputs are programmatically generated and saved to a dedicated figs/ directory for reproducibility and reporting.

A complete Python script with all exploratory analysis and visualization is available at: [data_cleaning_analysis_and_viz.py](https://github.com/martinorkuma/investigating_coral_bleaching/blob/main/scripts/data_cleaning_analysis_and_viz.py) 


## Selected Analyses ##
- #### Long-Term Sea Surface Temperature Trends ####  
    Yearly SST averages were computed to identify long-term warming patterns. A linear regression trend line highlights a sustained increase in SST across the study period, consistent with regional climate warming.

- #### Seasonal Sea Surface Temperature Patterns ####
    Monthly SST distributions reveal strong seasonality, with peak temperatures occurring in late summer. These periods coincide with the highest observed bleaching alert frequencies.

- #### Geospatial SST Hotspots #### 
    Spatial scatter plots of SST across latitude and longitude identify persistent hotspots where corals are exposed to elevated thermal stress, indicating areas of heightened vulnerability.

- #### Correlation Analysis #### 
    Correlation matrices demonstrate strong positive relationships between SST, Degree Heating Weeks, hotspots, and bleaching alert areas, supporting the role of sustained thermal stress as a primary driver of coral bleaching.

- #### Thermal Stress and Bleaching Risk #### 
    Scatter plots and regression analyses show that both higher SST values and increased DHW are associated with larger bleaching alert areas, with evidence of threshold-like behavior once critical temperature limits are exceeded.  


## Key Findings ## 
* Sea surface temperatures in the Florida Keys show a clear long-term upward trend from 1985 to 2025
* Bleaching risk is strongly seasonal, peaking during the warmest months
* Specific geographic regions consistently experience higher thermal stress
* Degree Heating Weeks is a strong predictor of bleaching severity
* Elevated SST directly corresponds to increased frequency and extent of bleaching alerts

## Project Structure ##
```text
Investigating_Coral_Bleaching/
├── data/
│   └── Florida_Keys.csv
├── figs/
│   └── (generated figures)
├── scripts/
│   └── data_cleaning_analysis_and_viz.py
└── README.md
```


## Reproducibility ## 
This project is designed for reproducibility. All figures are generated via Python scripts using pandas, matplotlib, and seaborn. Running the analysis script will automatically regenerate all visualizations in the figs/ directory.

## Conclusion ##
This analysis provides quantitative evidence linking rising sea surface temperatures and prolonged thermal stress to increased coral bleaching risk in the Florida Keys. The results reinforce the urgency of climate mitigation and adaptive reef management strategies to preserve coral reef ecosystems under ongoing ocean warming.  

## References ## 
[National Oceanic and Atmospheric Administration](https://www.noaa.gov/) (2025). Data in the Classroom: Investigating Coral Bleaching. National Oceanic and Atmospheric Administration, US Department of Commerce.
