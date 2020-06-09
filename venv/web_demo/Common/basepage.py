# coding: utf-8
# Author：zlp
# Date ：2020/5/23
# Tool ：PyCharm


import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time
from selenium import webdriver

from Common.dir_config import screenshot_dir


class BasePage:
    """
    包含了PageObjects中，用到的所有selenium底层方法
    实现日志记录、失败截图等
    """

    def __init__(self, driver):
        self.driver = driver

    def save_web_screenshot(self, img_doc):
        """
        失败截图：页面_功能_时间.png
        :param img_doc: 图片名称
        """

        now_time = time.strftime("%Y-%m-%d %H:%M:%S")
        filepath = f"{img_doc}_{now_time}.png"
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logging.info("网页截图成功")
        except:
            logging.exception("网页截屏失败！")

    def wait_ele_visible(self, loc, img_doc='', timeout=30, frequency=0.5):
        """
        等待元素可见
        :param loc: 元素定位表达式
        :param img_doc: 失败截图名称
        :param timeout: 超时时间
        :param frequency: 请求频率
        """
        try:
            # 等待元素
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            logging.exception("等待元素可见失败")
            # 等待失败时进行截图
            self.save_web_screenshot(img_doc)
            raise e

    def get_element(self, loc, img_doc=""):
        """
        查找元素
        :param loc: 元素定位，传入元组（定位类型，定位表达式）
        :param img_doc:
        :return ele:返回元素本身
        """
        try:
            # 查找元素
            ele = self.driver.find_element(*loc)
            return ele
        except:
            logging.exception("查找元素失败")
            self.save_web_screenshot(img_doc)
            raise

    def click_element(self, loc, img_doc='', timeout=30, frequency=0.5):
        """
        等待元素可见，找元素，然后点击元素
        :param loc: 定位表达式
        :param img_doc: 截图名称
        :param timeout: 等待时间
        :param frequency: 请求频率
        """
        # 等待元素可见
        self.wait_ele_visible(loc=loc, img_doc=img_doc, timeout=timeout, frequency=frequency)
        # 找元素
        ele = self.get_element(loc=loc, img_doc=img_doc)
        try:
            ele.click()
        except:
            logging.exception("点击元素失败")
            self.save_web_screenshot(img_doc)
            raise

    def input_text(self, loc, img_doc='', *args):
        """
        文本输入
        :param loc: 定位表达式
        :param img_doc: 截图名称
        :param args: 输入内容
        """
        self.wait_ele_visible(loc=loc, img_doc=img_doc)
        ele = self.get_element(loc=loc, img_doc=img_doc)

        try:
            ele.send_keys(*args)

        except:
            logging.exception("元素输入失败")
            self.save_web_screenshot(img_doc)
            raise

    def get_element_attribute(self, loc, attr_name, img_doc=''):
        """
        获取元素属性
        :param loc: 元素定位
        :param attr_name: 属性名称
        :param img_doc: 截图名称
        :return: 属性值
        """

        ele = self.get_element(loc, img_doc)

        try:
            attr_value = ele.get_attribute(attr_name)

            return attr_value
        except:
            logging.exception("获取元素属性失败")
            self.save_web_screenshot(img_doc)
            raise

    def get_element_text(self, loc, img_doc):
        """
        获取元素文本值
        :param loc: 元素定位
        :param img_doc: 截图名称
        :return: 文本值
        """
        ele = self.get_element(loc, img_doc)
        try:
            text = ele.text
            return text
        except:
            logging.exception("获取元素文本值")
            self.save_web_screenshot(img_doc)
            raise

    def windows_switch_to_iframe(self, loc):
        """
        切换至iframe
        :param loc: iframe的定位表达式
        :return:
        """
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        return self

    def windows_switch_to_alert(self):

        WebDriverWait(self.driver,20).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        #切换之后点击确定或取消使alert消失
        test = alert.text
        #确定
        alert.accept()
        #取消
        # alert.dismiss()
