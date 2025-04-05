from url_parser import parse_url

def test_complete_url():
    url = "https://sub.example.com/path/to/resource?param1=value1&param2=value2#section"
    result = parse_url(url)
    assert result == {
        "scheme": "https",
        "domain": "sub.example.com",
        "path": "/path/to/resource",
        "params": {"param1": "value1", "param2": "value2"},
        "fragment": "section"
    }

def test_minimal_url():
    result = parse_url("http://example.com")
    assert result == {
        "scheme": "http",
        "domain": "example.com",
        "path": "",
        "params": {},
        "fragment": ""
    }

def test_invalid_urls():
    assert parse_url("not_a_url") is None
    assert parse_url("http://") is None
    assert parse_url("://example.com") is None

def test_url_without_scheme():
    assert parse_url("example.com/path") is None
