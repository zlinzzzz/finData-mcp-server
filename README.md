<h1 align="center">
<img src="assets/logo.png" width="400" align=center/>
</h1><br>

<div align="center">

[![English](https://img.shields.io/badge/English-Click-yellow
)](README.md)
[![English](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-%E7%82%B9%E5%87%BB%E6%9F%A5%E7%9C%8B-orange)](README_zh.md)
[![License](https://img.shields.io/badge/License-Apache--2.0-green)](LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.11-blue)]()
[![Tushare](https://img.shields.io/badge/Tushare-purple)]()

</div>

<div class="toc" align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Demonstration">Demo</a> •
  <a href="#Quick-Start">Quick Start</a> •
  <a href="#Supported-Data-Providers">Supported Data Providers</a> •
  <a href="#Tools">Tools</a> 
</div>


# Overview

**FinData** is an open-source **Model Context Protocol(MCP) Server** that provides professional financial data access capabilities for LLM. It supports various data providers such as **Tushare**, **Wind**, **DataYes**, etc. This enables AI applications to quickly retrieve financial data.

Fully supports both **Stdio** and **SSE** transports, offering flexibility for different environments.


# Demonstration

https://github.com/user-attachments/assets/1a6d02af-22a3-44a0-ada7-a771a1c4818d

# Quick Start

## Prerequisites

Before getting started, please complete the following preparations:

- python => 3.11
- mcp[cli]>=1.6.0
- pandas>=2.2.3
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Depending on your data provider, install optional packages such as:

- tushare>=1.4.21

## Configuration

### Stdio Transport

You will need to edit the MCP client configuration file to add finData:

```JSON
{
  "mcpServers": {
    "finData": {
      "command": "uv", 
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/finData-mcp-server/src/findata", 
        "run",
        "server.py"
      ],
      "env": {
        "DATA_API_TOKEN": "",  // API Token for accessing data provider
        "PROVIDER": "tushare"  // Specified data provider
      }
    }
  }
}
```

### SSE Transport

Set the environment variables `DATA_API_TOKEN` and `PROVIDER` on the server hosting the MCP Server:

   **Windows**
   ```bash
    set DATA_API_TOKEN=<API Token for accessing data provider>
    set PROVIDER=<Specified data provider>
   ```

   **Linux**
  ```bash
    export DATA_API_TOKEN=<API Token for accessing data provider>
    export PROVIDER=<Specified data provider>
   ```

Then, start the MCP Server:

```bash
uv run server.py --transport sse   
```

- Optional Arguments:
  
  `--sse-host` Host to bind SSE server to (default: localhost)

  `--sse-port` Port for SSE server (default: 8000)

 
Once the MCP Server is running, update your MCP client's configuration with the following settings to connect to it.

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

**Note:** Variable names in configuration files may vary slightly between MCP clients. Refer to each client's documentation for proper configuration.

# Supported Data Providers

Set the `PROVIDER` environment variable to specify your provider:

- tushare

# Tools

## Tushare

### Market Data

- `daily` Get unadjusted daily stock market data.

### Fundamental Data

- `stock_basic` Get stock basic information including name, code, etc.
- `stock_company` Get listed company basic information.
- `bak_basic`  Get fundamental data for specific stocks within a given time range.
 
### Financial Data

- `income` Get company income statement data.
- `balancesheet` Get company balance sheet data.
- `cashflow` Get company cash flow statement data.

### Macroeconomic Data

- `shibor_lpr` Get Loan Prime Rate (LPR) data.
- `cn_gdp` Get Gross Domestic Product (GDP) data.
- `cn_cpi` Get Consumer Price Index (CPI) data.
- `cn_ppi` Get Producer Price Index (PPI) data.
- `cn_m` Get Money Supply data.
- `sf_month` Get Social Financing data.
- `cn_pmi` Get Purchasing Managers' Index (PMI) data.

# DataCanvas


![datacanvas](https://raw.githubusercontent.com/DataCanvasIO/HyperTS/main/docs/static/images/dc_logo_1.png)

This project is open-sourced by [DataCanvas](https://datacanvas.com/)


