# Unit 2 — Student Performance Analysis

## Overview

This laboratory activity focuses on using **PySpark DataFrames** to transform and analyze student performance data.

The dataset used for this activity is `summative_assessment.csv`. The analysis calculates assessment averages, identifies high-performing students, produces overall statistics, and compares performance across academic programs and learning modalities.

## Objectives

* Load and inspect a structured CSV dataset using PySpark.
* Create calculated columns using DataFrame transformations.
* Filter students based on multiple conditions.
* Calculate overall statistics from a dataset.
* Group and summarize data by program and learning modality.
* Identify DataFrame transformations and actions.
* Understand Spark's lazy evaluation.
* Understand why `collect()` should be used carefully with large datasets.
* Interpret analytical results from the processed data.

## Tasks

### 1. Create a SparkSession

Create a local `SparkSession` for running the PySpark program.

### 2. Load the Dataset

Load:

```text
summative_assessment.csv
```

### 3. Inspect the Dataset

Display:

* Schema
* First 10 records
* Number of records

### 4. Calculate Average Assessment

Create a new column called `AverageAssessment` using:

```text
(QuizScore + MidtermScore + FinalScore) / 3
```

Store the resulting DataFrame as `performance_df`.

Display:

* `StudentID`
* `QuizScore`
* `MidtermScore`
* `FinalScore`
* `AverageAssessment`

### 5. Identify High-Performing Students

Find students who meet **both** conditions:

* `FinalScore >= 90`
* `Attendance >= 95`

Store the result as `high_performers`.

Display:

* `StudentID`
* `Program`
* `FinalScore`
* `Attendance`

### 6. Calculate Overall Statistics

Calculate:

* Average `FinalScore`
* Highest `FinalScore`
* Lowest `FinalScore`
* Number of students

Display the results clearly.

### 7. Analyze Performance by Program

Group students by `Program`.

For each program, calculate:

* `NumberOfStudents`
* `AverageFinalScore`
* `HighestFinalScore`
* `LowestFinalScore`

### 8. Analyze Learning Modality

Group students by `LearningModality`.

Calculate:

* `NumberOfStudents`
* `AverageFinalScore`

### 9. Combined Student Analysis

Identify students who meet **all three** conditions:

* `StudyHours >= 10`
* `Attendance >= 90`
* `FinalScore >= 90`

Display:

* `StudentID`
* `Program`
* `StudyHours`
* `Attendance`
* `FinalScore`

### 10. Identify Transformations and Actions

Add comments to the code identifying at least:

**Four transformations**, such as:

* `select()`
* `filter()`
* `withColumn()`
* `groupBy()`

**Two actions**, such as:

* `show()`
* `count()`
* `first()`

### 11. Explain Lazy Evaluation

Add a 2–3 sentence comment or docstring explaining:

> Why does Spark use lazy evaluation?

### 12. Explain `collect()`

Add a 2–3 sentence comment or docstring explaining:

> Why should `collect()` be used carefully when processing large datasets?

### 13. Interpret the Results

Answer the following based on the program's output:

1. Which program has the highest average `FinalScore`?
2. Which program has the lowest average `FinalScore`?
3. Which learning modality has the highest average `FinalScore`?
4. How many students meet all three conditions from the combined analysis?
5. What general pattern can be observed from the results?

### 14. Stop Spark

End the program by properly stopping the Spark session:

```python
spark.stop()
```

## Concepts Practiced

* PySpark
* SparkSession
* DataFrames
* CSV data loading
* DataFrame inspection
* Calculated columns
* `withColumn()`
* `select()`
* `filter()`
* Multiple conditions
* `groupBy()`
* Aggregation
* Transformations
* Actions
* Lazy evaluation
* `collect()`
* Data interpretation
