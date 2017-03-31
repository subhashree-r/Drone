import math
import numpy as np

class Drone(object):
	def __init__(self):
		super(Drone, self).__init__()
		self._currRoad = None
		self._currPos = None
		self._currDirection = None

		self._velocity = 0
		self._time = 0



	def setSource(self, initRoad, initPos, initDirection):
		self._initRoad = initRoad
		self._initPos = initPos
		self._initDirection = initDirection
		self.setCurrent(self._initRoad, self._initPos, self._initDirection)

	def getSource(self):
		return {'road': self._initRoad, 'pos': self._initPos, 'direction': self._initDirection}

	def setDestination(self, destRoad, destPos):
		self._destRoad = destRoad
		self._destPos = destPos

	def getDestination(self):
		return {'road': self._destRoad, 'pos': self._destPos}

	def setCurrent(self, road, pos, direction):
		self._currRoad = road
		self._currPos = float(pos)
		self._currDirection = direction

	def getCurrent(self):
		return {'road': self._currRoad, 'pos': self._currPos, 'direction': self._currDirection}

	def getTime(self):
		return self._time
		
	def _displacement2Angle(self, displacement):
		return displacement * 360.0 / (2 * math.pi * self._currRoad.getRadius())

	def _addToCurrPos(self, degrees):
		if self._currDirection == '+':
			self._currPos = float(self._currPos) + degrees
			diff = 360 - self._currPos
			if diff < 0:
				self._currPos = abs(diff)
		elif self._currDirection == '-':
			self._currPos = self._currPos - degrees
			if self._currPos < 0:
				self._currPos = 360 + self._currPos

		print "currentpos: {0} -> {1}".format(self._currPos, self._currRoad.getId())
		

	# TODO: fix the function
	def _findNearest(self, array, pos):
		if pos <= 90 or pos >= 270:
			return  0
		else:
			return 180
		# smallestDiff = 360
		# nearest = None
		# if '0' in array:
		# 	array.append(360)

		# for val in array:
		# 	val = float(val)
		# 	newDiff = abs(val - pos)
		# 	if newDiff < smallestDiff:
		# 		smallestDiff = newDiff
		# 		nearest = val
		# if val == 360:
		# 	return 0

		# return val

	def _possibleRoadsAndPos(self):
		nearestIntersection = self._findNearest(self._currRoad.getIntersections().keys(), self._currPos)

		if not abs(self._currPos - nearestIntersection) < 0.2: # since exact intersection is hard to get as curr pos
			return 

		return self._currRoad.getIntersections().get(str(nearestIntersection))
		
	def GO(self):
		time = 1 # second
		accleration = 0
		if self._velocity < 4:
			accleration = 1

		self._velocity = self._velocity + accleration * time # v = u + at
		displacement = self._velocity * time + 0.5 * accleration * time * time # d = ut+(1/2)at^2
		degrees = self._displacement2Angle(displacement)
		self._addToCurrPos(degrees)
		self._time = self._time + 1


	def STOP(self):
		if self._velocity < 0:
			return
		time = 1 # second
		accleration = 0
		if self._velocity > 0:
			accleration = -1

		self._velocity = self._velocity + accleration * time # v = u + at
		displacement = self._velocity * time + 0.5 * accleration * time * time # d = ut+(1/2)at^2
		degrees = self._displacement2Angle(displacement)
		self._addToCurrPos(degrees)
		self._time = self._time + 1

	def REVERSE(self):
		self._time = self._time + 0.3
		if self._currDirection == '+':
			self._currDirection = '-'
		elif self._currDirection == '-':
			self._currDirection = '+'

	def TRANSFER(self, road):
		possibleIntersections = self._possibleRoadsAndPos()
		if not possibleIntersections:
			return
		for roadIdAndPos in possibleIntersections:
			if roadIdAndPos[0] == road.getId():
				self._time = self._time + 0.1
				self._currRoad = road
				self._currPos = roadIdAndPos[1]