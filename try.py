from os.path import exists
from random import random
import wda
import time
from time import strftime, localtime

s = wda.USBClient().session()



print(s(nameContains="发送失败", className="XCUIElementTypeStaticText").exists)


# assert s(name="删除hh成功", className="XCUIElementTypeStaticText").wait(timeout=1), "失败"


