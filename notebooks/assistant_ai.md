---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from openai import OpenAI
```

```python
import yaml

with open("../config/config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
```

```python

```

## Parameters

```python
to_cleanup = False
to_reset_agents = False
to_reset_thread = False

assistant_id = config["general_config"]["openai_config"]["assistant_id"]
file_id = config["general_config"]["openai_config"]["file_id"]
thread_id = config["general_config"]["openai_config"]["thread_id"]

knowledge_file = config["general_config"]["openai_config"]["knowledge_file"]
description = config["general_config"]["openai_config"]["description"]
instructions = config["general_config"]["openai_config"]["instructions"]
```

```python

```

```python
client = OpenAI()
```

```python
def get_messages(thread, run=None):
    if run is not None:
        run = client.beta.threads.runs.retrieve(
          thread_id=thread.id,
          run_id=run.id
        )
    
    if run is not None or \
       run.status == "completed":
        
        messages = client.beta.threads.messages.list(
          thread_id=thread.id
        )
        for d in messages.data[::-1]:
            print(d.role, ":", d.content[0].text.value)
            print("")
```

```python

```

```python
for d in client.beta.assistants.list().data:
    print(d.id)
    if to_cleanup:
        client.beta.assistants.delete(assistant_id=d.id)
```

```python
for d in client.files.list().data:
    print(d.id)
    if to_cleanup:
        client.files.delete(file_id=d.id)
```

```python

```

```python
if to_reset_agents:
    file = client.files.create(
      file=open(knowledge_file, "rb"),
      purpose='assistants'
    )
```

```python
if to_reset_agents:
    print(file)
```

```python

```

```python
if to_reset_agents:
    assistant = client.beta.assistants.create(
                    name="Study assistant",
                    description=description,
                    instructions=instructions,
                    model=config["general_config"]["openai_config"]["cutting_edge_model"],
                    tools=[{"type": "retrieval"}],
                    file_ids=[file.id]
    )
```

```python
if to_reset_agents:
    print(assistant)
```

```python

```

```python
if to_reset_agents:
    assistant_id = assistant.id
    file_id = file.id
else:
    assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)
    file = client.files.retrieve(file_id=file_id)
```

```python

```

```python
if to_reset_thread:
    thread = client.beta.threads.create(
      messages=[
        {
          "role": "user",
          "content": "Summarise knowledge base in 1 paragraph"
        }
      ]
    )
```

```python
if to_reset_thread:
    print(thread)
```

```python
if to_reset_thread:
    thread_id = thread.id
else:
    thread = client.beta.threads.retrieve(thread_id=thread_id)
```

```python

```

```python
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)
messages
```

```python

```

```python

```

```python
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Mr. Bear. The user has a premium account."
)
```

```python
get_messages(thread, run)
```

```python

```

```python
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Please come up with a multiple choice questions with 4 options, only 1 is correct. Please do not reveal the answer yet"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)
```

```python
get_messages(thread, run)
```

```python

```

```python
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is the answer of previous question"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)
```

```python
get_messages(thread, run)
```

```python

```
