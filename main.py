import time

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import address_from, phone_number, card_number


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    taxi_button = (By.CLASS_NAME, "button round")
    comfort_button = (By.XPATH, '//*[@id="root"] / div / div[3] / div[3] / div[2] / div[1] / div[5] / div[2]')
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, "phone")
    phone_send = (By.XPATH, '//*[@id="root"] / div / div[1] / div[2] / div[1] / form / div[2] / button')
    payment_method = (By.CLASS_NAME, "pp-text")
    card_add_button = (By.CLASS_NAME, "pp-title")
    add_credit_card = (By.XPATH, '//*[text() # "Agregar Tarjeta"]')
    add_card_number = (By.ID, "number")
    card_cvv = (By.XPATH, '//*[@id="code"]')


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

    def comfort_button_request(self):
        time.sleep(2)
        self.driver.find_element(*self.taxi_button).click()
        time.sleep(2)
        self.driver.find_element(*self.comfort_button).click()

    def phone_number_request(self):
        self.driver.find_element(*self.phone_number_button).click()

    def fill_phone_number(self):
        self.driver.find_element(*self.phone_input).send_keys(data.phone_number)

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



class TestUrbanRoutes:

    driver = None

    add_click_payment_method = (By.CLASS_NAME, "card-wrapper")
    driver_message = (By.XPATH, '//*[@id="comment"]')
    write_message = (By.CSS_SELECTOR, "#comment")
    input_phone_code = (By.ID, "code")
    requests_button = (By.CLASS_NAME, "reqs-head")
    blanket_and_scarves = (By.CLASS_NAME, "r-sw-label")
    ice_cream_counter = (By.CLASS_NAME, "r-counter")
    taxi_search_button = (By.CLASS_NAME, "smart-button-main")


    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(10)
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

#Probando los botones "pedir un taxi" y Comfort
        self.driver.implicitly_wait(10)
        taxi_button_text = self.driver.find_element(*self.taxi_button).text
        assert taxi_button_text == 'Pedir un taxi'
        assert self.driver.find_element(*self.taxi_button).is_enabled()
        self.driver.implicitly_wait(10)
        comfort_button_text = self.driver.find_element(*self.comfort_button).text
        assert comfort_button_text == 'Pedir un taxi'
        assert self.driver.find_element(*self.comfort_button).is_enabled()
        routes_page.select_comfort_rate()

    #Rellenar el no. de teléfono
        self.driver.implicitly_wait(10)
        routes_page.set_phone(phone_number)

    #Recuperar el código de confirmación del teléfono
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.input_phone_code).send_keys(phone_code)

    #Agregar una tarjeta de credito
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_card(card_number, card_code)

    #Escribir un mensaje para el controlador
        message = data.message_for_driver
        routes_page.write_message(message)

    #Pedir una manta y pañuelos
        routes_page.request_blanket_and_scarves()

    #Pedir 2 helados
        routes_page.request_ice_cream_counter(2)

    #Buscar un taxi
        routes_page.taxi_search_button.click()







    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
