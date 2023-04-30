import os

from api import PetFriends
from settings import valid_password, valid_email

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0



def test_add_new_pet(name='SuperCat', animal_type='dvorCat', age='4', pet_photo='images/cat.jpg'):
    """Получаем полный путь изображения питомца и сохраняем его в переменную pet_photo"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    """Запршиваем ключ api и сохраняем в переменную auth_key"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    """Добавляем питомца"""
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    """Сверяем полученный ответ с ожидаемым результатом"""
    assert status == 200
    assert result['name'] == name
