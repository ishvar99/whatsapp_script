from selenium import webdriver 
 
driver = webdriver.Chrome('D:/chromedriver') 
  
driver.get('https://web.whatsapp.com/')
while True:
	name = input('Enter the name of user or group : ')
	msg = input('Enter your message : ')
	count =int(input('Enter the count : '))

	input('Enter anything after scanning QR code')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div' )


	for i in range(count):
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_35EW6')
		button.click()