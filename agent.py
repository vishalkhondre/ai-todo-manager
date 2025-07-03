"""
To-Do Manager Agent

This module implements an AI-powered to-do list manager using Microsoft Semantic Kernel.
The agent can interact with users to create, manage, and track tasks through natural language.

Features:
- Azure OpenAI integration for natural language processing
- Function calling capabilities for task management
- Persistent chat history for context-aware conversations
- ToDo plugin integration for task operations

Dependencies:
- semantic_kernel: Microsoft's AI orchestration framework
- azure-openai: Azure OpenAI service integration
- python-dotenv: Environment variable management
"""

import asyncio
import logging
import os

from dotenv import load_dotenv

# Semantic Kernel imports for AI orchestration
from semantic_kernel import Kernel
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.chat_history import ChatHistory

# Azure-specific execution settings for function calling
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

# Local plugin for to-do operations
from todo_plugin import ToDoPlugin


async def main():
    """
    Main function that orchestrates the To-Do Manager agent.
    
    This function:
    1. Loads environment variables for Azure OpenAI configuration
    2. Sets up logging for debugging and monitoring
    3. Initializes the Semantic Kernel with Azure OpenAI service
    4. Registers the ToDo plugin for task management functions
    5. Configures function calling behavior for automatic plugin invocation
    6. Starts an interactive conversation loop with the user
    
    Environment Variables Required:
        AZURE_OPENAI_DEPLOYMENT_NAME: Azure OpenAI deployment name
        AZURE_OPENAI_API_KEY: Azure OpenAI API key
        AZURE_OPENAI_ENDPOINT: Azure OpenAI endpoint URL
    
    Returns:
        None
    """
    # Load environment variables from .env file
    load_dotenv()

    # Configure logging for debugging and monitoring
    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    # Initialize the Semantic Kernel instance
    kernel = Kernel()

    # Configure and add Azure OpenAI chat completion service
    # This service handles natural language processing and response generation
    chat_completion = AzureChatCompletion(
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )
    kernel.add_service(chat_completion)

    # Register the ToDo plugin to enable task management functions
    # The plugin provides functions like add_task, list_tasks, complete_task, etc.
    kernel.add_plugin(ToDoPlugin(), plugin_name="ToDo")

    # Configure execution settings to enable automatic function calling
    # This allows the AI to automatically invoke plugin functions when needed
    execution_settings = AzureChatPromptExecutionSettings()
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    # Initialize chat history to maintain conversation context
    # This enables the AI to remember previous interactions and provide contextual responses
    history = ChatHistory()

    # Display welcome message and instructions
    print("💡 To-Do Manager is ready! Type your tasks or type 'exit' to quit.\n")

    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You > ")

        # Check for exit command
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Add user message to conversation history
        history.add_user_message(user_input)

        # Generate AI response using the configured kernel and execution settings
        # The AI can automatically call ToDo plugin functions based on user input
        result = await chat_completion.get_chat_message_content(
            chat_history=history,
            settings=execution_settings,
            kernel=kernel,
        )

        # Display AI response and add to conversation history
        print("Assistant >", str(result))
        history.add_message(result)


if __name__ == "__main__":
    # Run the main function asynchronously
    asyncio.run(main())
