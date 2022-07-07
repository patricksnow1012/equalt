from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest
from behave import *

class Crypto(unittest.TestCase):

    @given('Equalt Start')
    def steps(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1920, 1080)
        self.browser.delete_all_cookies()
        self.browser.get('chrome://settings/')
        self.browser.execute_script('chrome.settingsPrivate.setDefaultZoom(0.9);')
        self.browser.get('https://equalt-main.ktsdev.ru/')
        time.sleep(2)
    
    @when('Questions Cryptobasics')
    def steps(self):
        lessonone = "/html/body/div[1]/main/div/section[1]/div/div[1]/div[2]/a"
        clickbutton = "/html/body/div[1]/main/div/section[1]/div/div[2]/a"
        nextlesson = "/html/body/div[1]/main/div/div/aside/nav/div[1]/a[2]"
        nextlesson2 = "/html/body/div[1]/main/div/div/aside/nav/div[2]/a[2]/span"
        nextlesson3 = "/html/body/div[1]/main/div/div/div/div[3]/div/a[2]/span"
        startfinal = "//*[contains(text(),'Start the quiz') ]"
        
        self.browser.find_element(By.XPATH, lessonone).click()
        time.sleep(2)

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 0)")

        self.browser.find_element(By.XPATH, clickbutton).click()
        time.sleep(3)

        self.browser.find_element(By.XPATH, nextlesson).click()
        time.sleep(3)

        self.browser.find_element(By.XPATH, nextlesson2).click()

        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        self.browser.find_element(By.XPATH, nextlesson3).click()
        time.sleep(2)

        self.browser.find_element(By.XPATH, nextlesson2).click()
        time.sleep(4)

        self.browser.find_element(By.XPATH, startfinal).click()
        time.sleep(4)

    @when('Completed Final Test')
    def steps(self):
#Вопросы-------------------------------------------------------------------------------------------------------------
        one = "//div[contains(text(),'Axie Infinity is an example of') ]"
        two = "//div[contains(text(),'What determines which cryptocurrency is needed to start in a P2E game?') ]"
        three = "//div[contains(text(),'Imagine that your friend has advised you on a new crypto game.') ]"
        four = "//div[contains(text(),'You have joined the Discord channel of the popular crypto game Axie Infinity.') ]"
        five = "//div[contains(text(),'If I come up with my own token and ask influencers to promote it') ]"
        six = "//div[contains(text(),'In 2010, one person paid for a pizza with 10,000 bitcoins') ]"
        seven = "//div[contains(text(),'What was more profitable to invest in 2008 (and is still relevant now)?') ]"
        eit = "//div[contains(text(),'you do with NFTs?') ]"
        ninth = "//div[contains(text(),'Select the options you') ]"
        ten = "//div[contains(text(),'Where is the blockchain data stored?') ]"
        eleven = "//div[contains(text(),'You have a Metamask wallet that helps you interact') ]"
        twelve = "//div[contains(text(),'You have decided to buy tokens for the game, which launches') ]"
        thirteen = "//div[contains(text(),'Which type of exchange is more secure and anonymous?') ]"
        fourteen = "//div[contains(text(),'Ethereum is the most convenient and cheap blockchain for making transaction') ]"
        fifteen = "//div[contains(text(),'You want to buy a new cryptocurrency, its developers promise that if') ]"
        sixteen = "//div[contains(text(),'In play-to-earn games everything depends on how much you') ]"
        seventeen = "//div[contains(text(),'On Twitter you saw a post from a blogger about a new game:') ]"
        eighteen = "//div[contains(text(),'The Ethereum blockchain is the only blockchain on which') ]"
        nighteen = "//div[contains(text(),'You want to make a transfer to a person abroad. Which method is faster?') ]"
        twenty = "//div[contains(text(),'What happens if a transaction is forged in the blockchain?') ]"
        twentyone = "//div[contains(text(),'Token price is determined by') ]"
        twentytwo = "//div[contains(text(),'Where do you store your cryptocurrency') ]"
        twentythree = "//div[contains(text(),'You transfer cryptocurrency to a friend. What information') ]"
        twentyfour = "//div[contains(text(),'Where is the least safe place to keep your cryptocurrency?') ]"
