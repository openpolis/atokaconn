__version__ = '0.1.7'

import json

from io import StringIO

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from requests_toolbelt import MultipartEncoder
from urllib3 import Retry


class AtokaConn(object):
    """Helper class to perform queries on ATOKA api service.

    Configuration values are secret and must be kept safe in environment variables.

    """
    allowed_roles = \
        "titolare firmatario,amministratore unico,consigliere,socio amministratore,socio accomandante," \
        "socio,socio accomandatario,presidente consiglio amministrazione,socio unico,amministratore,titolare," \
        "sindaco effettivo,vice presidente consiglio amministrazione,amministratore delegato,liquidatore," \
        "sindaco supplente,socio di societa' in nome collettivo,consigliere delegato,presidente," \
        "curatore fallimentare,presidente del collegio sindacale,vice presidente,legale rappresentante," \
        "revisore dei conti,legale rappresentante di societa',institore,direttore generale"

    def __init__(
        self,
        service_url: str = 'https://api.atoka.io',
        version: str = 'v2',
        key: str = None,
        max_retries=5, backoff_factor=0.5,
        max_batch_file_lines=200,
        logger=None
    ):
        """Instantiate the connection by creating a custom requests.Session
        with HTTPAdapter as transport and a custom Retry instance, to shape the retries pattern

        max_retries is set to 5 and backoff_factor to 1sec, so retries pattern will be:
        1s, 2s, 4s, 8s, 16s, backoff

        fails by raising an AtokaException if the key is not passed
        """
        self.service_url = service_url
        self.version = version
        self.max_batch_file_lines = max_batch_file_lines
        if not key:
            raise AtokaException(f"API key needed to connect to {self.service_url}")
        self.key = key
        self.session = requests.Session()
        self.logger = logger

        retries = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=frozenset({'OPTIONS', 'PUT', 'DELETE', 'GET', 'TRACE', 'HEAD', 'POST'})
        )
        self.session.mount(
            self.service_url, HTTPAdapter(max_retries=retries)
        )

    def get_person_from_tax_id(self, tax_id: str) -> dict:
        """get a single person from ATOKA API, from its tax_id
        raise Atoka exceptions if errors or no objects found

        :param tax_id: string - the tax_id as a string
        :return: dict - ATOKA result
        """
        try:
            response = self.session.get(
                '{0}/{1}/people'.format(
                    self.service_url, self.version
                ),
                params={
                    'token': self.key,
                    'taxIds': tax_id,
                    'packages': 'base,companies,shares'
                }
            )
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, RetryError):
            raise AtokaTimeoutException()

        if not response.ok:
            raise AtokaResponseError(response.reason)

        try:
            result = response.json()
        except Exception as e:
            raise Exception(e)

        if result['meta']['count'] == 0:
            raise AtokaObjectDoesNotExist(
                "Could not find person with tax_id {0} in Atoka.".format(tax_id)
            )
        if result['meta']['count'] > 1:
            raise AtokaMultipleObjectsReturned(
                "Found more than one person with tax_id {0} in Atoka.".format(tax_id)
            )

        return result['items'][0]

    def search(
        self, items_type: str, fields: str, query_params: dict,
        limit: int = 10, offset: int = 0, ordering: str = 'birthDateDesc',
        packages: str = None, verbose: bool = False
    ) -> dict:
        """Perform a _search on Atoka API, returning the result as a dict, or an AtokaObjectDoesNotExist exception
        """
        if not items_type:
            raise AtokaException("Need to specify an item_type. Choose among people and companies.")
        if items_type not in ['people', 'companies']:
            raise AtokaException(f"Wrong type of items to _search ({items_type}). Choose among people and companies.")
        params = {
            'token': self.key,
            'fields': fields,
            'limit': limit, 'offset': offset, 'ordering': ordering,
        }
        if packages:
            params['packages'] = packages
        params.update(query_params)

        try:
            response = self.session.get(
                f"{self.service_url}/{self.version}/{items_type}",
                params=params
            )
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, RetryError):
            raise AtokaTimeoutException()

        if not response.ok:
            raise AtokaResponseError(
                f"{response.status_code} - {response.reason} - {json.loads(response.text)['message']}"
            )

        params.pop('token')

        result = response.json()
        if result['meta']['count'] == 0:
            raise AtokaObjectDoesNotExist(
                "Could not find any person with parameters {0} in Atoka.".format(params)
            )

        if verbose:
            result['request'] = response.request

        return result

    def search_person(self, person: object) -> dict:
        """get a single person from ATOKA API, from its anagraphical
        raise Atoka exceptions if errors or no objects found

        :param person: an object instance of OPDM person type to look for into ATOKA
            needs these attributes:
            - family_name,
            - given_name,
            - birth_date (YYYY[-MM][-DD])
            - birth_location_area (object with name attribute)
        :return: dict - atoka result
        """
        params = {
            'token': self.key,
            'givenName': getattr(person, 'given_name', ''),
            'familyName': getattr(person, 'family_name', ''),
            'birthDateFrom': getattr(person, 'birth_date', ''),
            'birthDateTo': getattr(person, 'birth_date', ''),
            'birtPlaceMunicipalities': getattr(
                getattr(person, 'birth_location_area', object()), 'name', ''
            ),
            'packages': 'base,companies,shares'
        }
        try:
            response = self.session.get(
                '{0}/{1}/people'.format(
                    self.service_url, self.version
                ),
                params=params
            )
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, RetryError):
            raise AtokaTimeoutException()

        if not response.ok:
            raise AtokaResponseError(response.reason)

        params.pop('token')
        params.pop('packages')

        result = response.json()
        if result['meta']['count'] == 0:
            raise AtokaObjectDoesNotExist(
                "Could not find person with parameters {0} in Atoka.".format(params)
            )
        if result['meta']['count'] > 1:
            raise AtokaMultipleObjectsReturned(
                "Found more than one person with parameters {0} in Atoka.".format(params)
            )

        return result['items'][0]

    def post_requests(self, requests_list, api_endpoint, verbose: bool = False, **kwargs) -> dict:
        """Build batch API request from list, post and return json response
        """

        with StringIO() as file_io:

            for r in requests_list:
                print(r, file=file_io)

            fields = {
                'batch': ('batch.json', file_io),
                'limit': '50'
            }
            fields.update(kwargs)
            m = MultipartEncoder(
                fields=fields
            )

            try:
                response = self.session.post(
                    api_endpoint,
                    params={'token': self.key},
                    data=m,
                    headers={'Content-Type': m.content_type},
                )

            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, RetryError):
                raise AtokaTimeoutException()

            if response is None:
                raise AtokaObjectDoesNotExist()

            if not response.ok:
                raise AtokaResponseError(response.reason)

            portable_response = response.json()

            # tests responses are mocked and do not have request attributes
            # this check avoids tests to fail
            if hasattr(response, 'request'):
                response.request.body.__getattribute__('fields').pop('batch')
                body = response.request.body.__getattribute__('fields')
                body['batch_requests'] = requests_list

            if verbose:
                if hasattr(response, 'request'):
                    portable_response['request'] = {
                        'method': response.request.method,
                        'body': body,
                        'headers': dict(response.request.headers),
                        'url': response.request.url
                    }
                else:
                    portable_response['request'] = {}

            return portable_response

    def extend_response(
        self,
        responses: list,
        ids_field_name: str,
        api_endpoint: str,
        verbose: bool = False,
        **kwargs
    ) -> dict:
        """Extend the response whenever meta.count indicates that there are more than 50 items
        """
        #     total_response['meta']['count'] += json_response['meta']['count']
        #     total_response['meta']['error'] += json_response['meta']['error']
        #     total_response['meta']['success'] += json_response['meta']['success']
        #     total_response['responses'].update(json_response['responses'])

        complete_response = {
            'items': [],
            'meta': {
                'count': 0
            },
        }
        if verbose:
            complete_response['detailed_responses'] = responses

        for response in responses:
            for req_id, r in response.get('responses', {}).items():

                complete_response['items'].extend(r['items'])

                # if more than 50 results, get the others
                if r['meta']['count'] > 50:

                    # build requests_list
                    requests_list = [
                        json.dumps(
                            {
                                "reqId": "r{0:05d}".format(offset),
                                ids_field_name: req_id,
                                'offset': offset
                            }
                        ) for offset in range(50, r['meta']['count'], 50)
                    ]

                    try:
                        extended_json_response = self.post_requests(requests_list, api_endpoint=api_endpoint, **kwargs)
                        for _r in extended_json_response.get('responses', {}).values():
                            complete_response['items'].extend(_r['items'])
                            if verbose:
                                complete_response['detailed_responses'].append(extended_json_response)
                    except Exception as e:
                        if self.logger:
                            self.logger.warning(f"{e}. Skipping")
                        continue

        complete_response['meta']['count'] = len(complete_response['items'])
        return complete_response

    def get_items_from_ids(
        self, ids: list, item_type: str, ids_field_name: str = 'ids',
        batch_size: int = 50, verbose: bool = False, **kwargs
    ) -> list:
        """The response is transformed into a list and returned (back-compatibility)

        Results are returned as a list of dictionaries.

        :param ids: list
        :param item_type: str
        :param ids_field_name: ids, tax_ids
        :param batch_size: size of the number of ids searched by row of the batch IO
        :param verbose: whether to add a request property to the response, mostly for debugging purposes
        :param kwargs: - more atoka parameters for filtering results
            (ex: packages=base,shares, active='true', ccia='*')
        :return: results as a list of dicts
        """
        response = self.get_response_from_ids(
            ids, item_type, ids_field_name=ids_field_name,
            batch_size=batch_size, verbose=verbose,
            **kwargs
        )
        return response['items']

    def get_response_from_ids(
        self, ids: list, item_type: str, ids_field_name: str = 'ids',
        verbose: bool = False,
        batch_size: int = 50, **kwargs
    ) -> dict:
        """Transform a request for a list of ids larger than batch_size,
        to a batch request of enough rows with a limit of batch_size, so that all results
        can be returned.

        Results are composed and returned as a response dict

        :param ids: list
        :param item_type: str
        :param ids_field_name: ids, tax_ids
        :param batch_size: size of the number of ids searched by row of the batch IO
        :param verbose: whether to add a request property to the response, mostly for debugging purposes
        :param kwargs: - more atoka parameters for filtering results
            (ex: packages=base,shares, active='true', ccia='*')
        :return: results as a list of dicts
        """

        if ids_field_name not in ['ids', 'taxIds', 'companies', 'sharesOwnedIds']:
            raise AtokaException("ids_field_name parameter must take one of these values: <ids>, <taxIds>, <companies>")

        if batch_size < 1 or batch_size > 50:
            raise AtokaException("batch_size must be between 1 and 50")

        if item_type not in ['companies', 'people']:
            raise AtokaException("item_type must take one of these values: <companies>, <people>")

        if len(ids) == 0:
            return {
                'items': [],
                'meta': {
                    'count': 0
                },
            }

        api_endpoint = "{0}/{1}/{2}/".format(
            self.service_url, self.version, item_type
        )

        # internal function to split ids list into chunks
        def chunks(lst, size):
            """Yield successive size-sized chunks from lst."""
            for i in range(0, len(lst), size):
                yield lst[i:i + size]

        # build requests_list in chunks of batch_size
        requests_list = [
            json.dumps(
                {
                    'reqId': ','.join(r),
                    ids_field_name: ','.join(r)
                }
            ) for r in chunks(ids, batch_size)
        ]

        # build files_list in chunks of N
        grouped_requests = [
            r for r in chunks(requests_list, self.max_batch_file_lines)
        ]

        responses = []
        for gr in grouped_requests:
            try:
                json_response = self.post_requests(gr, api_endpoint=api_endpoint, verbose=verbose, **kwargs)
                responses.append(json_response)
            except Exception as e:
                if self.logger:
                    self.logger.warning(f"{e}. Skipping")
                continue

        complete_response = self.extend_response(
            responses, ids_field_name=ids_field_name, api_endpoint=api_endpoint,
            verbose=verbose, **kwargs
        )

        return complete_response

    def get_companies_from_tax_ids(self, tax_ids: list, **kwargs) -> list:
        """get all companies from ATOKA API, from given tax_ids list
        raise Atoka exceptions if errors or no objects found

        :param tax_ids: - the list of tax_ids to extract info from
        :param kwargs: - more atoka parameters for filtering results (ex: active='true', ccia='*')
        :return: dict - ATOKA result
        """
        return self.get_items_from_ids(tax_ids, 'companies', ids_field_name='taxIds', **kwargs)

    def get_companies_from_atoka_ids(self, atoka_ids: list, **kwargs) -> list:
        """get all companies from ATOKA API, from given atoka_ids list
        raise Atoka exceptions if errors or no objects found

        :param atoka_ids: - the list of ids to extract info from
        :param kwargs: - more atoka parameters for filtering results (ex: active='true', ccia='*')
        :return: dict - ATOKA result
        """
        return self.get_items_from_ids(atoka_ids, 'companies', ids_field_name='ids', **kwargs)

    def get_people_from_tax_ids(self, tax_ids: list, **kwargs) -> list:
        """get all people from ATOKA API, from given tax_ids list
        raise Atoka exceptions if errors or no objects found

        :param tax_ids: - the list of tax_ids to extract info from
        :param kwargs: - more atoka parameters for filtering results (ex: active='true', ccia='*')
        :return: dict - ATOKA result
        """
        return self.get_items_from_ids(tax_ids, 'people', ids_field_name='taxIds', **kwargs)

    def get_people_from_atoka_ids(self, atoka_ids: list, **kwargs) -> list:
        """get all people from ATOKA API, from given atoka_ids list
        raise Atoka exceptions if errors or no objects found

        :param atoka_ids: - the list of ids to extract info from
        :param kwargs: - more atoka parameters for filtering results (ex: active='true', ccia='*')
        :return: dict - ATOKA result
        """
        ids_field_name = kwargs.pop('ids_field_name', 'ids')
        return self.get_items_from_ids(atoka_ids, 'people', ids_field_name=ids_field_name, **kwargs)

    def get_roles_from_atoka_ids(self, atoka_ids: list, **kwargs) -> list:
        """get all people in given companies, used to extract roles

        :param atoka_ids:
        :param kwargs:
        :return:
        """
        # need a batch_size of 1 because the number of people in a single company can be great,
        # and 50 is the maximum limit for a single batch row request
        return self.get_items_from_ids(atoka_ids, 'people', ids_field_name='companies', batch_size=1, **kwargs)


class AtokaTimeoutException(Exception):
    pass


class AtokaException(Exception):
    pass


class AtokaObjectDoesNotExist(AtokaException):
    pass


class AtokaMultipleObjectsReturned(AtokaException):
    pass


class AtokaResponseError(AtokaException):
    pass
