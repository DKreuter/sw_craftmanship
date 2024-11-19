import folium
import pandas as pd
import requests
from geopy.distance import geodesic

url_bab = "https://verkehr.autobahn.de/o/autobahn"


def get_warnings(autobahn_id):
    url = f"{url_bab}/{autobahn_id}/services/warning"
    response = requests.get(url)
    return response.json()["warning"]


class TrafficWarning:
    def __init__(self, data):
        """
        Initialize the TrafficEvent class with data from the dictionary.

        :param data: dict, containing traffic event information
        """
        self.isBlocked = data.get("isBlocked")
        self.display_type = data.get("display_type")
        self.subtitle = data.get("subtitle")
        self.title = data.get("title")
        self.startTimestamp = data.get("startTimestamp")
        self.delayTimeValue = data.get("delayTimeValue")
        self.abnormalTrafficType = data.get("abnormalTrafficType")
        self.averageSpeed = data.get("averageSpeed")
        self.description = data.get("description")
        self.routeRecommendation = data.get("routeRecommendation")
        self.lorryParkingFeatureIcons = data.get("lorryParkingFeatureIcons")
        self.geometry = data.get("geometry")
        self.geo_df = self.create_geo_dataframe(self.geometry["coordinates"])

    def create_geo_dataframe(self, coordinates):
        df = pd.DataFrame(
            {
                "lat": [coord[0] for coord in coordinates],
                "long": [coord[1] for coord in coordinates],
            }
        ).dropna()
        return df


def calculate_traffic_length(coordinates):
    total_length = 0.0
    for i in range(len(coordinates) - 1):
        total_length += geodesic(coordinates[i], coordinates[i + 1]).kilometers
    return total_length


def map_plot(plotlist, on="aveg_speed"):
    on_stats = pd.concat(df[on] for df in plotlist).describe()
    colormap = folium.LinearColormap(
        ["green", "yellow", "red"], vmin=on_stats["min"], vmax=on_stats["max"]
    )

    m = folium.Map(
        pd.concat([data[["long", "lat"]] for data in plotlist]).mean(), zoom_start=10
    )
    for df in plotlist:
        points_ = [(point[0], point[1]) for point in df[["long", "lat"]].to_numpy()]
        folium.features.ColorLine(
            points_,
            colors=[data for data in df[on]],
            colormap=colormap,
            weight=5,
            smooth_factor=3,
        ).add_to(m)
    return m
