import os
from abc import ABC, abstractmethod
from typing import Dict, Type
import tushare as ts
from utils.findata_log import setup_logger

logger = setup_logger()

class LoginHandler(ABC):
    @abstractmethod
    def login(self):
        pass

class TushareLoginHandler(LoginHandler):
    """Tushare 登录处理器""" 
    def login(self,):
        api_token = os.getenv("DATA_API_TOKEN")
        ts.set_token(api_token)
        pro = ts.pro_api()

        return pro


class LoginFactory:
    """登录工厂类，负责创建合适的登录处理器"""
    
    _handlers = {
        "tushare": TushareLoginHandler,
    }
    
    @classmethod
    def get_handler(cls, provider: str) -> LoginHandler:
        """获取适合指定平台的登录处理器"""
        provider = provider.lower()
        if provider not in cls._handlers:
            logger.error(f"不支持的登录平台:{provider}") 
            raise ValueError(f"不支持的登录平台: {provider}")
        return cls._handlers[provider]()
    

def login() -> object:
    """
    登录函数
    """
    # 从环境变量获取平台设置
    provider = os.getenv("PROVIDER").lower()
    if not provider:
        logger.error(f"请设置环境变量 PROVIDER 来指定数据供应商") 
        raise ValueError("请设置环境变量 PROVIDER 来指定数据供应商")
    
    try:
        handler = LoginFactory.get_handler(provider)
        return handler.login()
    except Exception as e:
        logger.error(f"登录失败！\n ", exc_info=True) 
        return False
    
