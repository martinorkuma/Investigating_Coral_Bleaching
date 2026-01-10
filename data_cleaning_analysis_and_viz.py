# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from datetime import datetime

# load the dataset
df = pd.read_csv("Florida_Keys.csv")

# Display basic information about the dataset
print("\nDataset Information:")
df.info()

print("\nColumn Information:")
df.head().T

# Data Cleeaning
# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y")
# Extract Month for seasonal analysis
df['Month'] = df['Date'].dt.month


# Calculate the Time Series Analysis of Sea Surface Temperature
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Date", y="Sea_Surface_Temperature", label="SST")
plt.xlabel("Year")
plt.ylabel("Sea Surface Temperature (°C)")
plt.title("Time Series of Sea Surface Temperature in Florida Keys")
plt.legend()
plt.show()


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


# Heatmap of SST & HotSpots (Geospatial)
plt.figure(figsize=(10, 8))
sc = plt.scatter(df['Longitude'], df['Latitude'], c=df['Sea_Surface_Temperature'], 
                 cmap='coolwarm', alpha=0.5)
plt.colorbar(sc, label="Sea Surface Temperature (°C)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geospatial Heatmap of Sea Surface Temperature")
plt.show()


# Correlation Analysis
corr_matrix = df[['Sea_Surface_Temperature', 'HotSpots', 
                  'Degree_Heating_Weeks', 'Bleaching_Alert_Area']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Key Variables")
# Slant the x-axis labels
plt.xticks(rotation=45)
plt.show()


# Compute the average temperature per month to define color mapping
avg_temps = df.groupby("Month")["Sea_Surface_Temperature"].mean().sort_values()

# Create a color palette where warmer months get warmer colors
warm_palette = sns.color_palette("RdYlBu_r", len(avg_temps))  # Reversed to match warm-to-cool

# Map months to their corresponding colors based on average temperature
month_colors = {month: color for month, color in zip(avg_temps.index, warm_palette)}
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Month', y='Sea_Surface_Temperature', hue='Month', palette=month_colors)
plt.xlabel("Month")
plt.ylabel("Sea Surface Temperature (°C)")
plt.title("Seasonal Trends in Sea Surface Temperature")
plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position
plt.show()


# Impact of Degree Heating Weeks (DHW) on Coral Bleaching ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Degree_Heating_Weeks", y="Bleaching_Alert_Area", alpha=0.3)
plt.xlabel("Degree Heating Weeks (DHW)")
plt.ylabel("Bleaching Alert Area")
plt.title("Impact of DHW on Coral Bleaching")
plt.show()


# Visualization: Impact of Higher Temperatures on Coral Bleaching ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Sea_Surface_Temperature", y="Bleaching_Alert_Area", alpha=0.3)
sns.regplot(data=df, x="Sea_Surface_Temperature", y="Bleaching_Alert_Area", scatter=False, color='red', ci=None)  # Trend line
plt.xlabel("Sea Surface Temperature (°C)")
plt.ylabel("Bleaching Alert Area")
plt.title("Impact of Higher Temperatures on Coral Bleaching")
plt.show()
