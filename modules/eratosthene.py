class EratostheneMethod():
	"""docstring for Ératosthène"""
	def __str__(self):
		return "Eratos"
	def __init__(self, prime = 0, begin= 2):
		self._lastValue = prime
		self._lastInterval = begin
		self.history = [begin]

	def isPrime(self, x):
		for i in self.history:
			if x%i == 0:
				return False
		return True

	def getResult(self, end):
		history = []
		for x in range(self.history[-1], end):
			if self.isPrime(x):
				history.append(x)
		self.history += history
		self._lastValue += len(history)
		return self._lastValue

	def receiveFeedback(self, feedBack):
		if feedBack["status"] == "error":
			self._lastValue = feedBack["goodValue"] 
