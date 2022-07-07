from selenium import webdriver # Импорт драйвера селениум
from selenium.webdriver.common.keys import Keys # Чтобы взаимодействовать с командами клавиатуры
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # Наведение курсора на элемент
import unittest
from behave import *
import time #Таймаут на тест

class Equalt(unittest.TestCase):

    @given('Start Equalt')
    def steps(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1920, 1080) # Устанавливаю разрешение экрана
        self.browser.get('chrome://settings/')
        self.browser.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
        self.browser.get('https://equalt-main.ktsdev.ru')
        time.sleep(5)

# Авторизация под уже существующим аккаунтом
    @when('Authorization Equalt')
    def steps(self):
        xpath = "/html/body/div[1]/main/header/div/nav/div/div/div/div[1]/a"
        element = "//*[@id='root']/main/div[2]/section/div/div/div/a[4]"

        self.browser.find_element(By.XPATH, xpath).click()
        time.sleep(4)
        self.browser.find_element(By.XPATH, element).click()
        time.sleep(3)

    @when('Set Login and Password')
    def steps(self):
        form = "//*[@id='root']/main/div[2]/section/div/div/div/form/div[1]/div[1]/div[2]/input"
        password = "//*[@id='root']/main/div[2]/section/div/div/div/form/div[2]/div[1]/div[2]/input"
        click = "/html/body/div/main/div[2]/section/div/div/div/button"

        self.browser.find_element(By.XPATH, form).send_keys("kruj1985@gmail.com")
        self.browser.find_element(By.XPATH, password).send_keys("Fuckers228")
        self.browser.find_element(By.XPATH, click).click()
        time.sleep(15)

# Здесь авторизация закончилась
# А здесь мы выходим

    @then('Logout')
    def steps(self):
        option = ActionChains(self.browser); # Подключаю ActionChains для наведения курсора на элемент
        firsrLevelMenu = self.browser.find_element(By.XPATH, "/html/body/div[1]/main/header/div/nav/div/div/div/a/span")
        option.move_to_element(firsrLevelMenu).perform()
        secondLevelMenu = self.browser.find_element(By.XPATH, "/html/body/div[1]/main/header/div/nav/div/div/div/div/div/ul/li[2]/button")
        option.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(5)

# Практикуем регистрацию
    @then('Registration Page')
    def steps(self):
        elementreg = "/html/body/div[1]/main/header/div/nav/div/div/div/div[1]/a/span"
        buttonreg = "//*[@id='root']/main/div[2]/section/div/div/div/a[5]/p"
        newadrrs = "/html/body/div[8]/div[1]/div[2]/div[1]/div/div[1]/button"
        mailup = "/html/body/div[8]/div[1]/div[2]/div[1]/form/div/button"

        self.browser.find_element(By.XPATH, elementreg).click()
        time.sleep(2)
        
        self.browser.find_element(By.XPATH, buttonreg).click()
        time.sleep(5)

        self.browser.execute_script("window.open();") # Вызываю новое окно в браузере
        self.browser.switch_to.window(self.browser.window_handles[1]) # Переключаюсь на новую вкладку для работы с ней
        self.browser.get("https://tempmail.plus/ru/#!")
        time.sleep(10)
        
        self.browser.find_element(By.XPATH, newadrrs).click()
        time.sleep(3)
        
        self.browser.find_element(By.XPATH, mailup).click()
        self.browser.switch_to.window(self.browser.window_handles[0]) # Переключаюсь на старую вкладку

    @then('Finish')
    def steps(self):
        clickmail = "//*[@id='root']/main/div[2]/section/div/section/div/form/div[1]/div[1]/div[2]/input"
        paswd = "//*[@id='root']/main/div[2]/section/div/section/div/form/div[2]/div[1]/div[2]/input"
        clickbutton = "/html/body/div/main/div[2]/section/div/section/div/div[2]/div/label/div/div/div"
        start = "/html/body/div/main/div[2]/section/div/section/div/button"

        self.browser.find_element(By.XPATH, clickmail).send_keys(Keys.CONTROL + "v")
        
        self.browser.find_element(By.XPATH, paswd).send_keys("Fuckers228")
        
        self.browser.find_element(By.XPATH, clickbutton).click()
        
        self.browser.find_element(By.XPATH, start).click()
        time.sleep(5)

        self.browser.switch_to.window(self.browser.window_handles[1]) # Перехожу обратно на почту для подтверждения аккаунта
        self.browser.get("https://tempmail.plus/ru/#!")
        time.sleep(10)
        self.browser.refresh()
        time.sleep(10)
        self.browser.refresh()
        time.sleep(5)
        self.browser.find_element(By.XPATH, "//div[contains(text(),'Please approve your email') ]").click()
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//*[@id='info']/div[3]/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr/td/div/div/a/span/span")