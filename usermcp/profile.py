from mcp.server.fastmcp import FastMCP
from usermcp.prompt import get_user_profile_prompt
from usermcp.profile_manager import ProfileManager
from typing import Dict, Any

def register_user_profile_mcp(mcp: FastMCP):
    manager = ProfileManager()
    @mcp.prompt()
    def usermcp_guide_prompt():
        """User profile management"""
        return get_user_profile_prompt()

    @mcp.tool()
    def usermcp_query_user_profile(user_id: str):
        """Query user profile"""
        return manager.get_profile(user_id)

    @mcp.tool()
    def usermcp_insert_user_profile(user_id: str, profile: Dict[str, Any]):
        """Insert user profile"""
        return manager.insert_profile(user_id, profile)

    @mcp.tool()
    def usermcp_delete_user_profile(user_id: str):
        """Delete user profile"""
        success = manager.delete_profile(user_id)
        return {"deleted": success}