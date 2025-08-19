🎥 Streaming AI Agent with Gemini
This project demonstrates how to build a streaming AI agent using
Google Gemini models with an OpenAI-compatible API client.
It uses Python’s asyncio for handling streaming responses and rich for colorful terminal output.

🚀 Features
✅ Streaming AI responses in real-time
✅ Uses Google Gemini 2.0 Flash model
✅ Async implementation with Python’s asyncio
✅ Pretty printing with rich
✅ Environment variable support via .env
📂 Project Structure
. ├── main.py # Main entry point (async streaming example) ├── agents.py # Agent + Runner utilities ├── .env # Store your API key (not committed to git) └── README.md # Project documentation

yaml Copy Edit

⚙️ Installation
Clone the repository
git clone <your-repo-url>
cd <your-repo-name>
Create a virtual environment

bash Copy Edit python -m venv .venv source .venv/bin/activate # Mac/Linux .venv\Scripts\activate # Windows Install dependencies

bash Copy Edit pip install -r requirements.txt Example requirements:

txt Copy Edit openai python-dotenv rich (plus your local agents.py module)

🔑 Environment Variables Create a .env file in the project root:

env Copy Edit GEMINI_API_KEY=your_api_key_here ▶️ Usage Run the script:

bash Copy Edit python main.py If using uv:

bash Copy Edit uv run --no-cache main.py 🖥️ Example Output When you run the script, you’ll see streaming output like:

bash Copy Edit H He Hel Hell Hello, how can I help you today? (or styled text if using rich).

🛠️ Customization Change the initial prompt in main.py:

python Copy Edit result = Runner.run_streamed(agent, "Hi") 👉 Replace "Hi" with your own query.

Change the model in main.py:

python Copy Edit model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", ...)
