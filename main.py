from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Открываем файл для записи логов
file=open("log.txt","w")

# Инициализация драйвер браузера (Chrome)
driver=webdriver.Chrome()

# Переход на страницу сайта
driver.get('http://saucedemo.com/')
driver.maximize_window() # Максимальный размер окна

# Оформление процесса тестирования в виде функции
def login():
    user_name=driver.find_element(By.XPATH,'//*[@id="user-name"]') # Поиск поля для ввода логина
    login="standart_user"
    user_name.send_keys(login) # Ввод имени пользователя
    file.write("Success write login\n") # Запись в лог

    user_pass = driver.find_element(By.XPATH, '//*[@id="password"]')  # Поиск поля для ввода пароля
    password="secret_sauce"
    user_pass.send_keys(password)  # Ввод пароля
    file.write("Success write password\n")  # Запись в лог

    login_butt = driver.find_element(By.XPATH, '//*[@id="login-button"]')  # Поиск кнопки и клик по ней
    login_butt.click()
    file.write("Success click login\n")  # Запись в лог

sleep(2)

login()
sleep(2)
file.close()
sleep(2)
driver.quit() # Закрытие файла и завершение работы драйвера
