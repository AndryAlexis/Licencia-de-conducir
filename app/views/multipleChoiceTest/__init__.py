import flet as ft
import app.routes.paths as path

# Multiple choice test
class MultipleChoiceTest(ft.View):

    def __init__(self, page : ft.Page, route : str):
        controls = [
            ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.ElevatedButton("Go Home", on_click=lambda _: page.go(path.HOME)),
        ]
        super().__init__(route=route, controls=controls)