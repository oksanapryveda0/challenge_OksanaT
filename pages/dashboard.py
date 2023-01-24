from pages.base_page import BasePage


class Dashboard(BasePage):
    mainPage_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    players_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]'
    changeLanguage_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]'
    signOut_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]'
    addPlayerButton_ = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]'
    devTeamContactButton_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]'
    lastCreatedPlayerName_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]'
    lastUpdatedPlayerName_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]'
    lastCreatedMatch_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]'
    lastUpdatedMatch_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1]'

    pass

