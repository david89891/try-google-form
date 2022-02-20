import json
import re
import requests
import time

from msedge.selenium_tools import Edge, EdgeOptions

import lib


opt = EdgeOptions()
opt.use_chromium = True
opt.add_argument('inprivate')

# input the url (long or short)
url = input()
url_request = requests.get(url)
url = url_request.url

html_data = requests.get(url).text
data = json.loads(re.search(r"FB_PUBLIC_LOAD_DATA_ = (.*?);", html_data, flags=re.S).group(1))

lib.data = data[1][1]
url += lib.combine_url(url)

driver = Edge(executable_path='driver-for-selenium/msedgedriver.exe', options=opt)
driver.maximize_window()
driver.get(url)
time.sleep(100)
