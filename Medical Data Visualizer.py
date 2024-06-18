import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

df= pd.read_csv("medical_examination.csv")
df

df.info()
df.shape
df.describe().T

# Create the 'overweight' column in the df variable
# Calculate BMI
df['bmi']= df['weight'] / ((df['height'] / 100) ** 2) 

# Create 'overweight' column
df['overweight']= np.where(df['bmi'] > 25, 1, 0)

# Verify 'overweight' column
df.head()

# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)
df

# Convert the data into long format
melted_df= pd.melt(df, id_vars= ['id', 'cardio'], value_vars= ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'sex'])
melted_df


# Clean the data
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]



# Draw the categorical plot
chart = sns.catplot(data=melted_df, x='value', col='cardio', kind='count', col_wrap=2, hue='variable', palette='Set1')
chart.set_xticklabels(horizontalalignment='right')
chart.fig.subplots_adjust(top=0.9)
chart.fig.suptitle('Value Counts of Categorical Features by Cardio', fontsize=16)


# Calculate the correlation matrix
corr = df.corr()



# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

fig, ax =  plt.subplots(figsize=(11, 9))
sns.heatmap(corr, mask=mask, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".1f", ax=ax)






















