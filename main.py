from modules import DirectMethod, WilsonMethod, EratostheneMethod
from driver import Driver 




mod1 = DirectMethod()
mod2 = WilsonMethod()
mod3 = EratostheneMethod()
moduleList = [mod1, mod2, mod3]

driver = Driver(moduleList)

driver.test(range(10, 100, 10))


driver.run(110)