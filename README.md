# RFM Analysis with K-Means Clustering
## Overview
This project leverages RFM Analysis (Recency, Frequency, and Monetary) and K-Means Clustering to create data-driven customer segments for retail businesses. The goal is to improve customer targeting, enhance marketing strategies, and drive business growth by replacing manual or static segmentation methods.

The project is integrated with Streamlit to provide an interactive dashboard for stakeholders to visualize and explore customer clusters dynamically.

# Why RFM + K-Means?
## Limitations of Manual Segmentation:
Static: Relies on arbitrary thresholds, which don’t adapt to changes in customer behavior.

Time-Consuming: Manual segmentation is inefficient for large datasets.

Simplistic: Lacks granularity, leading to missed opportunities for personalized marketing.

## Advantages of RFM with K-Means
Dynamic Grouping: Automatically identifies patterns in customer behavior.

Scalable: Handles large datasets efficiently.

Actionable Insights: Segments customers based on real purchasing patterns, enabling tailored marketing and loyalty strategies.

# Key Features

## Streamlit:
Visualize customer clusters interactively.

Understand cluster-wise behavior based on average Recency, Frequency, and Monetary values.

## Data-Driven Customer Segments:
Clusters like Gold, Platinum, and Inactive identified for specific marketing actions.

## End-to-End Workflow:
RFM metric calculation.

Optimal cluster identification using K-Means and the Elbow Method.

Clear visualizations for insights and decision-making.

# Methodology

## RFM Analysis:
Recency: Days since last purchase.

Frequency: Number of transactions.

Monetary: Total amount spent.

## K-Means Clustering:
Standardized RFM data.

Determined the optimal number of clusters using the Elbow Method.

Applied K-Means to dynamically segment customers.

## Visualization:
Combined bar and line charts for cluster distribution and average RFM feature values.

Interactive Streamlit-based dashboard for easy exploration.

# Results and Insights
## Cluster Overview

| **Cluster Name**         | **Key Characteristics**             | **Actionable Strategies**                          |
|---------------------------|--------------------------------------|---------------------------------------------------|
| **Gold**                 | High activity, moderate spending    | Retain with loyalty programs and discounts.       |
| **Inactive**             | Low recency and activity            | Launch re-engagement campaigns.                   |
| **Platinum & Super Platinum** | High spending customers            | Provide VIP experiences and exclusive perks.       |
| **Occasional & Moderate**| Average activity and spending       | Use targeted promotions to boost engagement.      |

## Visualization (from Streamlit):
The chart below illustrates customer distribution and average RFM values for each cluster:

Gold Cluster: Largest in size with significant customer activity.

Platinum & Super Platinum: Top spenders driving revenue.

Inactive Cluster: Requires immediate reactivation efforts.
  

# Tools and Technologies
## Python Libraries:
Data Processing: pandas, numpy.

Clustering: scikit-learn.

Visualization: matplotlib, seaborn.

Dashboard: Streamlit.

# Business Value
This solution empowers retailers to:

Identify high-value customers for targeted retention strategies.

Reactivate inactive customers with personalized campaigns.

Increase customer lifetime value through tailored offers.
