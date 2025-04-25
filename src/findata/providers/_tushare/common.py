from utils.date_processor import standardize_date
from utils.auth import login

def get_trade_dates(
        start_date: str = "",
        end_date: str = "" ,
        exchange: str = "", 
        is_open: str = "1"
) -> dict:
    """
    获取各大交易所交易日历数据,默认提取的是上交所
    """
    # 登录tushare
    try:
        tsObj = login()

        # 日期标准化
        if start_date:
            start_date = standardize_date(start_date)

        if end_date:
            end_date = standardize_date(end_date)
        
        df = tsObj.trade_cal(exchange=exchange, start_date=start_date, end_date=end_date, is_open=is_open)

        return df['cal_date'].dropna().unique().tolist()

    except Exception as e:
            raise Exception(f"获取交易日列表失败！\n {str(e)}") from e





    
    