import importlib

import polars as pl
import streamlit as st
from dbnomics import fetch_series
from function_year import create_map_year, charts_year, charts_bop_year
from streamlit_option_menu import option_menu


# Décorateur pour mettre en cache les données
@st.cache_data
def fetch_trade_data(list_iso3):
    df_trade = fetch_series(
        "WB",
        "WDI",
        dimensions={
            "frequency": ["A"],
            "indicator": ["NE.TRD.GNFS.ZS"],
            "country": list_iso3,
        },
        max_nb_series=200,
    )
    df_trade = df_trade.dropna()
    return pl.from_pandas(df_trade)

def fetch_trade_bop(list_iso3): 
    df_trade_bop = fetch_series(
    "WB",
    "WDI",
    dimensions={
        "frequency": ["A"],
        "indicator": ["BN.GSR.GNFS.CD"],
        "country": list_iso3,
    },
    max_nb_series=200,
    )
    df_trade_bop = df_trade_bop.dropna()
    return pl.from_pandas(df_trade_bop)

def main() -> None:
    package_dir = importlib.resources.files("trade")
    st.set_page_config(
        page_title="Convergence of the European Union Countries",
        page_icon=str(package_dir / "images/favicon.png"),
    )
    st.image(str(package_dir / "images/dbnomics.svg"), width=300)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(str(package_dir / "assets/styles.css"))
    st.markdown(
        """
        <style>
        hr {
            height: 1px;
            border: none;
            color: #333;
            background-color: #333;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Explanations", "Trade map", "Trade Evolution","Trade BoP Evolution","Sources"],
            icons=[
                "book",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "search",
            ],
            menu_icon=":",
            default_index=0,
        )
    list_iso3 = [
        "AFG",
        "ALB",
        "DZA",
        "AND",
        "AGO",
        "ATG",
        "ARG",
        "ARM",
        "AUS",
        "AUT",
        "AZE",
        "BHS",
        "BHR",
        "BGD",
        "BRB",
        "BLR",
        "BEL",
        "BLZ",
        "BEN",
        "BTN",
        "BOL",
        "BIH",
        "BWA",
        "BRA",
        "BRN",
        "BGR",
        "BFA",
        "BDI",
        "CPV",
        "KHM",
        "CMR",
        "CAN",
        "CAF",
        "TCD",
        "CHL",
        "CHN",
        "COL",
        "COM",
        "COG",
        "COD",
        "CRI",
        "CIV",
        "HRV",
        "CUB",
        "CYP",
        "CZE",
        "DNK",
        "DJI",
        "DMA",
        "DOM",
        "ECU",
        "EGY",
        "SLV",
        "GNQ",
        "ERI",
        "EST",
        "SWZ",
        "ETH",
        "FJI",
        "FIN",
        "FRA",
        "GAB",
        "GMB",
        "GEO",
        "DEU",
        "GHA",
        "GRC",
        "GRD",
        "GTM",
        "GIN",
        "GNB",
        "GUY",
        "HTI",
        "HND",
        "HUN",
        "ISL",
        "IND",
        "IDN",
        "IRN",
        "IRQ",
        "IRL",
        "ISR",
        "ITA",
        "JAM",
        "JPN",
        "JOR",
        "KAZ",
        "KEN",
        "KIR",
        "KWT",
        "KGZ",
        "LAO",
        "LVA",
        "LBN",
        "LSO",
        "LBR",
        "LBY",
        "LIE",
        "LTU",
        "LUX",
        "MDG",
        "MWI",
        "MYS",
        "MDV",
        "MLI",
        "MLT",
        "MHL",
        "MRT",
        "MUS",
        "MEX",
        "FSM",
        "MDA",
        "MCO",
        "MNG",
        "MNE",
        "MAR",
        "MOZ",
        "MMR",
        "NAM",
        "NRU",
        "NPL",
        "NLD",
        "NZL",
        "NIC",
        "NER",
        "NGA",
        "PRK",
        "MKD",
        "NOR",
        "OMN",
        "PAK",
        "PLW",
        "PAN",
        "PNG",
        "PRY",
        "PER",
        "PHL",
        "POL",
        "PRT",
        "QAT",
        "ROU",
        "RUS",
        "RWA",
        "KNA",
        "LCA",
        "VCT",
        "WSM",
        "SMR",
        "STP",
        "SAU",
        "SEN",
        "SRB",
        "SYC",
        "SLE",
        "SGP",
        "SVK",
        "SVN",
        "SLB",
        "SOM",
        "ZAF",
        "KOR",
        "SSD",
        "ESP",
        "LKA",
        "SDN",
        "SUR",
        "SWE",
        "CHE",
        "SYR",
        "TJK",
        "TZA",
        "THA",
        "TLS",
        "TGO",
        "TON",
        "TTO",
        "TUN",
        "TUR",
        "TKM",
        "TUV",
        "UGA",
        "UKR",
        "ARE",
        "GBR",
        "USA",
        "URY",
        "UZB",
        "VUT",
        "VAT",
        "VEN",
        "VNM",
        "YEM",
        "ZMB",
        "ZWE",
    ]

    # Télécharger les données
    df_trade = fetch_trade_data(list_iso3)
    df_trade_bop = fetch_trade_bop(list_iso3)
    years = df_trade["original_period"].unique().sort()  # de 1960 à 2023
    country = df_trade["country (label)"].unique().sort()
    # page d'explications
    if selected == "Explanations":
        st.write("Work in progress")

    if selected == "Trade map":
        # carte
        select_year = st.selectbox("Choose a Period", years)

        fig = create_map_year(df_trade, select_year)
        st.plotly_chart(fig)

    if selected == "Trade Evolution":
        select_country = st.selectbox("Choose a country", country)

        fig1 = charts_year(df_trade, select_country)

        st.plotly_chart(fig1)
    if selected == "Trade BoP Evolution":
        select_country_bop = st.selectbox("Choose a country", country)

        fig3 = charts_bop_year(df_trade, select_country_bop)
        st.plotly_chart(fig3)


if __name__ == "__main__":
    main()
