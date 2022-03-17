import os
import pytest
import time

from common.log_util import log_out


def env_clear():
    path = os.getcwd()
    if os.path.exists(path + "/results"):
        os.system("rm -rf results")
    if os.path.exists(path + "/reports"):
        os.system("rm -rf reports")


def find_log():
    # curpath = os.path.dirname(os.path.realpath(__file__))
    # log_dir = os.path.join(curpath, "/Users/yangzhiqi/PycharmProjects/Selenium/log/")  # 日志存放目录
    # log_out(log_dir)

    log_dir = "/Users/yangzhiqi/PycharmProjects/Selenium/log/"  # 日志存放目录
    name_project = "ceshi"
    log_out(log_dir, name_project)


if __name__ == "__main__":
    # 清除上次报告
    env_clear()

    find_log()

    # 执行case
    # cmd = 'pytest TestCase --alluredir results'
    # os.system(cmd)
    # cmd = 'allure generate results -o reports --clean'

    time.sleep(5)
    pytest.main(["-vs", "--alluredir=results", "./TestCase"])
    os.system("allure generate ./results -o ./report --clean")


