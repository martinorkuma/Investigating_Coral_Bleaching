![Coral Dashboard Snap](https://github.com/user-attachments/assets/f40b345c-9ece-41a3-824c-56f061cb0358)

## Introduction

Coral bleaching is a significant environmental issue affecting marine ecosystems worldwide, particularly in regions like the Florida Keys. This phenomenon occurs when corals experience prolonged stress due to elevated sea surface temperatures, leading to the expulsion of their symbiotic algae, which provide essential nutrients and coloration. As ocean temperatures continue to rise due to climate change, the frequency and severity of coral bleaching events are increasing, posing a major threat to reef biodiversity and ecosystem health.

**Objective:**

The objective of this analysis is to examine the relationship between sea surface temperature (SST) and coral bleaching in the Florida Keys. Using historical data, from 1985 to 2025, this analysis identifies trends in SST over time, analyzes geospatial variations, and determines the correlation between SST, hotspots, and bleaching alert areas. This analysis aims to provide insights into how increasing ocean temperatures contribute to coral stress, helping inform conservation efforts and climate adaptation strategies.

**Data Source:**

The dataset used in this project was compiled by the [National Oceanic and Atmospheric Administration](https://www.noaa.gov/) from 1985 to 2025. [Click to download the dataset.](https://www.nnvl.noaa.gov/Portal/Output/NOAA_CRW_5km_Regional_Virtual_Stations/Florida_Keys.csv)

**Key Terms:**

Definitions of key terms can be found [here.](https://coralreefwatch.noaa.gov/product/5km/methodology.php#ssttrend)

### Key Analyses & Visualizations:

1. Data Processing and Cleaning

2. Time Series Analysis of Sea Surface Temperature

- Plot SST trends over the years to identify long-term warming patterns.
- Compare SST trends with bleaching alert areas.

3. Heatmap of SST & HotSpots

- Create a geospatial heatmap of SST and hotspots to identify high-risk areas.
- Identify seasonal variations in SST and bleaching.

4. Correlation Analysis

- Assess the correlation between SST, hotspots, and bleaching alert areas.
- Use scatter plots and regression analysis to examine relationships.

5. Seasonal Trends in Coral Bleaching

- Boxplots of SST and hotspots by month to understand seasonal patterns.
- Identify peak bleaching seasons.

6. Impact of Degree Heating Weeks (DHW) on Coral Bleaching

- Visualize how DHW relates to bleaching alerts.
- Identify threshold DHW values leading to mass bleaching events.

7. Impact of Higher Temperatures on Coral Bleaching
- Visualize how SST relates to bleaching alerts.

## Exploratory Data Analysis

See document for complete exploratory data analysis.

### Seasonal Trends in Sea Surface Temperature

The chart shows monthly variations in temperature across the year. 
Each month is represented by a number, with 1 = January and 12 = December.

```Python
# Compute the average temperature per month to define color mapping
avg_temps = df.groupby("Month")["Sea_Surface_Temperature"].mean().sort_values()

# Create a color palette where warmer months get warmer colors
warm_palette = sns.color_palette("RdYlBu_r", len(avg_temps))  # Reversed to match warm-to-cool

# Map months to their corresponding colors based on average temperature
month_colors = {month: color for month, color in zip(avg_temps.index, warm_palette)}

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=df, 
    x='Month', 
    y='Sea_Surface_Temperature', 
    hue='Month', 
    palette=month_colors  # Use our custom mapping
)

plt.xlabel("Month")
plt.ylabel("Sea Surface Temperature (°C)")
plt.title("Seasonal Trends in Sea Surface Temperature")

plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position

plt.show()

```

![Seasonal temp trend](https://github.com/user-attachments/assets/38ed507b-283d-47a2-a6cc-ffe4d41899b5)

## Summary and Key Insights

**Rising Sea Surface Temperature (SST) Trends**

- The time series analysis shows a clear upward trend in SST over the years, indicating long-term warming in the Florida Keys.
- Seasonal fluctuations are evident, with higher SST values typically observed during the summer months.

**Geospatial Hotspots for High Temperatures**

- The heatmap visualization highlights specific geographic areas experiencing consistently higher SST levels, correlating with increased coral stress.
- These high-temperature zones are more prone to experiencing frequent bleaching events.

**Strong Correlation Between SST and Coral Bleaching**

- A significant positive correlation exists between SST, hotspots, and bleaching alert areas, confirming that higher temperatures contribute to increased bleaching incidents.
- The regression analysis indicates that as SST exceeds a critical threshold, bleaching alert levels rise sharply.

**Seasonal Patterns of Bleaching Events**

- Boxplot analysis reveals that bleaching alerts peak during warmer months, typically in late summer when SST reaches its highest levels.
- This aligns with known coral bleaching patterns, reinforcing the impact of temperature stress.

**Degree Heating Weeks (DHW) as a Key Predictor**

- The analysis of DHW shows that prolonged exposure to elevated temperatures plays a crucial role in triggering mass bleaching events.
- Higher DHW values are closely linked to more severe bleaching alerts, suggesting that accumulated heat stress is a primary driver of coral bleaching.

**Higher Temperatures Directly Cause Increased Bleaching**

- The scatter plot and regression analysis of SST vs. bleaching alert areas confirm a clear trend: as SST rises, the number of bleaching alerts increases.
- The fitted trendline demonstrates that bleaching events become more frequent and severe once SST crosses a critical threshold.
- This finding supports global research showing that even small increases in ocean temperature can have devastating effects on coral ecosystems.

### Conclusion
This analysis underscores the direct impact of rising sea surface temperatures on coral bleaching in the Florida Keys. The findings highlight the urgency of addressing climate change and implementing conservation strategies to mitigate further damage to coral reef ecosystems.

## References

[National Oceanic and Atmospheric Administration](https://www.noaa.gov/) (2025). Data in the Classroom: Investigating Coral Bleaching. National Oceanic and Atmospheric Administration, US Department of Commerce.
