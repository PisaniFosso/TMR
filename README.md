# TMR
Triple modulo redundncy find the number of prime numbers within an interval



## Features


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

# Contributors

Ismail Bagayoko (eib3773), Pisani Fosso (epf4168)

