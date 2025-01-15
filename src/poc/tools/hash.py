from loguru import logger
import hashlib

def get_url_hash(url: str) -> str:
    """
    Generate a unique hash for a URL.
    
    Args:
        url: URL to hash
        
    Returns:
        str: MD5 hash of the URL
    """
    return hashlib.md5(url.encode('utf-8')).hexdigest() 