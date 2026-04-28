# ===== TESTS =====
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    
def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2
    
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    
# ===== IMPLEMENTACIÓN =====

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b    

def add(a, b):
    return a + b

# ===== RUN TESTS =====

def run_tests():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")
run_tests()
