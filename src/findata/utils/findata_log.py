import logging
import logging.handlers
import os
from datetime import datetime

def setup_logger(log_dir='logs', log_name='findata', max_days=7, level='INFO'):
    """
    设置日志记录器
    
    参数:
        log_dir (str): 日志目录
        log_name (str): 日志文件名前缀
        max_days (int): 最大保存天数
    """
    # 确保日志目录存在
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 创建日志文件名，格式为: 日志名_年月日.log
    log_filename = f"{log_name}_{datetime.now().strftime('%Y%m%d')}.log"
    log_path = os.path.join(log_dir, log_filename)
    
    # 创建日志记录器
    logger = logging.getLogger(log_name)
    logger.setLevel(level)
    
    # 如果已经有处理器，先清除(避免重复添加)
    if logger.handlers:
        logger.handlers = []
    
    # 创建文件处理器，使用TimedRotatingFileHandler实现按日期滚动
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=log_path,
        when='midnight',  # 每天午夜滚动
        interval=1,       # 每天
        backupCount=max_days,  # 最多保留7天
        encoding='utf-8'
    )
    file_handler.suffix = "%Y%m%d.log"  # 设置滚动文件的后缀
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    
    # 设置日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器到记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
