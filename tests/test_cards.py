import pytest
from selenium import webdriver

from royale.pages.base.card_details_page import CardDetailsPage
from royale.pages.cards_page import CardsPage
from royale.services import card_service

cards = card_service.get_all_cards()


@pytest.mark.parametrize('api_card', cards)
def test_card_is_displayed(api_card):  # EARTHQUAKE
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')

    cards_page = CardsPage(driver).goto()
    card_on_page = cards_page.get_card_by_name(api_card.name)
    assert card_on_page.is_displayed()


@pytest.mark.parametrize('api_card', cards)
def test_ice_spirit_details_displayed(api_card):
    driver = webdriver.Chrome()

    driver.get('https://statsroyale.com')

    CardsPage(driver).goto().get_card_by_name(api_card.name).click()

    card = CardDetailsPage(driver).get_base_card()

    assert card.name == api_card.name
    assert card.type == api_card.type
    assert card.arena == api_card.arena
    assert card.rarity == api_card.rarity


def test_mirror_spirit_details_displayed():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')

    CardsPage(driver).goto().get_card_by_name('Mirror').click()

    card = CardDetailsPage(driver).get_base_card()

    assert card.name == 'Mirror'
    assert card.type == 'Spell'
    assert card.arena == 12
    assert card.rarity == 'Epic'
