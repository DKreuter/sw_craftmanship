import streamlit as st
from autobahn.autobahn import get_warnings, TrafficWarning
from autobahn.autobahn import calculate_traffic_length

st.title("Autobahn Route Planner")

autobahn_number = st.text_input("Enter Autobahn Number", "A7")
warnings = get_warnings(autobahn_number)
traffic_warnings = [TrafficWarning(warning) for warning in warnings]
for traffic_warning in traffic_warnings:
    if traffic_warning.averageSpeed:
        st.write(
            f"{traffic_warning.title} with delay: {traffic_warning.delayTimeValue}, "
            f"speed: {float(traffic_warning.averageSpeed):.2f} km/h, "
            f"distance: {calculate_traffic_length(traffic_warning.geo_df):.2f} km"
        )
    else:
        st.write(
            f"{traffic_warning.title} with delay: {traffic_warning.delayTimeValue}, "
            f"distance: {calculate_traffic_length(traffic_warning.geo_df):.2f} km"
        )

# if st.button("Plot Route"):
#     if traffic_warnings:
#     #     speed = [float(tw.averageSpeed) if tw.averageSpeed else 80 for tw in traffic_warnings]
#     #     plotlist = [tw.geo_df.assign(speed=speed[ii]) for ii, tw in enumerate(traffic_warnings)]
#     #     plotlist = [df for df in plotlist if not df.empty]
#     #     m = map_plot(plotlist, on="speed")
#     #     st_data = st_folium(m, width=725)
#         m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
#         folium.Marker(
#             [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
#         ).add_to(m)
#     else:
#         st.write(f"No traffic warnings found for Autobahn {autobahn_number}.")
