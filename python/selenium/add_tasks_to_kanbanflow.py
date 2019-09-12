# this script is solely useful for users of kanbanflow.com
# for non premium users there is no way we can add list of tasks by upload
# so this scipt is used to upload and add all list of tasks to the board if we have an excel
# which contains list of tasks that need to be added to the board.

# import required libs
from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome()   #kickstart webdriver
driver.get('https://kanbanflow.com/board/1****')   # navigate to specific board
driver.find_elements_by_xpath('//*[@id="email"]')[0].send_keys('email') # email id/cred
driver.find_elements_by_xpath('//*[@id="password"]')[0].send_keys('pwd')  # pwd /cred
driver.find_elements_by_xpath('//*[@id="loginForm"]/p[4]/button')[0].click()  # submit form/login

driver.find_elements_by_xpath('//*[@id="board-table"]/thead/tr/th[1]/div/button')[0].click() # add into to-do 
# driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div[1]/textarea')[0].send_keys('test')
# driver.find_element_by_xpath('//*[@id="addTaskDialog-saveAndAddMore').click()

df = pd.read_excel('excel_file.xlsx') # load excel file to dataframe
df1 = df[:,1] #slice specific column of a dataframe

# run through all the rows from selected column as list and add them to board
for x in df1:
	driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div[1]/textarea').send_keys(x)
	sleep(2)
	driver.find_element_by_xpath('//*[@id="addTaskDialog-saveAndAddMore"]').click()
	sleep(1)
  
driver.quit()
