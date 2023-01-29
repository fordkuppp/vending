import pytest

import vending


@pytest.fixture
def app():
    return vending.app


@pytest.fixture
def models():
    return vending.models
