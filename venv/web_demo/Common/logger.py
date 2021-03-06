# coding: utf-8
# Author：zlp
# Date ：2020/5/24
# Tool ：PyCharm

import logging
import os


logger = logging.getLogger()
logger.setLevel("DEBUG")
fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]"
formatter = logging.Formatter(fmt=fmt)

# 控制台
# console_handler = logging.StreamHandler()
#
# console_handler.setLevel('DEBUG')
# console_handler.setFormatter(formatter)

# 文件
log_dir = os.path.dirname(__file__)
file_handler = logging.FileHandler(log_dir + "/case.log")
file_handler.setLevel('DEBUG')
file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
logger.addHandler(file_handler)




if __name__ == '__main__':

    logger.info("测试开始")
    logger.error("测试报错")
    logger.debug("测试数据")
    logger.info("测试结束")
