End-to-End Analysis of Global Video Game Sales
Project Overview
This project provides an in-depth analysis of the global video game market, utilizing a dataset of over 16,000 titles from 1980 to 2016. The goal of this analysis was to identify key trends, understand market dynamics, and extract actionable insights into consumer preferences, publisher performance, and the impact of critical reception on commercial success.

The entire project workflow, from data extraction and querying to final visualization, was handled using SQL for data analysis and Python for creating a visual dashboard.

Dataset
The dataset used for this analysis is the "Video Game Sales with Ratings" dataset, sourced from Kaggle.

Source: Kaggle Video Game Sales Dataset

Content: Contains 16,719 records of video game sales, including details on platform, genre, publisher, and sales figures for North America, Europe, Japan, and other regions.

Tools Used
Database: SQLite (managed via DB Browser for SQLite)

Data Querying: Advanced SQL (including CTEs, Window Functions, and Aggregates)

Data Visualization & Analysis: Python

Libraries: Pandas (for data manipulation), NumPy (for numerical operations), Matplotlib (for plotting)

SQL Analysis & Key Insights
Five key business questions were explored using advanced SQL queries to segment and analyze the data. The visualizations for these insights were generated using Python.

1. Market Leaders by Genre
Business Question: Who is the dominant publisher in each major game genre, and what does this say about market concentration?

Insight: The analysis reveals that publishers like Nintendo and Electronic Arts dominate multiple high-value genres (Platform, Sports, Racing, etc.), indicating strong brand loyalty and market control in specific categories.

2. Platform Lifespan vs. Commercial Success
Business Question: Does a longer market presence (lifespan) for a gaming platform correlate with higher total sales?

Insight: The scatter plot shows a positive but not perfect correlation. While platforms like the PS2 had both a long lifespan and high sales, others like the PC have an extremely long lifespan but more moderate total sales compared to dedicated consoles, suggesting that market longevity alone does not guarantee commercial dominance.

3. Regional Consumer Preferences
Business Question: How do gaming tastes differ between the North American and Japanese markets?

Insight: There are stark differences in market preferences. Genres like Shooter and Sports are vastly more popular in North America, whereas Role-Playing games are uniquely dominant in Japan, outselling even Action games. This highlights the need for regionally-tailored marketing and development strategies.

4. Impact of Critic Scores on Sales
Business Question: Is there a clear financial return on quality? Do games with higher critic scores sell better on average?

Insight: The data shows a strong, positive correlation. Critically acclaimed games (90+) have significantly higher average sales than games with mixed or poor reviews. This confirms that critical quality is a strong driver of commercial success.

5. Evolution of Genre Popularity by Decade
Business Question: How have the most popular game genres evolved from the 1980s to the 2010s?

Insight: The market has seen a dramatic shift. Platform games, which dominated the 80s and 90s, have been overtaken by Action games, which became the undisputed market leader in the 2000s and 2010s. The Shooter genre also shows a significant rise in popularity in the modern era.

