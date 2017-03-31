class Road(object):
	def __init__(self, id, radius):
		super(Road, self).__init__()
		self._id = id 				# A
		self._radius = radius 		# 2500
		self._intersections = {}  	# {0: [(B, 180), (D, 0)], 180: [(C, 0)]}

	def setId(self, id):
		self._id = id

	def getId(self):
		return self._id

	def setRadius(self, radius):
		self._radius = radius

	def getRadius(self):
		return float(self._radius)

	def getIntersections(self):
		return self._intersections

	def intersect(self, myPosition, roadId, roadPosition):
		if self._intersections.has_key(myPosition):
			self._intersections[myPosition].append((roadId, roadPosition))
		else:
			self._intersections[myPosition] = [(roadId, roadPosition)]


		