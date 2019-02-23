class EratostheneMethod():
	"""docstring for Ératosthène"""
	def __str__(self):
		return "Eratos"
	def __init__(self, begin= 2):
		self.prime = 2
		self.begin = begin
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
		self.prime += len(history)
		return self.prime

	def receiveFeedback(self, feedBack):
		if feedBack["status"] == "error":
			self.prime = feedBack["goodValue"] 