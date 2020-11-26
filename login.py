import requests
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
import getpass
from bs4 import BeautifulSoup

link = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
url = 'http://45.79.43.178/source_carts/wordpress/wp-admin'
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get(link)

usr = "admin"
pwd = "123456aA"


#Login's input
username_box = driver.find_element_by_id('user_login') 
username_box.send_keys(usr) 

password_box = driver.find_element_by_id('user_pass') 
password_box.send_keys(pwd) 

login_box = driver.find_element_by_id('wp-submit') 
login_box.click() 

#get username after login
soup = BeautifulSoup("""<span class="display-name">admin</span>""", "html.parser")
print(soup.string)





