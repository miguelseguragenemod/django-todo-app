from faker.providers import person, misc, lorem, internet, profile, credit_card, job
from faker import Factory


def instance_faker():
    faker = Factory.create()
    faker.add_provider(person)
    faker.add_provider(profile)
    faker.add_provider(lorem)
    faker.add_provider(misc)
    faker.add_provider(internet)
    faker.add_provider(credit_card)
    faker.add_provider(job)

    return faker
