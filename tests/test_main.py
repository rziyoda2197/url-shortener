import pytest
from url_shortener import URLShortener

@pytest.fixture
def url_shortener():
    return URLShortener()

def test_shorten_url(url_shortener):
    original_url = "https://www.example.com"
    shortened_url = url_shortener.shorten_url(original_url)
    assert shortened_url != original_url

def test_get_original_url(url_shortener):
    original_url = "https://www.example.com"
    shortened_url = url_shortener.shorten_url(original_url)
    assert url_shortener.get_original_url(shortened_url) == original_url

def test_shorten_same_url_twice(url_shortener):
    original_url = "https://www.example.com"
    shortened_url1 = url_shortener.shorten_url(original_url)
    shortened_url2 = url_shortener.shorten_url(original_url)
    assert shortened_url1 == shortened_url2

def test_get_non_existent_url(url_shortener):
    non_existent_url = "https://www.non-existent.com"
    with pytest.raises(ValueError):
        url_shortener.get_original_url(non_existent_url)
