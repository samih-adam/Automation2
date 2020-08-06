# selenium practice
from selenium import webdriver

# so this right here is to make sure that you are directing the program to chromedriver,
#  this is how we are going to open up webpages

PATH = "/Users/samieh/Desktop/chromedriver"

# this right here is setting driver to PATH variable
driver = webdriver.Chrome(PATH)

#this is the page we are going to, if you run the program from here it will allow you to go this webpage straignt from 
# terminal, just have to press run baby 
driver.get("https://techwithtim.net")
# this will close the tab
# driver.quit() will quit the whole page baby
#driver.title will show the title of the webpage
print(driver.title)
driver.quit()

