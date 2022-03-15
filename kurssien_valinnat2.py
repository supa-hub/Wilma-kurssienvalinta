
from selenium import webdriver
import time
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException

sähköposti = ""
password = ""

elements_list = ["/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/ul/li[4]/ul/li/a[22]",
                 "/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/ul/li[2]/ul/li/a[25]"]


class kurssienvalinta:
    #init vaa määrittelee sen chromedriver ei paljoo muuta
    def __init__(self):
        self.webdriver_path = Path("chromedriver.exe")
        self.driver = webdriver.Chrome(self.webdriver_path)
        self.j = True

    #tää osio kirjautuu wilmaan ja menee kurssitarjottimeen
    def kirjaudu_wilmaan(self):
        self.driver.get("https://edutampere.inschool.fi/")
        elem = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div/form/div[6]/div/a/button")
        elem.click()
        time.sleep(3)
        elem  = self.driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
        elem.send_keys(sähköposti)
        elem = self.driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input")
        elem.click()
        time.sleep(3)
        elem = self.driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input")
        elem.send_keys(password)
        elem = self.driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath("/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input")
        elem.click()
        time.sleep(3)

        time.sleep(1)
        

    #tää osa tarkistaa, jos voi valita kursseja ja sit ku voi, niin valitsee ne.
    def valitse_kurssit(self,element_list):

        self.driver.get("https://edutampere.inschool.fi/selection/view?")
        time.sleep(2)

        
        try:
            print("JOO")
            self.driver.get("https://edutampere.inschool.fi/selection/view?")
            time.sleep(2)
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[1]/a")
            elem.click()
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[2]/a")
            elem.click()
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[3]/a")
            elem.click()
            time.sleep(1)
            print("juuuuu")
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[1]/label/input")
            elem.click()
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[2]/ul/li[1]/ul/li/a[22]")
            elem.click()
            time.sleep(0.5)
            print("joo")
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[1]/a/spanjooooooo")

            print("eiii")
        except NoSuchElementException as e:
            print("eipä ollu ;(")
            self.driver.get("https://edutampere.inschool.fi/selection/view?")
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[1]/a")
            elem.click()
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[2]/a")
            elem.click()
            elem = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[3]/a")
            elem.click()
            time.sleep(1)
            for elements in element_list:
                elem = self.driver.find_element_by_xpath(elements)
                elem.click()
            self.j = False
            
            
            

            time.sleep(60)



x = kurssienvalinta()
x.kirjaudu_wilmaan()
x.valitse_kurssit(elements_list)
