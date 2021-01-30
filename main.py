# Module Import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# Important Variable
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Meeting Code and Message Input
code = input("Enter Meeting Code:")
msg = input("Enter Meeting Message:")

print("Get Ready to attende your Class/Meeting")
print("Your Meeting Code is", code)

# Log In with Gooogle Account
driver.get("https:/gmail.com/")
driver.find_element_by_id("identifierId").send_keys("Your Email")
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys("Your Email Password")
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

# Opening Google Meet
driver.get("https://meet.google.com/")

# Entering meeting code
driver.find_element_by_xpath('//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/input').send_keys(code)
pyautogui.press("enter")
time.sleep(3)

# Allowing POP-UP
pyautogui.click(x=320, y=180)
pyautogui.click(x=324, y=206)
time.sleep(2)

# Turning off Mic and Camera
pyautogui.hotkey('ctrl', 'd')
pyautogui.hotkey('ctrl', 'e')
time.sleep(2)

# Joining & Giving Attendence
Joinbutton = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')

if Joinbutton.text == "Join now":
    Joinbutton.click()
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span').click()
    time.sleep(2)
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button/i').click()

else:
    Joinbutton.click()
    time.sleep(120)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span').click()
    time.sleep(2)
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button/i').click()

# Centering Mouse
pyautogui.moveTo(950, 580)
