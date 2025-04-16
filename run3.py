from selenium import webdriver
import time

# Inisialisasi browser (Chrome)
driver = webdriver.Chrome()

# Buka halaman (misalnya Google)
driver.get("https://samplefocus.com/users/sign_up")
time.sleep(2)
print("Title halaman:", driver.title)
time.sleep(2)
