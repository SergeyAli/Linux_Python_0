"""
Задание 3
Создать отдельный файл для негативных тестов. Функцию проверки вынести в отдельную библиотеку. Повредить архив
(например, отредактировав его в текстовом редакторе). Написать негативные тесты работы архиватора с командами
распаковки (e) и проверки (t) поврежденного архива.
"""
from checkout import checkout_negative

foder_in = "/home/user/tst"
foder_out = "/home/user/out"
foder_ext = "/home/user/folder2"

def test_step1():
     #test1 проверяет, что команда архивации содержит текст «Everything is OK» и завершается с кодом 0.
    assert checkout_negative(f"cd {foder_in}; 7z a {foder_out}/arx2", "Everything is Ok"), "test1 FAIL"

def test_step2():
    # test2 проверяет, что команда разархивации содержит текст «Everything is OK» и завершается с кодом 0.
    assert checkout_negative(f"cd {foder_out}; 7z e arx2.7z -o{foder_ext} -y", "Everything is Ok"), \
        "test2 FAIL"
