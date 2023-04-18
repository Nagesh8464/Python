import matplotlib.pyplot as plt
import pandas as pd
import requests
l=["Aberporth","Armagh","Bradford","Camborne","Chivenor","Durham"]
print(l)
Name=input("enter any Name that shown in above:").strip().title()
if Name in l:
  a=Name.lower()+'data.txt'
# Set URL for the data file
  url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/'+a
  
  # Read the data file and create the dataframe
  weather_data = pd.read_csv(url, skiprows=7, delim_whitespace=True,on_bad_lines='skip')
  
  # Remove the last row, which contains only text
  weather_data = weather_data.iloc[:-1]
  
  # Rename the columns to be more descriptive
  weather_data.columns = ['Year', 'Month', 'Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall']
  
  # Convert the numeric columns to floats or integers
  weather_data['Tmax'] = pd.to_numeric(weather_data['Tmax'], errors='coerce')
  weather_data['Tmin'] = pd.to_numeric(weather_data['Tmin'], errors='coerce')
  weather_data['Tmean'] = pd.to_numeric(weather_data['Tmean'], errors='coerce')
  weather_data['Sunshine'] = pd.to_numeric(weather_data['Sunshine'], errors='coerce')
  weather_data['Rainfall'] = pd.to_numeric(weather_data['Rainfall'], errors='coerce')
  
  # Calculate monthly averages for each weather variable
  monthly_averages = weather_data.groupby('Month').mean()
  
  # Create a new figure for the chart
  fig, ax = plt.subplots(figsize=(10, 6))
  
  # Plot the monthly averages for minimum and maximum temperature
  ax.plot(monthly_averages.index, monthly_averages['Tmin'], label='Minimum Temperature')
  ax.plot(monthly_averages.index, monthly_averages['Tmax'], label='Maximum Temperature')
  
  # Plot the monthly averages for precipitation
  ax.bar(monthly_averages.index, monthly_averages['Rainfall'], label='Precipitation', alpha=0.5)
  
  # Plot the monthly averages for hours of sunlight
  ax.plot(monthly_averages.index, monthly_averages['Sunshine'], label='Hours of Sunlight')
  
  # Set the title and axis labels for the chart
  ax.set_title('Monthly Weather Averages')
  ax.set_xlabel('Month')
  ax.set_ylabel('Value')
  
  # Add a legend to the chart
  ax.legend()
  
  # Show the chart
  plt.show()
else:
  print("enter valid Name")
