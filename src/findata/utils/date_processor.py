from datetime import datetime
import re


# 标准化日期
def standardize_date(input_date):
    """
    将各种格式的日期标准化为 YYYYMMDD 格式
    
    参数:
        input_date (str): 输入的日期字符串，可以是各种格式
        
    返回:
        str: 标准化后的日期，格式为 YYYYMMDD
    """
    if len(input_date) == 8:

        input_date = str(input_date)

        # 尝试常见日期格式
        common_formats = [
            '%Y-%m-%d',    # 2023-04-15
            '%Y/%m/%d',    # 2023/04/15
            '%m/%d/%Y',    # 04/15/2023
            '%d-%m-%Y',    # 15-04-2023
            '%d.%m.%Y',     # 15.04.2023
            '%Y%m%d',      # 20230415 (已经是目标格式)
            '%b %d, %Y',    # Apr 15, 2023
            '%B %d, %Y',    # April 15, 2023
            '%d %b %Y',     # 15 Apr 2023
            '%d %B %Y',    # 15 April 2023
        ]
        
        # 尝试解析日期
        for fmt in common_formats:
            try:
                dt = datetime.strptime(input_date, fmt)
                return dt.strftime('%Y%m%d')
            except ValueError:
                continue
        
        
        # 尝试处理中文日期（如2023年4月15日）
        cn_match = re.match(r'(\d{4})年(\d{1,2})月(\d{1,2})日', input_date)
        if cn_match:
            year = cn_match.group(1)
            month = cn_match.group(2).zfill(2)
            day = cn_match.group(3).zfill(2)
            try:
                datetime.strptime(f"{year}{month}{day}", '%Y%m%d')
                return f"{year}{month}{day}"
            except ValueError:
                pass
    
    # 如果所有尝试都失败，抛出异常
    raise ValueError(f"无法解析日期: {input_date}")