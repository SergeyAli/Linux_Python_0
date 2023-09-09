import subprocess
def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    #test1
    assert checkout("cd /home/zerg/tst; 7z a ../out/arx2", "Everything in OK"), "test1 FAIL"
    #test2
    assert checkout("cd /home/zerg/out; 7z e arx2.7z /home/zerg/folder1", "Everything in OK"), "test2 FAIL"
    #test3
    assert checkout("cd /home/zerg/out; 7z t arx2,7z /home/zerg/folder1", "Everything in OK"), "test3 FAIL"