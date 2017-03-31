from road import Road
from drone import Drone

class Parser(object):
	def __init__(self, absFilePath):
		super(Parser, self).__init__()
		self._filePath   = absFilePath
		self._drone = Drone()
		self._roads = {}
		self._roadsAndDrone = {'roads': self._roads, 'drone': self._drone}

	def parse(self):
		try:
			file = open(self._filePath, 'r')
			for line in file:
				if not self._comment(line):
					vals = line.split()
					if len(vals) == 3:
						if vals[2] in ['+', '-']:
							# Set source to the drone
							self._drone.setSource(self.getRoadById(vals[0]), vals[1], vals[2]) 
						else:
							# Define Road
							road = Road(vals[0], vals[1])
							self._roads[vals[0]] = road
					elif len(vals) == 4: # Define Intersection
						road = self.getRoadById(vals[0])
						road.intersect(vals[1], vals[2], vals[3])
					elif len(vals) == 2: # Set destination to the drone
						self._drone.setDestination(self.getRoadById(vals[0]), vals[1])
		except Exception as e:
			raise

		return self._roadsAndDrone

	def getRoadById(self, roadId):
		return self._roads[roadId]

	def _comment(self, line):
		return line.startswith("#")
		