@tool("Code Transformer")
def transform_tool(codemod: str, target_path: str, from_field: str, to_field: str) -> dict:
    """Runs a named codemod to rename fields across source files."""
    return requests.post(f"{MCP}/code_transformer",
                         json={"codemod": codemod, "targetPath": target_path,
                               "options": {"from": from_field, "to": to_field}}).json()

@tool("Dependency Graph Mapper")
def dep_tool(target_path: str, focus_on: str) -> dict:
    """Finds all files that import or reference a given file."""
    return requests.post(f"{MCP}/dependency_graph_mapper",
                         json={"targetPath": target_path, "focusOn": focus_on}).json()

@tool("Contract Test Runner")
def test_tool(spec_path: str) -> dict:
    """Validates an OpenAPI spec for correctness and field consistency."""
    return requests.post(f"{MCP}/contract_test_runner", json={"specPath": spec_path}).json()