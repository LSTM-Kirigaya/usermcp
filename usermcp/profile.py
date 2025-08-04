from mcp.server.fastmcp import FastMCP
from usermcp.prompt import get_user_profile_prompt

def register_user_profile_mcp(mcp: FastMCP):
    @mcp.prompt()
    def usermcp_guide_prompt():
        """User profile management"""
        return get_user_profile_prompt()

    @mcp.tool()
    def usermcp_query_user_profile():
        """Query user profile"""
        pass


    @mcp.tool()
    def usermcp_insert_user_profile():
        """Insert user profile"""
        pass


    @mcp.tool()
    def usermcp_delete_user_profile():
        """Delete user profile"""
        pass
