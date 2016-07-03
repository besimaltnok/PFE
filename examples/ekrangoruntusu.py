#brew install phantomjs
#pip install selenium

from selenium import webdriver
import time
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get('http://site')
time.sleep(5)
driver.save_screenshot('isim.png')
driver.close()
driver.quit()
