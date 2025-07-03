# 🤖 AI To-Do Manager — Semantic Kernel Plugin Example

A practical demonstration of Microsoft Semantic Kernel's plugin system, showcasing how to build an AI agent that can manage tasks through natural language interactions.

## ✨ Features

- **Natural Language Processing**: Chat with the AI using everyday language
- **Automatic Function Calling**: AI automatically invokes Python functions using Semantic Kernel plugins
- **Task Management**: Add, list, and remove tasks from a to-do list
- **Context Awareness**: Maintains conversation history for contextual responses
- **Extensible Architecture**: Foundation for building real-world AI-first applications

## 🎯 What This Demonstrates

- **Semantic Kernel Plugins**: How to create and integrate custom Python functions
- **AI Orchestration**: Combining LLMs with custom business logic
- **Function Calling**: Automatic invocation of native code based on user intent
- **Real-World Patterns**: Practical foundation for building AI Copilots

## 🏗️ Architecture Overview

```
User Input → Semantic Kernel → LLM Analysis → Plugin Function Call → Response Generation
```

The system works by:
1. User provides natural language input
2. Semantic Kernel processes the request through Azure OpenAI
3. LLM determines if a plugin function is needed
4. Plugin function executes (add/list/remove tasks)
5. Results are returned to the LLM for final response generation

## 📁 Project Structure

```
ai-todo-manager/
├── agent.py          # Main chat loop and kernel orchestration
├── todo_plugin.py    # To-Do management plugin with kernel functions
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (API keys, not committed)
└── README.md         # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Azure OpenAI service account
- Git (for cloning)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-todo-manager.git
cd ai-todo-manager
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name_here
```

**Note**: Replace the placeholder values with your actual Azure OpenAI credentials.

### 5. Run the Application

```bash
python agent.py
```

## 💬 Usage Examples

Once the application is running, you can interact with it using natural language:

```
💡 To-Do Manager is ready! Type your tasks or type 'exit' to quit.

You > I need to finish my quarterly report
Assistant > Task added: "I need to finish my quarterly report"

You > Also remind me to buy groceries tomorrow
Assistant > Task added: "Also remind me to buy groceries tomorrow"

You > What tasks do I have?
Assistant > Here are your current tasks:
1. I need to finish my quarterly report
2. Also remind me to buy groceries tomorrow

You > Remove the second task
Assistant > Removed task: "Also remind me to buy groceries tomorrow"

You > List my tasks again
Assistant > Here are your current tasks:
1. I need to finish my quarterly report
```

## 🔧 Available Plugin Functions

The `ToDoPlugin` exposes three main functions that the AI can automatically call:

### `AddTask`
- **Purpose**: Adds a new task to the to-do list
- **Trigger**: When user mentions adding, creating, or needing to do something
- **Example**: "I need to call the client" → Adds task

### `ListTasks`
- **Purpose**: Displays all current tasks with numbered indices
- **Trigger**: When user asks about current tasks, what's on the list, etc.
- **Example**: "What do I have to do?" → Lists all tasks

### `RemoveTask`
- **Purpose**: Removes a task by its index number
- **Trigger**: When user wants to delete, remove, or complete a specific task
- **Example**: "Remove task 2" → Removes the second task

## 🛠️ Technical Implementation

### Core Components

1. **Semantic Kernel**: Microsoft's AI orchestration framework
2. **Azure OpenAI**: Language model for natural language understanding
3. **Plugin System**: Custom Python functions exposed to the AI
4. **Function Calling**: Automatic invocation based on user intent

### Key Files

- **`agent.py`**: Main application logic, kernel setup, and chat loop
- **`todo_plugin.py`**: Plugin implementation with kernel functions
- **`requirements.txt`**: Project dependencies

## 🔄 Extending the Application

### Adding Persistence
```python
# In todo_plugin.py, replace in-memory storage with:
import json

def save_tasks(self):
    with open('tasks.json', 'w') as f:
        json.dump(self.tasks, f)

def load_tasks(self):
    try:
        with open('tasks.json', 'r') as f:
            self.tasks = json.load(f)
    except FileNotFoundError:
        self.tasks = []
```

### Adding Task Priorities
```python
@kernel_function(
    name="AddPriorityTask",
    description="Add a task with priority level (high, medium, low)"
)
def add_priority_task(self, task: str, priority: str) -> str:
    task_with_priority = f"[{priority.upper()}] {task}"
    self.tasks.append(task_with_priority)
    return f'Priority task added: "{task_with_priority}"'
```

### Adding Due Dates
```python
@kernel_function(
    name="AddTaskWithDueDate",
    description="Add a task with a due date"
)
def add_task_with_due_date(self, task: str, due_date: str) -> str:
    task_with_date = f"{task} (Due: {due_date})"
    self.tasks.append(task_with_date)
    return f'Task with due date added: "{task_with_date}"'
```

## 🌟 Real-World Use Cases

This pattern can be extended for various applications:

- **Database Operations**: Query and modify databases through natural language
- **API Integration**: Interact with external services and APIs
- **IoT Control**: Manage smart home devices and sensors
- **Business Processes**: Handle CRM operations, scheduling, and reporting
- **Content Management**: Create, edit, and organize digital content

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed in your virtual environment
2. **API Key Issues**: Verify your Azure OpenAI credentials in the `.env` file
3. **Deployment Name**: Confirm your Azure OpenAI deployment name is correct
4. **Network Issues**: Check your internet connection and Azure service status

### Debug Mode

Enable debug logging by modifying the logging level in `agent.py`:
```python
logging.getLogger("kernel").setLevel(logging.DEBUG)
```

## 📚 Learning Resources

- [Microsoft Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Semantic Kernel GitHub Repository](https://github.com/microsoft/semantic-kernel)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Function Calling Guide](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins/using-plugins)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Microsoft Semantic Kernel team for the excellent framework
- Azure OpenAI for providing the language model capabilities
- The open-source community for inspiration and support

---

**Happy Building! 🚀**

*Inspired by this example? Feel free to fork, remix, and build your own AI-first applications. If you write about it, please share your blog post - we'd love to see what you create!*
