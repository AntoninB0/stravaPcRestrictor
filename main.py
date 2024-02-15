from config import strava_id, strava_secret ,email , password
import requests
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import time

url = 'https://www.strava.com/api/v3/'
authorization_url = 'https://www.strava.com/oauth/authorize'
redirect_uri = 'http://localhost:8080/callback'
scope = 'read_all,activity:read_all'

authorize_params = {
    'client_id': strava_id,
    'redirect_uri': redirect_uri,
    'response_type': 'code',
    'scope': scope,
}

authorize_url = f'{authorization_url}?{urlencode(authorize_params)}'
print(f'Authorize the app by visiting the following link and copy the authorization code from the URL:\n{authorize_url}')

################################################

driver = webdriver.Firefox()
driver.get(authorize_url)

driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
driver.find_element(By.XPATH, '//*[@id="authorize"]').click()

time.sleep(10)
redirected_url = driver.current_url
driver.quit()

################################################


print(redirected_url.split("&")[1].replace("code=",""))

authorization_code = redirected_url.split("&")[1].replace("code=","")

token_url = 'https://www.strava.com/oauth/token'
token_params = {
    'client_id': strava_id,
    'client_secret': strava_secret,
    'code': authorization_code,
    'grant_type': 'authorization_code',
}

token_response = requests.post(token_url, data=token_params)
access_token = token_response.json()['access_token']

activities_url = f'{url}athlete/activities'
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(activities_url, headers=headers)
activities = response.json()

print(activities[-1])