import streamlit as st
import pandas as pd
import plotly.express as px

# Load in the January P & L data
df = pd.read_csv(('./resources/master_filtered.csv'), index_col = [0])
df['DESCRIPTION'] = df.index




st.sidebar.subheader('Select a category to filter by')
sidebar_selection = st.sidebar.selectbox(label = "Select an Option",options=['Home Page','Forecast Variance', 'Last Year Variance'])

if sidebar_selection == 'Home Page':
    st.header('Margaritaville January P & L')
    st.markdown('##### Select an option on the sidebar to continue.  P & L can be sorted by values in the forecast variance\
    columns by total amount or percentage of revenue.  The same can be done for comparisons to last year.  You can then view charts of the P & L filtered by\
        your selections.  The charts are interactive and can be zoomed in on.  Hover over the bars to see the exact values.\
            Click on the legend to hide or show the data.  Click on the chart to expand it.')


elif sidebar_selection == 'Forecast Variance':
    forecast_choice = st.sidebar.radio(label = "Select an option", options = ['Total Variance Amount', "Variance as Percentage of Revenue"])
    if forecast_choice == 'Total Variance Amount':
        # Sort the data by the forecast variance amount
        total_fc_var = df.sort_values(by = 'FC_VARIANCE_AMT', ascending = False)
        
        # Create a select box that allows the user to select top 20 or bottom 20 and then display the data with a plotly bar chart
        fc_var_selection = st.selectbox(label = "Select an option", options = ['Top Positive Variance Amounts', "Top Negative Variance Amounts"])
        if fc_var_selection == 'Top Positive Variance Amounts':
            # Create a plotly bar chart with top x forecast variance amounts
            fc_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            top_fc_var = total_fc_var.iloc[0:int(f'{fc_total_slider}')]
            st.markdown('##### Hover over chart and expand for a better view')
            fig = px.bar(top_fc_var, x = 'DESCRIPTION', y = 'FC_VARIANCE_AMT', color = 'FC_VARIANCE_AMT', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {fc_total_slider} Positive Forecast Variance Amounts', xaxis_title = 'Description', yaxis_title = 'Forecast Variance Amount')
            st.plotly_chart(fig)
        elif fc_var_selection == 'Top Negative Variance Amounts':
            # Create a plotly bar chart with bottom x forecast variance amounts
            fc_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            st.markdown('##### Hover over chart and expand for a better view')
            bottom_fc_var = total_fc_var.iloc[-int(f'{fc_total_slider}'):]
            fig = px.bar(bottom_fc_var, x = 'DESCRIPTION', y = 'FC_VARIANCE_AMT', color = 'FC_VARIANCE_AMT', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {fc_total_slider} Negative Forecast Variance Amounts', xaxis_title = 'Description', yaxis_title = 'Forecast Variance Amount')
            st.plotly_chart(fig)
    elif forecast_choice == 'Variance as Percentage of Revenue':
        # Sort the data by the forecast variance amount
        total_fc_var = df.sort_values(by = 'FC_VARIANCE%REV', ascending = False)
        
        # Create a select box that allows the user to select top 20 or bottom 20 and then display the data with a plotly bar chart
        fc_var_selection = st.selectbox(label = "Select an option", options = ['Top Positive Variance Amounts (by Percentage of Revenue)', "Top Negative Variance Amounts (by Percentage of Revenue)"])
        if fc_var_selection == 'Top Positive Variance Amounts (by Percentage of Revenue)':
            # Create a plotly bar chart with top x forecast variance amounts
            fc_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            top_fc_var = total_fc_var.iloc[0:int(f'{fc_total_slider}')]
            st.markdown('##### Hover over chart and expand for a better view')
            fig = px.bar(top_fc_var, x = 'DESCRIPTION', y = 'FC_VARIANCE%REV', color = 'FC_VARIANCE%REV', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {fc_total_slider} Positive Forecast Variance as % of Revenue', xaxis_title = 'Description', yaxis_title = 'Forecast Variance as Percent of Revenue')
            st.plotly_chart(fig)
        elif fc_var_selection == 'Top Negative Variance Amounts (by Percentage of Revenue)':
            # Create a plotly bar chart with bottom x forecast variance amounts
            fc_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            st.markdown('##### Hover over chart and expand for a better view')
            bottom_fc_var = total_fc_var.iloc[-int(f'{fc_total_slider}'):]
            fig = px.bar(bottom_fc_var, x = 'DESCRIPTION', y = 'FC_VARIANCE%REV', color = 'FC_VARIANCE%REV', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {fc_total_slider} Negative Forecast Variance as % of Revenue', xaxis_title = 'Description', yaxis_title = 'Forecast Variance as % of Revenue')
            st.plotly_chart(fig)
elif sidebar_selection == 'Last Year Variance':
    last_year_choice = st.sidebar.radio(label = "Select an option", options = ['Total Variance Amount', "Variance as Percentage of Revenue"])
    if last_year_choice == 'Total Variance Amount':
        # Sort the data by the forecast variance amount
        total_ly_var = df.sort_values(by = 'LY_VARIANCE_AMT', ascending = False)
        
        # Create a select box that allows the user to select top 20 or bottom 20 and then display the data with a plotly bar chart
        ly_var_selection = st.selectbox(label = "Select an option", options = ['Top Positive Variance Amounts', "Top Negative Variance Amounts"])
        if ly_var_selection == 'Top Positive Variance Amounts':
            # Create a plotly bar chart with top x forecast variance amounts
            ly_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            top_ly_var = total_ly_var.iloc[0:int(f'{ly_total_slider}')]
            st.markdown('##### Hover over chart and expand for a better view')
            fig = px.bar(top_ly_var, x = 'DESCRIPTION', y = 'LY_VARIANCE_AMT', color = 'LY_VARIANCE_AMT', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {ly_total_slider} Positive Last Year Variance Amounts', xaxis_title = 'Description', yaxis_title = 'Last Year Variance Amount')
            st.plotly_chart(fig)
        elif ly_var_selection == 'Top Negative Variance Amounts':
            # Create a plotly bar chart with bottom x forecast variance amounts
            ly_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            st.markdown('##### Hover over chart and expand for a better view')
            bottom_ly_var = total_ly_var.iloc[-int(f'{ly_total_slider}'):]
            fig = px.bar(bottom_ly_var, x = 'DESCRIPTION', y = 'LY_VARIANCE_AMT', color = 'LY_VARIANCE_AMT', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {ly_total_slider} Negative Last Year Variance Amounts', xaxis_title = 'Description', yaxis_title = 'Last Year Variance Amount')
            st.plotly_chart(fig)
    elif last_year_choice == 'Variance as Percentage of Revenue':
        # Sort the data by the forecast variance amount
        total_ly_var = df.sort_values(by = 'LY_VARIANCE_%REV', ascending = False)
        
        # Create a select box that allows the user to select top 20 or bottom 20 and then display the data with a plotly bar chart
        ly_var_selection = st.selectbox(label = "Select an option", options = ['Top Positive Variance Amounts (by Percentage of Revenue)', "Top Negative Variance Amounts (by Percentage of Revenue)"])
        if ly_var_selection == 'Top Positive Variance Amounts (by Percentage of Revenue)':
            # Create a plotly bar chart with top x forecast variance amounts
            ly_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            top_ly_var = total_ly_var.iloc[0:int(f'{ly_total_slider}')]
            st.markdown('##### Hover over chart and expand for a better view')
            fig = px.bar(top_ly_var, x = 'DESCRIPTION', y = 'LY_VARIANCE_%REV', color = 'LY_VARIANCE_%REV', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {ly_total_slider} Positive Last Year Variance as % of Revenue', xaxis_title = 'Description', yaxis_title = 'Last Year Variance as Percent of Revenue')
            st.plotly_chart(fig)
        elif ly_var_selection == 'Top Negative Variance Amounts (by Percentage of Revenue)':
            # Create a plotly bar chart with bottom x forecast variance amounts
            ly_total_slider = int(st.slider(label = 'Number of items to display', min_value = 1, max_value = 40, value = 10, step = 1))
            st.markdown('##### Hover over chart and expand for a better view')
            bottom_ly_var = total_ly_var.iloc[-int(f'{ly_total_slider}'):]
            fig = px.bar(bottom_ly_var, x = 'DESCRIPTION', y = 'LY_VARIANCE_%REV', color = 'LY_VARIANCE_%REV', color_continuous_scale = 'spectral')
            fig.update_layout(title = f'Top {ly_total_slider} Negative Last Year Variance as % of Revenue', xaxis_title = 'Description', yaxis_title = 'Last Year Variance as % of Revenue')
            st.plotly_chart(fig)
