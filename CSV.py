import pandas as pd

# Correct file path
file_path = r'D:\VS Codes\Internship\Dataset .csv'  # Use raw string for file paths in Windows

# Load the dataset
df = pd.read_csv(file_path)

# Display the first few rows to verify the data
print(df.head())

# Distribution of restaurants by city and country
city_distribution = df['City'].value_counts()
country_distribution = df['Country Code'].value_counts()

# Display the top 10 cities and countries
top_cities = city_distribution.head(10)
top_countries = country_distribution.head(10)

print("Top 10 Cities with Most Restaurants:")
print(top_cities)

print("\nTop 10 Countries with Most Restaurants:")
print(top_countries)
