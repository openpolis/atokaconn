# coding: utf-8
import os

import typer
from . import people
from . import companies


app = typer.Typer()
state = {"verbose": False}

app.add_typer(people.app, name="people", help="Read people's data")
app.add_typer(companies.app, name="companies", help="Read companies' data")


@app.callback()
def main(
    verbose: bool = False,
    token: str = typer.Option(os.environ.get('ATOKA_API_KEY', None), help="The API token to authenticate."),
):
    """
    A command to read data from ATOKA API.

    Copyright © 2021 <Fondazione Openpolis>.
    """
    state["token"] = token
    if verbose:
        state["verbose"] = True
