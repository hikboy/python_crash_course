class Car:
	"""A simple attemp to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Update the odometer value"""

		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can not roll back an oaometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

	def fill_gas_tank(self):
		"""Car need fiil gas"""
		print("Car fill gas")

class Battery:
	"""A simple attemp to model a battery for an electric car."""
	def __init__(self, battery_size=75):
		"""Initialize battery's attri"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing"""
		print(f"This car has a {self.battery_size}-KWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")


class Electric(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
#		self.battery_size = 75
		self.bat = Battery()

#	def describe_battery(self):
#		"""Print battery infomation"""
#		print(f"This car has a {self.battery_size}-KWh battery")

	def fill_gas_tank(self):
		"""Electric car fill gas tank."""
		print("Electric car fill gas tank")


my_tesla = Electric('teslal', 'model s', 2019)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.bat.describe_battery()
my_tesla.bat.get_range()

my_new_car  = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23

my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()