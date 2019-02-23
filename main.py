from modules import DirectMethod
from driver import Driver 




mod1 = DirectMethod()
moduleList = [mod1]

driver = Driver(moduleList)

driver.test(range(10, 100, 10))
