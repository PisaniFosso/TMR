# TMR
Triple modular redundancy find the number of prime numbers within an interval



## Features
In computing, triple modular redundancy, sometimes called triple-mode redundancy (TMR) is a fault-tolerant form of N-modular redundancy, in which three systems perform a process and that result is processed by a majority-voting system to produce a single output. If any one of the three systems fails, the other two systems can correct and mask the fault.

## Usage

You can find some usage examples in the main.py file

```python
from modules import DirectMethod, WilsonMethod, EratostheneMethod
from driver import Driver 

driver = Driver([DirectMethod(), WilsonMethod(), EratostheneMethod()])

# run it on array off intervals [10, 20, 30, ..., 100]
driver.test(range(10, 100, 10))

# to run it a sinlge value interval like [0, 120]
driver.run(120)

```

For test purpose you can edit a module last value 
```python 
# edit the first module value in modules list
driver.setModule(0, value=10)
# after 2 execution the value will be automatically corrected
```
To create your own module you should create a class tha implemente getResult and receiveFeedback and have _lastValue and _lastInterval as attributes
```python

class Method(Object):
	"""docstring for wilson"""
	def __str__(self):
		return "methode name"
	def __init__(self,lastValue = 0, lastInterval=2):
		self._lastValue = lastValue
		self._lastInterval = lastInterval

	def getResult(self, interval):
		prime = 0
		for i in range(self._lastInterval, end+1):
			if isPrime(i):
				prime += 1
		self._lastValue += prime
		self._lastInterval = end+1
		return self._lastValue

	def receiveFeedback(self, feedBack):
		if feedBack["status"] == "error":
			self._lastValue = feedBack["goodValue"] 

```


# Contributors

Ismail Bagayoko (eib3773), Pisani Fosso (epf4168)

