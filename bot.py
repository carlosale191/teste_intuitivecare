import pyautogui as auto
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
#from PyPDF2 import PdfReader, PdfWriter
import shutil

download_dir = os.path.abspath("meus_pdfs")
# Garante que a pasta exista
os.makedirs(download_dir, exist_ok=True)
# Configurações do Chrome para download automático
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True  # faz o Chrome baixar o PDF em vez de abri-lo
}
options.add_experimental_option("prefs", prefs)

site = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
driver = webdriver.Chrome(options=options)
driver.get(site)
sleep(2)

auto.PAUSE = 0.5
driver.maximize_window()
auto.click(x=970, y=641)
sleep(2)

link1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Anexo I").click()
driver.switch_to.window(driver.window_handles[0])
sleep(5)
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Anexo II").click()
sleep(5)
driver.quit()

# compactar pdf
base_name = os.path.join(download_dir, "arquivos")
archive_path = shutil.make_archive(base_name, "zip", root_dir=download_dir)

input('')
