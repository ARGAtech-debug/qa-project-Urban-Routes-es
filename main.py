# Se han eliminado los import fuera de uso.
import helpers
import data
import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import phone_number



class TestUrbanRoutes:
    driver = None


    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self, EC=None):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.wait_for_load_routes()
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

#Probando los botones "pedir un taxi" y Comfort
#A partir de esta prueba se generan cada prueba por independiente con su objeto de la clase UrbanRoutesPage
# Se ha sustituido los tiempos de espera simples desde una forma sleep o implícitas a explícitas tomando como referencia algun objeto en cuestión.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_comfort_fare(self, EC=None):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button round")))
        taxi_button_text = self.driver.find_element(*self.UrbanRoutesPage.taxi_button).text
        assert taxi_button_text == 'Pedir un taxi'
        assert self.driver.find_element(*self.UrbanRoutesPage.taxi_button).is_enabled()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'tariff-card-4')))
        comfort_button_text = self.driver.find_element(*self.UrbanRoutesPage.comfort_button).text
        assert comfort_button_text == 'Comfort'
        assert self.driver.find_element(*self.UrbanRoutesPage.comfort_button).is_enabled()
        routes_page.select_comfort_rate()

#Rellenar el no. de teléfono
#Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_set_phone_number(self, EC=None):
        routes_page = UrbanRoutesPage(self.driver)
# Se ha sustituido los tiempos de espera simples desde una forma sleep o implícitas a explícitas tomando como referencia algun objeto en cuestión.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal")))
        routes_page.set_phone(phone_number)
        assert routes_page.set_phone(phone_number) == data.phone_number

#Recuperar el código de confirmación del teléfono
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_set_phone_code(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.input_phone_code).send_keys(phone_code)
        assert routes_page.set_phone_code == helpers.retrieve_phone_code

#Agregar una tarjeta de credito
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_card(card_number, card_code)
        assert routes_page.add_card == data.card_number, data.card_code

#Escribir un mensaje para el controlador
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_write_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.write_message(message)
        assert routes_page.write_message(message) == data.message_for_driver

#Pedir una manta y pañuelos
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_write_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_blanket_and_scarves()
        assert routes_page.request_blanket_and_scarves() == True

#Pedir 2 helados
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
#También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_request_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_cream_counter(2)
        assert routes_page.request_ice_cream_counter == 2

#Buscar un taxi
# Se ha agregado su nombre de prueba y objeto de la clase para llamar localizadores.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_search_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.taxi_search_button.click()
        assert self.driver.find_element(*self.UrbanRoutesPage.taxi_search_button).is_enabled()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
