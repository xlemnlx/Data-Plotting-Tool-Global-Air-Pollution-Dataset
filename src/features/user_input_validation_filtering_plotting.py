import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
import os

#----------------------------------------------------------------------------------------------------
# Collection of functions that checks the user's input.
#----------------------------------------------------------------------------------------------------
def input_checker(user_input, max_value):
    question_handler = user_input
    while True:
        try:
            user_input = input(question_handler)
            if user_input.lower == "exit":
                exit()
            
            user_input = int(user_input)
            
            if 1 <= user_input <= max_value:
                return user_input
            else:
                print("Invalid input. Please enter a number within the given range only.\n")
        except ValueError:
            print("Invalid input. Please enter a number only.\n")

def input_checker_countries(user_input, max_value, country_list):
    question_handler = user_input
    while True:
        try:
            user_input = input(question_handler)
            if user_input.lower().capitalize() in country_list:
                return user_input.lower().capitalize()
            elif user_input in country_list:
                return user_input
            elif 1 <= int(user_input) <= max_value:
                return user_input
            else:
                raise ValueError("Invalid input. Please enter again.\n")
        except ValueError as e:
            print(e)
            continue

def input_checker_cities(dataset, user_input, cities_option, cities_list, country, selected_aqi_type, selected_aqi_category):
    question_handler = user_input
    while True:
        try:
            print("These are the resulted list of cities based on what you've picked:\n" + cities_option)
            option_selected = input_checker(question_handler, 3)
            
            if option_selected == 1:
                data_plot(dataset, selected_aqi_type, selected_aqi_category, country)
                return False
            
            if option_selected == 2:
                df_selected_cities = input_checker_cities_selection(dataset, cities_option, cities_list)
                data_plot(df_selected_cities, selected_aqi_type, selected_aqi_category, country)
                return False
            
            if option_selected == 3:
                df_cities_range = input_checker_cities_range(dataset, cities_option, cities_list)
                data_plot(df_cities_range, selected_aqi_type, selected_aqi_category, country)
                return False
        except ValueError:
            print("Invalid input. Please enter again.\n")
            
def input_checker_cities_selection(dataset, cities_option, cities_list):    
    while True:
        try:
            subset_selected_cities = pd.DataFrame() # Empty DF. To hold the filtered cities base on the user input.
            
            user_input = input(f"List of cities available (Seperate the numbers by spaces):\n{cities_option}")
            int_list = [] # will hold the converted str numbers into int.
            selected_cities = [] # will hold the selected cities base on the numbers tha user input.
            
            input_list = user_input.split(" ")
            
            for per_input in input_list:
                if per_input.isdigit():
                    int_list.append(int(per_input))
            
            if len(int_list) <= 0:
                raise ValueError("Cannot be letters or special characters or empty or spaces or negative values.\n")
            if len(int_list) > len(cities_list):
                raise ValueError("You have exceeded the total available cities.\n")
            if max(int_list) > len(cities_list):
                raise ValueError("A number in the list exceeds the limit of available cities.\n")
            if min(int_list) <= 0:
                raise ValueError("A number in the list cannot be 0 or negative.\n")
            
            for per_digit in int_list:
                selected_cities.append(cities_list[per_digit - 1])
            
            selected_cities = list(set(selected_cities)) # removes the duplicates
            
            selected_cities = pd.Series(selected_cities).sort_values(ascending=True).tolist() # using pandas, arrange it to alphabetical order and converts it back to list.
            
            for per_city in selected_cities:
                subset = dataset[dataset["City"] == per_city].copy()
                subset_selected_cities = pd.concat([subset_selected_cities, subset], axis=0, ignore_index=True)
            
            return subset_selected_cities
        except ValueError as e:
            print(e)
            continue

