import os
import pandas as pd
from typing import Optional
from utils.date_processor import standardize_date
from utils.auth import login


async def daily(
    ts_code: Optional[str] = "",
    trade_date: Optional[str] = "",
    start_date: Optional[str] = "",
    end_date: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    
    """
    Name:
        A股日线行情。

    Description:
        获取股票未复权的日线行情数据。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | ts_code    | str   | 否    | 股票代码（支持多个股票同时提取，逗号分隔） |
        | trade_date | str   | 否    | 交易日期（YYYYMMDD），不与start_date和end_date同时出现 |
        | start_date | str   | 否    | 开始日期（YYYYMMDD），与end_date同时出现 |
        | end_date   | str   | 否    | 结束日期（YYYYMMDD），与start_date同时出现  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - ts_code: 股票代码
        - trade_date: 交易日期
        - open: 开盘价
        - high: 最高价
        - low: 最低价
        - close: 收盘价
        - pre_close: 昨收价【除权价，前复权】
        - change: 涨跌额
        - pct_chg: 涨跌幅 【基于除权后的昨收计算的涨跌幅：（今收-除权昨收）/除权昨收】
        - vol: 成交量 （手）
        - amount: 成交额 （千元）

    """
    try:       
        # 登录tushare
        tsObj = login()

        # 日期标准化
        if trade_date:
            trade_date = standardize_date(trade_date)

        if start_date:
            start_date = standardize_date(start_date)

        if end_date:
            end_date = standardize_date(end_date)


        #TODO 股票代码 标准化


        # 添加交易日
        if  fields:
            fields.append('trade_date')
            fields = list(set(fields))
        
            
        df = tsObj.daily(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date, fields=fields)
        return df
        # return df.to_json()
    except Exception as e:
        raise Exception(f"获取股票日线行情数据失败！\n {str(e)}") from e

