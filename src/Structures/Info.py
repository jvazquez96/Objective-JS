class Info(object):
	def __init__(self, type=None, visibility=None):
		if type is None and visibility is None:
			self._info = []
		else:
			self._info = [type, visibility]
	def getInfo(self):
		return self._info
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