import plotly.graph_objects as go
import polars as pl


def create_map_year(df, year):
    year = str(year)
    df_year = df.filter(pl.col("original_period") == year)
    fig = go.Figure(
        data=go.Choropleth(
            locations=df_year["country"],
            z=df_year["original_value"],
            colorscale="Blues",
            reversescale=False,
            autocolorscale=False,
            marker_line_color="white",
            zmin= df_year["original_value"].min(),
            zmax= df_year["original_value"].quantile(0.75),
        )
    )

    fig.update_layout(
        title_text=f"Trade as a percentage of GDP for {year}",
        geo=dict(
            showframe=False, showcoastlines=False, projection_type="equirectangular"
        ),
    )

    return fig

def charts_year(df, country):
    df_country = df.filter(pl.col("country (label)") == country)
    fig = go.Figure(
        go.Line(
        x = df_country["original_period"],
        y = df_country["original_value"]
    ))

    fig.update_layout(
        title_text=f"Trade evolution for {country} - as a percentage of GDP", 
    )
    
    return fig

def charts_bop_year(df, country):
    df_country = df.filter(pl.col("country (label)") == country)
    fig = go.Figure(
        go.Line(
        x = df_country["original_period"],
        y = df_country["original_value"]
    ))

    fig.update_layout(
        title_text=f"Trade evolution for {country} - current US$", 
    )
    
    return fig