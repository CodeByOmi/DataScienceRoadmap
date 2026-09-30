# Retail Sales Analysis

## Project Overview

This project analyzes retail sales data to understand sales performance, profitability, customer behavior, product performance, and regional trends.

The goal is to use Python and Pandas to transform raw retail transaction data into meaningful business insights that could support better decision-making.

---

## Business Problem

A retail business needs to understand:

* How sales and profit are changing over time
* Which categories and products perform well
* Which products or transactions generate losses
* Which regions and customers contribute most to profit
* How sales vary across months
* Where the business should investigate opportunities to improve profitability

---

## Dataset

The dataset contains **5,901 retail transactions** with information about:

* Orders and customers
* Products and categories
* Sales and quantity
* Profit
* Regions and cities
* Shipping methods
* Payment methods
* Order and shipping dates

The analysis covers **2019 and 2020**.

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* VS Code

---

## Data Preparation

The following data-quality checks and transformations were performed:

* Checked dataset structure and data types
* Checked missing values
* Checked duplicate rows
* Converted order and shipping dates to datetime
* Checked for invalid quantities
* Investigated negative-profit transactions
* Created `Year`, `Month`, and `Month_Name` features
* Created aggregated business metrics for analysis

The dataset contained no missing values or duplicate rows.

---

## Key Performance Indicators

| Metric                   |         Value |
| ------------------------ | ------------: |
| Total Sales              | ₹1,565,804.32 |
| Total Profit             |   ₹175,262.11 |
| Total Quantity           |        22,317 |
| Unique Customers         |           773 |
| Loss-Making Transactions |         1,098 |
| Overall Profit Margin    |        11.19% |

---

## Yearly Performance

| Year |         Sales |     Profit | Quantity |
| ---- | ------------: | ---------: | -------: |
| 2019 |   ₹564,679.50 | ₹81,823.44 |    9,838 |
| 2020 | ₹1,001,125.00 | ₹93,438.66 |   12,479 |

Sales increased by approximately **77.3% from 2019 to 2020**.

Both years contain all 12 months, making this yearly comparison directly comparable within the dataset.

---

## Category Performance

| Category        |       Sales |     Profit | Profit Margin |
| --------------- | ----------: | ---------: | ------------: |
| Furniture       | ₹451,508.65 | ₹10,006.61 |         2.22% |
| Office Supplies | ₹643,707.69 | ₹74,797.25 |        11.62% |
| Technology      | ₹470,587.99 | ₹90,458.25 |        19.22% |

A notable finding is the difference between sales and profitability.

Furniture generated substantial sales but had a much lower profit margin than Technology. This suggests that sales volume alone is not enough to evaluate category performance.

---

## Key Business Findings

### 1. Strong growth in yearly sales

Sales increased from approximately ₹564.7K in 2019 to ₹1.001M in 2020, representing approximately 77.3% growth.

This indicates substantially higher sales volume in 2020 within the dataset.

### 2. Technology has a strong profit margin

Technology generated approximately ₹470.6K in sales and ₹90.5K in profit, resulting in a 19.22% profit margin.

This is considerably higher than the Furniture category's 2.22% margin.

### 3. Furniture requires profitability investigation

Furniture generated approximately ₹451.5K in sales but only ₹10.0K in profit.

The relatively low margin suggests that the business should investigate factors such as pricing, discounts, product costs, or other operational costs.

The dataset does not contain enough information to determine the exact cause.

### 4. Loss-making transactions are significant

There were **1,098 loss-making transactions** in the dataset.

These transactions should be investigated at the product, customer, region, and order levels to understand where profitability is being lost.

### 5. Sales are concentrated toward the end of the year

Monthly analysis showed substantially higher sales during September–December, with December having the highest monthly sales.

This pattern may be worth investigating further for possible seasonal demand, promotions, or product-specific effects. The dataset alone does not establish the cause.

---

## Visualizations

The notebook contains visualizations covering:

* Sales by Category
* Yearly Sales Trend
* Monthly Sales Trend
* Sales by Region
* Profit by Region
* Profit Margin by Category
* Product performance

These visualizations help identify trends that are difficult to see from aggregated tables alone.

---

## Business Recommendations

Based on the analysis, the following areas should be investigated:

1. **Investigate loss-making products and transactions** to understand the causes of negative profit.
2. **Investigate Furniture's low profit margin** despite substantial sales.
3. **Analyze high-margin categories and products** to understand what contributes to stronger profitability.
4. **Study the September–December sales pattern** to determine whether inventory and marketing strategies should account for seasonal demand.
5. **Compare sales and profit together** when evaluating products, customers, and regions rather than relying on sales alone.

---

## Project Structure

```text
01_RETAIL_SALES_ANALYSIS/
│
├── data/
│   ├── SuperStore_Sales_Dataset.csv
│   └── SuperStore_Sales_Cleaned.csv
│
├── notebooks/
│   └── retail_sales_analysis.ipynb
│
├── README.md
└── requirements.txt
```

---

## How to Run

1. Clone or download the repository.
2. Open the project in VS Code.
3. Activate the project virtual environment.
4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Open:

```text
notebooks/retail_sales_analysis.ipynb
```

6. Run the notebook cells from top to bottom.

---

## Project Outcome

This project demonstrates practical skills in:

* Data cleaning
* Pandas
* NumPy
* Feature engineering
* GroupBy and aggregation
* Business metrics
* Profitability analysis
* Data visualization
* Business insight generation

The project focuses not only on **what happened in the data**, but also on **what a business should investigate next** based on those findings.
