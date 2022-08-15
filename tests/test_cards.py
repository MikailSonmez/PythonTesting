from selenium import webdriver
from selenium.webdriver.common.by import By

from royale.pages.base.card_details_page import CardDetailsPage
from royale.pages.cards_page import CardsPage


def test_ice_spirit_is_displayed():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')

    cards_page = CardsPage(driver).goto()
    ice_spirit = cards_page.get_card_by_name('Ice Spirit')
    assert ice_spirit.is_displayed()


def test_ice_spirit_details_displayed():
    driver = webdriver.Chrome()

    # 1. go to statsroyale.com
    driver.get('https://statsroyale.com')

    # 2. go to cards page
    # 3. assert Ice Spirit is displayed
    CardsPage(driver).goto().get_card_by_name('Ice Spirit').click()

    # 4. get the card, name, type. arena, and rarity
    details_page = CardDetailsPage(driver)
    card_name = details_page.map.card_name.text
    split = details_page.map.card_category.text.split(', ')
    card_type = split[0]
    card_arena = split[1]
    card_rarity = details_page.map.card_rarity.text.split('\n')[1]

    # 5. assert they are correct
    assert card_name == 'Ice Sprit'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'
