
class WilsonMethod():
	"""docstring for wilson"""
	def __init__(self, beguin=2):
		self.prime = 0
		self.beguin = beguin

	def Factoriel(self, N):
	    if N > 1: return N * self.Factoriel(N - 1)
	    else: return 1

	def getResult(self, end):
		prime = 0
		for i in range(self.beguin, end+1):
			number = self.Factoriel(i-1)%i
			if number == (i-1):
				prime += 1
		self.prime += prime
		return prime
	def receiveFeedback(self, feedBack):
		if feedBack["status"] == "error":
			self.prime = feedBack["goodValue"] 
