from main import prime_factors  


def test_import_prime_factors():
    try: 
        assert callable(prime_factors), "prime_factors is not callable"  
    except ImportError as error:  
        assert False, error

def test_if_f_returns_factors_list():
    assert type(prime_factors(127)) == list


def test_p_f_2():
    assert prime_factors(2) == [2]