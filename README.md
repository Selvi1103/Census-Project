# Census Data Standardization and Analysis Pipeline
This Project is to clean, process, and analyze census data from a given source, including data renaming, missing data handling, state/UT name standardization, new state/UT formation handling, data storage, database connection, and querying. The goal is to ensure uniformity, accuracy, and accessibility of the census data for further analysis and visualization.

# Technologies Used:
Languages: Python, SQL
Databases: MongoDB, MySQL
Visualization Tool: Streamlit

# Dataset
Attached in the Repository

# Project Tasks

## Task 1: Rename Column Names
For uniformity renamed some columns and reduced the length of some column names.

## Task 2: Rename State/UT Names
The first character of each word in the name is in upper case and the rest are in lower case ,“and” to be in lower case.

## Task 3: New State/UT formation
Renamed the State/UT From “Andhra Pradesh” to “Telangana” for the given districts.
Renamed the State/UT From “Jammu and Kashmir” to “Ladakh” for the given districts. 

## Task 4: Find and process Missing Data
Missing data has been filled using the following formulas:
  1. Populatio=Male+Female
  2. Literate=Literate_Male +Literate_Female
  3. SC=Male_SC+Female_SC
  4. ST=Male_ST+Female_ST
  5. Workers=Male_Workers+Female_Workers
  6. Workers=Main_Workers+Marginal_Workers
  7. Workers=Cultivator_Workers+Agricultural_Workers+Household_Workers+Other_Workers
  8. Total_Education=Illeterate_Education+Literate_Education
  9. Literate_Education=Below_Primary_Education+Primary_Education+Middle_Education+Secondary_Education+Graduate_Education+Other_Education
  10. Households=Households_Rural+Households_Urban
  11. Filled the null values using information from other cells and some of the Null values finally get filled with 0.

## Task 5: Save Data to MongoDB
Saved the processed data to a MongoDB collection named census.

## Task 6: Database Connection
Fetching the data from MongoDb 
Uploading the data into the Relational database(MYSQL).

## Task 7: Run SQL Queries
Executed queries to analyze the census data. 

  1. What is the total population of each district? </br>
  2. How many literate males and females are there in each district? </br>
  3. What is the percentage of workers (both male and female) in each district? </br>
  4. How many households have access to LPG or PNG as a cooking fuel in each district?
  5. What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?
  6. How many households have internet access in each district?
  7. What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?
  8. How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?
  9. What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility)in each district?
  10. How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?
  11. What is the total number of households in each state?
  12. How many households have a latrine facility within the premises in each state?
  13. What is the average household size in each state?
  14. How many households are owned versus rented in each state?
  15. What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?
  16. How many households have access to drinking water sources near the premises in each state?
  17. What is the average household income distribution in each state based on the power parity categories?
  18. What is the percentage of married couples with different household sizes in each state?
  19. How many households fall below the poverty line in each state based on the power parity categories?
  20. What is the overall literacy rate (percentage of literate population) in each state?

## Task 8: Interactive Streamlit Dashboard
Created an interactive dashboard to visualize census data insights.
