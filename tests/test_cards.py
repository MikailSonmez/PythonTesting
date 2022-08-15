from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ice_spirit_is_displayed():
    driver = webdriver.Chrome()

    # 1. go to statsroyale.com
    driver.get('https://statsroyale.com')

    # 2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    # 3. assert Ice Spirit is displayed
    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert ice_spirit_card.is_displayed()

    # 4. get the card, name, type. arena, and rarity
    card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text
    split = driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text.split(', ')
    card_type = split[0]
    card_arena = split[1]
    card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*=rarityCaption']").text.split('\n')[1]

    # 5. assert they are correct
    assert card_name == 'Ice Sprit'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'
