# -*- coding: utf-8 -*-
"""Project_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FS9SbA6P0z62ZVPKSQb4M4wcdhBynR6e
"""

import pandas as pd
import numpy as np

## Q1: Write Pandas  code to read olympix_data.csv file"""
df = pd.read_csv('/content/olympix_data_organized_with_header (1).csv')
df

## Q2: Write Pandas code to print the Olympic Sports/games in the dataset."""
df['sports'].unique()

## Q3: Write Pandas code to plot the total number of medals in  each Olympic Sport/game. Sort the result based on the the total number of medals.
df.groupby(by = 'sports')['total_medal'].sum()

### Q4: Find the total number of medals won by each country in swimming.
df_swimming = df[df['sports'] == 'Swimming']
total_medals_swimming_per_country = df_swimming.groupby('country')['total_medal'].sum()
total_medals_swimming_per_country

### Q5: Find the total number of medals won by each country in Skeleton.
df_skeleton = df[df['sports'] == 'Skeleton']
total_medals_skeleton_per_country = df_skeleton.groupby('country')['total_medal'].sum()
total_medals_skeleton_per_country

### Q6 Find the number of medals that the US won yearly.
df_US = df[df['country'] == 'United States']
df_win_yearly_US = df_US.groupby('year')['total_medal'].sum()
df_win_yearly_US

### Q7 Find the total number of medals won by each country.
df.groupby('country')['total_medal'].sum()

### Q8 Who was the oldest athletic in the olympics? whcih country was he/she from?
max_age = df['age'].max()
df_oldest = df[df['age'] == max_age][['name','country']]
df_oldest