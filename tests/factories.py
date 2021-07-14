import random
import factory


class Person(object):
    def __init__(self, **kwargs):
        for attr in [
            'gender', 'given_name', 'family_name', 'name',
            'birth_date', 'birth_location',
            'additional_name', 'email', 'biography'
        ]:
            setattr(self, attr,  kwargs.get(attr, ''))


class PersonFactory(factory.Factory):
    class Meta:
        model = Person

    gender = random.choice(["M", "F"])
    given_name = factory.Faker("first_name")
    family_name = factory.Faker("last_name")
    name = factory.LazyAttribute(lambda o: o.given_name + " " + o.family_name)
    birth_date = factory.Faker("date", pattern="%Y-%m-%d", end_datetime="-27y")
    birth_location = factory.Faker("city")
    additional_name = factory.Faker("first_name")
    email = factory.Faker("ascii_safe_email")
    biography = factory.Faker("paragraph", nb_sentences=7, variable_nb_sentences=True, ext_word_list=None)


ISTAT_CLASSIFICATIONS = [
    "NAZ",
    "RIP",
    "REG",
    "PROV",
    "CM",
    "COM",
    "MUN",
    "ZU",
]


class Area(object):
    def __init__(self, **kwargs):
        for attr in [
            'name', 'identifier', 'classification',
            'istat_classification', 'inhabitants',
            'parent'
        ]:
            setattr(self, attr,  kwargs.get(attr, ''))


class AreaFactory(factory.Factory):
    class Meta:
        model = Area

    name = factory.Faker("city")
    identifier = factory.Faker("pystr", max_chars=4)
    classification = factory.Faker("pystr", max_chars=5)
    inhabitants = factory.Faker("pyint")

    @factory.lazy_attribute
    def istat_classification(self):
        return random.choice(ISTAT_CLASSIFICATIONS)
