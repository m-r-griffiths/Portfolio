# Clustering 1,400 cities

## Problem
In order to get feedback from key stakeholders, there was a need to quickly develop an MVP to show how Cities could be grouped into clusters that resonated with City leaders. 

## Methodology
Seven data sets from the OECD were identified that presented data, at a City level, on features such as population density and exposure to risks such as flooding or pollution. APIs were used to access this data.

The Elbow method was used with Within Cluster Sum of Squares (WCSS), silhouette scores and a dendogram to identify the right k value for Clustering. For visiualisation, t_SNE dimensonality reduction, and radar plots using Plotly presented the results.

## Business Impact
The MVP provided a visual way to engage senior leaders with what would otherwise be very abstract questions. For example, by asking them questions such as 'do you recognise yourself in this peer group of Cities?', or 'what data is missing that is needed to fully refelect the context you operate in?"
