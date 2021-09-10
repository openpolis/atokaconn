from enum import Enum
from urllib.parse import parse_qs

from atokaconn import AtokaConn, AtokaException


class IdType(str, Enum):
    atoka = "ids"
    tax = "taxIds"
    companies = "companies"
    shares = "sharesOwnedIds"


def _search(
    items_type, token,
    filters: str = None,
    count: bool = False,
    limit: int = 10,
    offset: int = 0,
    ordering: str = None,
    packages: str = None,
    verbose: bool = False,
):
    """Create AtokaConn instance and perform the _search (items_type)

    Returns a dict, with items, meta and request (if verbose).
    """
    try:
        from . import main
        conn = AtokaConn(key=token)
    except AtokaException as e:
        raise AtokaException(f"Error while creating AtokaConn instance: {str(e)}")

    result = conn.search(
        items_type,
        fields='items' if not count else 'none',
        limit=limit, offset=offset, ordering=ordering,
        packages=packages,
        query_params=dict(parse_qs(filters)),
        verbose=verbose
    )
    if main.state['verbose']:
        request = result.pop('request')
        result['request'] = {
            'body': request.body,
            'headers': dict(request.headers),
            'method': request.method,
            'url': request.url
        }
    return result
