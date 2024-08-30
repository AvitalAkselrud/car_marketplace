import pandas as pd
import plotly.express as px
import streamlit as st

data=pd.read_csv('vehicles_us.csv')

st.title("Let's choose a car!")
st.subheader('Use this app to select the best car for you')


# Display the image
st.image('mainimage.jpg', caption='Choose the car that speaks to you', use_column_width=True)

#Slider

price_range = st.slider(
     "Set the price range", 
     min_value=200, max_value=70000, value=(200,70000))

actual_range=list(range(price_range[0],price_range[1]+1))
filtered_data=data[data.price.isin(actual_range)]

# Histograph
condition_order = data['condition'].value_counts().index.tolist()

fig1 = px.histogram(data, x='condition', title='Distribution of Condition',
                    category_orders={'condition': condition_order})

st.plotly_chart(fig1)

# Checkbox
data_grouped = data.groupby(['type', 'condition']).size().reset_index(name='count')

stacked = st.checkbox('Stacked Bar Chart', value=True)

barmode = 'stack' if stacked else 'group'

fig_type6 = px.bar(data_grouped, x='type', y='count', color='condition', 
                   title='Type vs. Condition',
                   labels={'type': 'Type', 'count': 'Count', 'condition': 'Condition'},
                   color_discrete_sequence=px.colors.qualitative.Plotly,
                   barmode=barmode)

fig_type6.update_layout(yaxis_title='Count')

st.plotly_chart(fig_type6)

# Scatter Plot
filtered_data = data[data['price'] < 20000]

fig7 = px.scatter(filtered_data, x='model', y='price', color='type',
                 title='Model vs. Price (Colored by Type, Under 20k)',
                 labels={'model': 'Model', 'price': 'Price', 'type': 'Type'})

st.plotly_chart(fig7)