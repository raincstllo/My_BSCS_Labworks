# Unit 2 Lab 2 — PySpark Data Acquisition and Inspection

## Overview

This laboratory activity focuses on using **PySpark DataFrames** to acquire, inspect, select, and filter structured data from a CSV file.

The dataset used for this activity is `book_sales.csv`, which contains book sales records.

## Objectives

* Create a `SparkSession` in a local Spark environment.
* Load a CSV dataset into a PySpark DataFrame.
* Inspect the DataFrame's columns, schema, records, and row count.
* Select specific columns from the dataset.
* Filter records based on sales conditions.
* Apply multiple filtering conditions.
* Identify DataFrame transformations in the code.
* Properly stop the Spark session after execution.

## Tasks

### 1. Create a SparkSession

Create a local `SparkSession` to run the PySpark program.

### 2. Load the Dataset

Load `book_sales.csv` using `spark.read.csv()` with:

* `header=True`
* `inferSchema=True`

### 3. Inspect the Dataset

Display:

* Column names
* DataFrame schema
* First 10 records
* Total number of records

### 4. Select Sales Information

Create a new DataFrame called `sales_data` containing:

* `Book_Title`
* `Category`
* `Quantity`
* `Price`
* `Total_Sale`

### 5. Find High-Value Sales

Create a DataFrame called `high_sales` containing records where:

`Total_Sale >= 5000`

Display:

* `Book_Title`
* `Quantity`
* `Total_Sale`
* `Sale_Level`

### 6. Find Qualified Sales

Create a DataFrame called `qualified_sales` containing records where both conditions are met:

* `Quantity >= 10`
* `Total_Sale >= 5000`

Display:

* `Book_Title`
* `Quantity`
* `Price`
* `Total_Sale`

### 7. Identify Transformations

Add comments in the code to identify DataFrame operations that are **transformations**.

At least two transformations should be identified.

Examples include:

* `select()`
* `filter()`

### 8. Stop Spark

End the program by properly stopping the Spark session:

```python
spark.stop()
```

## Concepts Practiced

* PySpark
* `SparkSession`
* DataFrames
* CSV data acquisition
* Schema inspection
* `select()`
* `filter()`
* DataFrame transformations
* Multiple filtering conditions
* Local Spark execution
