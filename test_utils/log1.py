import logging
import time
import os


class TestLog(object):
    '''
    封装后的logging
    '''

    def __init__(self, logger=None):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)

        # 相当于总的记录日志的级别
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log_file')
        # self.log_path = os.path.join(os.getcwd(), 'log_file')report用的getcwd()此处在用就会报错
        self.log_name = self.log_path + '\\' + self.log_time + 'test.log'
        # fh = logging.FileHandler(self.log_name, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的

        # 文件记录日志的级别，依赖于总的记录日志的级别
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    log = TestLog().get_log()

    log.debug('bbb')
    log.info('aaa')
    log.info('a1a1a1')
    log.warning('ccc')
    log.error('eee')
