from loguru import logger

from tools import download_url_content, get_url_hash, store_content
import asyncio

from autogen_agentchat.agents import UserProxyAgent, AssistantAgent
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient



# Create an OpenAI model client.



def setup_agents() -> MagenticOneGroupChat:
    """Setup autogen agents for content fetching and analysis."""

    model_client = AzureOpenAIChatCompletionClient(
        model="gpt-4o",
    )

    researcher = AssistantAgent(
        name="ResearchCoordinator",
        description="Coordinates a research effort",
        model_client=model_client,
        system_message="""
        You are the Research Coordinator Agent. Your responsibilities include:
            1. Coordinating with the WebScraper Agent to download specified web content.
            2. Collaborating with the Summarizer Agent to condense the downloaded content.
            3. Ensuring the summarized content is stored appropriately in the designated data folder.
            Maintain clear communication with each agent, monitor the progress of each task, and handle any issues that arise during the process.
        """
    )

    scraper = MultimodalWebSurfer(
        name="webscraper_agent",
        description="Web researcher",        
        model_client=model_client,
    )

    summarizer = AssistantAgent(
        name="content_summarizer",
        description="Content summarizer and archiver",        
        tools=[get_url_hash, store_content],
        model_client=model_client,
        system_message=""" 
            You are the Summarizer Agent. Your responsibilities include:
            1. Receiving raw content from the WebScraper Agent.
            2. Generating concise and accurate summaries of the provided content.
            3. Ensuring that the summaries capture the essential information and main points.
            4. Store this summary content with a filename that is a hash of the URL
            4. Communicating any challenges encountered during the summarization process promptly.
            Upon completing a summarization task, respond with 'TERMINATE' to indicate completion.
        """
    )

    user = UserProxyAgent(
        name="user",
    )

    text_termination = TextMentionTermination("APPROVE")
    team = MagenticOneGroupChat([researcher, scraper, summarizer, user], termination_condition=text_termination, model_client=model_client)
    return team
