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
from openai import OpenAI
import json
```

```python

```

```python
client = OpenAI()
```

```python

```

```python
student_1_description = """
David Nguyen is a sophomore majoring in computer science at Stanford University. 
He is Asian American and has a 3.8 GPA. 
David is known for his programming skills and is an active member of the university's Robotics Club. 
He hopes to pursue a career in artificial intelligence after graduating."""
```

```python
# A simple prompt to extract information from "student_description" in a JSON format.
prompt1 = f'''
Please extract the following information from the given text and return it as a JSON object:

name
major
school
grades
club

This is the body of text to extract the information from:
{student_1_description}
'''
```

```python
prompt1
```

```python

```

```python
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt1}]
)
openai_response.choices[0].message.content
```

```python
json_response = json.loads(openai_response.choices[0].message.content)
json_response
```

```python

```

```python
student_2_description="""
Ravi Patel is a sophomore majoring in computer science at the University of Michigan. 
He is South Asian Indian American and has a 3.7 GPA. 
Ravi is an active member of the university's Chess Club and the South Asian Student Association. 
He hopes to pursue a career in software engineering after graduating."""
```

```python
prompt2 = f'''
Please extract the following information from the given text and return it as a JSON object:

name
major
school
grades
club

This is the body of text to extract the information from:
{student_2_description}
'''
```

```python
prompt2
```

```python

```

```python

```

```python
openai_response_2 = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt2}]
)
openai_response_2.choices[0].message.content
```

```python
json_response = json.loads(openai_response_2.choices[0].message.content)
json_response
```

```python

```

```python

```

```python
student_custom_functions = [
    {
        'name': 'extract_student_info',
        'description': 'Get the student information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person'
                },
                'major': {
                    'type': 'string',
                    'description': 'Major subject.'
                },
                'school': {
                    'type': 'string',
                    'description': 'The university name.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                },
                'club': {
                    'type': 'string',
                    'description': 'School club for extracurricular activities. '
                }
                
            }
        }
    }
]
```

```python
sample
```

```python
student_description = [prompt1, prompt2]
for sample in student_description:
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role': 'user', 'content': sample}],
        functions = student_custom_functions,
        function_call = 'auto'
    )
    json_response = json.loads(response.choices[0].message.function_call.arguments)
    print(json_response)
```

```python

```

```python

```
