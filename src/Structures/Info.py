class Info(object):
	def __init__(self, type=None, visibility=None, isList=None, listSize=0):
		if type is None and visibility is None:
			self._info = []
		else:
			self._info = [type, visibility, isList, listSize]
	def getInfo(self):
		return self._info
	def getType(self):
		if not self._info:
			return []
		else:
			return self._info[0]
	def getVisibility(self):
		if not self._info:
			return []
		else:
			return self._info[1]
	def isList(self):
		return self._info[2]
	def getListSize(self):
		return self._info[3]