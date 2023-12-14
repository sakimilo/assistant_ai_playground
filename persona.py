from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import yaml

with open("config/config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def compose_poem():
    try:
        client = OpenAI()
        completion = client.chat.completions.create(
        model=config["general_config"]["openai_config"]["model_name"],
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
        )
        return completion.choices[0].message.content
    
    except Exception as e:
        return "failed"

def calculate_math():
    try:
        interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
                                    name="langchain assistant",
                                    instructions="""
                                        You are a personal math tutor. 
                                        When asked a question, write and run Python code to answer the question.
                                    """,
                                    tools=[{"type": "code_interpreter"}],
                                    model=config["general_config"]["openai_config"]["model_name"]
                                )
        output = interpreter_assistant.invoke({"content": "Work out the sum of 1, 2 and 3"})
        return output[0].content[0].text.value
    
    except Exception as e:
        return "failed"

if __name__ == "__main__":

    pass