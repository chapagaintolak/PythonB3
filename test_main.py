# pip install pytest
from mainprogram import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(4, 8) == 12
   
def test_sub():
    assert sub(2, 3) == -1
    assert sub(4, 8) == -4
   


