#----------------------------------------------------------------------------------------------------
# Make imports
#----------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import os

#----------------------------------------------------------------------------------------------------
# Load dataset
#----------------------------------------------------------------------------------------------------

base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "..", "..", "data", "raw")
file_path = os.path.join(data_path, "global air pollution dataset.csv")

df_original = pd.read_csv(file_path)


    #----------------------------------------------------------------------------------------------------
    # Trying it per country first before making it into a function
    #----------------------------------------------------------------------------------------------------
subset = df_original[(df_original["City"] == "Manila") | (df_original["Country"] == "Philippines")]
subset_unhealthy = subset[subset["AQI Category"] == "Unhealthy"].sort_values(by="AQI Value", ascending=False)

cities = list(subset_unhealthy["City"])
aqi_values = list(subset_unhealthy["AQI Value"])

plt.figure(figsize=(10, 10))
plt.plot(cities, aqi_values, marker="o", linestyle="-")
plt.xlabel("City:")
plt.ylabel("AQI Value:")
plt.title("Cities in the Phillipines with Unhealthy Air Quality:")
plt.xticks(rotation=45, ha="right")

plt.grid(True, linestyle="--", linewidth=0.5, color="gray", which="both", axis="y")

plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------------------------------
# Filling the NA with Unknown
#----------------------------------------------------------------------------------------------------
df_na_filled = df_original.fillna({"Country": "Unknown", "City": "Unknown"})
df_na_filled.index = df_na_filled["Country"]
del df_na_filled["Country"]

#----------------------------------------------------------------------------------------------------
# Exporting the new dataset
#----------------------------------------------------------------------------------------------------
base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "..", "..", "data", "interim")
file_path = os.path.join(data_path, "global air pollution dataset_filled.csv")

df_na_filled.to_csv(file_path)

#----------------------------------------------------------------------------------------------------
# Some extra code. Just validating if all country has good to hazardous AQI category
# from overall AQI to individual AQI.
#----------------------------------------------------------------------------------------------------
df_dropna = df_original.dropna(subset=["Country","City"])

aqi_category = list(df_dropna["AQI Category"].unique())
aqi_types = [
    "AQI Category", 
    "CO AQI Category",
    "Ozone AQI Category",
    "NO2 AQI Category",
    "PM2.5 AQI Category"
]

for per_type in aqi_types:
    for per_category in aqi_category:
        subset = df_dropna[df_dropna[per_type] == per_category]
        country_len = len(list(subset["Country"].unique()))
        
        print(f"Current: {per_type} : {per_category} : Count: {country_len}")
    #----------------------------------------------------------------------------------------------------
    # This proves that not all country has all the AQI category. 
    #----------------------------------------------------------------------------------------------------