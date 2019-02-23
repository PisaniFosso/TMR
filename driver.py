class Driver(object):
  def __init__(self, modules):
    self._modules = modules
    self._intervals  = []
    self._values     = []
  def test(self, intervals):
    
    for index, interval in enumerate(intervals):
      results = [module.getResult(interval) for module in self._modules] 
      from collections import defaultdict
      votes = dict()
      for res in results:
        try:
          votes[res]+=1
          
        except:
          votes[res] = 0
          
      import operator
      winner  = max(votes.items(), key=operator.itemgetter(1))[0]
      self._values.append(winner)
      self._intervals.append(interval)
      for i, module in enumerate(self._modules):
        if results[i]==winner:
          module.receiveFeedback({'status':'ok'})
        else:
          module.receiveFeedback({'status':'error', good_value:winner})
        
      
    
