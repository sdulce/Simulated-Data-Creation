# Simulated-Data-Creation
This document will showcase an analysis on the data created from projects 1 and 2.  The analysis will show important data points and explanations of the code that mined that data.

1. This code identifies the top car brands, models, and paint colors by counting occurrences in the respective columns of a DataFrame. It splits the Car Brand & Model column into Brand and Model, calculates the sales count for each unique value using .value_counts(), formats the results into DataFrames, and displays the top 5 entries for each category.
# Project 3 - Best Selling Items Analysis
Overview
This project analyzes the best-selling items for each store and across the entire organization. The analysis is based on customer basket data to identify the most frequently purchased items.

Goals
Identify top-selling items for each store and organization-wide.

Discover prevalent itemsets using market basket analysis and data mining techniques.

Methodology
Market Basket Analysis: Perform Apriori algorithm to find frequent itemsets and association rules.

Store-Specific Analysis: Calculate total sales and units sold for the top 10 products in each of the top 10 stores.

Organization-Wide Analysis: Summarize the overall best-selling products.

Results
Top 10 Products Frequently Bought Together: Identified using market basket analysis.

Best-Selling Items by Store: Top 10 products for each of the top 10 stores.

Overall Best-Selling Products: Summary of top-selling products across the organization.

Repository Structure
notebook.ipynb: Jupyter notebook with the analysis.

data/: Directory with CSV files used for analysis.

README.txt: This file.
