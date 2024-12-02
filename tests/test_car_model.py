from geopy.distance import geodesic
from autobahn.car_model import Car


def test_car_initialization():
    car = Car(start_location=(52.5200, 13.4050))
    assert car.location == (52.5200, 13.4050)
    assert car.route == []
    assert car.distance_traveled == 0.0


def test_drive_to():
    car = Car(start_location=(52.5200, 13.4050))
    destination = (48.8566, 2.3522)
    car.drive_to(destination)
    assert car.location == destination
    assert car.route == [destination]
    assert car.distance_traveled == geodesic((52.5200, 13.4050), destination).kilometers


def test_multiple_drives():
    car = Car(start_location=(52.5200, 13.4050))
    destinations = [(48.8566, 2.3522), (51.5074, -0.1278)]
    for dest in destinations:
        car.drive_to(dest)
    assert car.location == destinations[-1]
    assert car.route == destinations
    total_distance = sum(
        geodesic(destinations[i], destinations[i + 1]).kilometers
        for i in range(len(destinations) - 1)
    )
    total_distance += geodesic((52.5200, 13.4050), destinations[0]).kilometers
    assert car.distance_traveled == total_distance
