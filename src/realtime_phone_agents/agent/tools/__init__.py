from langchain.tools import tool

@tool
def search_property_mock_tool(location: str) -> str:
    return (
        "I found one apartment in that area. It features 3 rooms, "
        "2 bathrooms, and a beatifully designed living room."
    )