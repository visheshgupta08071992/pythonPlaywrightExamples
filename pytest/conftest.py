import pytest


@pytest.fixture(scope="session")
def initialze():
    print("Initialized")
    yield
    print("Closing")