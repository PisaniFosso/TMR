from modules import DirectMethod, WilsonMethod
from driver import Driver 




mod1 = DirectMethod()
mod2 = WilsonMethod()
moduleList = [mod1,mod2]

driver = Driver(moduleList)

driver.test(range(10, 100, 10))
