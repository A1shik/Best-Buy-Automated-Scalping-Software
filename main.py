# Best Buy scalper bot
#
# Description: This application takes in a link to buy an item
# from Best Buy and automatically purchases the item once it
# becomes available for purchase.
#
# Inputs: In the source code below, you will need to specify your
# Best Buy login information and cvv# for your credit card that is
# saved as your primary card
# on the website.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# insert your path for your chromedriver here
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("insert best buy item link here")

# flag for checkout button availability
buyButton = False

# loop until add to cart button is available
while not buyButton:
    try:
        driver.find_element_by_class_name("c-button-disabled")
        print("add to cart button is not ready yet")

        time.sleep(1)
        driver.refresh()
    except:
        buyButton = True
        print("button is ready")

# after add to cart button is available execute actions to buy the item
try:
    # click add to cart
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fulfillment-add-to-cart-button"))
    )
    element.click()
    print("add to cart button was clicked")

    # click go to cart
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "go-to-cart-button"))
    )
    element.click()
    print("go to cart button was clicked")

    # click checkout
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "checkout-buttons__checkout"))
    )
    element.click()
    print("checkout button was clicked")

    # input email
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fld-e"))
    )
    element.clear()
    element.send_keys("insert email here...")
    print("inputted email address")

    # input password
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fld-p1"))
    )
    element.clear()
    element.send_keys("insert password here...")
    print("inputted password")

    # click login
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cia-form__controls"))
    )
    element.click()

    # input cvv
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cvv"))
    )
    element.clear()
    element.send_keys("insert cvv here...")

    # place order button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "payment__order-summary"))
    )
    element.click()
    print("place order button was clicked")
except:
    driver.quit()