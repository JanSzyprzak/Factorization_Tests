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

def test_if_number_is_gt_than_1():
    assert prime_factors(1) == [], "Number must be greater than 1"

def test_if_p_f_returns_all_factors_list():
    number = 124
    factors = [2,2,31]
    
    assert prime_factors(number) == factors, "Something went wrong"

