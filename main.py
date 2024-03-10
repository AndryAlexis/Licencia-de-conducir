from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def main():
    return html.h1('Hello world! xd')

app = FastAPI()
configure(app, main)