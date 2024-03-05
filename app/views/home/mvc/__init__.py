import flet as ft
from typing import Callable
import app.routes.paths as path

class Model:
    """
    El modelo representa los datos.
    """
    def __init__(self) -> None:
        self._title_app_bar = "Flet app"
        self._bgcolor_app_bar = ft.colors.SURFACE_VARIANT

        self._text_route_button = 'Visita store'

    @property
    def title_app_bar(self):
        return self._title_app_bar
    @property
    def bgcolor_app_bar(self):
        return self._bgcolor_app_bar
    
    @property
    def text_route_button(self):
        return self._text_route_button

class View:
    """
    La vista es la capa de presentación de la aplicación.
    """
    def __init__(self) -> None:
        self._title_app_bar = ft.Text()
        self._app_bar = ft.AppBar()
        self._route_button = ft.ElevatedButton()
    
    def title_app_bar(self, value):
        self._title_app_bar.value = value
        return self._title_app_bar
    
    def app_bar(self, title, bgcolor):
        self._app_bar.title = title
        self._app_bar.bgcolor = bgcolor
        return self._app_bar
    
    def route_button(self, text, on_click : Callable[..., None]):
        self._route_button.text = text
        self._route_button.on_click = on_click
        return self._route_button

class Controller:
    """
    El controlador actúa como intermediario entre el modelo y la vista. 
    """
    def __init__(self, model : Model, view : View, page : ft.Page) -> None:
        self._model = model
        self._view = view
        self._page = page
    
    def run(self):

        controls = [
            self._create_app_bar(),
            self._create_route_button()
        ]

        return controls
    
    def _create_app_bar(self) -> ft.AppBar:
        title_app_bar = self._view.title_app_bar(self._model.title_app_bar)

        app_bar = self._view.app_bar(
            title=title_app_bar, 
            bgcolor=self._model.bgcolor_app_bar
        )

        return app_bar
    
    def _create_route_button(self) -> ft.ElevatedButton:
        route_button = self._view.route_button(
            self._model.text_route_button,
            on_click=lambda _ : self._page.go(path.MULTIPLE_CHOICE_TEST))
        
        return route_button
