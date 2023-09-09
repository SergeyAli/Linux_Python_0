from checkout import checkout_positive


foder_in = "/home/user/tst"
foder_out = "/home/user/out"
foder_ext = "/home/user/folder1"


def test_step1():
     #test1 проверяет, что команда архивации содержит текст «Everything is OK» и завершается с кодом 0.
    assert checkout_positive("cd /home/user/tst; 7z a /home/user/out/arx2", "Everything is Ok"), "test1 FAIL"

def test_step2():
    # test2 проверяет, что команда разархивации содержит текст «Everything is OK» и завершается с кодом 0.
    assert checkout_positive("cd /home/user/out; 7z e arx2.7z -o/home/user/folder1 -y", "Everything is Ok"), \
        "test2 FAIL"


def test_step3():
    # test3 проверяет, что команда тестирования файлов в архиве содержит текст «Everything is OK»
    # и завершается с кодом 0.
    assert checkout_positive("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


"""
Добавить в проект тесты, проверяющие работу команд d (удаление из архива) и u (обновление архива). Вынести в отдельные
переменные пути к папкам с файлами, с архивом и с распакованными файлами. Выполнить тесты с ключом -v.
"""


def test_step4():
    # test4 удаление из архива
    assert checkout_positive("cd /home/user/out; 7z d arx2.7z", "Everything is Ok"), "test3 FAIL"

def test_step5():
    # test5 обновление архива
    assert checkout_positive("cd /home/user/out; 7z u arx2.7z", "Everything is Ok"), "test3 FAIL"
