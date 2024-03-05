import flet as ft

from app.views.home.mvc import Model, View, Controller

class Home(ft.View):
    
    def __init__(self, page : ft.Page, route : str) -> None:
        model = Model()
        view = View()
        controller = Controller(model=model, view=view, page=page)

        controls = controller.run()
        
        super().__init__(route=route, controls=controls)