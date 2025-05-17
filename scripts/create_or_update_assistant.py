import os
from src.base.voice_agent_providers.vapi import VapiAI
from src.prompts import VOICE_AGENT_PROMPT
from dotenv import load_dotenv

load_dotenv()

# Before creating your assistant, you must first create the needed tools
# Copy their ids(str) in the list below.
# If your assistant does not require any tool, leave empty
tool_ids_list = ["b1e688dd-e6cc-48b5-bd3e-77e68bb74adb"]

assistant_config = {
    "name": "Alex",
    "transcriber": {
        "provider": "deepgram",  # Transcriber provider
        "language": "en"
    },
    "model": {
        "provider": "deep-seek",  # Changed to deepseek
        "model": "deepseek-chat",  # DeepSeek model
        "toolIds": tool_ids_list,
        "messages": [
            {
                "role": "system",
                "content": VOICE_AGENT_PROMPT
            }
        ]
    },
    "voice": {
        "provider": "openai",  # Voice provider
        "voiceId": "alloy"  # Voice ID
    },
    "first_message": "Hi, is this {{firstName}}?",
    "end_call_message": "Thanks for your time.",
    "analysis_plan": {
        "summaryPlan": {
            "messages": [],
            "enabled": False,
        },
        "structuredDataPlan": {
            "messages": [],
            "enabled": False,
        },
        "successEvaluationPlan": {
            "rubric": "NumericScale",
            "messages": [],
            "enabled": False
        }
    },
    # "server_url": f"{os.getenv('SERVER_URL')}/webhook"
}


vapi_client = VapiAI()

# Create a new assistant using the above config
output = vapi_client.create_agent(assistant_config)
print(output)

# # Get the assistant id, copy it to .env
# print(output["id"])


# Update an existing assistant with the above config
# assistant_id = "7be79d69-2156-4b65-af56-3cef98fdfd34"
# output = vapi_client.update_agent(assistant_id, assistant_config)
# print(output)