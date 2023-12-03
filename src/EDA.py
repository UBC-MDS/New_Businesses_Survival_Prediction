from DataPreprocess import *
from DataFetch import *
import pandas as pd
import altair as alt
alt.data_transformers.enable("vegafusion")
import click

def numeric_feature_visualization(data, features):
    """
    Generates a grid of density plots for numeric features, grouped by survival status.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame containing numeric features and the 'survival_status' column.
    - features (list of str): List of column names corresponding to numeric features in the DataFrame.

    Returns:
    - An Altair LayerChart displaying density plots for numeric features grouped by survival status.
    """
    charts_numeric = []
    for feature in features:
        chart = alt.Chart(data).transform_density(
            feature,
            as_=[feature, 'density'],
            groupby=['survival_status']
        ).mark_area(opacity=0.5).encode(
            x=alt.X(feature, title=f'{feature} Distribution'),
            y=alt.Y('density:Q', title='Density'),
            color=alt.Color('survival_status:O', legend=alt.Legend(title="Survival Status")).scale(scheme='dark2')
        ).properties(
            width=180,
            height=120,
            title=f'Density Plot of {feature} by Survival Status'
        )
        charts_numeric.append(chart)
    
    chart_grid = alt.vconcat(*[
        alt.hconcat(*charts_numeric[i:i+2]) for i in range(0, len(charts_numeric), 2)
    ])
    
    chart_grid.save('results/figures/numeric_features.png')

def fee_paid_visualization(data, feature='FeePaid'):
    """
    Generates a density plot for the 'FeePaid' feature with a restricted x-axis domain, grouped by survival status.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame containing the 'FeePaid' feature and the 'survival_status' column.

    Returns:
    - An Altair Chart displaying a density plot for the 'FeePaid' feature with a restricted x-axis domain.
    """
    chart = alt.Chart(data).transform_density(
        feature,
        as_=[feature, 'density'],
        groupby=['survival_status']
    ).mark_area(opacity=0.5).encode(
        x=alt.X(feature, title=f'{feature} Distribution', scale=alt.Scale(domain=[0, 5000])).stack(False),
        y=alt.Y('density:Q', title='Density'),
        color=alt.Color('survival_status:O', legend=alt.Legend(title="Survival Status")).scale(scheme='dark2')
    ).properties(
        width=120,
        height=120,
        title=f'Density Plot of {feature} by Survival Status'
    )
    
    png_name = f'results/figures/numeric_{feature}.png'
    chart.save(png_name)
    # return chart

def num_of_employee_visualization(data, feature='NumberofEmployees'):
    """
    Generates a density plot for the 'NumberofEmployees' feature with a restricted x-axis domain, grouped by survival status.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame containing the 'NumberofEmployees' feature and the 'survival_status' column.

    Returns:
    - An Altair Chart displaying a density plot for the 'NumberofEmployees' feature with a restricted x-axis domain.
    """
    chart = alt.Chart(data[data['NumberofEmployees'] <= 20]).transform_density(
        'NumberofEmployees',
        as_=['NumberofEmployees', 'density'],
        groupby=['survival_status']
    ).mark_area(opacity=0.5).encode(
        x=alt.X(feature, title=f'{feature} Distribution').stack(False),
        y=alt.Y('density:Q', title='Density'),
        color=alt.Color('survival_status:O', legend=alt.Legend(title="Survival Status")).scale(scheme='dark2')
    ).properties(
        width=120,
        height=120,
        title=f'Density Plot of {feature} by Survival Status'
    )
    
    png_name = f'results/figures/numeric_{feature}.png'
    chart.save(png_name)
    # return chart

def categorical_feature_visualization(data, feature):
    """
    Generates a faceted bar chart for a categorical feature, colored by survival status.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame containing the categorical feature and the 'survival_status' column.
    - feature (str): The column name corresponding to the categorical feature in the DataFrame.

    Returns:
    - An Altair Chart displaying a faceted bar chart for the specified categorical feature grouped by survival status.
    """
    
    chart = alt.Chart(data).mark_bar(opacity=0.5).encode(
        x=alt.X(feature, sort='-y', title=f'{feature} Categories'),  
        y=alt.Y('count()', title='Frequency'),  
        color=alt.Color('survival_status:O', legend=alt.Legend(title="Survival Status")).scale(scheme='dark2')
    ).facet(
        column='survival_status:O'
    ).resolve_scale(
        x='independent', 
        y='independent'
    ).properties(
        width=180,
        height=180,
        title=f'Frequency of {feature} by Survival Status'
    )

    png_name = f'results/figures/categorical_{feature}.png'
    chart.save(png_name)

def varianced_categorical_feature_visualization(data, feature='BusinessType'):
    """
    Generates a faceted bar chart for a categorical feature with high variance, colored by survival status.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame containing the categorical feature and the 'survival_status' column.
    - feature (str): The column name corresponding to the categorical feature in the DataFrame.

    Returns:
    - An Altair Chart displaying a faceted bar chart for the specified categorical feature with high variance, grouped by survival status.
    """

    top_20_categories = data[feature].value_counts().head(20).index.tolist()
    filtered = data[data[feature].isin(top_20_categories)]

    chart = alt.Chart(filtered).mark_bar(opacity=0.5).encode(
        x=alt.X(feature, title=f'Top 20 {feature} Categories', sort='-y'), 
        y=alt.Y('count()', title='Frequency'), 
        color=alt.Color('survival_status:O', legend=alt.Legend(title="Survival Status")).scale(scheme='dark2')
    ).facet(
        column='survival_status:O',  
        columns=2 
    ).properties(
        title=f'Frequency of Top 20 {feature} by Survival Status',
        width=180,
        height=180
    )

    png_name = f'results/figures/varianced_categorical_{feature}.png'
    chart.save(png_name)



@click.command()
@click.option('--merged_data_path') # merged_data_path = 'data/processed/business_econ.csv'

def main(merged_data_path):
    # Load final merged data
    data = pd.read_csv(merged_data_path, low_memory=False)

    # Numeric
    numeric_features = ['GDPValue', 'ConsumerPriceValue', 'EmploymentValue', 'InvestmentConstructionValue'] 
    numeric_feature_visualization(data, numeric_features)

    num_of_employee_visualization(data)
    fee_paid_visualization(data)
    
    # Categorical
    categorical_features = ['LocalArea']
    varianced_categorical_feature = ['BusinessType']

    for categorical_feat in categorical_features:
        categorical_feature_visualization(data, categorical_feat)

    for varianced_categorical_feat in varianced_categorical_feature:
        varianced_categorical_feature_visualization(data, varianced_categorical_feat)


if __name__ == "__main__":
    main()

# python  src/EDA.py --merged_data_path=data/processed/business_econ.csv