from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from usermcp import register_user_profile_mcp

mcp = FastMCP(name="DrawingMCP")

# 注册用户偏好管理功能
register_user_profile_mcp(mcp)

# 定义绘制圆形的参数 DTO
class DrawCircle(BaseModel):
    radius: int
    color: str
    line_width: int


class DrawRectangle(BaseModel):
    width: int
    height: int
    color: str = "black"
    line_width: int = 1


@mcp.tool()
def draw_circle(user_id: str, config: DrawCircle):
    """绘制圆形"""
    return {
        "action": "draw_circle",
        "user_id": user_id,
        "radius": config.radius,
        "color": config.color,
        "line_width": config.line_width,
        "status": "success"
    }


# 工具函数 - 绘制矩形
@mcp.tool()
def draw_rectangle(user_id: str, config: DrawRectangle):
    """绘制矩形"""
    return {
        "action": "draw_rectangle",
        "user_id": user_id,
        "width": config.width,
        "height": config.height,
        "color": config.color,
        "line_width": config.line_width,
        "status": "success"
    }
