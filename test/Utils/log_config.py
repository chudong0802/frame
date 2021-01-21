# coding=utf-8

"""
author: MiaZhang
Created on 2020/5/22 10:33
"""
import datetime
import logging


class LogConfig:
    def __init__(self, name=__name__, level='DEBUG'):
        self.__nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
        self.__name = name
        self.__path = './Log/' + self.__nowTime + '.log'
        self.__level = level
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def __ini_handler(self):
        """初始化handler"""
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.__path, encoding='utf-8')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d]'
                                      ' %(levelname)s: %(message)s')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回looger"""
        stream_handler, file_handler = self.__ini_handler()
        self.__set_handler(stream_handler, file_handler)
        self.__set_formatter(stream_handler, file_handler)
        self.__close_handler(stream_handler, file_handler)
        return self.__logger

# if __name__ == '__main__':
#     log = LogConfig()
#     logger = log.Logger
#     logger.debug('I am a debug message')
