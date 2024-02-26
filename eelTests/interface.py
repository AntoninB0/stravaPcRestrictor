import eel
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Set web files folder
eel.init('eelTests/web')






def connexion(url,z):
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox()#options=firefox_options
    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(z[0])
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(z[1])
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="name"]').send_keys("PcRestrictor")
    
    driver.find_element(By.XPATH, '//*[@id="react-select-4-input"]').send_keys("Motivation sociale")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div/div/main/div/div/form/div[1]/div/div[1]/div[2]').send_keys("Motivation sociale")
    
    driver.find_element(By.XPATH, '//*[@id="userSupportUrl"]').send_keys("https://github.com/fafathebest")
    driver.find_element(By.XPATH, '//*[@id="domain"]').send_keys("read_all")
    driver.find_element(By.XPATH, '//*[@id="apiAgreement"]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div/div/main/div/div/form/button').click()




    

    

@eel.expose                         # Expose this function to Javascript
def submit_py(x,y,z):

    connexion("https://www.strava.com/settings/api",z)

    print(x,y,z)




eel.start('main.html', size=(1000, 1000))  # Start