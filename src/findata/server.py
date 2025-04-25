import os
import importlib
import inspect
from types import ModuleType
from mcp.server.fastmcp import FastMCP
from utils.findata_log import setup_logger

logger = setup_logger()

def decorate_async_functions(module: ModuleType, tool_decorator):
    for name, func in inspect.getmembers(module, inspect.iscoroutinefunction):
        setattr(module, name, tool_decorator(func))

def main():
    try:
            logger.info("Init finData MCP Server")
            # 创建MCP服务器实例
            mcp = FastMCP("finData")

            # 获取数据供应商
            data_provider = os.getenv("PROVIDER").lower()
            logger.debug("data provider: " + data_provider)

            if not data_provider:
                logger.error("请设置环境变量 PROVIDER 来指定数据供应商")
                raise ValueError("请设置环境变量 PROVIDER 来指定数据供应商")

            module = importlib.import_module("providers._"+data_provider)

            # 添加MCP装饰器
            decorate_async_functions(module, mcp.tool())

            mcp.run(transport="stdio")

    except Exception as e:
        logger.error(f"初始化失败！\n ", exc_info=True) 
        raise Exception(f"初始化失败！\n {str(e)}") from e

if __name__ == "__main__":
    main()
