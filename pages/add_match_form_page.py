from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddMatchFormPage(BasePage):
    myTeamInput_name = BasePage.driver.find_element(By.NAME, 'myName')
    enemyTeamInput_name = BasePage.driver.find_element(By.NAME, 'enemyTeam')
    myTeamScoreInput_name = BasePage.driver.find_element(By.NAME, 'myTeamScore')
    datePicker_name = BasePage.driver.find_element(By.NAME, 'date')
    tShirtSize_name = BasePage.driver.find_element(By.NAME, 'tshirt')
    league_name = BasePage.driver.find_element(By.NAME, 'league')
    timePlayed_name = BasePage.driver.find_element(By.NAME, 'timePlayed')
    number_name = BasePage.driver.find_element(By.NAME, 'number')
    webMatch_name = BasePage.driver.find_element(By.NAME, 'webMatch')
    general_name = BasePage.driver.find_element(By.NAME, 'general')
    submitButton_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[1]'





    pass