#--------------------------------------------------------------------------------------------------------------------

        self.listning = [one, two, three, four, five, six, seven, eit, ninth, ten, eleven, twelve, eighteen, fourteen, fifteen, sixteen, seventeen, eighteen, nighteen, twenty, twentyone, twentytwo, twentythree, twentyfour]
        for self.listning in range(10):
            #Axie Infinity is an example of
            try:
                self.browser.find_element(By.XPATH, one)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'A famous') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #What determines which cryptocurrency is needed to start in a P2E game?
            try:
                self.browser.find_element(By.XPATH, two)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Blockchain on which the game runs and the native utility token of the project') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Imagine that your friend has advised you on a new crypto game
            try:
                self.browser.find_element(By.XPATH, three)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Make additional research, maybe read reviews and find additional info') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #You have joined the Discord channel of the popular crypto game Axie Infinity.
            try:
                self.browser.find_element(By.XPATH,four)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'I will message the moderator and block that user.') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #If I come up with my own token and ask influencers to promote it
            try:
                self.browser.find_element(By.XPATH, five)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'No, because the value of a crypto depends on many variables') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #In 2010, one person paid for a pizza with 10,000 bitcoins
            try:
                self.browser.find_element(By.XPATH, six)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//*[contains(text(),'True') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #What was more profitable to invest in 2008 (and is still relevant now)?
            try:
                self.browser.find_element(By.XPATH, seven)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'bitcoins') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #you do with NFTs?
            try:
                self.browser.find_element(By.XPATH, eit)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Copy them and sell these copies') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Select the options you
            try:
                self.browser.find_element(By.XPATH, ninth)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'cash out without changing it to fiat') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Where is the blockchain data stored?
            try:
                self.browser.find_element(By.XPATH, ten)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Worldwide on different devices') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #You have a Metamask wallet that helps you interact
            try: 
                self.browser.find_element(By.XPATH, eleven)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Just open a wallet that works with Tron (like Trust Wallet)') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #You have decided to buy tokens for the game, which launches
            try:
                self.browser.find_element(By.XPATH, twelve)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Asset to start the game') ]").click()
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Possibility to get additional functions in the future') ]").click()
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Ability for trading these tokens') ]").click()
                self.browser.find_element(By.XPATH, "//div[contains(text(),'The ability to make decisions in the development of the game') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Which type of exchange is more secure and anonymous?
            try:
                self.browser.find_element(By.XPATH, thirteen)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Decentralized exchanges') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Ethereum is the most convenient and cheap blockchain for making transaction
            try:
                self.browser.find_element(By.XPATH, fourteen)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'No, Ethereum is one of the most expensive') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #You want to buy a new cryptocurrency, its developers promise that if'
            try:
                self.browser.find_element(By.XPATH, fifteen)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Not invest, the cryptocurrency') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #In play-to-earn games everything depends on how much you
            try:
                self.browser.find_element(By.XPATH, sixteen)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'False') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #On Twitter you saw a post from a blogger about a new game:
            try:
                self.browser.find_element(By.XPATH, seventeen)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'No') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #The Ethereum blockchain is the only blockchain on which
            try:
                self.browser.find_element(By.XPATH, eighteen)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'False') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #You want to make a transfer to a person abroad. Which method is faster?
            try:
                self.browser.find_element(By.XPATH, nighteen)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Transfer cryptocurrency') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #What happens if a transaction is forged in the blockchain?
            try:
                self.browser.find_element(By.XPATH, twenty)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Nothing - the fake transaction will not be verified') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Token price is determined by
            try:
                self.browser.find_element(By.XPATH, twentyone)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Supply and demand') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Where do you store your cryptocurrency
            try:
                self.browser.find_element(By.XPATH, twentytwo)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Digital Wallet') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #You transfer cryptocurrency to a friend. What information
            try:
                self.browser.find_element(By.XPATH, twentythree)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'Wallet address') ]").click()
                self.browser.find_element(By.XPATH, "//div[contains(text(),'The amount of crypto') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
            #Where is the least safe place to keep your cryptocurrency?
            try:
                self.browser.find_element(By.XPATH, twentyfour)
            except BaseException:
                print("Пропускаем")
            else:
                self.browser.find_element(By.XPATH, "//div[contains(text(),'On an exchange') ]").click()
                time.sleep(2)
                self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/button").click()
                time.sleep(3)
    
    @then('Metapass')
    def steps(self):
        time.sleep(2)
        getreward = "/html/body/div[1]/main/div/div/section[2]/div/div/a[1]"
        self.browser.find_element(By.XPATH, getreward).click()
        time.sleep(5)