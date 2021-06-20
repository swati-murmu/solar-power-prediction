# solar-power-prediction


The primary goal of the project is to calculate the ideal number of solar panels based on the zipcodes in Orange County and the power consumption of the user's household.  Approached this by answering three research questions that helped us predict the number of solar panels. The following were the research questions: 

1) Can we predict the weather based on several variables?

 The first task is to determine if we can predict the weather based on several variables. We have the following two approaches to dig deeper into this question:

●	Predicting the wind speed using time series analysis to get an understanding of the wind speed patterns for future periods-Time Series Analysis using SARIMA

●	To predict temperatures of Orange County broken down into 69 Zipcodes for the next 25 years using Random Forest Algorithm. These temperature estimates will be used to calculate the number of solar panels required for a single household unit-Machine Learning Model: Random Forest Algorithm

2) How has solar irradiation changed over the past ten years?

The purpose of this research question is to analyze the trend in solar irradiation observed between the years 2010 - 2019 and search for any significant changes over time. It will provide valuable input into the model to predict the number of solar panels required for a particular household located within a zip code. I combined the variables “Year,” “Month,” and "Day" to create an index column titled “Date”.  Variable ”GHI” and variable “Zipcode” were selected to find the average monthly GHI for each zip code. The results were displayed using line charts for each zip code.

3) How many solar panels would be needed for generating the power required to support a household within Orange County?

This section uses the result from the previous sections to predict the number of solar panels required for a household with our model. The model receives user inputs such as   annual power usage and the zip code where the home is located within Orange County. 
 


 
# Dataset
National Solar Radiation Database- extracted solar data on all 69 Orange County zip code zones along with the information on cloud type, solar zenith angle, temperature, and wind speed through the API (Application Programming Interface) service of the National Solar Radiation Database (https://nsrdb.nrel.gov/) and integrated the API into the Python code and collected the information on the hourly format between the year 2010 to the year 2019. 

Opendatasoft.com - The National Solar Radiation Database data does not specify the zip code zones. The only provided location information is latitude and longitude. Hence, I  extracted the latitude and longitude information of each Orange County zip code. 

# Data Preprocessing

The only preprocessing I had to do was to match zip code zones with the corresponding latitude and longitude in our dataset. The dataset from Opendatasoft includes three columns: Zip, Latitude, and Longitude.

Hence, I looked for zip codes with the minimum distance from our solar radiation records and calculated the distance based on the Euclidean distance. 










