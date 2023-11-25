import altair as alt
alt.data_transformers.enable("vegafusion")
import matplotlib.pyplot as plt

def numeric_feature_visualization(data, features):
    """
    Generates a grid of density plots for numeric features, grouped by survival status.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame containing numeric features and the 'survival_status' column.
    - features (list of str): List of column names corresponding to numeric features in the DataFrame.

    Returns:
    - An Altair LayerChart displaying density plots for numeric features grouped by survival status.
    """
    charts_numeric = [alt.Chart(data).transform_density(
        feature,
        as_=[feature, 'density'],
        groupby=['survival_status']
    ).mark_area(opacity=0.5).encode(
        x=alt.X(feature, title=feature).stack(False),
        y='density:Q',
        color=alt.Color('survival_status:O').scale(scheme='dark2')
    ).properties(
        width=180,
        height=120
    ) for feature in features]
    
    chart_grid = alt.vconcat(*[
        alt.hconcat(*charts_numeric[i:i+2]) for i in range(0, len(charts_numeric), 2)
    ])
    
    return chart_grid

def large_variance_numeric_feature_visualization(data, feature):
    """
    Generates a density plot for a numeric feature with a restricted x-axis domain, grouped by survival status.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame containing the numeric feature and the 'survival_status' column.
    - feature (str): The column name corresponding to the numeric feature in the DataFrame.

    Returns:
    - An Altair Chart displaying a density plot for the specified numeric feature with a restricted x-axis domain.
    """
    chart = alt.Chart(data).transform_density(
        feature,
        as_=[feature, 'density'],
        groupby=['survival_status']
    ).mark_area(opacity=0.5).encode(
        x=alt.X(feature, title=feature, scale=alt.Scale(domain=[0, 5000])).stack(False),
        y='density:Q',
        color=alt.Color('survival_status:O').scale(scheme='dark2')
    ).properties(
        width=120,
        height=120
    )
    
    return chart

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
        alt.X(feature, sort='-y').stack(False),
        y='count()',
        color=alt.Color('survival_status:O').scale(scheme='dark2')
    ).facet(
        'survival_status:O', columns = 2
    )
    
    return chart

def varianced_categorical_feature_visualization(data, feature):
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
        alt.X(feature, sort='-y').stack(False),
        y='count()',
        color=alt.Color('survival_status:O').scale(scheme='dark2')
    ).facet(
        'survival_status:O', columns = 2
    )
    
    return chart