import random
from collections import Counter

import pytest


@pytest.mark.parametrize('number_of_facts', [random.randint(0, 100) for _ in range(10)], indirect=True)
def test_different_number_of_facts(request, number_of_facts):
    assert len(number_of_facts) == request.node.callspec.params['number_of_facts']

    counter = Counter(number_of_facts)
    non_unique_facts = [item for item, count in counter.items() if count > 1]
    assert len(
        non_unique_facts) == 0, f'Some facts in the list are repeated. IDs of the repeated facts: {non_unique_facts}'


@pytest.mark.parametrize('fact_by_type', ['cat', 'dog', 'snail', 'horse'], indirect=True)
def test_random_fact_type_matches(request, fact_by_type):
    requested_type = request.node.callspec.params['fact_by_type']
    obtained_type = fact_by_type.type
    assert obtained_type == requested_type, (f'The type of the obtained fact does not match the requested type. '
                                             f'Requested: {requested_type}, obtained: {obtained_type}')
