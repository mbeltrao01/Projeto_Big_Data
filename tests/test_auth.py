from security.auth import authenticate

def test_authenticate_success():
    assert authenticate("admin", "senha123") == True

def test_authenticate_fail():
    assert authenticate("admin", "senha_errada") == False
