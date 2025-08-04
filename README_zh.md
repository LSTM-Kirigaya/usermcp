# usermcp

只需一行代码，您的 MCP 或代理就可以通过用户配置文件 MCP 记录和管理用户偏好，而无需任何数据库依赖。

## 简介

usermcp 是一个轻量级的用户偏好管理组件，旨在简化 MCP 或代理记录和管理用户偏好的流程。它提供了简单的接口用于记录、查询、更新和删除用户偏好，而无需依赖任何数据库。

## 功能特性

- **无数据库依赖**: 不需要安装和配置数据库即可管理用户偏好
- **一行代码集成**: 只需一行代码即可将用户偏好管理功能集成到您的 MCP 或代理中
- **完整的 CRUD 操作**: 支持创建(Create)、读取(Read)、更新(Update)、删除(Delete)用户偏好
- **自动提示管理**: 提供内置提示管理用户偏好

## 安装

```bash
pip install usermcp
```

## 使用方法

### 基本用法

```python
from mcp.server.fastmcp import FastMCP
from usermcp import register_user_profile_mcp

# 创建 FastMCP 实例
mcp = FastMCP('Your MCP Name')

# ...
# implement your MCP logic here
# ...

# 注册用户偏好管理功能
register_user_profile_mcp(mcp)

# 运行 MCP 服务
mcp.run()
```

### 核心功能

usermcp 提供以下工具函数:

- `usermcp_query_user_profile`: 查询用户偏好
- `usermcp_insert_user_profile`: 插入用户偏好
- `usermcp_delete_user_profile`: 删除用户偏好

### 提示管理

usermcp 内置了提示管理功能，可以根据上下文自动调用相应的工具函数:

- 当上下文中包含相关用户信息（如用户名等）时，主动调用 `usermcp_query_user_profile`
- 当上下文中触发相关信息时，调用 `usermcp_insert_user_profile`
- 当用户反馈与预期不同时，调用 `usermcp_delete_user_profile`

## 依赖

- Python >= 3.10
- mcp >= 1.12.3

## 许可证

MIT