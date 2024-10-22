# Se han eliminado los import fuera de uso.
from cffi.cffi_opcode import CLASS_NAME

import helpers
import data
#importación de UrbanRoutesPage a main.py
import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def is_displayed():
    pass


class TestUrbanRoutes:
    driver = None

    def __init__(self):
        self.routes_page = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
#Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

#Probando los botones "pedir un taxi" y Comfort
#A partir de esta prueba se generan cada prueba por independiente con su objeto de la clase UrbanRoutesPage
# Se ha sustituido los tiempos de espera simples desde una forma sleep o implícitas a explícitas tomando como referencia algun objeto en cuestión.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_comfort_fare(self, EC=None):
# Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button round")))
#Sustitución de llamado UrbanRoutesPage por su objeto de clase.
        taxi_button_text = self.driver.find_element(*self.routes_page.taxi_button).text
        assert taxi_button_text == 'Pedir un taxi'
#Sustitución de llamado UrbanRoutesPage por su objeto de clase.
        assert self.driver.find_element(*self.routes_page.taxi_button).is_enabled()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'tariff-card-4')))
#Cambio de orden en la ejecución, primero seleccionamos tarifa Comfort y posteriormente se hacen las validaciones.
#Cambio al nombre de la función a la existente en UrbanRoutesPage.
        routes_page.comfort_button()
#Sustitución de llamado UrbanRoutesPage por su objeto de clase.
        comfort_button_text = self.driver.find_element(*self.routes_page.comfort_button).text
        assert comfort_button_text == 'Comfort'
#Sustitución de llamado UrbanRoutesPage por su objeto de clase.
        assert self.driver.find_element(*self.routes_page.comfort_button).is_enabled()

#Esta prueba y sus validaciones se han reestructurado por completo de acuerdo a lo solicitado.
# También se ha agregado un assert correspondiente para la validación de la prueba realizada.
    def test_set_phone_number(self, EC=None):
 # Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal")))
#Primero introducir el teléfono.
        routes_page.fill_phone_number(data.phone_number)
#Luego recuperar el código y escribirlo.
        phone_code = helpers.retrieve_phone_code(self.driver)
# Sustitución de llamado UrbanRoutesPage por su objeto de clase.
        self.driver.find_element(*self.routes_page.input_phone_code).send_keys(phone_code)
#Validación del código.
        assert routes_page.input_phone_code == helpers.retrieve_phone_code
        self.driver.find_element(*self.routes_page.phone_send).click()
# La validación se realiza después de cerrar la sección donde se confirma el código del celular, con el campo del formulario de reserva.
        assert self.driver.find_element(By.CLASS_NAME, "np-text") == data.phone_number

#Agregar una tarjeta de credito
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_add_card(self):
# Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_card(card_number, card_code)
        assert routes_page.add_card == data.card_number, data.card_code

#Escribir un mensaje para el controlador
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_write_message(self):
# Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.write_message(message)
        assert routes_page.write_message(message) == data.message_for_driver

#Pedir una manta y pañuelos
#Se ha creado la función dentro de UrbanRoutesPage.py, también se han modificado los nombres de la prueba y algunos de sus elementos para que estén relacionados al tema.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_request_blanket(self):
# Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.additional_request_blanket()
        assert routes_page.additional_request_blanket() == True

#Pedir 2 helados
# Esta prueba se ha reestructurado, de igual forma su función fue creada y sus elementos renombrado para que tengan relación entre ellos.
#También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_request_ice_cream(self):
# Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_cream()
        assert self.driver.find_element(By.CLASS_NAME, "r-counter") == 2

#Buscar un taxi
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_search_taxi(self):
# Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
#Sustitución de llamado UrbanRoutesPage por su objeto de clase.
        assert routes_page.taxi_search_section.is_displayed()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
