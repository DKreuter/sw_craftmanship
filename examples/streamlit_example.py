import streamlit as st
from streamlit_folium import st_folium
from autobahn.autobahn import get_warnings, TrafficWarning, map_plot

st.title("Autobahn Route Planner")

autobahn_number = st.text_input("Enter Autobahn Number", "A1")

if st.button("Plot Route"):
    warnings = get_warnings(autobahn_number)
    traffic_warnings = [TrafficWarning(warning) for warning in warnings]

    if traffic_warnings:
        plotlist = [tw.geo_df for tw in traffic_warnings]
        m = map_plot(plotlist, on="averageSpeed")
        st_data = st_folium(m, width=725)
    else:
        st.write(f"No traffic warnings found for Autobahn {autobahn_number}.")
