# Proyecto Urban Routes 

Sprint 8 - Automatización de pruebas de la aplicación web.
Arturo Gallardo Garduño cohort 14 es.

¿Qué librerías se requieren?
Para este proyecto se ocuparán dos librerías:
Pytest: para la creación y ejecución de tests o automatización de pruebas.
Request: para trabajar con las solicitudes HTTP en Python.
Selenium: para trabajar con localizadores, métodos y el modelo de objetos de página(POM).

¿Cómo instalarlas?

Pytest: Se tiene dos maneras de instalar este paquete de la librería:
A) A través de la terminal.
	1.- Donde debemos de abrirla como primer paso del proceso.
	2.- Ingresa el comando pip install pytest.
B) Mediante la pestaña "Python Packages" (paquetes de Python).
	1.- En PyCharm, dirígete al panel inferior y selcciona la pestaña "Python Packages" (Paquetes de Python).
	2.- En la barra de búsqueda, escribe "Pytest".
	3.- Localiza y selecciona el paquete "Pytest" de la lista.
	4.- Finalmente, haz clic en el botón "Install" (instalar).

Request: Se tiene dos maneras de instalar este paquete de la librería:
A) A través de la terminal.
	1.- Donde debemos de abrirla como primer paso del proceso.
	2.- Ingresa el comando pip install request.
B) Mediante la pestaña "Python Packages" (paquetes de Python).
	1.- En PyCharm, dirígete al panel inferior y selcciona la pestaña "Python Packages" (Paquetes de Python).
	2.- En la barra de búsqueda, escribe "request" (solicitudes).
	3.- Localiza y selecciona el paquete "request" de la lista.
	4.- Finalmente, haz clic en el botón "Install" (instalar).

Selenium: Se tiene dos maneras de instalar este paquete de la librería:
A) A través de la terminal.
	1.- Donde debemos de abrirla como primer paso del proceso.
	2.- Ingresa el comando pip install selenium.
B) Mediante la pestaña "Python Packages" (paquetes de Python).
	1.- En PyCharm, dirígete al panel inferior y selcciona la pestaña "Python Packages" (Paquetes de Python).
	2.- En la barra de búsqueda, escribe "selenium" (solicitudes).
	3.- Localiza y selecciona el paquete "selenium" de la lista.
	4.- Finalmente, haz clic en el botón "Install" (instalar).

¿Cómo usarlas?

Ejecución de pruebas: de igual forma que en la instalación, tenemos dos opciones para ejecutar tus pruebas, directamente
directamente desde la consola de PyCharm o utilizando su interfaz gráfica.

A) A través de la terminal.
	1.- Para ejecutar todas la pruebas de tu proyecto, simplemente escribe: pytest ruta/del/proyecto.
	2.- Para ejecutar las pruebas de un solo archivo, simplemente escribe: pytest nombre_de_proyecto.py
B) Ejecución desde la interfaz de PyCharm.
	1.- Mediante el corrido de las pruebas.

Dentro de las necesidades del proyecto, se plantea el uso de 2 archivos que deberán de involucrarse para generar un proyecto
integro, los cuales son los siguientes:

-data.py : datos requeridos y formatos de estos.
-main.py : archivo con dos clases: 
				~UrbanRoutesPages: donde se denotarán los localizadores y métodos.
				~TestUrbanRoutes: pruebas automatizadas.
-README.md : descripción del proyecto en general.

A través del método POM realizaremos pruebas automatizadas con la ayuda de la localización de elementos para probar la
funcionalidad de la aplicación Urban Routes.


Requerimentos del proyecto:

Dentro del proyecto se toma como objetivo general será el escribir pruebas automatizadas para llevar a cabo el proceso
completo para pedir un taxi.
Para ello, las pruebas deben cubrir estas acciones:

1.-Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
2.-Seleccionar la tarifa Comfort.
3.-Rellenar el número de teléfono.
4.-Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV de la tarjeta
en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar el enfoque, puedes simular
que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla).
*El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido para
agregar una tarjeta.
5.-Escribir un mensaje para el controlador.
6.-Pedir una manta y pañuelos.
7.-Pedir 2 helados.
8.-Aparece el modal para buscar un taxi.
9.-Esperar a que aparezca la información del conductor en el modal (opcional). Además de los pasos anteriores, hay un paso
opcional que puedes comprobar; este es un poco más complicado que los demás, pero es una buena práctica, ya que es probable
que en tu trayectoria profesional encuentres tareas más difíciles.

Siendo todo esto lo requerido, gracias por la atención.