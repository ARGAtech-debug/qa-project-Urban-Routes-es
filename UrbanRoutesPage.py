# Se han agregado bastantes localizadores, se han eliminado algunos también que se encontraban en desuso o duplicados.
# De igual forma se han moficcado, agregado y eliminado métodos en base al uso de una estructura de modelo POM, para que el código quedara mas limpio y funcional.

import data
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class UrbanRoutesPage:
# Localizadores para métodos prueba de colocación de ruta.
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

# Localizadores para métodos de prueba de tarifa comfort.
    taxi_button = (By.CLASS_NAME, "button round")
    comfort_button = (By.ID, 'tariff-card-4')
    blanket_and_scarves = (By.CLASS_NAME, "r-sw-label")

# Localizadores para métodos de prueba al agregar un teléfono.
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_input_window = (By.CLASS_NAME, 'modal')
    phone_input = (By.ID, "phone")
    confirm_button = (By.CLASS_NAME, "button full")
    input_phone_code = (By.ID, "code")

# Localizadores para métodos de prueba al agregar una tarjeta como metodo de pago.
    payment_method = (By.CLASS_NAME, "pp-text")
    card_add_button = (By.CLASS_NAME, "pp-title")
    click_activate_inputs = (By.CLASS_NAME, "head")
    card_number = (By.CSS_SELECTOR, "#number.card-input")
    card_cvv = (By.CSS_SELECTOR, '#code.card-input')
    click_submit_card = (By.CSS_SELECTOR, '[type="submit"]')
    close_add_card_window = (By.CLASS_NAME, 'close-button section-close')

# Localizadores para métodos que serán utilizados para enviar un mensaje al conductor.
    driver_message = (By.CSS_SELECTOR, "#comment.input")

# Localizadores para métodos que serán utilizados para pedir una manta y pañuelos.
    blanket_and_scarves_label = (By.CLASS_NAME,'class="r-sw-label"')
    blanket_and_scarves_switch = (By.CSS_SELECTOR, '.switch-input')

# Localizadores para métodos que serán utilizados para pedir 2 helados
    ice_cream_label = (By.CLASS_NAME, "r-counter-label")
    ice_cream_counter_plus = (By.CLASS_NAME, "counter-plus")
    ice_cream_counter = (By.CLASS_NAME, "counter-value")

# Localizadores para métodos que serán utilizados solicitar el taxi.
    taxi_search_button = (By.CLASS_NAME, "smart-button-wrapper")
    taxi_search_section = (By.CLASS_NAME, "order-body")

#Localizadores para métodos que serán utiizados para la espera de datos del taxi.
    taxi_info_wait = (By.CLASS_NAME, "order-header-time")
    taxi_info_number = (By.CLASS_NAME, "order-number")

    def __init__(self, driver):
        self.driver = driver

# Métodos para probar la creación de una ruta.
    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'from')))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

# Métodos para probar la tarifa comfort.
    def wait_for_taxi_button_presence(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "button round")))

    def taxi_button_request(self):
        self.driver.find_element(self.taxi_button).click()

    def wait_for_comfort_button_presence(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'tariff-card-4')))

    def comfort_button_request(self):
        self.driver.find_element(self.comfort_button).click()

# Métodos para agregar un número de celular, confirmando código.
    def scroll_into_phone_button(self):
        element = self.driver.find_element(self.phone_number_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def phone_number_request(self):
        self.driver.find_element(self.phone_number_button).click()

    def wait_phone_input_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'modal')))

    def fill_phone_number(self):
        self.driver.find_element(self.phone_input).send_keys(data.phone_number)

    def send_phone_number(self):
        self.driver.find_element(self.confirm_button).click()

    def set_phone_code(self):
        self.driver.find_element(self.input_phone_code).send_keys(helpers.retrieve_phone_code)

    def send_code_number(self):
        self.driver.find_element(self.confirm_button).click()

# Métodos para agregar una tarjeta como metodo de pago
    def scroll_into_payment_method(self):
        element = self.driver.find_element(self.payment_method)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def payment_method_button(self):
        self.driver.find_element(self.payment_method).click()

    def wait_card_input_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'modal')))

    def pick_card_button(self):
        self.driver.find_element(self.card_add_button).click()

    def wait_form_add_card(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'card-wrapper')))

    def click_for_change_focus(self):
        self.driver.find_element(self.click_activate_inputs).click()

    def add_card(self):
        self.driver.find_element(self.card_number).send_keys(data.card_number)

    def add_cvv(self):
        self.driver.find_element(self.card_cvv).send_keys(data.card_code)

    def send_card(self):
        self.driver.find_element(self.click_submit_card).click()

    def wait_card_added_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[for="card-1"]')))

    def close_card_add_window(self):
        self.driver.find_element(self.close_add_card_window).click()


# Métodos para enviar un mensaje al conductor.
    def scroll_into_message_driver(self):
        element = self.driver.find_element(self.driver_message)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def write_message_driver(self):
        self.driver.find_element(*self.driver_message).send_keys(data.message_for_driver)

    def get_message_driver(self):
        return self.driver.find_element(self.driver_message).get_property('value')

# Métodos para solicitar una manta y pañuelos.
    def scroll_into_blanket(self):
        element = self.driver.find_element(self.blanket_and_scarves_label)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_text_blanket_label(self):
        blanket_label_text = self.driver.find_element(self.blanket_and_scarves_label).text
        assert blanket_label_text == 'Manta y pañuelos'

    def additional_request_blanket(self):
        self.driver.find_element(*self.blanket_and_scarves_switch).click()

# Métodos para solicitar un helado.
    def scroll_into_ice_cream(self):
        element = self.driver.find_element(self.ice_cream_label)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def request_ice_cream(self):
        self.driver.find_element(*self.ice_cream_counter_plus).click()

    def check_text_ice_cream_counter(self):
        ice_cream_counter_text = self.driver.find_element(self.ice_cream_counter).text
        assert ice_cream_counter_text == '2'

# Métodos para esperar el taxi.
    def taxi_search(self):
        self.driver.find_element(self.taxi_search_button).click()

    def wait_taxi_search_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.taxi_search_section))

# Métodos para esperar a que aparezca la información del conductor en el modal
    def wait_taxi_info(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.taxi_info_number))

