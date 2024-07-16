from urllib.parse import urljoin

import pytest
import requests

from utils import BASE_URL, CatFact, convert_dict_to_dataclass


@pytest.fixture
def number_of_facts(request) -> list[CatFact]:
    amount_of_facts = request.param

    url = urljoin(BASE_URL, f'/facts/random?amount={amount_of_facts}')

    response = requests.get(url)

    facts = []

    received_facts = response.json()
    received_facts = [received_facts] if not isinstance(received_facts, list) else received_facts

    for fact in received_facts:
        facts.append(convert_dict_to_dataclass(CatFact, fact))

    return facts


@pytest.fixture
def fact_by_type(request) -> CatFact:
    animal_type = request.param
    url = urljoin(BASE_URL, f'/facts/random?animal_type={animal_type}')

    response = requests.get(url)

    fact = convert_dict_to_dataclass(CatFact, response.json())

    return fact
