import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv() 
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")



# Check if the API key is present; if not, raise an error
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
    
)

model = OpenAIChatCompletionsModel(
    model="openai/gpt-oss-120b:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


agent = Agent(
    name="Writer Agent",
    instructions="You are a helpful assistant that writes short stories, short essay, poems etc, based on user prompts.",
)

response = Runner.run_sync(
    agent, 
    input="Write a short quotes to motivate.",
    run_config=config
)

print(response.final_output)