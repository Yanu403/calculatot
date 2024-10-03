# calculator.py

def add(a, b):
    """Menambahkan dua angka."""
    return a + b

def subtract(a, b):
    """Mengurangkan angka kedua dari angka pertama."""
    return a - b

def multiply(a, b):
    """Mengalikan dua angka."""
    return a * b

def divide(a, b):
    """Membagi angka pertama dengan angka kedua."""
    if b == 0:
        raise ValueError("Tidak dapat membagi dengan nol!")
    return a / b
