from main import prime_factors  

def test_import_prime_factors():
    try:
        
        assert callable(prime_factors), "prime_factors not callable"  
    except ImportError as error:  
        assert False, error
