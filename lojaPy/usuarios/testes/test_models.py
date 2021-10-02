import pytest 

from ..models import Usuario 

pytestmark = pytest.mark.django_db 


def test_create_user(): 
    usuarios = Usuario.objects.create_user( 
        username="usuario_test", email="usuario@test.com", password="passw0rd"
    )

    assert usuarios.username == "usuario_test" 
    assert usuarios.email == "usuario@test.com"
    assert usuarios.is_active
    assert not usuarios.is_staff
    assert not usuarios.is_superuser


def test_create_superuser():
    usuarios = Usuario.objects.create_superuser(
        username="admin_test", email="admin@test.com", password="passw0rd"
    )
    assert usuarios.username == "admin_test"
    assert usuarios.email == "admin@test.com"
    assert usuarios.is_active
    assert usuarios.is_staff
    assert usuarios.is_superuser