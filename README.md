# Data Plotting Tool - Global Air Pollution Dataset

## Table of contents:
<a id="table-of-contents"></a>

1. [About the project](#heading-1)
2. [About the dataset](#heading-2)
3. [Demo and plot results](#heading-3)
4. [Project Structure](#heading-4)

<a id="heading-1"></a>

## [About the project:](#table-of-contents)
This personal project aims to make a visual representation of the data by generating a plot based on the user's choices. The generated plot is automatically saved to the "Downloads" folder of the user's computer. This project used Pandas, Matplotlib, OS, and datetime packages. Pandas and Matplotlib were used for filling the missing rows with "unknown" and to generate the plot, respectively. The OS was used to make the location of the CSV and the Downloads folder cross-platform. While the datetime was used for the naming scheme of the plot to make sure no plot had the same name, this prevented overwriting the old plot file. The plot file is an PNG file with a DPI of 250, leading to a resolution of 2500x2500. This is to make sure that the plot file is of high quality and easy to read.

<a id="heading-2"></a>

## [About the dataset:](#table-of-contents)
The dataset is a CSV file and contains the air quality index (AQI) value for all cities in the world. It has five categories:
1. Overall AQI - Overall AQI value of the city.
2. CO AQI - Carbon Monoxide AQI value of the city.
3. Ozone AQI - Ozone AQI value of the city
4. NO2 AQI - Nitrogen Dioxide AQI value of the city
5. PM2.5 AQI - Particulate Matter within 2.5 micrometers or less within the city.
   
The dataset is from [Kaggle](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset) and was updated just last year.

<a id="heading-3"></a>

## [Demo and plot results:](#table-of-contents)

<figure>
    <figcaption>Demo of the program:</figcaption>
    <img src="/media/demo.gif">
</figure>

<figure>
    <figcaption>Sample for Overall AQI:</figcaption>
    <img src="/media/Plot_India_AQI Value_Hazardous_20240217.09-06-08.png", width="800", height="800">
</figure>

<figure>
    <figcaption>Sample for Carbon Monoxide AQI:</figcaption>
    <img src="/media/Plot_Spain_CO AQI Value_Good_20240217.09-09-10.png", width="800", height="800">
</figure>

<figure>
    <figcaption>Sample for Ozone AQI:</figcaption>
    <img src="/media/Plot_Japan_Ozone AQI Value_Moderate_20240217.09-09-51.png", width="800", height="800">
</figure>

<figure>
    <figcaption>Sample for Nitrogen Dioxide AQI:</figcaption>
    <img src="/media/Plot_Romania_NO2 AQI Value_Good_20240217.09-10-27.png", width="800", height="800">
</figure>

<figure>
    <figcaption>Sample for PM2.5 AQI:</figcaption>
    <img src="/media/Plot_Pakistan_PM2.5 AQI Value_Very Unhealthy_20240217.09-07-01.png", width="800", height="800">
</figure>

<a id="heading-4"></a>

## [Project Structure:](#table-of-contents)

This project structure is based on [Cookie Cutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) and has been edited to fit this personal project.

Here's a better look of the project structure:

```
├── README.md          <- The top-level README.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── media              <- Contains the photos and gif files used for the markdown.
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module.
│   │
│   ├── data           <- Scripts to download or generate data.
│   │   └── Old Files  <- Files here are the intial codes for the project.
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling.
│   │   └── Old Files  <- Files here are the intial codes for the project.
│   │   └── main.py    <- main program of the project.
│   │   └── user_input_validation_filtering_plotting.py <- This is a collection of the functions I made to used for this project.
│   
```

## Thank you for visiting!