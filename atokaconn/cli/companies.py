import json
import select
import sys

import typer
from atokaconn.cli import _search, IdType
from atokaconn import AtokaException, AtokaTimeoutException, AtokaResponseError, AtokaObjectDoesNotExist, AtokaConn

app = typer.Typer()


@app.command()
def search(
    filters: str = typer.Argument(
        None,
        help="Filters as url parameters, ex: ageMax=20&active=false. "
        "See: https://developers.atoka.io/v2/companies.html#companies_general"
    ),
    count: bool = typer.Option(
        False,
        help="Get just the number of companies matched. If not set, then items are shown"
    ),
    limit: int = typer.Option(10, help="Number of items returned."),
    offset: int = typer.Option(0, help="Starting offset when returning items"),
    ordering: str = typer.Option(
        None, help="The order in which results are returned. "
        "See: https://developers.atoka.io/v2/companies.html#companies_pagination"
    ),
    packages: str = typer.Option(
        None, help="The packages to show in results items. "
        "See: https://developers.atoka.io/v2/companies.html#companies_packages"
    )
):
    """Search companies.
    """
    try:
        from . import main
        result = _search(
            items_type='companies',
            token=main.state['token'],
            verbose=main.state['verbose'],
            filters=filters,
            count=count,
            limit=limit, offset=offset, ordering=ordering,
            packages=packages
        )
        typer.echo(json.dumps(result, indent=4))
    except AtokaTimeoutException:
        typer.secho("A timeout occurred while searching", fg="red")
    except AtokaResponseError as e:
        typer.secho(f"Error {e}", fg="red")
    except AtokaObjectDoesNotExist:
        typer.secho("No results found", fg="red")
    except AtokaException as e:
        typer.secho(f"Error {e}", fg="red")


@app.command()
def bulk_ids(
    ids_type: IdType = typer.Option(IdType.atoka, help="Type of ID to use."),
    ids: str = typer.Option("", help="Comma separated IDs."),
    ids_file: typer.FileText = typer.Option(
        sys.stdin,
        help="Path to file containing list of ID, one per row. Defaults to standard input."
    ),
    batch_size: int = typer.Option(50, help="Size of the batches of IDS for each request's row"),
    packages: str = typer.Option(
        None, help="The packages to show in results items. "
        "See: https://developers.atoka.io/v2/companies.html#companies_packages"
    )
):
    """
    Fetch data starting from ids.

    IDs may be of type 'ids', 'taxIds', 'companies', 'sharesOwnedIds'.

    IDs may be fetched from a comma separated list (--ids option),
    through a file (--ids-file), or the standard input (one ID per line).
    This option is overridden by the --ids option. By default ids are read from the standard input,
    but only if the standard input is not an interactive tty.

    This means that something like this is possible:

        cat ids.csv | atokaconn --verbose --token=2f8d8506177a4772c817f98aa3be0d57 companies bulk-ids

    Bulk operations may be *expensive* from the perspective of used credits.
    """

    ids_list = [x for x in ids.split(",") if x != ""]
    if not ids_list:
        # check that the stream is not empty (avoid hanging when ids_file == sys.stdin)
        rfds, wfds, efds = select.select([ids_file], [], [], 0.5)
        if rfds:
            ids_list = [line.strip(" \n") for line in ids_file]

    try:
        from . import main
        conn = AtokaConn(key=main.state['token'], max_batch_file_lines=5)
    except AtokaException as e:
        raise AtokaException(f"Error while creating AtokaConn instance: {str(e)}")

    result = conn.get_response_from_ids(
        ids=ids_list, item_type='companies', ids_field_name=ids_type,
        batch_size=batch_size,
        packages=packages, verbose=main.state['verbose']
    )

    typer.echo(json.dumps(result, indent=4))
