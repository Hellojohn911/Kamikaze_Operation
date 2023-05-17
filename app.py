#We will import the necessary libraries for the analysis. We will use pandas for data manipulation, numpy for numerical calculations, and matplotlib for data visualization.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#We will import the dataset and store it in a variable called data. We will use the read_csv function from pandas to read the csv file.

data = pd.read_csv('CCR.csv')

#We will use the head function to display the first 5 rows of the dataset.

data.head()

#We will use the describe function to get a statistical summary of the dataset". T is used to transpose the data."

data.describe().T

#We will use the info function to get a concise summary of the dataset.

data.info() 

print("*"*100)
#We will use the isnull function to check for missing values in the dataset.

data.isnull().sum()

#We will use the value_counts function to get the count of unique values in the dataset.

data.value_counts()

def CS_Category(CreditScore):
    if CreditScore >= 300 and CreditScore < 580:
        CreditScore = 'Very Poor'
    elif CreditScore >= 580 and CreditScore < 670:
        CreditScore = 'Fair'
    elif CreditScore >= 670 and CreditScore < 740:
        CreditScore = 'Good'
    elif CreditScore >= 740 and CreditScore < 800:
        CreditScore = 'Very Good'
    elif CreditScore >= 800 and CreditScore <= 850:
        CreditScore = 'Exceptional'
    return CreditScore

#We will add a new column called age_category to the dataset.

data['CS_Category'] = data['CreditScore'].apply(CS_Category)

data.head()

#We will use the nuninque function to get the number of unique values in each column.

data.nunique()

def age_cat(Age):
    if Age <=30:
        Age= 'young'
    elif Age >30 and Age <=50:
        Age= 'middle'
    else:
        Age= 'old'
    return Age

data['age_category'] = data['Age'].apply(age_cat)

#We will use the drop_duplicates function to remove duplicate rows from the dataset.

data.drop_duplicates(inplace=True)

#We will use the shape function to get the number of rows and columns in the dataset.

data.shape

#We will use the drop function to remove the columns that are not needed for the analysis.

data.drop(['CustomerId','Surname'],axis=1,inplace=True)

# We will compare the age of the customers with the number of complaints.
data.groupby("age_category")["Complain"].value_counts()

# We will compare the age of the customers with the number of exited customers.
data.groupby("age_category")["Exited"].value_counts()

# We will compare gender with the number of complaint customers.
data.groupby("Gender")["Complain"].value_counts()

# We assign the values 1 and 0 to the columns that have categorical values.
data['Complain'].replace({1: 'Yes', 0: 'No'} ,inplace=True)

# We will make a data frame to compare the age of the customers with the number of complaints.
grouped_df = data.groupby(['age_category', 'Complain']).size().reset_index(name='Count')
grouped_df

# We will compare the age of the customers with the activity of customers.
data.groupby("age_category")["IsActiveMember"].mean()

#  We will compare activity of customers with the number of complaints.
data.groupby("IsActiveMember")["Complain"].value_counts()

# We will compare the complaints of customers with the estimated salary of customers.
data.groupby("Complain")["EstimatedSalary"].sum() 

# We will compare the age of the customers with the Credit Score Ranks of customers.
data.groupby("age_category")["CS_Category"].value_counts()

# create a bar chart to visualize the count of each category
data['age_category'].value_counts().plot(kind='bar', figsize=(10, 6), rot=0, color='blue', fontsize=15, ylabel='Count', xlabel='Age Category', title='Count of Age Category', grid=True, legend=True)

# create a bar chart to visualize the count of each category
data['CS_Category'].value_counts().plot(kind='bar', figsize=(10, 6), rot=0, color='red', fontsize=15, ylabel='Count', xlabel='Credit Score Category', title='Count of Credit Score Category', grid=True, legend=True)

# create a bar chart to visualize the count of each category
data['Geography'].value_counts().plot(kind='bar', figsize=(10, 6), rot=0, color='green', fontsize=15, ylabel='Count', xlabel='Country', title='Count of Country', grid=True, legend=True)

# create a bar chart to visualize the count of each category
data['Card Type'].value_counts().plot(kind='bar', figsize=(10, 6), rot=0, color='yellow', fontsize=15, ylabel='Count', xlabel='Card Type', title='Count of Card Type', grid=True, legend=True)

import plotly.express as px

# Calculate complaints for age category and complain
grouped_df = data.groupby(['IsActiveMember', 'Complain']).size().reset_index(name='Count')

# Create the plot
fig = px.bar(grouped_df, x='IsActiveMember', y='Count', color='Complain', barmode='group',
             title='Comparing Complaints with Active Customers',
             labels={'IsActiveMember': 'Is Customer Active?', 'Count': 'Is Customer Complaining?'})

# Show the plot
fig.show()

import plotly.express as px

# Calculate complaints for age category and complain
grouped_df = data.groupby(['CS_Category', 'age_category']).size().reset_index(name='Count')

# Define the desired order of CS_Category
cs_category_order = ['Very Poor', 'Fair', 'Good', 'Very Good', 'Exceptional']

# Create the plot
fig = px.bar(grouped_df, x='CS_Category', y='Count', color='age_category',
             title='Comparing Credit Score Ranks with Age Categories',
             labels={'CS_Category': 'Age Categories', 'Count': 'Credit Score Ranks'},
             category_orders={'CS_Category': cs_category_order})

# Customize the layout
fig.update_layout(barmode='group')
fig.update_traces(marker_opacity=0.8)

# Show the plot
fig.show()

import plotly.express as px

# Calculate complaints for age category and complain
grouped_df = data.groupby(['age_category', 'Complain']).size().reset_index(name='Count')

# Define the desired order of age_category
age_category_order = ['Young', 'Middle', 'Old']

# Create the plot
fig = px.bar(grouped_df, x='age_category', y='Count', color='Complain',
             title='Comparing Complaints with Age Categories',
             labels={'age_category': 'Age Categories', 'Count': 'Complaining Values'},
             category_orders={'age_category': age_category_order})

# Customize the layout
fig.update_layout(
    barmode='group',
    plot_bgcolor='white',  # Set plot background color to white
    paper_bgcolor='white',  # Set plot paper background color to white
    font_family='Arial',
    font_color='black',
    legend=dict(
        title='Complain',
        orientation='h',
        yanchor='top',
        y=-0.2,
        xanchor='center',
        x=0.5
    ),
    xaxis=dict(
        title='Age Categories',
        tickfont=dict(size=12),
        showgrid=False,
        showline=True,
        linewidth=1,
        linecolor='gray'
    ),
    yaxis=dict(
        title='Complaining Values',
        tickfont=dict(size=12),
        showgrid=True,
        gridcolor='lightgray',
        gridwidth=0.5,
        zeroline=False,
        showline=True,
        linewidth=1,
        linecolor='gray'
    )
)

# Update bar colors
fig.update_traces(marker=dict(line=dict(width=0.5, color='black')), opacity=0.8)

# Show the plot
fig.show()
