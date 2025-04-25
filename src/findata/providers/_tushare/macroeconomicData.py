import os
import pandas as pd
from typing import Optional
from utils.date_processor import standardize_date
from utils.auth import login


# LPR
async def shibor_lpr(
    start_date: Optional[str] = "",
    end_date: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    
    """
    Name:
        LPR贷款基础利率。

    Description:
        获取LPR贷款基础利率。贷款基础利率（Loan Prime Rate，简称LPR），是基于报价行自主报出的最优贷款利率计算并发布的贷款市场参考利率。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | start_date | str   | 否    | 开始日期（YYYYMMDD），与end_date同时出现 |
        | end_date   | str   | 否    | 结束日期（YYYYMMDD），与start_date同时出现  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - date：日期
        - 1y：1年贷款利率
        - 5y：5年贷款利率

    """
    try:
        # 登录tushare
        tsObj = login()

        # 日期标准化
        if start_date:
            start_date = standardize_date(start_date)

        if end_date:
            end_date = standardize_date(end_date)


        #TODO 股票代码 标准化
        
            
        df = tsObj.shibor_lpr(start_date=start_date, end_date=end_date, fields=fields)
        # return df.to_json()
        return df
    except Exception as e:
        raise Exception(f"获取LPR贷款基础利率失败！\n {str(e)}") from e


# GDP
async def cn_gdp(
    q: Optional[str] = "",
    start_q: Optional[str] = "",
    end_q: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    
    """
    Name:
        GDP数据。

    Description:
        获取国民经济之GDP数据。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | q | str   | 否    | 季度（2019Q1表示，2019年第一季度），支持多个季度同时输入，逗号分隔 |
        | start_q | str   | 否    | 开始季度（2019Q1表示，2019年第一季度），与end_q同时使用 |
        | end_q   | str   | 否    | 结束季度（2019Q1表示，2019年第一季度），与start_q同时使用  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - quarter: 季度
        - gdp: GDP累计值（亿元）
        - gdp_yoy: 当季同比增速（%）
        - pi: 第一产业累计值（亿元）
        - pi_yoy: 第一产业同比增速（%）
        - si: 第二产业累计值（亿元）
        - si_yoy: 第二产业同比增速（%）
        - ti: 第三产业累计值（亿元）
        - ti_yoy: 第三产业同比增速（%）

    """
    try:
        # 登录tushare
        tsObj = login()

        # 添加季度字段
        if  fields:
            fields.append('quarter')
            fields = list(set(fields))
            
        df = tsObj.cn_gdp(q=q, start_q=start_q, end_q=end_q, fields=fields)
        # return df.to_json()
        return df
    except Exception as e:
        raise Exception(f"获取GDP数据失败！\n {str(e)}") from e

# CPI
async def cn_cpi(
    m: Optional[str] = "",
    start_m: Optional[str] = "",
    end_m: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        居民消费价格指数。

    Description:
        获取CPI居民消费价格数据，包括全国、城市和农村的数据。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | m | str   | 否    | 月份（YYYYMM），支持多个月份同时输入，逗号分隔 |
        | start_m | str   | 否    | 开始月份（YYYYMM），与end_m同时使用 |
        | end_m   | str   | 否    | 结束月份（YYYYMM），与start_m同时使用  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - month: 月份
        - nt_val: 全国当月值
        - nt_yoy: 全国同比（%）
        - nt_mom: 全国环比（%）
        - nt_accu: 全国累计值
        - town_val: 城市当月值
        - town_yoy: 城市同比（%）
        - town_mom: 城市环比（%）
        - town_accu: 城市累计值
        - cnt_val: 农村当月值
        - cnt_yoy: 农村同比（%）
        - cnt_mom: 农村环比（%）
        - cnt_accu: 农村累计值
    """
    try:
        # 登录tushare
        tsObj = login()

        # 添加季度字段
        if  fields:
            fields.append('month')
            fields = list(set(fields))
            
        df = tsObj.cn_cpi(m=m, start_m=start_m, end_m=end_m, fields=fields)
        # return df.to_json()
        return df
    except Exception as e:
        raise Exception(f"获取CPI数据失败！\n {str(e)}") from e

# PPI
async def cn_ppi(
    m: Optional[str] = "",
    start_m: Optional[str] = "",
    end_m: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        工业生产者出厂价格指数。

    Description:
        获取PPI工业生产者出厂价格指数数据。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | m | str   | 否    | 月份（YYYYMM），支持多个月份同时输入，逗号分隔 |
        | start_m | str   | 否    | 开始月份（YYYYMM），与end_m同时使用 |
        | end_m   | str   | 否    | 结束月份（YYYYMM），与start_m同时使用  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - month: 月份(格式为YYYYMM)
        - ppi_yoy: 工业品出厂价格指数(PPI)-全部工业品-当月同比
        - ppi_mp_yoy: PPI-生产资料-当月同比
        - ppi_mp_qm_yoy: PPI-生产资料-采掘业-当月同比
        - ppi_mp_rm_yoy: PPI-生产资料-原料业-当月同比
        - ppi_mp_p_yoy: PPI-生产资料-加工业-当月同比
        - ppi_cg_yoy: PPI-生活资料-当月同比
        - ppi_cg_f_yoy: PPI-生活资料-食品类-当月同比
        - ppi_cg_c_yoy: PPI-生活资料-衣着类-当月同比
        - ppi_cg_adu_yoy: PPI-生活资料-一般日用品类-当月同比
        - ppi_cg_dcg_yoy: PPI-生活资料-耐用消费品类-当月同比

        - ppi_mom: PPI-全部工业品-环比
        - ppi_mp_mom: PPI-生产资料-环比
        - ppi_mp_qm_mom: PPI-生产资料-采掘业-环比
        - ppi_mp_rm_mom: PPI-生产资料-原料业-环比
        - ppi_mp_p_mom: PPI-生产资料-加工业-环比
        - ppi_cg_mom: PPI-生活资料-环比
        - ppi_cg_f_mom: PPI-生活资料-食品类-环比
        - ppi_cg_c_mom: PPI-生活资料-衣着类-环比
        - ppi_cg_adu_mom: PPI-生活资料-一般日用品类-环比
        - ppi_cg_dcg_mom: PPI-生活资料-耐用消费品类-环比

        - ppi_accu: PPI-全部工业品-累计同比
        - ppi_mp_accu: PPI-生产资料-累计同比
        - ppi_mp_qm_accu: PPI-生产资料-采掘业-累计同比
        - ppi_mp_rm_accu: PPI-生产资料-原料业-累计同比
        - ppi_mp_p_accu: PPI-生产资料-加工业-累计同比
        - ppi_cg_accu: PPI-生活资料-累计同比
        - ppi_cg_f_accu: PPI-生活资料-食品类-累计同比
        - ppi_cg_c_accu: PPI-生活资料-衣着类-累计同比
        - ppi_cg_adu_accu: PPI-生活资料-一般日用品类-累计同比
        - ppi_cg_dcg_accu: PPI-生活资料-耐用消费品类-累计同比
    """

    try:
        # 登录tushare
        tsObj = login()

        # 添加季度字段
        if  fields:
            fields.append('month')
            fields = list(set(fields))
            
        df = tsObj.cn_ppi(m=m, start_m=start_m, end_m=end_m, fields=fields)
        # return df.to_json()
        return df
    except Exception as e:
        raise Exception(f"获取PPI数据失败！\n {str(e)}") from e


# 货币供应量
async def cn_m(
    m: Optional[str] = "",
    start_m: Optional[str] = "",
    end_m: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        货币供应量。

    Description:
        获取货币供应量之月度数据。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | m | str   | 否    | 月份（YYYYMM），支持多个月份同时输入，逗号分隔 |
        | start_m | str   | 否    | 开始月份（YYYYMM），与end_m同时使用 |
        | end_m   | str   | 否    | 结束月份（YYYYMM），与start_m同时使用  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - month: 月份（YYYYMM）
        - m0: M0（亿元）
        - m0_yoy: M0同比（%）
        - m0_mom: M0环比（%）
        - m1: M1（亿元）
        - m1_yoy: M1同比（%）
        - m1_mom: M1环比（%）
        - m2: M2（亿元）
        - m2_yoy: M2同比（%）
        - m2_mom: M2环比（%）
    """
    try:
        # 登录tushare
        tsObj = login()

        # 添加季度字段
        if  fields:
            fields.append('month')
            fields = list(set(fields))
            
        df = tsObj.cn_m(m=m, start_m=start_m, end_m=end_m, fields=fields)
        # return df.to_json()
        return df
    except Exception as e:
        raise Exception(f"获取货币供应量数据失败！\n {str(e)}") from e


# 社融数据（月度）
async def sf_month(
    m: Optional[str] = "",
    start_m: Optional[str] = "",
    end_m: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        社融数据（月度）。

    Description:
        获取月度社会融资数据。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | m | str   | 否    | 月份（YYYYMM），支持多个月份同时输入，逗号分隔 |
        | start_m | str   | 否    | 开始月份（YYYYMM），与end_m同时使用 |
        | end_m   | str   | 否    | 结束月份（YYYYMM），与start_m同时使用  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - month: 月度
        - inc_month: 社融增量当月值（亿元）
        - inc_cumval: 社融增量累计值（亿元）
        - stk_endval: 社融存量期末值（万亿元）
    """
    try:
        # 登录tushare
        tsObj = login()

        # 添加季度字段
        if  fields:
            fields.append('month')
            fields = list(set(fields))
            
        df = tsObj.sf_month(m=m, start_m=start_m, end_m=end_m, fields=fields)
        # return df.to_json()
        return df
    except Exception as e:
        raise Exception(f"获取社融数据数据失败！\n {str(e)}") from e

# pmi
async def cn_pmi(
    m: Optional[str] = "",
    start_m: Optional[str] = "",
    end_m: Optional[str] = "",
    fields: Optional[list] = [],
) -> dict:
    """
    Name:
        采购经理人指数(PMI)。

    Description:
        获取采购经理人指数(PMI)数据。

    Args:
        | 名称       | 类型  | 必填 | 描述                                   |
        |------------|-------|------|----------------------------------------|
        | m | str   | 否    | 月份（YYYYMM），支持多个月份同时输入，逗号分隔 |
        | start_m | str   | 否    | 开始月份（YYYYMM），与end_m同时使用 |
        | end_m   | str   | 否    | 结束月份（YYYYMM），与start_m同时使用  |
        | fields     | list  | 否    | 从Fields中选取需要查询的字段  |

    Fields:
        - month - 月份YYYYMM
        - pmi010000 - 制造业PMI
        - pmi010100 - 制造业PMI-企业规模-大型企业
        - pmi010200 - 制造业PMI-企业规模-中型企业
        - pmi010300 - 制造业PMI-企业规模-小型企业
        - pmi010400 - 制造业PMI-构成指数-生产指数
        - pmi010401 - 制造业PMI-构成指数-生产指数-企业规模-大型企业
        - pmi010402 - 制造业PMI-构成指数-生产指数-企业规模-中型企业
        - pmi010403 - 制造业PMI-构成指数-生产指数-企业规模-小型企业
        - pmi010500 - 制造业PMI-构成指数-新订单指数
        - pmi010501 - 制造业PMI-构成指数-新订单指数-企业规模-大型企业
        - pmi010502 - 制造业PMI-构成指数-新订单指数-企业规模-中型企业
        - pmi010503 - 制造业PMI-构成指数-新订单指数-企业规模-小型企业
        - pmi010600 - 制造业PMI-构成指数-供应商配送时间指数
        - pmi010601 - 制造业PMI-构成指数-供应商配送时间指数-企业规模-大型企业
        - pmi010602 - 制造业PMI-构成指数-供应商配送时间指数-企业规模-中型企业
        - pmi010603 - 制造业PMI-构成指数-供应商配送时间指数-企业规模-小型企业
        - pmi010700 - 制造业PMI-构成指数-原材料库存指数
        - pmi010701 - 制造业PMI-构成指数-原材料库存指数-企业规模-大型企业
        - pmi010702 - 制造业PMI-构成指数-原材料库存指数-企业规模-中型企业
        - pmi010703 - 制造业PMI-构成指数-原材料库存指数-企业规模-小型企业
        - pmi010800 - 制造业PMI-构成指数-从业人员指数
        - pmi010801 - 制造业PMI-构成指数-从业人员指数-企业规模-大型企业
        - pmi010802 - 制造业PMI-构成指数-从业人员指数-企业规模-中型企业
        - pmi010803 - 制造业PMI-构成指数-从业人员指数-企业规模-小型企业
        - pmi010900 - 制造业PMI-其他-新出口订单
        - pmi011000 - 制造业PMI-其他-进口
        - pmi011100 - 制造业PMI-其他-采购量
        - pmi011200 - 制造业PMI-其他-主要原材料购进价格
        - pmi011300 - 制造业PMI-其他-出厂价格
        - pmi011400 - 制造业PMI-其他-产成品库存
        - pmi011500 - 制造业PMI-其他-在手订单
        - pmi011600 - 制造业PMI-其他-生产经营活动预期
        - pmi011700 - 制造业PMI-分行业-装备制造业
        - pmi011800 - 制造业PMI-分行业-高技术制造业
        - pmi011900 - 制造业PMI-分行业-基础原材料制造业
        - pmi012000 - 制造业PMI-分行业-消费品制造业
        - pmi020100 - 非制造业PMI-商务活动
        - pmi020101 - 非制造业PMI-商务活动-分行业-建筑业
        - pmi020102 - 非制造业PMI-商务活动-分行业-服务业业
        - pmi020200 - 非制造业PMI-新订单指数
        - pmi020201 - 非制造业PMI-新订单指数-分行业-建筑业
        - pmi020202 - 非制造业PMI-新订单指数-分行业-服务业
        - pmi020300 - 非制造业PMI-投入品价格指数
        - pmi020301 - 非制造业PMI-投入品价格指数-分行业-建筑业
        - pmi020302 - 非制造业PMI-投入品价格指数-分行业-服务业
        - pmi020400 - 非制造业PMI-销售价格指数
        - pmi020401 - 非制造业PMI-销售价格指数-分行业-建筑业
        - pmi020402 - 非制造业PMI-销售价格指数-分行业-服务业
        - pmi020500 - 非制造业PMI-从业人员指数
        - pmi020501 - 非制造业PMI-从业人员指数-分行业-建筑业
        - pmi020502 - 非制造业PMI-从业人员指数-分行业-服务业
        - pmi020600 - 非制造业PMI-业务活动预期指数
        - pmi020601 - 非制造业PMI-业务活动预期指数-分行业-建筑业
        - pmi020602 - 非制造业PMI-业务活动预期指数-分行业-服务业
        - pmi020700 - 非制造业PMI-新出口订单
        - pmi020800 - 非制造业PMI-在手订单
        - pmi020900 - 非制造业PMI-存货
        - pmi021000 - 非制造业PMI-供应商配送时间
        - pmi030000 - 中国综合PMI-产出指数
    """

    try:
        # 登录tushare
        tsObj = login()

        # 添加季度字段
        if  fields:
            fields.append('month')
            fields = list(set(fields))
            
        df = tsObj.cn_pmi(m=m, start_m=start_m, end_m=end_m, fields=fields)
        # return df.to_json()
        return df
    except Exception as e:
        raise Exception(f"获取PMI数据失败！\n {str(e)}") from e


