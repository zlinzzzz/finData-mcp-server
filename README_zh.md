<h1 align="center">
<img src="https://github.com/user-attachments/assets/5c6cadf7-b9b0-4204-af55-9116e8b1aa1f" width="400" align=center/>
</h1><br>

<div align="center">


[![English](https://img.shields.io/badge/English-Click-yellow
)](README.md)
[![Chinese](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-%E7%82%B9%E5%87%BB%E6%9F%A5%E7%9C%8B-orange)](README_zh.md)
[![License](https://img.shields.io/badge/License-Apache--2.0-green)](LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.11-blue)]()
[![Tushare](https://img.shields.io/badge/Tushare-purple)]()


</div>

<div class="toc" align="center">
  <a href="#概述">概述</a> •
  <a href="#演示">演示</a> •
  <a href="#快速开始">快速开始</a> •
  <a href="#已支持的数据供应商">已支持的数据供应商</a> •
  <a href="#工具列表">工具列表</a> 
</div>


# 概述

**finData**是一个开源的金融数据查询**Model Context Protocol(MCP) Server**，向大模型提供专业级金融数据访问的能力。支持**Tushare**、**Wind**、**通联**等多种数据供应商接口，助力用户在AI应用中快速获取金融数据。

全面支持**Stdio**和**SSE**两种通信模式，灵活满足本地部署与远程调用等多样化的使用需求。

# 演示

https://github.com/user-attachments/assets/1a6d02af-22a3-44a0-ada7-a771a1c4818d

# 快速开始

## 环境准备

开始前，请先安装下列工具包：

- python => 3.11
- mcp[cli]>=1.6.0
- pandas>=2.2.3
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

根据所使用的数据供应商，请自行选择安装
- tushare>=1.4.21

## 配置MCP Server

### Stdio模式

将下面的内容添加到MCP client的配置文件中来调用MCP Server。

```JSON
{
  "mcpServers": {
    "finData": {
      "command": "uv", 
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/finData-mcp-server/src/findata", // finData MCP Server所在目录
        "run",
        "server.py"
      ],
      "env": {
        "DATA_API_TOKEN": "",  // 访问数据供应商的API Token
        "PROVIDER": "tushare"  // 指定数据供应商
      }
    }
  }
}
```

### SSE模式

在运行MCP Server的服务器上，设置数据供应商相关的环境变量`DATA_API_TOKEN`和`PROVIDER`：

   **Windows**
   ```bash
    set DATA_API_TOKEN=<访问数据供应商的API Token>
    set PROVIDER=<指定数据供应商>
   ```

   **Linux**
  ```bash
    export DATA_API_TOKEN=<访问数据供应商的API Token>
    export PROVIDER=<指定数据供应商>
   ```

然后启动MCP Server：
  
```bash
uv run server.py --transport sse   
```

- 可选参数
  
  `--sse-host` SSE服务绑定的主机，默认为localhost

  `--sse-port` SSE服务端口，默认为8000

  
MCP Server启动成功后，将下面的内容添加到MCP client的配置文件中来调用MCP Server。不同client配置文件中的变量名会有细微的差异，请根据client的说明进行调整。

```JSON
{
  "mcpServers": {
    "finData": {
      "name": "finData",
      "type": "sse",
      "baseUrl": "http://localhost:8000/sse"
    }
  }
}
```


# 已支持的数据供应商

通过环境变量`PROVIDER`使用指定的供应商

- tushare

# 工具列表

## Tushare

### 行情数据

- `daily` 获取股票未复权的日线行情数据。

### 基础数据

- `stock_basic` 获取股票的名称、代码等基础信息。
- `stock_company` 获取上市公司基础信息。
- `bak_basic`  获取某支股票在指定时间范围内的基本面数据。
 
### 财务数据

- `income` 获取上市公司利润表数据。
- `balancesheet` 获取上市公司资产负债表数据。
- `cashflow` 获取上市公司现金流量表数据。

### 宏观数据

- `shibor_lpr` 获取LPR贷款基础利率。
- `cn_gdp` 获取GDP数据。
- `cn_cpi` 获取CPI居民消费价格数据。
- `cn_ppi` 获取PPI工业生产者出厂价格指数数据。
- `cn_m` 获取货币供应量数据。
- `sf_month` 获取社会融资数据。
- `cn_pmi` 获取采购经理人指数(PMI)数据。

# DataCanvas



![datacanvas](https://raw.githubusercontent.com/DataCanvasIO/HyperTS/main/docs/static/images/dc_logo_1.png)

本项目由[DataCanvas](https://datacanvas.com/)开源

