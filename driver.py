class Driver(object):
  def __init__(self, modules):
    self._modules = modules
    self._intervals  = []
    self._values     = []
  def test(self, intervals):
    
    for index, interval in enumerate(intervals):
      results = [module.getResult(interval) for module in self._modules] 
      votes = defaultdict(int)
      for res in results:
        votes[res]+=1
      import operator
      winner  = max(stats.iteritems(), key=operator.itemgetter(1))[0]
      self._values.append(winner)
      self._intervals.append(interval)
      for i, module in enumerate(self._modules):
        if results[i]==winner:
          module.giveFeedback({status:'ok'})
        else:
          module.giveFeedback({status:'error', goodvalue:winner})
        
      
    
