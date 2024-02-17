import pandas as pd
import os
import user_input_validation_filtering_plotting as my_func

#----------------------------------------------------------------------------------------------------
# Load the Data
#----------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------
    # Using OS to make the file path cross-platform compatible.
    #----------------------------------------------------------------------------------------------------
base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "..", "..", "data", "interim")
file_path = os.path.join(data_path, "global air pollution dataset_filled.csv")

df = pd.read_csv(file_path)

    #----------------------------------------------------------------------------------------------------
    # Declaring the proper naming to be selected for the Column and Row.
    #----------------------------------------------------------------------------------------------------
aqi_types_list = {
    1: "AQI Category", 
    2: "CO AQI Category",
    3: "Ozone AQI Category",
    4: "NO2 AQI Category",
    5: "PM2.5 AQI Category"
}
aqi_category_list = {
    1: "Good",
    2: "Moderate",
    3: "Unhealthy for Sensitive Groups",
    4: "Unhealthy",
    5: "Very Unhealthy",
    6: "Hazardous",
}

#----------------------------------------------------------------------------------------------------
# First Question - Asking the user for the AQI Type
#----------------------------------------------------------------------------------------------------
max_types = 5
aqi_types_statement = "Please select which AQI do you want to see (Select the number only):\n1. Overall AQI\n2. CO AQI\n3. Ozone AQI\n4. NO2 AQI\n5. PM2.5 AQI\n"
aqi_types_ans = my_func.input_checker(aqi_types_statement, max_types)

#----------------------------------------------------------------------------------------------------
# Second Question - Asking the user for the AQI Category
#----------------------------------------------------------------------------------------------------
match aqi_types_ans:
    case 1:
        max_category = 6
        aqi_category_statement = "\nPlease select the category (Select the number only):\n1. Good\n2. Moderate\n3. Unhealthy for Sensitive Groups\n4. Unhealthy\n5. Very Unhealthy\n6. Hazardous\n"
        aqi_category_ans = my_func.input_checker(aqi_category_statement, max_category)
    case 2:
        max_category = 3
        aqi_category_statement = "\nPlease select the category (Select the number only):\n1. Good\n2. Moderate\n3. Unhealthy for Sensitive Groups\n"
        aqi_category_ans = my_func.input_checker(aqi_category_statement, max_category)
    case 3:
        max_category = 5
        aqi_category_statement = "\nPlease select the category (Select the number only):\n1. Good\n2. Moderate\n3. Unhealthy for Sensitive Groups\n4. Unhealthy\n5. Very Unhealthy\n"
        aqi_category_ans = my_func.input_checker(aqi_category_statement, max_category)
    case 4:
        max_category = 2
        aqi_category_statement = "\nPlease select the category (Select the number only):\n1. Good\n2. Moderate\n"
        aqi_category_ans = my_func.input_checker(aqi_category_statement, max_category)
    case 5:
        max_category = 6
        aqi_category_statement = "\nPlease select the category (Select the number only):\n1. Good\n2. Moderate\n3. Unhealthy for Sensitive Groups\n4. Unhealthy\n5. Very Unhealthy\n6. Hazardous\n"
        aqi_category_ans = my_func.input_checker(aqi_category_statement, max_category)

    #----------------------------------------------------------------------------------------------------
    # Setting the proper names base on the user input
    #----------------------------------------------------------------------------------------------------
selected_aqi_type = aqi_types_list[aqi_types_ans]
selected_aqi_category = aqi_category_list[aqi_category_ans]

#----------------------------------------------------------------------------------------------------
# Third Question - Asking the user for the Country base on the available option.
#----------------------------------------------------------------------------------------------------
country_option, country_list,  max_country, df_filtered_country = my_func.filtered_country(df, selected_aqi_type, selected_aqi_category)
print("These are the resulted list of countries based on what you've picked:\n" + country_option)
country_statement = "Please enter either the corresponding number to the name of the country you want or the name of the country itself (CASE SENSITIVE):\n"
country_selected = my_func.input_checker_countries(country_statement, max_country, country_list)

#----------------------------------------------------------------------------------------------------
# Fourth Question - Asking the user for the Cities base on the available option - Data Plotting.
#----------------------------------------------------------------------------------------------------
cities_option, cities_list,  max_cities, df_filtered_cities, country = my_func.filtered_cities(df_filtered_country, country_list, country_selected)
city_statement = "Please select which option would you like to plot:\n1. All\n2. Selection\n3. Range\n"
city_selected = my_func.input_checker_cities(df_filtered_cities, city_statement, cities_option, cities_list, country, selected_aqi_type, selected_aqi_category)