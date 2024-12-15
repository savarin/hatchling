from contextlib import ExitStack
from unittest.mock import patch

import pandas as pd
import pytest

from .data import load_data


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "category": ["a", "b"],
            "value": [1, 2],
        }
    )


def test_load_data(df: pd.DataFrame) -> None:
    with ExitStack() as stack:
        stack.enter_context(patch("pandas.read_csv", return_value=df))

        df = load_data("data.csv")
        assert list(df["category"].values) == ["a", "b"]
        assert list(df["value"].values) == [1, 2]
