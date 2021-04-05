
#assisted by Professor Rossetti's screen sharing

# TODO: import some code
import os
from pandas import read_csv
from app.shopping import format_usd, lookup_product

# TODO: test the code

def test_format_usd():
    #assert 2 == 2

    assert format_usd(9.5) == "$9.50"