#!/usr/bin/env python3
from loguru import logger
import logging

from ingest import ingest_sources
import dotenv
import asyncio
from autogen_core import TRACE_LOGGER_NAME, EVENT_LOGGER_NAME

class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Retrieve the corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find the caller from where the log message originated
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

# Clear existing handlers
logging.root.handlers = []

# Set up basic configuration for logging
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)


async def main():
    """Main entry point of the application."""
    logger.info("🚀 Starting application")
    try:
        dotenv.load_dotenv()

        logger.add("app.log", rotation="500 MB", level="DEBUG")

        # Step 1: Ingestion
        logger.info("📥 Starting ingestion phase...")
        ingest_results = await ingest_sources()
        logger.debug(f"✅ Ingestion completed with {len(ingest_results)} items")
        
        # Step 2: Reasoning (placeholder)
        logger.info("🧠 Starting reasoning phase...")
        
        # Step 3: Actions (placeholder)
        logger.info("⚡ Starting actions phase...")
        
    except Exception as e:
        logger.error(f"❌ Error occurred: {e}")
        raise
    
    logger.info("🏁 Application completed successfully")

def setup():
    """Initialize any necessary configurations or resources."""
    logger.info("🔧 Initializing application")

def cleanup():
    """Clean up any resources before program exit."""
    logger.info("🧹 Cleaning up resources")

if __name__ == "__main__":
    try:
        setup()
        asyncio.run(main())
    finally:
        cleanup()
