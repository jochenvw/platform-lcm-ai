from loguru import logger
from pathlib import Path
from .hash import get_url_hash
from typing import Optional

def store_content(content: str, url: str) -> Optional[str]:
    """
    Store content with URL-based filename and return the path.
    
    Args:
        content: Content to store
        url: Source URL used for filename generation
        
    Returns:
        str: Path where content was stored, None if failed
    """
    try:
        # Generate filename from URL hash
        filename = f"{get_url_hash(url)}.txt"
        filepath = Path("_data") / filename
        
        # Create directory if it doesn't exist
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # Write content to file
        logger.debug(f"📝 Writing content to: {filepath}")
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
            
        logger.debug(f"✅ Successfully wrote to: {filepath}")
        return str(filepath)
        
    except Exception as e:
        logger.error(f"❌ Failed to store content for {url}: {e}")
        return None 