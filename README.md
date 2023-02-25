# CIS3330-CODE-5-Pandas-Practice

## Instructions

In this coding assignment, your will practice data filtering and retrival from a CSV file using the Python module Pandas. To complete the assignment, your program must have the following functions:

* `get_big_mac_price_by_year`
  + The function receives the **year** and the **country_code in lower case**
  + The function should return **mean value** in the **specific year** of the big mac in dollars ('dollar_pice' column)
  + The value must be rounded to **2** decimal numbers
* `get_big_mac_price_by_country`
  + The function receives the **country_code in lower case**
  + The function should return **mean value** of the big mac in dollars ('dollar_pice' column)
  + The value must be rounded to **2** decimal numbers
* `get_the_cheapest_big_mac_price_by_year`
  + The function receives the **year** 
  + The function should return the following output from the place that has the cheapest big mac: "country_name(country_code): $dollar_price" (replace the appropriate values)
  + For example, the output for 2008 will be: **'Malaysia(MYS): $1.7'**
* `get_the_most_expensive_big_mac_price_by_year`
  + The function receives the **year** 
  + The function should return the following output from the place that has the most expensive big mac: "country_name(country_code): $dollar_price" (replace the appropriate values)
  + For example, the output for 2003 will be: **'Switzerland(CHE): $4.6'**

## Important notes

* The country_code is stored under the column **'iso_a3'**
* The price of the big mac in dollars is stored under the column **'dollar_price'**
* Program your interface under the if statement: `if __name__ == "__main__":`.
* Use the built-in function round() to round decimal numbers. For example: `round(0.5556,2)` should return **0.56**

## Copyright disclosure

* The file `US_chronic_diseases.csv` records the "U.S. Chronic Disease Indicators (CDI)" and was obtained from Data.Gov [https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi]
