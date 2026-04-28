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

def test_sqrt():
    result = sqrt(9)
    assert abs(result - 3) < 0.001

    result = sqrt(16)
    assert abs(result - 4) < 0.001
    
# ===== IMPLEMENTACIÓN =====

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b    

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def sqrt(x):
    if x < 0:
        raise ValueError("No se puede calcular raíz de número negativo")

    guess = x / 2 if x != 0 else 0.0

    for _ in range(10):  # iteraciones suficientes para precisión
        if guess == 0:
            return 0
        guess = (guess + x / guess) / 2

    return guess
# ===== RUN TESTS =====

def run_tests():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_sqrt()
    print("All tests passed!")
run_tests()
