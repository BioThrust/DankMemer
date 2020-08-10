
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from pynput.keyboard import Key, Listener, Controller as KeyController
from pynput import keyboard as KB
from pynput.mouse import Button, Controller
import random
fCounter = 0
chromedriver = 'C:/Users/neppa/Downloads/drive-download-20200810T210848Z-001/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--headless")
listing = ['woah a big one', 'fish fish fish fishy', 'hook line sinker', 'big fishy', 'get the camera ready', 'this is very fishy', 'Big bait catches big fish']
plsopenfile = open("email.txt")
email = plsopenfile.read()
plsopenfile2 = open("password.txt")
password = plsopenfile2.read()
plsopenfile3 = open("destination.txt")
destination = plsopenfile3.read()
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

browser.get("https://discord.com/channels/722915812175773716/723525411052585049")
browser.implicitly_wait(10)
inputElement = browser.find_element_by_name("email")
keyboard = KeyController()
mouse = Controller()





def on_release(key):
    if key == Key.esc:
        browser.quit()
        os._exit(0)

listener = KB.Listener(
    on_release=on_release)
listener.start()



 


inputElement.send_keys("sciscor.x@gmail.com")
inputSecondaryElement = browser.find_element_by_name("password")
inputSecondaryElement.send_keys("12345green")
inputSecondaryElement.send_keys(Keys.ENTER)
time.sleep(5)
input3Element = browser.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')

def enter(times):
    
    input3Element.send_keys(Keys.ENTER)
    time.sleep(times)
while True:
    c = "pls beg pls fish pls hunt"
    def detection():
        last5 = browser.find_elements_by_class_name('message-2qnXI6')[-5:]
        for i in last5:
            try:
                if(i.find_element_by_class_name('inline') and i.find_element_by_class_name('inline').text in listing):
                    input3Element.send_keys(i.find_element_by_class_name('inline').text)
                    input3Element.send_keys(Keys.ENTER)
            except:
                pass
        

    for char in c:
        
        input3Element.send_keys(char)
        if(char == "g"):       
            enter(random.randint(10,51))
        elif (char == "h" and fCounter == 0):
            
            input3Element.send_keys(Keys.ENTER)
            detection()
            
            
            time.sleep(random.randint(50,60))
            fCounter = 1
        elif (char == "t"):
            enter(random.randint(1, 31))
            fCounter = 0
            
        
            


browser.quit()