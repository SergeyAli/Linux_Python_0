import pytest

from sshcheckers import ssh_checkout, ssh_getout, ssh_checkout_negative
import yaml

# folder_in = '/home/user/tst'
# folder_out = '/home/user/out'
# folder_ext = '/home/user/folder1'
# folder_bad = '/home/user/folder2'

with open('config.yaml') as fy:
    data = yaml.safe_load(fy)


class TestNegative:
    def test_negative1(self, make_folder, clear_folder, make_files, create_bad_archive):  # e извлекли из архива

        assert ssh_checkout_negative(f'cd {data["folder_bad"]}; 7z e arx2.7z -o{data["folder_ext"]} -y', "ERRORS", False)

    def test_negative2(self, make_folder, clear_folder, make_files,
                       create_bad_archive):  # t проверка целостности архива
        assert ssh_checkout_negative(f'cd {data["folder_bad"]}; 7z t arx2.7z', "Is not", False)



if __name__ == '__main__':
    pytest.main(['-vv'])