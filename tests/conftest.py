import pytest

import vending


@pytest.fixture
def app() -> vending.app:
    return vending.app


@pytest.fixture
def models() -> vending.models:
    return vending.models
