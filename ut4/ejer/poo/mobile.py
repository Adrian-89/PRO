'''
Escriba una clase MobilePhone que represente un teléfono móvil.

Atributos:

    manufacturer (cadena de texto)

    screen_size (flotante)

    num_cores (entero)

    apps (lista de cadenas de texto)

    status (False: apagado, True: encendido)

Métodos:

    __init__(self, manufacturer, screen_size, num_cores)

    power_on(self)

    power_off(self)

    install_app(self, app) (no instalar la app si ya existe)

    uninstall_app(self, app) (no borrar la app si no existe)

¿Serías capaz de extender el método install_app() para instalar varias aplicaciones a la vez?
Lanzar tests: pytest -xq test_mobile.py
'''


class MobilePhone:
    def __init__(
        self, manufacturer: str, screen_size: float, num_cores: int
    ):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, app: str):
        if app not in self.apps:
            self.apps.append(app)

    def uninstall_app(self, app: str):
        if app in self.apps:
            self.apps.remove(app)
