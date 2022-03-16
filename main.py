import os
import time

import pytest
from common.log_util import log_out

'''
def file():
    curpath = os.path.dirname(os.path.realpath(__file__))
    log_dir = os.path.join(curpath, "/Users/yangzhiqi/PycharmProjects/Selenium/log/")  # 日志存放目录
    # log_out(log_dir)
    log_out(log_dir)
'''

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)

    # curpath = os.path.dirname(os.path.realpath(__file__))
    log_dir = "/Users/yangzhiqi/PycharmProjects/Selenium/log/" # 日志存放目录
    name_project = "ceshi"
    log_out(log_dir, name_project)

    os.system("allure generate ./results -o ./reports --clean")
