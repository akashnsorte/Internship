import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import contextily as ctx

# Load the dataset
file_path = r'D:\VS Codes\Internship\Dataset .csv'
df = pd.read_csv(file_path)

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

# Set the coordinate reference system to WGS84 (EPSG:4326)
gdf.crs = {'init': 'epsg:4326'}

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
gdf.plot(ax=ax, color='red', markersize=5, alpha=0.5)
ctx.add_basemap(ax, crs=gdf.crs.to_string())
plt.title('Restaurant Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

#Analyzing Location
locality_distribution = df['Locality'].value_counts()
top_localities = locality_distribution.head(10)

print("Top 10 Localities with Most Restaurants:")
print(top_localities)

#Analyzing Restaurant Ratings by City
average_rating_city = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

print("Average Rating by City:")
print(average_rating_city)

#Average Rating by Locality
average_rating_locality = df.groupby('Locality')['Aggregate rating'].mean().sort_values(ascending=False)

print("Average Rating by Locality:")
print(average_rating_locality)
