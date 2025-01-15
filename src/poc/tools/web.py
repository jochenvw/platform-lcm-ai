from loguru import logger
import requests
from bs4 import BeautifulSoup
from typing import Optional

def download_url_content(url: str) -> Optional[str]:
    """
    Download content from a given URL.
    
    Args:
        url: The URL to download content from
        
    Returns:
        str: The content of the URL if successful, None if failed
    """
    try:
        logger.debug(f"🌐 Downloading content from: {url}")
        response = requests.get(url)
        response.raise_for_status()


        soup = BeautifulSoup(response.content, 'html.parser')

        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text
        
    except Exception as e:
        logger.error(f"❌ Failed to download from {url}: {e}")
        return None


