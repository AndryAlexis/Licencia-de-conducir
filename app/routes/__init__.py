import flet as ft
import app.routes.paths as path
from app.views.home import Home
from app.views.multipleChoiceTest import MultipleChoiceTest 

def routes(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()

        page.views.append(
            Home(
                page=page,
                route=path.HOME, 
            )
        )

        if page.route == path.MULTIPLE_CHOICE_TEST:
            page.views.append(
                MultipleChoiceTest(
                    page=page,
                    route=path.MULTIPLE_CHOICE_TEST
                )
            )
        page.update()

    #Si se retrocede una pantalla, esta última sale del historial de vistas
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)



