import requests
from crewai.tools import tool

MCP = "http://localhost:3001/tools"

@tool("Inspect Source AST")
def ast_tool(file_path: str) -> dict:
    """Reads a JS/TS source file and extracts routes, field references, and exports."""
    return requests.post(f"{MCP}/inspect_source_ast", json={"filePath": file_path}).json()

@tool("Database Introspector")
def db_tool(compare_with: str) -> dict:
    """Samples MongoDB and compares actual fields against an OpenAPI spec."""
    return requests.post(f"{MCP}/database_introspector", json={"compareWith": compare_with}).json()

@tool("Schema Diff Engine")
def diff_tool(baseline_path: str, head_path: str) -> dict:
    """Diffs two OpenAPI spec files and reports breaking changes."""
    return requests.post(f"{MCP}/schema_diff_engine",
                         json={"baselinePath": baseline_path, "headPath": head_path}).json()

