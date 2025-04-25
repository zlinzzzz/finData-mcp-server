import os
import pandas as pd
from typing import Optional
from utils.date_processor import standardize_date
from .common import get_trade_dates
from utils.auth import login
from utils.findata_log import setup_logger

logger = setup_logger()

async def stock_basic(
    ts_code: Optional[str] = "",
    name: Optional[str] = "",
    market: Optional[str] = "",
    list_status: Optional[str] = "",
    exchange: Optional[str] = "",
    is_hs: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        股票基础信息。

    Description:
        获取股票的名称、代码等基础信息。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | ts_code    | str   | 否    | 股票代码，每次只能查询一支股票    |
        | name       | str   | 否    | 股票名称 |
        | market     | str   | 否    | 市场类别 （主板/创业板/科创板/CDR/北交所） |
        | list_status    | str   | 否    | 上市状态（L：上市，D：退市，P：暂停上市。默认是L） |
        | exchange   | str   | 否    | 交易所代码 (上交所：SSE， 深交所：SZSE  北交所：BSE) |
        | is_hs   | str   | 否    | 是否沪深港通标的（N：否，H：沪股通，S：深股通） |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - ts_code: TS代码
        - symbol: 股票代码
        - name: 股票名称
        - area: 地域
        - industry: 所属行业
        - fullname: 股票全称
        - enname: 英文全称
        - cnspell: 拼音缩写
        - market: 市场类型（主板/创业板/科创板/CDR）
        - exchange: 交易所代码
        - curr_type: 交易货币
        - list_status: 上市状态 L上市 D退市 P暂停上市
        - list_date: 上市日期
        - delist_date: 退市日期
        - is_hs: 是否沪深港通标的，N否 H沪股通 S深股通
        - act_name: 实控人名称
        - act_ent_type: 实控人企业性质
    """
    try:
        logger.debug("call stock basic!")
        # 登录tushare
        tsObj = login()

        #TODO 股票代码 标准化
            
        df = tsObj.stock_basic(ts_code=ts_code, name=name, market=market, list_status=list_status, exchange=exchange, is_hs=is_hs, fields=fields)
        # return df.to_json()
        return df
    
    except Exception as e:
        logger.error(f"获取股票基本信息失败！\n ", exc_info=True) 
        raise Exception(f"获取股票基本信息失败！\n {str(e)}") from e


async def stock_company(
    ts_code: Optional[str] = "",
    exchange: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        上市公司基本信息。

    Description:
        获取上市公司基础信息。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | ts_code    | str   | 否    | 股票代码，每次只能查询一家公司    |
        | exchange   | str   | 否    | 交易所代码 (上交所：SSE， 深交所：SZSE  北交所：BSE) |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - ts_code：股票代码
        - com_name：公司全称
        - com_id：统一社会信用代码
        - exchange：交易所代码
        - chairman：法人代表
        - manager：总经理
        - secretary：董秘
        - reg_capital：注册资本(万元)
        - setup_date：注册日期
        - province：所在省份
        - city：所在城市
        - introduction：公司介绍
        - website：公司主页
        - email：电子邮件
        - office：办公室
        - employees：员工人数
        - main_business：主要业务及产品
        - business_scope：经营范围

    """
    try:
        # 登录tushare
        tsObj = login()

        #TODO 股票代码 标准化
            
        df = tsObj.stock_company(ts_code=ts_code, exchange=exchange, fields=fields)
        # return df.to_json()
        return df
    
    except Exception as e:
        logger.error(f"获取上市公司基本信息数据失败！\n ", exc_info=True) 
        raise Exception(f"获取上市公司基本信息数据失败！\n {str(e)}") from e




async def bak_basic(
    ts_code: str,
    start_date: str,
    end_date: str,
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        股票基本面信息。

    Description:
        获取某支股票在指定时间范围内的基本面数据，数据从2016年开始。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | ts_code    | str   | 是    | 股票代码，每次只能查询一支股票    |
        | start_date | str   | 是    | 开始日期（YYYYMMDD） |
        | end_date | str   | 是    | 开始日期（YYYYMMDD） |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - trade_date：交易日期
        - ts_code：TS股票代码
        - name：股票名称
        - industry：行业
        - area：地域
        - pe：市盈率（动）
        - float_share：流通股本（亿）
        - total_share：总股本（亿）
        - total_assets：总资产（亿）
        - liquid_assets：流动资产（亿）
        - fixed_assets：固定资产（亿）
        - reserved：公积金
        - reserved_pershare：每股公积金
        - eps：每股收益
        - bvps：每股净资产
        - pb：市净率
        - list_date：上市日期
        - undp：未分配利润
        - per_undp：每股未分配利润
        - rev_yoy：收入同比（%）
        - profit_yoy：利润同比（%）
        - gpr：毛利率（%）
        - npr：净利润率（%）
        - holder_num：股东人数

    """
    try:
        # 登录tushare
        tsObj = login()

        # 日期标准化
        start_date = standardize_date(start_date)

        end_date = standardize_date(end_date)

        #TODO 股票代码 标准化

        # 获取指定时间范围内的交易日
        trade_dates = get_trade_dates(start_date=start_date, end_date=end_date)

        if not trade_dates:
            raise ValueError(f"指定的时间范围内，没有交易日")

        # 查询单支股票所有的基本面数据    
        if  fields:
            fields.append('trade_date')
            fields = list(set(fields))

        df = tsObj.bak_basic(ts_code=ts_code, fields=fields)

        res = df[df['trade_date'].isin(trade_dates)]

        # return res.to_json()
        return res
    
    except Exception as e:
        logger.error(f"获取股票基本面数据失败！\n ", exc_info=True) 
        raise Exception(f"获取股票基本面数据失败！\n {str(e)}") from e




