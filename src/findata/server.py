import os
import importlib
import argparse
import inspect
from types import ModuleType
from mcp.server.fastmcp import FastMCP
from utils.findata_log import setup_logger

logger = setup_logger()

def decorate_async_functions(module: ModuleType, tool_decorator):
    for name, func in inspect.getmembers(module, inspect.iscoroutinefunction):
        setattr(module, name, tool_decorator(func))


def run(args):
    try:
        logger.info("Init finData MCP Server")

        # 获取数据供应商
        data_provider = os.getenv("PROVIDER").lower()
        logger.debug("data provider: " + data_provider)

        if not data_provider:
            logger.error("请设置环境变量 PROVIDER 来指定数据供应商")
            raise ValueError("请设置环境变量 PROVIDER 来指定数据供应商")

        module = importlib.import_module("providers._"+data_provider)

        if args.transport == 'stdio':
            # 创建MCP服务器实例
            mcp = FastMCP("finData")
            # 添加MCP装饰器
            decorate_async_functions(module, mcp.tool())
            mcp.run(transport="stdio")


        elif args.transport == 'sse':
            # 创建MCP服务器实例
            mcp = FastMCP(
                "finDatta",
                host=args.sse_host,
                port=args.sse_port,
            )
            # 添加MCP装饰器
            decorate_async_functions(module, mcp.tool())
            mcp.run(transport='sse')

    except Exception as e:
        logger.error(f"初始化失败！\n ", exc_info=True) 
        raise Exception(f"初始化失败！\n {str(e)}") from e


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="finData MCP Server")

    parser.add_argument(
        "--transport",
        type=str,
        choices=["stdio", "sse"],
        default="stdio",
        help="Select MCP transport: stdio (default) or sse",
    )

    parser.add_argument(
        "--sse-host",
        type=str,
        default="localhost",
        help="Host to bind SSE server to (default: localhost)",
    )

    parser.add_argument(
        "--sse-port",
        type=int,
        default=8000,
        help="Port for SSE server (default: 8000)",
    )

    args = parser.parse_args()
    
    logger.info(f"Running MCP Server with parameters: {args}")

    run(args)
