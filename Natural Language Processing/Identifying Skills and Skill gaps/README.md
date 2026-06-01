# Measuring the readiness of the UK Civil Service to deliver ambitious change

## Problem
At the time of this analysis, a new admistration in the UK was committed to a set of five missions in order to "put an end to sticking plaster politics". A mission-driven approach to governing is a [...]

In many ways, this approach makes greater demands on government bureaucracies. However, there were no data driven insights available into, on the one hand, the skills that governments need to draw [...]

This research filled those gaps. Its findings were described by an expert external reviewer as "a substantial advance on academic or professional thinking."

## Methodology
Without direct access to people data in the UK Civil Service, job vacancies issued through the UK Civil Service Recruitment Gateway were treated as proxy meansures of the skills that they recognis[...]

Alongside this, a corpus of expert writings on 'Mission driven change was collected. This amounted to over one million words of writing and covered perspectives that ranged from 'making the case' [...]

A bottom-up process was used to identify the skills that were mentioned in this corpus. For example, skills such as 'creating a coalition' or 'experiementation' were identified. These were then tr[...]

## Data
The analysis is based on 35 documents from the literature, and nearly 5,000 civil service vacancies.

## Results
A heat-map comparison of how important a skill is in expert literature compared to its importance in the bank of Civil Service job vacancies shows this picture:

![Preview](./Heatmap.png)

For example, it shows that the skill of 'experimenation' is a key capability gap.

**How to Reproduce**

The four files in this repository are executed in the following sequence:

One: Vacancy Scraper - to web-scrape Civil Service vacancies

Two: Skill_Patterns - to create the .json file of patterns that are used for matching in the other two files

Three: Skills_ID - to identify the skills, and their importance, in the corpus of expert literature

Four: Gap_Analysis - to identify the difference, in importance, that the skills recieve in expert literatures Vs in Civil Service Vacancies
