class DirectMethod(object):
  def __init__(self, last_value=0, last_interval=0):
    self._lastValue = last_value    
    self._lastInterval = last_interval

  def getResult(self, interval):
    total = 0
    for num in range(self._lastInterval+1, interval+1):
      if DirectMethod.isPrime(num):
        total+=1
    self._lastValue+= total
    self._lastInterval = interval
    return self._lastValue
  
  
  def receiveFeedback(self, feedback):
    if feedback['status']=='error':
      self._lastValue = feedback['goodvalue']
       
  @staticmethod
  def isPrime(num):
    from math import sqrt
    racine = int(sqrt(num))
    if racine*racine==num:
      return False
    for i in range(2, racine):
      if num % i == 0:
        return False
    return True

    
