# Simulated-Data-Creation

## Overview
This repository showcases a comprehensive analysis of the simulated data generated across three projects. Each project builds on the previous one to provide insights into customer purchasing patterns within a corporation.

### Project Summaries
1. **Project 1: Digital Twin for a Corporation**
   - Created a digital twin using object-oriented Python to simulate customer orders and generate sales data.

2. **Project 2: Data Mining and Trend Analysis**
   - Utilized Pandas to analyze sales data, identifying prevalent products, large-basket purchases, and customer demographics.

3. **Project 3: Market Basket Analysis**
   - Conducted market basket analysis to discover frequently bought item sets and best-selling products.

### Results
- **Top Products**: Identified prevalent items and frequently bought together products.
- **Customer Insights**: Analyzed large-basket buyers and their purchasing patterns.
- **Store Performance**: Ranked stores based on customer purchase data.

## Visualizations
- Included visualizations to illustrate key insights and trends.

## Repository Structure
- `notebook.ipynb`: Jupyter notebook with the analysis and visualizations.
- `data/`: Directory with CSV files.
- `README.md`: This file.


# Project 1 - Introductory Python: Digital Twin for a Corporation

## Overview
This project builds a digital twin for a corporation using object-oriented Python. The digital twin models a corporation with various objects that simulate the creation and processing of orders over a year.

## Goals
- Model a Corporation using Python classes.
- Track sales data and generate a consolidated CSV file.
- Simulate a year's worth of transactions for a distributed corporation with many stores.

## Model Structure
### Objects
- **Car**: Represents a product with a brand, model, paint color, and price.
- **Order**: A list of products created by a customer.
- **Customer**: Creates and manages orders.
- **Store**: Contains records of customers and their orders.
- **Corporation**: Contains records of all stores and manages the simulation of sales.

## Methodology
1. **Data Model**:
    - **Car**: Includes brand, model, paint color, and price.
    - **Order**: Tracks order ID, customer ID, list of cars, and timestamp.
    - **Customer**: Manages customer information and orders.
    - **Store**: Manages customers and generates orders.
    - **Corporation**: Generates stores, customers, and simulates sales.

2. **Sales Simulation**:
    - Simulate sales by generating orders for customers in each store.
    - Each order includes randomly selected cars.
    - Track all transactions and export to a CSV file.

## Results
- The project generates a CSV file named `luxury_dealership_sales_data.csv` containing:
  - Date
  - Time
  - StoreID
  - CustomerID
  - OrderID
  - Car Brand & Model
  - Paint Color
  - Price

## Example Usage
To run the project, simply execute the provided Python code to simulate sales and generate the CSV file with the sales data.

# Project 2 - Introductory Pandas: Data Mining and Trend Analysis

## Overview
This project uses Pandas techniques to mine data from the corporation created in Project 1. The analysis aims to report on various trends, focusing on customer purchasing behaviors and product prevalence.

## Goals
- Identify the most prevalent products in customer baskets.
- Analyze the frequency of large-basket purchases by customers.
- Determine which stores have the most large-basket buyers and the extent of their purchases.
- Visualize the top stores by frequency of large-basket customers.
- Provide a top-n list of typical products for customers with large baskets.
- Categorize and analyze the demographic makeup of large-basket customer baskets.

## Methodology
1. **Data Loading**: Load sales data from the CSV file generated in Project 1.
2. **Data Analysis**:
    - Use Pandas to identify prevalent products in customer baskets.
    - Calculate the frequency of large-basket purchases by customers.
    - Identify stores with the most large-basket buyers and quantify their purchases.
3. **Visualization**:
    - Create a visualization ranking the top stores with large-basket customers.
    - Formulate a visualization categorizing the makeup of large-basket customer baskets.
4. **Top-n List**: Generate a list of products typical to customers with large baskets.

## Results
- **Prevalent Products**: Identified the most frequently occurring products in customer baskets.
- **Large-Basket Frequency**: Analyzed the frequency of large-basket purchases by customers.
- **Top Large-Basket Stores**: Ranked stores by the frequency and extent of large-basket purchases.
- **Top-n List of Products**: Provided a list of typical products for large-basket customers.
- **Categorical Analysis**: Analyzed and visualized the demographic makeup of large-basket customer baskets.

## Visualization
Included visualizations for:
- Ranking the top stores by frequency of large-basket customers.
- Categorizing the average makeup of large-basket customer baskets.

## Repository Structure
- `notebook.ipynb`: Jupyter notebook with the complete analysis and visualizations.
- `data/`: Directory with the CSV file from Project 1.
- `README.md`: This file.

## Instructions
To run the project, open the `notebook.ipynb` file in Google Colab and follow the steps to load, analyze, and visualize the data.

# Project 3 - Best Selling Items Analysis

## Overview
This project analyzes the best-selling items for each store and across the entire organization. The analysis is based on customer basket data to identify the most frequently purchased items.

## Goals
- Identify top-selling items for each store and organization-wide.
- Discover prevalent itemsets using market basket analysis and data mining techniques.

## Methodology
- **Market Basket Analysis**: Perform Apriori algorithm to find frequent itemsets and association rules.
- **Store-Specific Analysis**: Calculate total sales and units sold for the top 10 products in each of the top 10 stores.
- **Organization-Wide Analysis**: Summarize the overall best-selling products.

## Results
- **Top 10 Products Frequently Bought Together**: Identified using market basket analysis.
- **Best-Selling Items by Store**: Top 10 products for each of the top 10 stores.
- **Overall Best-Selling Products**: Summary of top-selling products across the organization.

## Repository Structure
- `notebook.ipynb`: Jupyter notebook with the analysis.
- `data/`: Directory with CSV files used for analysis.
- `README.md`: This file.
er notebook with the analysis.

data/: Directory with CSV files used for analysis.

README.txt: This file.
