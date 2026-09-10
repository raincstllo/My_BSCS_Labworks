# Step 1: Create the SparkSession

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, count

spark = SparkSession.builder \
    .appName("Lab Activity 3") \
    .master("local[*]") \
    .getOrCreate()

# Step 2: Load the CSV Dataset: summative_assessment.csV

df = spark.read.csv(
    "summative_assessment.csv",
    header=True,
    inferSchema=True
)

# Step 3: Inspect the Dataset

print("Schema:")
df.printSchema()

print("First 10 Records:")
df.show(10) # Action - show()

print("Number of Records: ", df.count()) # Action - count()

# Step 4: Create a Calculated Column

# Transformation - withColumn()
performance_df = df.withColumn(
    "AverageAssessment",
    (col("QuizScore") + col("MidtermScore") + col("FinalScore")) / 3
)

# Transformation - Select
print("Average Assessment:")
performance_df.select(
    "StudentID",
    "QuizScore",
    "MidtermScore",
    "FinalScore",
    "AverageAssessment"
).show() # Action - show()

# Step 5: Identify High-Performing Students

# Transformation - Filter
high_performers = df.filter(
    (df["FinalScore"] >= 90) &
    (df["Attendance"] >= 95)
)

# Transformation - Select
print("High Performers:")
high_performers.select(
    "StudentID",
    "Program",
    "FinalScore",
    "Attendance"
).show(10) # Action - show()

# Step 6: Calculate Overall Statistics
# Calculate:

print("Average Final Score:")
df.select(avg("FinalScore")).show() # Transformation - Select # Action - show()

print("Highest Final Score:")
df.select(max("FinalScore")).show() # Transformation - Select # Action - show()

print("Lowest Final Score:")
df.select(min("FinalScore")).show() # Transformation - Select # Action - show()

print("Number of Students: ")
df.select(count("StudentID")).show() # Transformation - Select # Action - show() # Action - count()

# Step 7: Analyze Performance by Program

# Transformation - groupBy()
df_byprog = df.groupBy("Program").agg(
    count("StudentID").alias("NumberOfStudents"), # Action - count()
    avg("FinalScore").alias("AverageFinalScore"),
    max("FinalScore").alias("HighestFinalScore"),
    min("FinalScore").alias("LowestFinalScore"),
)

print("By Program:")
df_byprog.show() # Action - show()

# Step 8: Analyze Learning Modality

# Transformation - groupBy()
df_learningmodal = df.groupBy("LearningModality").agg(
    count("StudentID").alias("NumberOfStudents"), # Action - count()
    avg("FinalScore").alias("AverageFinalScore")
)

print("By Learning Modality:")
df_learningmodal.show() # Action - show()

# Step 9: Create a Combined Analysis

# Transformation - Filter
combined_analysis = df.filter(
    (df["StudyHours"] >= 10) &
    (df["Attendance"] >= 90) &
    (df["FinalScore"] >= 90)
)

print("Combined Analysis:")
# Transformation - Select
combined_analysis.select(
    "StudentID",
    "Program",
    "StudyHours",
    "Attendance",
    "FinalScore",
).show() # Action - show()

# Step 10: Identify Transformations and Actions
# Look at comments that serve as labeling

# Step 11: Explain Lazy Evaluation
"""
Spark uses lazy evaluation so it can wait until an action is requested before
executing transformations. This allows Spark to optimize the entire sequence
of operations and execute them more efficiently.
"""

# Step 12: Explain collect()
"""
collect() should be used carefully because it brings all the data from the Spark
cluster into the driver's memory. For large datasets, this can use too much memory
and may cause the program to slow down or crash.
"""

# Step 13: Data Interpretation

# 1. Which program has the highest average FinalScore?
""" BSDS with an AVG of 89.0625 """
# 2. Which program has the lowest average FinalScore?
""" BSIT with an AVG if 89.0 """
# 3. Which learning modality has the highest average FinalScore?
""" Blended with an Average Final SCore of 93.3529411764706 """
# 4. How many students meet all three conditions in Step 9?
""" 24 """
# 5. What general pattern can you observe from the results?
""" I noticed that all programs have almost the same average but
blended learning students excel more than those in the other
learning modalities. """

# Step 14: Stop Spark

spark.stop()