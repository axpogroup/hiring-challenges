# Trainee Data Engineer Challenge: Daily Electricity Flows Analysis

## Intro

Welcome to the Data Engineering Traineeship Challenge! In this challenge,
you will work with real-world electricity flow data for Switzerland.
Your task is to analyze the daily electricity flows into and out of Switzerland,
identify trends, and present meaningful insights.
This exercise will test your data engineering, analysis, and communication skills.

## Objective

The goal of this challenge is to analyze hourly electricity flow data, aggregate it into daily totals,
and generate insights that can help optimize Swit-zerland's electricity imports and exports.

## Dataset Description

You will be provided with a dataset that contains hourly electricity flows into and out of
Switzerland for different neighboring countries. The dataset has the following columns:

* Datetime: Timestamp of the record (including time zone offset)
* AT_CH_MWh: Electricity imported from Austria (in MWh)
* DE_CH_MWh: Electricity imported from Germany (in MWh)
* FR_CH_MWh: Electricity imported from France (in MWh)
* IT_CH_MWh: Electricity imported from Italy (in MWh)
* CH_AT_MWh: Electricity exported to Austria (in MWh)
* CH_DE_MWh: Electricity exported to Germany (in MWh)
* CH_FR_MWh: Electricity exported to France (in MWh)
* CH_IT_MWh: Electricity exported to Italy (in MWh)
* Nettoimport: Net electricity imports (Total imports - Total exports)

The dataset can be downloaded here:
https://opendata.swiss/de/dataset/energiedashboard-ch-tagliche-flusse-in-die-und-aus-der-schweiz-strom

## Your mission, should you choose to accept it:

Below are the tasks you need to complete as part of this challenge:

### 1. Data Preparation

* Parse the data to get it in a usable format.
* Aggregate the data to compute daily, weekly and monthly totals for each flow column.
* Add calculated columns for total daily imports and exports.

### 2. Exploratory Data Analysis

* Visualize daily electricity imports and exports for Switzerland over time.
* Identify peak import/export days and trends (e.g., seasonal variations).
* Determine which country contributes the most to imports and ex-ports.

### 3. Insights and Recommendations

* Calculate the daily net balance of electricity (Netto Import).
* Identify periods of net exports and net imports.
* Provide recommendations for balancing Switzerland’s electricity flows based on your findings.

### 4. Advanced (Optional)

* Correlate electricity flows with external factors, such as seasonality (e.g., winter vs. summer).
* Build a simple forecasting model to predict net imports for the next week.

## Submission Instructions

Please submit your completed analysis and code in the following format:

* The source code with your data preparation, analysis, and visualizations.
* A brief presentation (in PowerPoint) summarizing your approach, findings and recommendations,
  which you will present on the selection day.
* Ensure your submission is well-documented and easy to follow.

## Evaluation Criteria

You will be evaluated based on the following criteria:

* Data Preparation: Correctness and completeness of data preprocessing.
* Visualization: Clarity and informativeness of visualizations.
* Insights and Recommendations: Depth and practicality of in-sights.
* Code Quality: Readability, documentation, and efficiency of your code.

Good Luck!

We look forward to seeing your analysis and solutions. Good luck with the challenge!
