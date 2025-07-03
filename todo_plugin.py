# todo_plugin.py

"""
ToDo Plugin for Semantic Kernel

This module provides a plugin for managing to-do tasks through Semantic Kernel.
The plugin offers functions for adding, listing, and removing tasks from a simple
in-memory task list.

The plugin is designed to be used with Microsoft Semantic Kernel's function calling
capabilities, allowing AI agents to manage tasks through natural language interactions.

Features:
- Add new tasks to the to-do list
- List all current tasks with numbered indices
- Remove tasks by their index number
- In-memory task storage (tasks are lost when the application restarts)

Usage:
    The plugin is automatically registered with the kernel in agent.py and can be
    invoked by the AI agent when users request task management operations.
"""

from semantic_kernel.functions import kernel_function


class ToDoPlugin:
    """
    A Semantic Kernel plugin for managing to-do tasks.
    
    This class provides kernel functions that can be called by AI agents to
    perform task management operations. The tasks are stored in memory and
    will be lost when the application is restarted.
    
    Attributes:
        tasks (list): A list of strings representing the current tasks
    """
    
    def __init__(self):
        """
        Initialize the ToDoPlugin with an empty task list.
        
        Creates a new instance of the plugin with an empty list to store tasks.
        """
        self.tasks = []

    @kernel_function(
        name="AddTask",
        description="Add a new task to the to-do list"
    )
    def add_task(self, task: str) -> str:
        """
        Add a new task to the to-do list.
        
        This function appends the provided task to the internal task list
        and returns a confirmation message.
        
        Args:
            task (str): The task description to add to the list
            
        Returns:
            str: A confirmation message indicating the task was added
            
        Example:
            >>> plugin = ToDoPlugin()
            >>> plugin.add_task("Buy groceries")
            'Task added: "Buy groceries"'
        """
        self.tasks.append(task)
        return f'Task added: "{task}"'

    @kernel_function(
        name="ListTasks",
        description="List all tasks in the to-do list"
    )
    def list_tasks(self) -> str:
        """
        List all current tasks in the to-do list.
        
        This function returns a formatted string containing all tasks with
        their corresponding indices (starting from 1). If no tasks exist,
        it returns a message indicating the list is empty.
        
        Returns:
            str: A formatted string listing all tasks with indices, or
                 "No tasks yet!" if the list is empty
                 
        Example:
            >>> plugin = ToDoPlugin()
            >>> plugin.add_task("Task 1")
            >>> plugin.add_task("Task 2")
            >>> plugin.list_tasks()
            '1. Task 1\n2. Task 2'
        """
        if not self.tasks:
            return "No tasks yet!"
        return "\n".join(f"{idx+1}. {t}" for idx, t in enumerate(self.tasks))

    @kernel_function(
        name="RemoveTask",
        description="Remove a task by its index (starting at 1)"
    )
    def remove_task(self, index: int) -> str:
        """
        Remove a task from the to-do list by its index.
        
        This function removes the task at the specified index (1-based indexing)
        and returns a confirmation message. If the index is invalid, it returns
        an error message.
        
        Args:
            index (int): The 1-based index of the task to remove
            
        Returns:
            str: A confirmation message with the removed task, or
                 "Invalid task index!" if the index is out of range
                 
        Example:
            >>> plugin = ToDoPlugin()
            >>> plugin.add_task("Task to remove")
            >>> plugin.remove_task(1)
            'Removed task: "Task to remove"'
        """
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            return f'Removed task: "{removed}"'
        return "Invalid task index!"
