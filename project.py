

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
import time 



def Facebook():
	try:
		driver.get("https://www.facebook.com/")
	except:
		print("could'nt find the site")
	return

def Facebook_Login(username , password):
		name=driver.find_element_by_xpath('//*[@id="email"]')
		name.send_keys(username)
		PASS=driver.find_element_by_xpath('//*[@id="pass"]')
		PASS.send_keys(password)
		PASS.send_keys(Keys.RETURN)
		expected_url="https://www.facebook.com/"
		currenturl= driver.current_url
		print(currenturl)
		if currenturl!=expected_url:
			print("INVALID LOGIN :( ...!!!... Please Try again  ")
			username = input("Enter facebook ID: ")
			password = getpass.getpass("Password: ")
			driver.get("https://www.facebook.com/")
			Facebook_Login(username,password)

		return

def Birthdaywish():
	driver.get("https://www.facebook.com/events/birthdays/")
	wishes=driver.find_elements_by_xpath('//*[@class="enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput"]')
	if len(wishes)==0:
		print("No friends have birthday today")
		return
	for wish in wishes:
		wish.send_keys("Happy birthday")
		wish.send_keys(Keys.RETURN)
	#print(len(wishes))
	return

#global driver

username = input("Enter facebook ID: ")
password = getpass.getpass("Password: ")

path = "/home/dell/Desktop/chromedriver"
driver = webdriver.Chrome(path)

Facebook()

print("login .....  ")
Facebook_Login(username , password)

Birthdaywish()

#driver.quit()



