from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()

pesquisas = ['jó', 'reus', 'abacaxi', 'pindoretama', 'filmes', 'oscar', 'brinquedo', 'panela',
             'morango', 'receitas', 'bolos', 'chatgpt', 'surf', 'skate', 'Bíblia', 'ciencia', 'dados',
             'TI', 'python', 'turing', 'musicas', 'cifras', 'anime', 'AD', 'circo', 'oficina',
             'opera', '3', 'netflix', 'amazon', 'liverpool', 'tinta', 'bitwarden', 'peixe']

driver.get('https://www.bing.com/search?q=BB&qs=HS&sk=HS4&sc=10-0&cvid=77090C75775F472C928FAF56AA8375D0&FORM=QBLH&sp=5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bnp_btn_accept")))
driver.find_element(By.CSS_SELECTOR, "#bnp_btn_accept").click()
sleep(8)
cont = 1

for c in pesquisas:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sb_form"]/div/div[2]/div[1]')))
    elemento = driver.find_element(By.XPATH, '//*[@id="sb_form"]/div/div[2]/div[1]')
    ActionChains(driver).double_click(elemento).\
        send_keys(Keys.BACKSPACE).\
        send_keys(c).\
        perform()
    driver.find_element(By.XPATH, '//*[@id="sb_go_par"]').click()
    print(cont)
    cont += 1

driver.quit()
