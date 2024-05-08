import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

file=open('config.txt')
lines=file.readlines()
username=lines[0]
password_from_file=lines[1]

browser=webdriver.Firefox()

# Navigate to LinkedIn login page
browser.get('https://www.linkedin.com/login')

# Enter username
username_field = browser.find_element(By.ID, 'username')
username_field.send_keys(username)

# Enter password
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys(password_from_file)

# Submit login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(30)

# Example profile URL
profile_url =['https://pk.linkedin.com/in/muhammad-hamza-435a012a6',
                'https://uk.linkedin.com/in/siobhang',
                'https://de.linkedin.com/in/stevenmorell',
                'https://www.linkedin.com/in/josh-g-roth',
                'https://www.linkedin.com/in/collincadmus']

# Navigate to the profile page
for i in profile_url:
        browser.get(i)

        # Wait for the page to load
        time.sleep(5)
        try:
            more_button = browser.find_element(By.XPATH, "(//span[text()='More'])[2]")
            more_button.click()
            connect_button=browser.find_element(By.ID,"ember68")
            connect_button.click()
            print("Clicked 'More' option.")
        except Exception as e:
            print(f"Failed to click 'More' option: {e}")

        # Wait for the connection options to load
        time.sleep(2)



    
