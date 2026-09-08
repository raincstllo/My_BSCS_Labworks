# Step 1: Create the SparkSession

from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Lab Activity 2") \
    .master("local[*]") \
    .getOrCreate()

# Step 2: Load the CSV Dataset: book_sales.csv

df = spark.read.csv(
    "book_sales.csv",
    header=True,
    inferSchema=True
)

# Step 3: Inspect the Dataset

print("========== COLUMNS ==========")
print(df.columns)

print("\n========== SCHEMA ==========")
print(df.schema)

print("\n========== FIRST 10 RECORDS ==========")
df.show(10)

print("\n========== NUMBER OF RECORDS ==========")
print(df.count())

# Step 4: Select Required Columns

# Transformation (Select)
sales_data = df.select(
    "Book_Title",
    "Category",
    "Quantity",
    "Price",
    "Total_Sale"
)

sales_data.show()

# Step 5: Filter High Sales

# Transformation (Filter)
high_sales = df.filter(df["Total_Sale"] >= 5000)

# Transformation (Select)
high_sales.select(
    "Book_Title",
    "Quantity",
    "Total_Sale",
    "Sale_Level"
).show()

# Step 6: Apply Multiple Conditions

# Transformation (Filter)
qualified_sales = df.filter(
    (df["Quantity"] >= 10) &
    (df["Total_Sale"] >= 5000)
)

# Transformation (Select)
qualified_sales.select(
    "Book_Title",
    "Quantity",
    "Price",
    "Total_Sale"
).show()

# Step 7: Identify Transformations
# Look at "Transformation" comments that serve as labeling

# Step 8: Stop Spark

spark.stop()