# Se han eliminado los import fuera de uso.
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
#Se han movido todos los localizadores a esta clase UrbanRoutesPage.
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    taxi_button = (By.CLASS_NAME, "button round")
#Se sustituyó la ruta de XPATH que podía quedar obsoleta y se identificó el elemento a través de ID o CLASS
    comfort_button = (By.ID, 'tariff-card-4')
    close_phone_section = (By.CLASS_NAME, "close-button section-close")
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, "phone")
#Se sustituyó la ruta de XPATH que podía quedar obsoleta y se identificó el elemento a través de ID o CLASS
    phone_send = (By.CLASS_NAME, "button full")
    payment_method = (By.CLASS_NAME, "pp-text")
    card_add_button = (By.CLASS_NAME, "pp-title")
    add_credit_card = (By.XPATH, '//*[text() # "Agregar Tarjeta"]')
    add_card_number = (By.ID, "number")
    card_cvv = (By.XPATH, '//*[@id="code"]')
    add_click_payment_method = (By.CLASS_NAME, "card-wrapper")
    driver_message = (By.XPATH, '//*[@id="comment"]')
    write_message = (By.CSS_SELECTOR, "#comment")
    input_phone_code = (By.ID, "code")
    requests_button = (By.CLASS_NAME, "reqs-head")
    blanket_and_scarves = (By.CLASS_NAME, "r-sw-label")
    ice_cream_counter = (By.CLASS_NAME, "r-counter")
    taxi_search_button = (By.CLASS_NAME, "smart-button-main")
    taxi_search_section = (By.CLASS_NAME, "order-header-title")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def comfort_button_request(self, EC=None):
# Se ha sustituido los tiempos de espera simples desde una forma sleep o implícitas a explícitas tomando como referencia algun objeto en cuestión.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button round")))
        self.driver.find_element(*self.taxi_button).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'tariff-card-4')))
        self.driver.find_element(*self.comfort_button).click()

    def phone_number_request(self):
        self.driver.find_element(*self.phone_number_button).click()

    def fill_phone_number(self):
        self.driver.find_element(*self.phone_input).send_keys(data.phone_number)

    def set_phone_code(self):
        self.driver.find_element(*self.input_phone_code).click()

    def send_phone_number(self):
        self.driver.find_element(*self.phone_send).click()

    def payment_method_button(self):
        self.driver.find_element(*self.payment_method).click()

    def pick_card_button(self):
        self.driver.find_element(*self.card_add_button).click()

    def add_card(self):
        self.driver.find_element(*self.add_credit_card).click()

    def add_number(self):
        self.driver.find_element(*self.add_card_number).send_keys(data.card_number, data.card_code)

    def write_message(self):
        self.driver.find_element(*self.driver_message).send_keys(data.message_for_driver)

#Se han generado las funciones restantes de aquí en adelante para poder llamarlas dentro de main.py en las funciones de pruebas.
    def additional_request_blanket(self):
        self.driver.find_element(*self.blanket_and_scarves).click()

    def request_ice_cream(self):
        self.driver.find_element(*self.ice_cream_counter).click(2)

    def is_displayed(self):
        pass

    def taxi_search(self):
        self.driver.find_element(*self.taxi_search_button).click()