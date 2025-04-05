"""
URL Parser Problem

Objective:
Write a function that parses URLs into their components.

Requirements:
1. Parse scheme (http/https)
2. Parse domain (including subdomains)
3. Parse path 
4. Parse query parameters (return as dictionary)
5. Parse fragment identifier
6. Handle invalid URLs gracefully

Example:
Input: "https://example.com/path?param=value#section"
Output: {
    "scheme": "https",
    "domain": "example.com",
    "path": "/path",
    "params": {"param": "value"},
    "fragment": "section"
}
"""

def parse_url(url):
    """
    Parse a URL into its constituent components
    
    Args:
        url (str): The URL to parse
        
    Returns:
        dict: Dictionary containing URL components or None if invalid
    """
    # TODO: Implement URL parsing
    pass
