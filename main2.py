from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Открываем файл для записи логов
file=open("log.txt","w")

# Инициализация драйвер браузера (Chrome)
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # Опция, которая оставляет страницу открытой
#options.add_argument("--headless") # Режим без открытия браузера
driver = webdriver.Chrome(options=options)

# Sc function............
def set_up():# Переход на страницу сайта в виде функции
    driver.get('http://saucedemo.com/')
    driver.maximize_window()# Максимальный размер окна


# Оформление процесса тестирования в виде функции
def login():
    user_name=driver.find_element(By.XPATH,'//*[@id="user-name"]') # Поиск поля для ввода логина
    login="standard_user"
    user_name.send_keys(login) # Ввод имени пользователя
    file.write("Success write login\n") # Запись в лог

    user_pass = driver.find_element(By.XPATH, '//*[@id="password"]')  # Поиск поля для ввода пароля
    password="secret_sauce"
    user_pass.send_keys(password)  # Ввод пароля
    file.write("Success write password\n")  # Запись в лог

    login_butt = driver.find_element(By.XPATH, '//*[@id="login-button"]')  # Поиск кнопки и клик по ней
    login_butt.click()
    file.write("Success click login\n")  # Запись в лог

def fake_login():
    user_name=driver.find_element(By.XPATH,'//*[@id="user-name"]') # Поиск поля для ввода логина
    login="standard_user"
    user_name.send_keys(login) # Ввод имени пользователя
    file.write("Success write login\n") # Запись в лог

    user_pass = driver.find_element(By.XPATH, '//*[@id="password"]')  # Поиск поля для ввода пароля
    password="secret_sauce1"
    user_pass.send_keys(password)  # Ввод пароля
    file.write("Success write fake password\n")  # Запись в лог

    login_butt = driver.find_element(By.XPATH, '//*[@id="login-button"]')  # Поиск кнопки и клик по ней
    login_butt.click()
    file.write("Success click login\n")  # Запись в лог
# End of Sc function............

def test_login_redirect(): # Функция правильного открытия нужной веб. страницы
    correct_url="https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")

def test_context_after_login_is_correct(): # Проверка правильного текста на странице
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK \n")

# Конец теста

def test_fake_login_Label():
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text == current_text.text, "test_fake_login_Label is Failed"
    file.write("test_fake_login_Label is OK \n")

def sc_real_login():
    set_up()
    login()


    test_login_redirect()
    test_context_after_login_is_correct()


def sc_fake_login():
    set_up()
    fake_login()
    test_fake_login_Label()

sc_fake_login()
sleep(2)
file.close()

driver.quit() # Закрытие файла и завершение работы драйвера
