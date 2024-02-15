from config import url, authorization_url, redirect_uri, scope, strava_id, strava_secret ,email , password
from urllib.parse import urlencode
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, date
import os

import time

def scrapping(authorize_url):
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(authorize_url)

    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="authorize"]').click()

    time.sleep(5)
    redirected_url = driver.current_url
    driver.quit()
    return redirected_url.split("&")[1].replace("code=","")

def loginApi():

    authorize_params = {
        'client_id': strava_id,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
        'scope': scope,
    }

    authorize_url = f'{authorization_url}?{urlencode(authorize_params)}'

    authorization_code = scrapping(authorize_url)

    token_url = 'https://www.strava.com/oauth/token'
    token_params = {
        'client_id': strava_id,
        'client_secret': strava_secret,
        'code': authorization_code,
        'grant_type': 'authorization_code',
    }

    token_response = requests.post(token_url, data=token_params)
    access_token = token_response.json()['access_token']

    return access_token

access_token = loginApi()

activities_url = f'{url}athlete/activities'
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(activities_url, headers=headers)
activities = response.json()

if (int(activities[0]["moving_time"]) < 900) or (date.fromisoformat(activities[0]["start_date"].split("T")[0]) != date.fromisoformat(datetime.now().strftime('%Y-%m-%d'))):
    os.popen("shutdown /f /s /t 0")