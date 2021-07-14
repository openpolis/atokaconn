[![Latest Version](https://img.shields.io/pypi/v/atokaconn.svg)](https://pypi.python.org/pypi/atokaconn)
[![Latest Version](https://img.shields.io/pypi/pyversions/atokaconn.svg)](https://pypi.python.org/pypi/atokaconn)
[![License](https://img.shields.io/pypi/l/atokaconn.svg)](https://pypi.python.org/pypi/atokaconn)
[![Downloads](https://pepy.tech/badge/atokaconn/month)](https://pepy.tech/project/atokaconn/month)

![Tests Badge](https://op-badges.s3.eu-west-1.amazonaws.com/atokaconn/tests-badge.svg?2)
![Coverage Badge](https://op-badges.s3.eu-west-1.amazonaws.com/atokaconn/coverage-badge.svg?2)
![Flake8](https://op-badges.s3.eu-west-1.amazonaws.com/atokaconn/flake8-badge.svg?2)


`atokaconn` is a python package that allows connections to and data extractions from the 
[ATOKA](https://atoka.io/pages/en/) API service.

ATOKA is a service provided by SpazioDati (Cerved), based on companies' data from the 
Camera di Commercio.

An extensive introduction to these data's structure is available here: https://atoka.io/pages/en/data-structure/.

The API reference is availabel here: https://developers.atoka.io/v2/.

## Installation

Python versions from 3.6 are supported.

The package is hosted on pypi, and can be installed, for example using pip:

    pip install atokaconn

## Usage

Once a key has been obtained from ATOKA's service (you need to pay for this), then

    atoka_conn = AtokaConn(key=MYKEY)
    atoka_p = atoka_conn.get_person_from_tax_id(tax_id)
 
ATOKA has an incredibly rich set of endpoints and filters, allowing a wide variety of usages 
for their API. This package implements a very limited set of methods. 

See https://gitlab.com/spaziodati/atoka-cli for a go-based CLI implementation.

See the Contributing section to increase coverage.

### `get_person_from_tax_id`
Gets a single person, as a dict, from its tax_id. 
Raises one of the Atoka exceptions if errors are present or no persons are found.
see: https://developers.atoka.io/v2/people.html#people_taxIds

### `search_person`
Retrieves a single person from ATOKA API, starting from its anagraphical data.
Raises Atoka exceptions if errors or no objects are found.
 
`person` is an object instance of Popolo Person type to look for into ATOKA
  Can be an instance of an object with these attributes:
    - family_name,
    - given_name,
    - birth_date (YYYY[-MM][-DD])
    - birth_location_area (object of Popolo Area type, an instance with a name attribute will do)

TODO: this is not generic enough, as OPDM/Popolo concepts creeps in. Must be generalized.

### `get_people_from_atoka_ids`
Returns a list of dictionaries, with persons corresponding to the passed atoka ids.

### `get_people_from_tax_ids`
Returns a list of dictionaries, with persons corresponding to the passed tax ids

### `get_companies_from_atoka_ids`
Returns a list of dictionaries, with companies corresponding to the passed atoka ids.

### `get_companies_from_tax_ids`
Returns a list of dictionaries, with companies corresponding to the passed tax ids.

### `get_roles_from_atoka_ids`
Returns all people in companies with given atoka ids, used to extract people with roles in these companies

Most of the above methods are based on the internal generic `get_items_from_ids`, which uses 
`posts_requests`, in order to correctly build the multipart *batch* post request.

When extracting roles, we hit a 50 items limit, and the `extend_response` method must be used, in order to fetch 
items when the returned count is greater than 50.   

## Support

There is no guaranteed support available, but authors will try to keep up with issues 
and merge proposed solutions into the code base.

## Project Status
This project is currently being developed by the [Openpolis Foundation](https://www.openpolis.it/openpolis-foundation/)
and does only cover those parts of the ATOKA API that are needed in the Foundation's projects. 
Should more be needed, you can either ask to increase the coverage, or try to contribute, following instructions below.

## Contributing
In order to contribute to this project:
* verify that python 3.6+ is being used (or use [pyenv](https://github.com/pyenv/pyenv))
* verify or install [poetry](https://python-poetry.org/), to handle packages and dependencies in a leaner way, 
  with respect to pip and requirements
* clone the project `git clone git@github.com:openpolis/atokaconn.git` 
* install the dependencies in the virtualenv, with `poetry install`,
  this will also install the dev dependencies
* develop and test 
* create a [pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
* wait for the maintainers to review and eventually merge your pull request into the main repository

### Testing
Tests are under the tests folder, and can be launched with 

    pytest

Requests and responses from ATOKA's API are mocked, in order to avoid having to connect to 
the remote service during tests (slow and needs an API key).

Coverage is installed as a dev dependency and can be used to see how much of the package's code is covered by tests:

    coverage run -m pytest

    # sends coverage report to terminal
    coverage report -m 

    # generate and open a web page with interactive coverage report
    coverage html
    open htmlcov/index.html 

Syntax can be checked with `flake8`.

Coverage and flake8 configurations are in their sections within `setup.cfg`.

## Authors
Guglielmo Celata - guglielmo@openpolis.it

## Licensing
This package is released under an MIT License, see details in the LICENSE.txt file.
