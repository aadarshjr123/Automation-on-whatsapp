try:
  from selenium import webdriver
except ImportError:
    print('\nError: Module Selenium not found!\n\nPress any key to continue...')
    x=input()
    exit(1)
from time import sleep
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')


name =input('Enter the name:')
msg=input('Enter the message:')
count = int(input('Enter the count:'))
filepath =input('Enter your filepath (images/video):')


ch=input('Enter anything after scan')


user= driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()

attachment_box= driver.find_element_by_xpath('//div[@title = "Attach"]').click()


image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(filepath)

sleep(3)


send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]').click()






msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):

    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_3M-N-').click()
