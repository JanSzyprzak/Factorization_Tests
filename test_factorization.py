from main import prime_factors  


def test_import_prime_factors():
    try: 
        assert callable(prime_factors), "prime_factors is not callable"  
    except ImportError as error:  
        assert False, error

def test_if_f_returns_factors_list():
    assert type(prime_factors(127)) == list


def test_p_f_input_validation():    
    
    invalid_inputs = ["hello", 3.14, True, [2, 3, 4]]

    for invalid_input in invalid_inputs:
        try:
            prime_factors(invalid_input)
            assert False, "Function should raise TypeError when called with non-integer argument"
        except TypeError as e:
            assert str(e) == "Input must be an integer"