def input_checker_cities_range(dataset, cities_option, cities_list):
    while True:
        try:
            subset_cities_range = pd.DataFrame()
            
            print(f"List of cities available:\n{cities_option}")
            user_input = input("Please enter the range that you want to plot\nExample:\n1. If you want to plot the first 10 rows, just enter: 10\n2. If you want to set the start to end, enter: 5 10\n") 
            input_list = user_input.split(" ")
            int_list = []
            cities_range = []
            range_from = 0
            range_to = None
            
            for per_input in input_list:
                if per_input.isdigit():
                    int_list.append(int(per_input))
            
            if len(int_list) <= 0:
                raise ValueError("Cannot be letters or special characters or empty or spaces or negative values.\n")
            if len(int_list) > 2:
                raise ValueError("Values must be two at maximum only.\n")
            if max(int_list) > len(cities_list):
                raise ValueError("You have entered a value outisde the range of the option.\n")
            
            if len(int_list) == 1:
                range_to = max(int_list)
                for per_count in range(range_to):
                    cities_range.append(cities_list[per_count])
            else:
                range_from = min(int_list)
                range_to = max(int_list)
                count = range_to - range_from
                for per_count in range(count + 1):
                    cities_range.append(cities_list[range_from - 1])
                    range_from += 1
            
            for per_city in cities_range:
                subset = dataset[dataset["City"] == per_city].copy()
                subset_cities_range = pd.concat([subset_cities_range, subset], axis=0, ignore_index=True)
                
            return subset_cities_range
        except ValueError as e:
            print(e)
            continue

#----------------------------------------------------------------------------------------------------
# This two functions make the approriate data filtering base on the user's choices.
#----------------------------------------------------------------------------------------------------
def filtered_country(dataset, selected_aqi_type, selected_aqi_category):
    subset_filtered_country = dataset[dataset[selected_aqi_type] == selected_aqi_category]
    country_list = pd.Series(
        subset_filtered_country["Country"].unique()
        ).sort_values(ascending=True).tolist()
    country_list_len = len(country_list)
    
    print("\n") # Spacer
    
    selection_list = []
    count = 1
    for per_country in country_list:
        selections = f"{count}. {per_country}\n"
        count += 1
        selection_list.append(selections)
    final_selection = "".join(selection_list)
    
    return final_selection, country_list, country_list_len, subset_filtered_country

def filtered_cities(dataset, country_list, country_selected):
    country = ""
    subset_filtered_cities = pd.DataFrame()
    
    if country_selected.isdigit():
        country_selected = int(country_selected)
        country_selected -= 1
        country = country_list[country_selected]
        subset_filtered_cities = dataset[dataset["Country"] == country].copy()
    else:
        country = country_selected
        subset_filtered_cities = dataset[dataset["Country"] == country].copy()
    
    cities_list = pd.Series(
        subset_filtered_cities["City"].unique()
        ).sort_values(ascending=True).tolist()
    cities_list_len = len(cities_list)
    
    print("\n") # Spacer
    
    selection_list = []
    count = 1
    for per_city in cities_list:
        selections = f"{count}. {per_city}\n"
        count += 1
        selection_list.append(selections)
    final_selection = "".join(selection_list)
    
    return final_selection, cities_list, cities_list_len, subset_filtered_cities, country

#----------------------------------------------------------------------------------------------------
# This function plots and saved the file to "Downloads" folder of the user's computer.
#----------------------------------------------------------------------------------------------------
def data_plot(dataset, selected_aqi_type, selected_aqi_category, country):
    current_datetime = datetime.now()
    datetime_str = current_datetime.strftime("%Y%m%d.%H-%M-%S") # will be use for unique file naming of the plot.
    
    username = os.getlogin() # gets the username then insert it into the path_plot.
    path_plot = f"C:/Users/{username}/Downloads"
    
    subset = dataset.copy()
                
    cities = list(subset["City"])
    selected_aqi_type = selected_aqi_type.replace("Category", "Value")
    selected_aqi_type_title = selected_aqi_type.replace("Category", "")
    aqi_values = list(subset[selected_aqi_type])
    
    mpl.rcParams["figure.dpi"] = 250
    plt.figure(figsize=(10, 10))
    plt.plot(cities, aqi_values, marker="o", linestyle="-")
    plt.xlabel("City:")
    plt.ylabel(f"{selected_aqi_type}:")
    plt.title(f"Cities in the {country} with {selected_aqi_category} Quality for {selected_aqi_type_title}:")
    plt.xticks(rotation=45, ha="right")

    plt.grid(True, linestyle="--", linewidth=0.5, color="gray", which="both", axis="y")

    plt.tight_layout()
    plt.savefig(f"{path_plot}/Plot_{country}_{selected_aqi_type}_{selected_aqi_category}_{datetime_str}.png")
    os.startfile(path_plot)
    print("Thank you. The plot has been saved to the Downloads folder and has been been opened to you.")