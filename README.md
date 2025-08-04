# usermcp

With just one line of code, your MCP or agent can record and manage user preferences with the user profile MCP, without requiring any database dependencies.

## Introduction

usermcp is a lightweight user preference management component designed to simplify the process of recording and managing user preferences for MCPs or agents. It provides simple interfaces for recording, querying, updating, and deleting user preferences without requiring any database dependencies.

## Features

- **No Database Dependencies**: Manage user preferences without installing or configuring a database
- **One-line Integration**: Integrate user preference management into your MCP or agent with just one line of code
- **Full CRUD Operations**: Supports Create, Read, Update, Delete operations for user preferences
- **Automatic Prompt Management**: Built-in prompt management for user preferences

## Installation

```bash
pip install usermcp
```

## Usage

### Basic Usage

```python
from mcp.server.fastmcp import FastMCP
from usermcp import register_user_profile_mcp

# Create FastMCP instance
mcp = FastMCP('Your MCP Name')

# ...
# implement your MCP logic here
# ...

# Register user profile management functions
register_user_profile_mcp(mcp)

# Run MCP service
mcp.run()
```

### Core Functions

usermcp provides the following tool functions:

- `usermcp_query_user_profile`: Query user preferences
- `usermcp_insert_user_profile`: Insert user preferences
- `usermcp_delete_user_profile`: Delete user preferences

### Prompt Management

usermcp includes built-in prompt management that automatically invokes the appropriate tool functions based on context:

- Actively invoke `usermcp_query_user_profile` when the context contains relevant tokens like the user's name or other personal information
- Invoke `usermcp_insert_user_profile` when the relevant information is triggered in your context
- Invoke `usermcp_delete_user_profile` when the user's feedback is different from what you expected

## Dependencies

- Python >= 3.10
- mcp >= 1.12.3

## License

MIT