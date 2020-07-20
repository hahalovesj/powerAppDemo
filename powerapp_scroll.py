#coding=utf-8
from appium import webdriver
import time
def get_driver():
    capabilities = {
        "app": "/Users/shine/Downloads/powerapp_202007101205.apk",
        "platformName": "Android",
        "deviceName": "CFM7N18A18000471",
        "appActivity": "com.lizihang.powerapp.activities.SplashActivity",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub",capabilities)
    time.sleep(10)
    return driver

def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height

#向左边滑动   
def swipe_left():
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10*1
    driver.swipe(x1,y1,x,y1)

#向上边滑动   
def swipe_up():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10*9
    y2 = get_size()[1]/10*1
    driver.swipe(x1,y1,x1,y2,3000)  

#滚动,scroll() 与swipe()的区别，swipe是可以根据自己需要设置滑动的距离，而scroll是根据页面中两个元素位置距离进行滑动。
def scroll_page(list):
	#获取两个元素，将页面向上滑动
	time.sleep(5)
	stop_element=list[0]
	start_element=list[3]
	driver.scroll(start_element,stop_element,3000)  

#TODO https://www.jianshu.com/p/9b6d851a766a
def scrollToElement(): #使用scrollIntoView方法实现滚动到指定控件元素
    webElement = driver.find_element_by_android_uiautomator(
    "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text(\"Display\"))")
        
       

driver = get_driver()    
#进入新房
driver.find_element_by_id("com.lizihang.powerapp:id/tv_onehand").click()
time.sleep(5)
#进入第一个新房详情
list = driver.find_elements_by_id("com.lizihang.powerapp:id/oneLl")
scroll_page(list)
#print(list[0].get_attribute("text"))
#list[0].click()
time.sleep(5)
#楼盘名称
#resblockname = driver.find_element_by_id("com.lizihang.powerapp:id/resblockName")
#楼盘价格
#totalPriceRange = driver.find_element_by_id("com.lizihang.powerapp:id/totalPriceRange")
#print(resblockname.get_attribute("text"))
#print(totalPriceRange.text)
#time.sleep(5)
#退出详情
#driver.find_element_by_id("com.lizihang.powerapp:id/iv_title_bar_left_icon").click()
#time.sleep(5)
#新房列表滑动
#swipe_up()
#time.sleep(5)


driver.quit()