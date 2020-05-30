import counter
import pytest

def test_counter_inc():
        assert counter.inc(4) == 5
        
def test_counter_dec():
         assert counter.dec(5) == 4
        
def test_counter_inc_by_2():
         assert counter.dec(4) == 6

def test_counter_dec_by_2():
         assert counter.dec(6) == 4

    
