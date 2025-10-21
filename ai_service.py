import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description: str) -> list[str]:
    if not client.api_key:
        return ["Error: OpenAI API key not found."]
    
    try:
        prompt = f"""Please break down the following complex task into three to five clear, actionable subtasks:
            Task: {description}

            Response format:
            - Subtask one
            - Subtask two
            - Subtask three
            (Add more subtasks if necessary)

            Response only with the subtasks list, one per line, starting with a hyphen.
        """
        params = {
            "model": "gpt-4o-mini",
            "messages":[
                {"role": "system", "content": "You are an expert task breakdown assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300
        }

        response = client.chat.completions.create(**params)

        print(response.model_dump_json(indent=2))
        choice = response.choices[0]
        if not choice.message or not choice.message.content:
            return [f"Error: assistant returned no text (finish_reason={choice.finish_reason})"]

        content = response.choices[0].message.content.strip()
        
        subtasks = []

        for line in content.split("\n"):
            line = line.strip()

            if line and line.startswith("-"):
                subtask = line[1:].strip()
                subtasks.append(subtask)

        return subtasks if subtasks else ["Error: No subtasks found in the response."]
    except Exception as e:
        return ["Error: Failed to create tasks."]