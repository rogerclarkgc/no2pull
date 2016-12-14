import time
from NO2pull import No2API
from NO2pull import runtask

pull = No2API()
runtask(pull.runspy, day = 0, hour = 0, minute = 30, second = 0)

