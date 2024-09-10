from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()
    url = "https://www.saucedemo.com/"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        username = driver.find_element(By.ID, "user-name")
        username.send_keys('standard_user')

        wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password = driver.find_element(By.ID, "password")
        password.send_keys('secret_sauce')
        password.send_keys(Keys.RETURN)
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))
        products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        product = None
        for i in products:
            product = i.find_element(By.CLASS_NAME, 'inventory_item_name')
            if product.text == "Sauce Labs Backpack":
                i.find_element(By.TAG_NAME, 'button').click()
        
        if product:
            cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
            cart.click()

        wait.until(EC.presence_of_element_located((By.ID, 'cart_contents_container')))
        cart = driver.find_element(By.ID, 'cart_contents_container')
        cart_list = cart.find_elements(By.CLASS_NAME, 'cart_list')
        items = None
        for i in cart_list:
            items = i.find_elements(By.CLASS_NAME, 'cart_item')
        if items:
            for i in items:
                check_name_product = i.find_element(By.CLASS_NAME, 'inventory_item_name')
                if check_name_product.text == 'Sauce Labs Backpack':
                    print("Товар успешно добавлен в корзину!")
                else:
                    print("Ошибка, товара в корзине нет.")
                    driver.quit()

        driver.find_element(By.ID, 'checkout').click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'checkout_info')))
        f_name_info = driver.find_element(By.ID, 'first-name')
        f_name_info.send_keys('Alex')
        l_name_info = driver.find_element(By.ID, 'last-name')
        l_name_info.send_keys('Black')
        p_code_info = driver.find_element(By.ID, 'postal-code')
        p_code_info.send_keys('123456')
        driver.find_element(By.ID, 'continue').click()
        
        driver.find_element(By.ID, 'finish').click()
        
        complete_text = driver.find_element(By.CLASS_NAME, 'complete-text')
        if complete_text.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!":
            print("Заказ успешно оформлен и будет отправлен в ближайшее время!")
        else:
            print("Ничего не вышло, заказ потерялся...")
            driver.quit()
    except:
        print('Error')

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
