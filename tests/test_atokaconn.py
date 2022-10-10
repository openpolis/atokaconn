import logging

from requests.exceptions import Timeout

from atokaconn import __version__, AtokaObjectDoesNotExist, AtokaResponseError, AtokaMultipleObjectsReturned, \
    AtokaException, AtokaTimeoutException
from atokaconn import AtokaConn
from faker import Factory
from unittest import TestCase
from unittest.mock import patch
from tests.factories import AreaFactory, PersonFactory
from tests.mocked_responses import get_void_response, get_person_ok, get_person_multiple, \
    get_companies_economics, get_companies


def test_version():
    assert __version__ == '0.1.8'


faker = Factory.create("it_IT")  # a factory to create fake data for tests
logger = logging.getLogger(__name__)


class MockResponse:
    """class that mocks requests' response (json method)
    """

    def __init__(self, json_data, status_code, ok, reason=None):
        self.json_data = json_data
        self.status_code = status_code
        self.ok = ok
        self.reason = reason

    def json(self):
        return self.json_data


class MockBrokenJsonResponse:
    """class that mocks requests' response with a broken json
    """

    def __init__(self, json_data, status_code, ok, reason=None):
        self.json_data = json_data
        self.status_code = status_code
        self.ok = ok
        self.reason = reason

    def json(self):
        raise Exception("Json is broken")


class ConnectionsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ConnectionsTestCase, cls).setUpClass()
        setattr(cls, 'mock_get_patcher', patch('requests.Session.get'))
        setattr(cls, 'mock_post_patcher', patch('requests.Session.post'))
        cls.mock_get = getattr(cls, 'mock_get_patcher').start()
        cls.mock_post = getattr(cls, 'mock_post_patcher').start()

    @classmethod
    def tearDownClass(cls):
        getattr(cls, 'mock_get_patcher').stop()
        getattr(cls, 'mock_post_patcher').stop()
        super(ConnectionsTestCase, cls).tearDownClass()


