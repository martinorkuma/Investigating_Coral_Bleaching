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

2. Time Series Analysis of Sea Surface Temperature: Plot SST trends over the years to identify long-term warming patterns.

3. Heatmap of SST & HotSpots: Create a geospatial heatmap of SST and hotspots to identify high-risk areas.

4. Correlation Analysis: Assess the correlation between SST, hotspots, and bleaching alert areas.

5. Seasonal Trends in Coral Bleaching: Boxplots of SST and hotspots by month to understand seasonal patterns.

6. Impact of Degree Heating Weeks (DHW) on Coral Bleaching: Visualize how DHW relates to bleaching alerts.

7. Impact of Higher Temperatures on Coral Bleaching

## Exploratory Data Analysis

See file [Investigating_Coral_Bleaching](https://github.com/martinorkuma/Investigating_Coral_Bleaching/blob/main/Investigating_Coral_Bleaching.ipynb) for complete exploratory data analysis.

### Analysis of Sea Surface Temperature Over Time

```Python
# Extract the year and calculate the yearly average SST
df_yearly = df.groupby(df["Date"].dt.year)["Sea_Surface_Temperature"].mean().reset_index()

# Rename columns for clarity
df_yearly.rename(columns={"Date": "Year"}, inplace=True)

# Plot the yearly average sea surface temperature
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_yearly, x="Year", y="Sea_Surface_Temperature", label="Average SST per Year")

# Add a trend line using Seaborn’s regplot (Linear Regression)
sns.regplot(data=df_yearly, x="Year", y="Sea_Surface_Temperature", scatter=False, ci=None, color="red", label="Trend Line")

plt.xlabel("Year")
plt.ylabel("Sea Surface Temperature (°C)")
plt.title("Yearly Average Sea Surface Temperature in Florida Keys")
plt.legend()
plt.grid(True)  # Optional for better readability
plt.show()
```

![Temp over time](https://github.com/user-attachments/assets/840dbb3f-52eb-41f9-a7af-d7ce37b521e4)


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

**Geospatial Hotspots for High Temperatures**

- The heatmap visualization highlights specific geographic areas experiencing consistently higher SST levels, correlating with increased coral stress.

**Strong Correlation Between SST and Coral Bleaching**

- A significant positive correlation exists between SST, hotspots, and bleaching alert areas, confirming that higher temperatures contribute to increased bleaching incidents.

**Seasonal Patterns of Bleaching Events**

- Boxplot analysis reveals that bleaching alerts peak during warmer months, typically in late summer when SST reaches its highest levels.
  
**Degree Heating Weeks (DHW) as a Key Predictor**

- The analysis of DHW shows that prolonged exposure to elevated temperatures plays a crucial role in triggering mass bleaching events.

**Higher Temperatures Directly Cause Increased Bleaching**

- The scatter plot and regression analysis of SST vs. bleaching alert areas confirm a clear trend: as SST rises, the number of bleaching alerts increases.
- The fitted trendline demonstrates that bleaching events become more frequent and severe once SST crosses a critical threshold.

### Conclusion
This analysis underscores the direct impact of rising sea surface temperatures on coral bleaching in the Florida Keys. The findings highlight the urgency of addressing climate change and implementing conservation strategies to mitigate further damage to coral reef ecosystems.

## References

[National Oceanic and Atmospheric Administration](https://www.noaa.gov/) (2025). Data in the Classroom: Investigating Coral Bleaching. National Oceanic and Atmospheric Administration, US Department of Commerce.
