import pytest
from pydantic import ValidationError

from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 15 Pro Max"


def test_schemas_return_raise():
    data = {"name": "Iphone 15 Pro Max", "quantity": 10, "price": 9.500}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 15 Pro Max", "quantity": 10, "price": 9.5},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }
