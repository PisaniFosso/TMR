
class WilsonMethod():
	"""docstring for wilson"""
	def __str__(self):
		return "Wilson"
	def __init__(self,prime = 0, begin=2):
		self.prime = prime
		self.begin = begin

	def Factoriel(self, N):
	    if N > 1: return N * self.Factoriel(N - 1)
	    else: return 1

	def getResult(self, end):
		prime = 0
		for i in range(self.begin, end+1):
			number = self.Factoriel(i-1)%i
			if number == (i-1):
				prime += 1
		self.prime += prime
		self.begin = end+1
		return self.prime

	def receiveFeedback(self, feedBack):
		if feedBack["status"] == "error":
			self.prime = feedBack["goodValue"] 
