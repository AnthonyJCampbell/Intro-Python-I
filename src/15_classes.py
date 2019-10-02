# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
  def __init__(self, lat = 0, lon = 0):
    self.lat = lat
    self.lon = lon

  def printLatLon(self):
    print(f"{self.lat} x {self.lon}")

l1 = LatLon(17, 51)

l1.printLatLon()

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.



class Waypoint(LatLon):
  # Initialising class instance
  def __init__(self, name, lat, lon):
    # Making LatLon a subclass of Waypoint
    super().__init__(lat, lon)
    self.name = name
  
  def printLocation(self):
    return print(f"""
    Waypoint
    Name: {self.name}
    Lat: {self.lat}
    Lon: {self.lon}
    """)

  def __str__(self):
    return f'Waypoint:\nName: {self.name}\nLat-Lon: ({self.lat}, {self.lon})\n'

l2 = Waypoint("SF", 17, 51)

l2.printLocation()

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    super().__init__(name, lat, lon)
    self.difficulty = difficulty
    self.size = size

  def printGeocache(self):
    return print(f"""
    Geocache
    Name: {self.name} 
    Difficulty: {self.difficulty}
    Size: {self.size}
    Lat-Lon: ({self.lat}, {self.lon})
    """)

  def __str__(self):
    return f'Geocache: \nName: {self.name} \nDifficulty: {self.difficulty} \nSize: {self.size} \nLat-Lon: {self.lat}-{self.lon}'

l3 = Geocache("Golden Goose", "10/10", "1 cubic foot", 39.151, -56.315)

l3.printGeocache()

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

l4 = Waypoint("Catacombs", 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
l4.printLocation()
print(l4)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

l5 = Geocache("Newberry Views", "diff 1.5", 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(l5)
