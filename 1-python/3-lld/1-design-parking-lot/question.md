# **Write LLD of a parking lot system**

The parking lot has two kinds of parking spaces: type = 2 for 2 wheeler vechiles & 4 for 4 wheeler vechiles.

There are multiple floors in the parking lot. On each floor, vechiles are parked in parking spots arranged in rows & cols.

For simplicity assume each floor will have same no of rows.

```python
class Solution:
	def init(self, helper, parking: list):
		self.helper = helper
	def park(self, vechile_type: int, vechile_number: str, ticket_id: str) -> str:
	return ""
# use helper method to get floor, row, col of pared vechile from spot_id
# location = self.helper.get_spot_location(spot_id)
# floor, row, col = location[0], location[1], location[2]

def remove_vechile(self, spot_id: str, vechile_number: str, ticket_id: str) -> int:
```

## Requirements:

1. Park your vechile
   `park(vechile_type:int, vechile_number: str, ticket_id: str)`
2. Unpark or remove vechile
   `def remove_vechile(self, spot_id: str, vechile_number: str, ticket_id: str) -> int:`
3. Display empty spots count
   `get_free_spots_count(floot: int, vechile_type: int)`
4. Search Vechile incase of lost their `ticketsearch_vechile(self, vehicle_number: str, ticket_id: str)`

## Method Signature:

```python
class Solution:
	def init(self, helper, parking: list):
		self.helper = helper


	def park(self, vechile_type: int, vechile_number: str, ticket_id: str) -> str:
	return ""


        def remove_vechile(self, spot_id: str, vechile_number: str, ticket_id: str) -> int:
	return 404


        def get_free_spots_sount(self, floor: int, vehicle_type:int) -> int:
	return 0


        def search_vechile(self, vechile_number: str, ticket_id: str) -> str:
	return ""

```

## Enitites

1. ParkingFloor
2. ParkingSpot
3. SearchManager

Any low level Design System, there are two types of class

1. CRUD (park, unpark) Classes
2. Search or View Classes

```python
class ParkingSpot:
	def __init(self, spot_id:str, vechile_type):
		self.spot_id = spot_id
		self.vehicle_type = vehicle_type
		self.is_spot_parked = False


	def is_parked(self) -> bool:
		return self.is_spot_parked


	def park_vehicle(self):
		self.is_spot_parked = False


	def get_spot_id(self) -> str:
		return self.spot_id


	def get_vehicle_type(self) -> int:
		return self.vechile_type
```

```python
  class ParkingFloor:
	def __init__(self, floor:int, parking_floor: list, vehicle_types: list, helper):
		self.parking_spots = [[None for _ in range(len(parking_floor[0]))] for _ in range(len(parking_floor))]
		self.free_spots_count = {vehicle_type: 0 for vehicle_type in vehicle_types}

		for row in range(len(parking_floor)):
	  		for col in range(len(parking_floor[row])):
	      			if parking_floor[row][col].endsWith("1")
					vehicle_type = int(parking_floor[row][col].split("-")[0])
					self.parking_spots[row][col] = ParkingSpot(helper.get_spot_id(floor, row, col), vehicle_type)
					self.free_spots_count[vehicle_type] += 1

	def get_free_spots_count(self, vehicle_type: int) -> int:
		return self.free_spots_count.get(vehicle_type, 0)

	def remove_vehicle(self, row: int, col: int) -> int:
		if row < 0 or row >= len(self.parking_spots) or col < 0 or col >= len(self.parking_spots[row][cols]).is_parked():
	return 404

	vechicle_type = self.parking_spots[row][col].get_vehicle_type()
	self.parking_spot[row][col].remove_vehicle()
	self.free_spots_count[vehicle_type] +=1
	return 201


	def park(self, vehicle_type: int, vehicle_number: str, ticket_id: str) -> str:
		if self.free_spots_count.get(vehicle_type, 0) == 0:
			return ""
		for row in self.parking_spots:
			for spot in row:
		    		if spot is not None and not spot.is_parked() and spot.get_vehivle_type() == vehicle_type:
					self.free_spots_count[vehicle_type] -= 1
					spot.park_vhicle()
					return spot.get_spot_id()



```

```python
class SearchManager:
	def __init__(self):
		self.cache = {}

	def search_vehicle(self, vehicle_number: str, ticket_id: str) -> str:
		if vehicle_number.strip():
			return self.cache.get(vehicle_number)
		if ticket_id.strip():
			return self.cache.get(ticket_id)
		return ""

	def index(self, spot_id, vehicle_number, ticket_id):
		self.cache[vehicle_number] = spot_id
		self.cache[ticket_id] = spot_id

```
