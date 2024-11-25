from geopy.distance import geodesic


class Car:
    def __init__(self, start_location):
        self.location = start_location
        self.route = []
        self.distance_traveled = 0.0

    def drive_to(self, destination):
        self.route.append(destination)
        self.distance_traveled += geodesic(self.location, destination).kilometers
        self.location = destination
