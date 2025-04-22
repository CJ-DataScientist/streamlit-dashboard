import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import statsmodels.api as sm
# Load the dataset
data = pd.read_csv('Cleaned_BSS_Retail_Data.csv')
#data = pd.read_csv('FileFoldersSKU6.csv')

# App Title and Description
st.write("Team 05 ADTA5410")
st.title("BSS Retail Analysis")

st.header("Introduction")
st.write("The objective is to investigate how advertising cost impacts sales and profit")

# Sidebar Filters
st.sidebar.header("Filter Options")   #give a title for the sidebar menu

# Sidebar selection
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
selected_col = st.sidebar.selectbox("Select a variable to visualize:", numeric_columns)
sku_list = data['sku'].unique().tolist()
selected_sku = st.sidebar.selectbox("Select SKU to visualize:", sku_list)


st.header("Data Exploration")
## Add a histogram
# Section: Distribution of the Numerical Variables
#st.header("Distribution of the Numerical Variables")
st.write("This histogram shows the distribution of the selected numerical variable")

# Plot histogram
if selected_col:
    st.subheader(f"Histogram of '{selected_col}'")
    fig, ax = plt.subplots()
    ax.hist(data[selected_col].dropna(), bins=30, color="skyblue", edgecolor="black")
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)



# Adding a Scatter Plot
#st.header("Scatter Plot: Sales vs. Advertisement Costs")
st.write("This scatter plot shows the relationship between sales and advertising costs for the selected sku")
# Filter data based on selected SKU
filtered_df = data[data['sku'] == selected_sku]

# Scatter plot
st.subheader(f"Sales vs Advertising Costs for SKU: {selected_sku}")
fig, ax = plt.subplots()
ax.scatter(filtered_df['adspend'], filtered_df['sales'], color="green", alpha=0.7)
ax.set_xlabel("Advertising Costs")
ax.set_ylabel("Sales")
ax.set_title(f"{selected_sku}")
st.pyplot(fig)


# Adding a Scatter Plot
#st.header("Scatter Plot: Profit vs. Units Ordered")
st.write("This scatter plot shows the relationship between profit and Units Ordered for the selected sku")
# Filter data based on selected SKU
#filtered_df = data[data['sku'] == selected_sku]

# Scatter plot
st.subheader(f"Profit vs Units Ordered for SKU: {selected_sku}")
fig, ax = plt.subplots()
ax.scatter(filtered_df['profit'], filtered_df['unitsordered'], color="orange", alpha=0.7)
ax.set_xlabel("Profit")
ax.set_ylabel("Units Ordered")
ax.set_title(f"{selected_sku}")
st.pyplot(fig)



st.header("Insights")
st.write("*Advertising costs have significant influence on sales")
st.write("*As customers order more units, profit increases significantly")

st.header("Recommendations")
st.write("*Heavily investing in advertising and formulating strategies that will help boost sales for BSS Retail using advertising")
st.write("*Implementing incentives towards bulk ordering, which will encourage customers to purchase in larger quantities, thereby increasing profit")



## Add a correlation matrix

# Section: Correlation Matrix
#st.header("Correlation Matrix")
#st.write("Check the box to view the correlation matrix for numerical variables.")

#continuous_vars = ['price', 'unitsordered','cogs','adspend','profit']

# Show correlation matrix
#if st.checkbox("Show Correlation Matrix"):
#    corr_matrix = data[continuous_vars].corr()
#    fig, ax = plt.subplots(figsize=(8, 6))
#    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
#    st.pyplot(fig)