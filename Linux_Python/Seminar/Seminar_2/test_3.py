"""
Задание 3
Создать отдельный файл для негативных тестов. Функцию проверки вынести в отдельную библиотеку. Повредить архив
(например, отредактировав его в текстовом редакторе). Написать негативные тесты работы архиватора с командами
распаковки (e) и проверки (t) поврежденного архива.
"""
from checkout import checkout_negative

foder_in = "/home/user/tst"
foder_out = "/home/user/out"
foder_ext = "/home/user/folder1"
foder_ext_bad = "/home/user/folder2"

def test_step1():
     #test1 негативный тест работы архиватора с командой распаковки (e).
    assert checkout_negative(f"cd {foder_ext_bad}; 7z e arx2.7z -o{foder_ext} -y", "ERRORS"), "test1 FAIL"

def test_step2():
    # test2 негативный тест работы архиватора с командой проверки (t) поврежденного архива.
    assert checkout_negative(f"cd {foder_ext_bad}; 7z t arx2.7z", "ERRORS"), "test2 FAIL"
