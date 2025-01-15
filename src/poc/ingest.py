from loguru import logger
import json
from typing import Dict, List
import asyncio

from agents.ingest_agents import setup_agents


async def load_sources() -> Dict:
    """Load sources from JSON configuration."""
    try:
        with open('./input/sources.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"❌ Failed to load sources: {e}")
        raise

async def ingest_sources() -> List[Dict]:
    """Ingest data from configured sources using web tools and autogen agents."""
    logger.debug("📖 Loading source configurations")
    sources = await load_sources()
    
    logger.info("🤖 Initializing autogen agents")
    team = setup_agents()
    
    results = []
    for source in sources['sources']:
        logger.info(f"📡 Processing source: {source['Name']}")
       
        try:
            await team.run(task=f"""
            Get the content from the following {source}, summarize the content and store the summary as a file in the _data folder
            """)
            await team.reset()
            logger.info(f"✅ Completed analysis for: {source['Name']}")
            
        except Exception as e:
            logger.error(f"❌ Failed to process {source['Name']}: {e}")
            results.append({
                'source': source['Name'],
                'url': source['URL'],
                'status': 'failed',
                'error': str(e)
            })
    
    return results
