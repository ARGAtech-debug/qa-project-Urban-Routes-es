# He tomado los colearning y he disipado mi duda principal acerca de la estructura, ordenamiento y flujo del código. Con esto he tomado la desición
# de modificar por completo la esctructura de las pruebas acercándola en general al módelo POM, de manera que el trabajo quede mas limpio, ordenado y
# se realice de una mejor manera, tomando en cuenta las esperas de ventanas emergentes, cambios de enfoque y scrolls para navegar la página.
import data
from UrbanRoutesPage import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Prueba para colocación de ruta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

# Se ha modificado la estructura completa de las pruebas para hacer uso del modelo POM, evitando asi hardcordear el código.

    def test_comfort_fare(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_taxi_button_presence()
        routes_page.taxi_button_request()
        routes_page.wait_for_comfort_button_presence()
        routes_page.comfort_button_request()
#Validación con un objeto que esta desplegado unicamente cuando la tarifa comfort está seleccionada
        assert self.driver.find_element(routes_page.blanket_and_scarves).is_displayed()

# Agregar un número de teléfono.
# Esta prueba y sus metodos se han reestructurado por completo de acuerdo a lo solicitado, armar la ruta paso a paso con esperas de acuerdo a los elementos que surgen en ellos.
# También se ha agregado un assert correspondiente para la validación de la prueba realizada que compara el número registrado al final, cn nuestro dato inicial..
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.scroll_into_phone_button()
        routes_page.phone_number_request()
        routes_page.wait_phone_input_window()
        routes_page.fill_phone_number()
        routes_page.set_phone_code()
        routes_page.send_code_number()
        assert routes_page.phone_number_button == data.phone_number

# Agregar una tarjeta de credito
# Se han modificado los métodos llamados y reestructurados en un paso a paso, tomando en cuenta las esperas de los elementos que surgen en ellos y el
# cambio de enfoque que se solicita en los requisitos, para activar el botón de confirmar.
# También se ha agregado el assert sugerido correspondiente para la confirmación de la prueba realizada.
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.scroll_into_payment_method()
        routes_page.payment_method_button()
        routes_page.wait_card_input_window()
        routes_page.pick_card_button()
        routes_page.wait_form_add_card()
        routes_page.click_for_change_focus()
        routes_page.add_card()
        routes_page.add_cvv()
        routes_page.click_for_change_focus()
        routes_page.send_card()
        routes_page.wait_card_added_window()
        routes_page.close_card_add_window()
        assert self.driver.find_element(By.CLASS_NAME, 'pp-value-text') == data.card_number

# Escribir un mensaje para el controlador
# Se han modificado los métodos llamados y reestructurados en un paso a paso, tomando en cuenta las esperas de los elementos que surgen en ellos.
# También se ha agregado un assert correspondiente para la confirmación de la prueba realizada.
    def test_write_message(self):
# Objeto de la clase UrbanRoutesPage
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.scroll_into_message_driver()
        routes_page.write_message_driver()
        assert routes_page.get_message_driver() == message_for_driver

# Pedir una manta y pañuelos
# Se han modificado los métodos llamados y reestructurados en un paso a paso, tomando en cuenta las esperas de los elementos que surgen en ellos.
    def test_request_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.scroll_into_blanket()
        routes_page.check_text_blanket_label()
        routes_page.blanket_and_scarves_switch()
        assert routes_page.blanket_and_scarves_switch().is_selected()

#Pedir 2 helados
# Esta prueba se ha reestructurado junto con sus métodos y localizadores, ahora vamos paso a paso, tomando en cuenta los desplazamientos en pantalla,
# repitiendo 2 veces el metodo para solicitar helado ya que se requieren 2 unidades.
# La validación se da comprobando que el texto del contador sea 2 y se vuelve a validar al final comprobando que sea cierto.
    def test_request_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.scroll_into_ice_cream()
        routes_page.request_ice_cream()
        routes_page.request_ice_cream()
        routes_page.check_text_ice_cream_counter()
        assert routes_page.check_text_ice_cream_counter() == True

#Buscar un taxi
# Esta prueba se ha reestructurado junto con sus métodos y localizadores, ahora vamos paso a paso.
# También se ha agregado un assert correspondiente para la confirmación de la aparición del modal de espera en búsqueda de taxi.
    def test_search_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.taxi_search()
        routes_page.wait_taxi_search_window()
        assert routes_page.wait_taxi_search_window().is_displayed()

# Esperar a que aparezca la información del conductor en el modal
# Esta prueba se ha creado desde 0.
    def test_wait_taxi_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_taxi_info()
        assert routes_page.taxi_info_number.is_displayed()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