class ATOKAConnTest(ConnectionsTestCase):

    def test_no_key_failure(self):
        with self.assertRaises(AtokaException):
            _ = AtokaConn()

    def test_get_person_from_tax_id_ok(self):
        """Test get_person_from_tax_id returns the correct result
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_person_ok(tax_id=tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_p = atoka_conn.get_person_from_tax_id(tax_id)

        self.assertEqual(atoka_p['base']['taxId'], tax_id)

    def test_get_person_from_tax_id_broken_json_failure(self):
        """Test get_person_from_tax_id fails when json is broken
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockBrokenJsonResponse(
            get_person_ok(tax_id=tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(Exception):
            _ = atoka_conn.get_person_from_tax_id(tax_id)

    def test_get_person_from_tax_id_timeout_failure(self):
        """Test get_person_from_tax_id fails when connection fails
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_person_ok(tax_id=tax_id),
            status_code=200,
            ok=True
        )

        self.mock_get.side_effect = Timeout()

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaTimeoutException):
            _ = atoka_conn.get_person_from_tax_id(tax_id)

        self.mock_get.side_effect = None

    def test_search_person_ok(self):
        """Test get_person_from_tax_id returns the correct result
        """
        parent_area = AreaFactory(name='Lazio')
        area = AreaFactory(name='Roma', parent=parent_area)
        person = PersonFactory.create(
            family_name=faker.last_name_male(),
            given_name=faker.first_name_male(),
            birth_date=faker.date(pattern="%Y-%m-%d", end_datetime="-47y"),
            birth_location_area=area
        )
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_person_ok(tax_id=tax_id, search_params={
                "family_name": person.family_name,
                "given_name": person.given_name,
                "birth_date": person.birth_date,
            }),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_p = atoka_conn.search_person(person)

        self.assertEqual(atoka_p['name'], person.name)
        self.assertEqual(atoka_p['base']['taxId'], tax_id)

    def test_search_person_timeout_failure(self):
        """Test timeout during search_person invocations
        """
        parent_area = AreaFactory(name='Lazio')
        area = AreaFactory(name='Roma', parent=parent_area)
        person = PersonFactory.create(
            family_name=faker.last_name_male(),
            given_name=faker.first_name_male(),
            birth_date=faker.date(pattern="%Y-%m-%d", end_datetime="-47y"),
            birth_location_area=area
        )
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_person_ok(tax_id=tax_id, search_params={
                "family_name": person.family_name,
                "given_name": person.given_name,
                "birth_date": person.birth_date,
            }),
            status_code=200,
            ok=True
        )

        self.mock_get.side_effect = Timeout()

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaTimeoutException):
            _ = atoka_conn.search_person(person)

        self.mock_get.side_effect = None

    def test_get_person_from_tax_id_fails_doesnotexist(self):
        """Test get_person_from_tax_id returns void result
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_void_response(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaObjectDoesNotExist):
            atoka_conn.get_person_from_tax_id(tax_id)

    def test_get_person_from_tax_id_fails_notok(self):
        """Test get_person_from_tax_id returns not ok
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_void_response(),
            status_code=404,
            ok=False,
            reason="Requested URI was not found here",
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaResponseError):
            atoka_conn.get_person_from_tax_id(tax_id)

    def test_get_person_from_tax_id_fails_multiple(self):
        """Test get_person_from_tax_id returns void result
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_person_multiple(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaMultipleObjectsReturned):
            atoka_conn.get_person_from_tax_id(tax_id)

    def test_search_person_fails_doesnotexist(self):
        """Test search_person returns a not found result
        """
        parent_area = AreaFactory(name='Lazio')
        area = AreaFactory(name='Roma', parent=parent_area)
        person = PersonFactory.create(
            family_name=faker.last_name_male(),
            given_name=faker.first_name_male(),
            birth_date=faker.date(pattern="%Y-%m-%d", end_datetime="-47y"),
            birth_location_area=area
        )
        person.tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_void_response(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaObjectDoesNotExist):
            atoka_conn.search_person(person)

    def test_search_person_fails_notok(self):
        """Test search_person returns not ok
        """
        parent_area = AreaFactory(name='Lazio')
        area = AreaFactory(name='Roma', parent=parent_area)
        person = PersonFactory.create(
            family_name=faker.last_name_male(),
            given_name=faker.first_name_male(),
            birth_date=faker.date(pattern="%Y-%m-%d", end_datetime="-47y"),
            birth_location_area=area
        )
        person.tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_void_response(),
            status_code=404,
            ok=False,
            reason="Requested URI was not found here",
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaResponseError):
            atoka_conn.search_person(person)

    def test_search_person_fails_multiple(self):
        """Test search_person returns multiple results
        """
        parent_area = AreaFactory(name='Lazio')
        area = AreaFactory(name='Roma', parent=parent_area)
        person = PersonFactory.create(
            family_name=faker.last_name_male(),
            given_name=faker.first_name_male(),
            birth_date=faker.date(pattern="%Y-%m-%d", end_datetime="-47y"),
            birth_location_area=area
        )
        person.tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_get.return_value = MockResponse(
            get_person_multiple(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaMultipleObjectsReturned):
            atoka_conn.search_person(person)

    def test_get_companies_from_tax_id_ok(self):
        """Test getcompany_from_tax_id returns one result
        """
        tax_id = "80002270660"

        # mock atoka request using tax_id
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing', logger=logger)
        atoka_p = atoka_conn.get_companies_from_tax_ids(tax_id.split(","), packages='base,shares', active="true")

        self.assertEqual(len(atoka_p), 1)
        self.assertEqual(atoka_p[0]['base']['taxId'], tax_id)
        self.assertEqual('shares' in atoka_p[0], True)

    def test_get_companies_from_tax_id_ok_extend_response(self):
        """Test get_companies_from_tax_id returns more than 50 results
        """
        tax_id = "01234567890"

        # mock atoka request using tax_id
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing', logger=logger)
        atoka_p = atoka_conn.get_companies_from_tax_ids(tax_id.split(","), packages='base,shares', active="true")

        self.assertGreaterEqual(len(atoka_p), 50)

    def test_get_companies_from_tax_id_multiple_results(self):
        """Test getcompany_from_tax_id returns more than one result
        """
        tax_id = "02438750586"

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_p = atoka_conn.get_companies_from_tax_ids(tax_id.split(","), packages='base,shares', active="true")

        self.assertEqual(len(atoka_p), 2)
        self.assertEqual(atoka_p[0]['base']['taxId'], tax_id)
        self.assertEqual(atoka_p[1]['base']['taxId'], tax_id)
        self.assertEqual('shares' in atoka_p[0], True)
        self.assertEqual('shares' in atoka_p[1], False)

    def test_get_companies_from_tax_id_returns_empty_if_missing(self):
        """Test get_person_from_tax_id returns void result
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_void_response(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        items = atoka_conn.get_companies_from_tax_ids(tax_id, packages='base,shares', active="true")
        self.assertEqual(items, [])

    def test_get_companies_from_tax_id_empty_if_post_response_notok(self):
        """Test get_companies_from_tax_id returns empty list when response is not ok
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_void_response(),
            status_code=404,
            ok=False,
            reason="Requested URI was not found here",
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        items = atoka_conn.get_companies_from_tax_ids(tax_id, packages='base,shares', active="true")
        self.assertEqual(items, [])

    def test_get_companies_from_tax_id_empty_if_post_request_timeouts(self):
        """Test get_companies_from_tax_id returns empty list when post reuest timeouts
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_void_response(),
            status_code=404,
            ok=False,
            reason="Requested URI was not found here",
        )

        # do the test
        self.mock_post.side_effect = Timeout()

        atoka_conn = AtokaConn(key='testing')
        items = atoka_conn.get_companies_from_tax_ids(tax_id, packages='base,shares', active="true")
        self.assertEqual(items, [])
        self.mock_post.side_effect = None

    def test_get_companies_from_tax_id_empty_if_post_request_response_void(self):
        """Test get_companies_from_tax_id returns empty list when post reuest returns a void response
        """
        tax_id = faker.ssn()

        # mock atoka request using tax_id
        self.mock_post.return_value = None

        # do the test
        atoka_conn = AtokaConn(key='testing')
        items = atoka_conn.get_companies_from_tax_ids(tax_id, packages='base,shares', active="true")
        self.assertEqual(items, [])

    def test_get_items_from_ids_fails_wrong_ids_field_name(self):
        """Test get_items_from_ids fails when an unknown ids_field_name is passed
        """
        tax_id = "02438750586"

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaException):
            _ = atoka_conn.get_items_from_ids(
                tax_id.split(","),
                item_type='companies',
                ids_field_name='cfs',
                batch_size=50,
                packages='base,shares', active="true"
            )

    def test_get_items_from_ids_fails_wrong_item_type(self):
        """Test get_items_from_ids fails when an unknown iem_type is passed
        """
        tax_id = "02438750586"

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaException):
            _ = atoka_conn.get_items_from_ids(
                tax_id.split(","),
                item_type='smurfs',
                ids_field_name='taxIds',
                batch_size=50,
                packages='base,shares', active="true"
            )

    def test_get_items_from_ids_fails_wrong_batch_size(self):
        """Test get_items_from_ids fails when an batch_size out of range is passed
        """
        tax_id = "02438750586"

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        with self.assertRaises(AtokaException):
            _ = atoka_conn.get_items_from_ids(
                tax_id.split(","),
                item_type='companies',
                ids_field_name='taxIds',
                batch_size=100,
                packages='base,shares', active="true"
            )

    def test_get_items_from_ids_returns_empty_list_if_empty_ids(self):
        """Test get_items_from_ids returns and empy items list when an empty ids list is passed
        """
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_void_response(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        ids = atoka_conn.get_items_from_ids(
            [],
            item_type='companies',
            ids_field_name='taxIds',
            batch_size=50,
            packages='base,shares', active="true"
        )
        self.assertEqual(len(ids), 0)

    def test_get_items_from_ids_ok_with_chunks_and_logger(self):
        """Test get_items_from_ids is ok when requests are grouped in chunks (batch_size=1)
        """
        tax_id = "02438750586"

        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing', max_batch_file_lines=1, logger=logger)
        items = atoka_conn.get_items_from_ids(
            ["02438750586", "01234567890"],
            item_type='companies',
            ids_field_name='taxIds',
            batch_size=1,
            packages='base,shares', active="true"
        )
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['base']['taxId'], tax_id)

    def test_get_companies_economics_ok(self):
        """Test get_companies_from_tax_ids with economics details has the correct information
        """
        tax_ids = ['02241890223', '09988761004']

        # mock atoka request using tax_id
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies_economics(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_resp = atoka_conn.get_companies_from_tax_ids(tax_ids, packages='base,economics', active="true")
        self.assertEqual(len(atoka_resp), 2)
        c = atoka_resp[0]
        self.assertEqual(c['base']['taxId'], tax_ids[0])
        self.assertEqual('economics' in c, True)
        ce = c['economics']
        self.assertEqual('balanceSheets' in ce, True)
        self.assertEqual(len(ce['balanceSheets']) > 1, True)
        self.assertEqual('employees' in ce, True)
        self.assertEqual(len(ce['employees']) > 1, True)

    def test_get_companies_from_atoka_ids_ok(self):
        """Test test get_companies_from_atoka_ids returns one result

        The test only needs to test the correct wrapping of get_items_from_ids,
        so it mocks the usual response, not a correct one
        """
        tax_id = "80002270660"

        # mock atoka request using tax_id
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_p = atoka_conn.get_companies_from_atoka_ids(tax_id.split(","), packages='base,shares', active="true")

        self.assertEqual(len(atoka_p), 1)

    def test_get_people_from_tax_ids_ok(self):
        """Test test get_people_from_tax_ids returns one result

        The test only needs to test the correct wrapping of get_items_from_ids,
        so it mocks the usual response, not a correct one
        """
        tax_id = "80002270660"

        # mock atoka request using tax_id
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_p = atoka_conn.get_people_from_tax_ids(tax_id.split(","), packages='base,shares', active="true")

        self.assertEqual(len(atoka_p), 1)

    def test_get_people_from_atoka_ids_ok(self):
        """Test test get_people_from_atoka_ids returns one result

        The test only needs to test the correct wrapping of get_items_from_ids,
        so it mocks the usual response, not a correct one
        """
        tax_id = "80002270660"

        # mock atoka request using tax_id
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_p = atoka_conn.get_people_from_atoka_ids(tax_id.split(","), packages='base,shares', active="true")

        self.assertEqual(len(atoka_p), 1)

    def test_get_roles_from_atoka_ids_ok(self):
        """Test test get_roles_from_atoka_ids returns one result

        The test only needs to test the correct wrapping of get_items_from_ids,
        so it mocks the usual response, not a correct one
        """
        tax_id = "80002270660"

        # mock atoka request using tax_id
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_companies(tax_id),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        atoka_p = atoka_conn.get_roles_from_atoka_ids(tax_id.split(","), packages='base,shares', active="true")

        self.assertEqual(len(atoka_p), 1)

    def test_get_roles_from_atoka_ids_handles_doesnotexist(self):
        """Test get_roles_from_atoka_ids handles the AtokaObjectDoesNotExist exception and returns empty list
        """
        # mock atoka request using tax_id
        self.mock_post.return_value = MockResponse(
            get_void_response(),
            status_code=200,
            ok=True
        )

        # do the test
        atoka_conn = AtokaConn(key='testing')
        items = atoka_conn.get_roles_from_atoka_ids([faker.ssn(), faker.ssn()])
        self.assertEqual(len(items), 0)
