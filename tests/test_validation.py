from typing_extensions import Annotated
from pydantic import BaseModel, ValidationError, BeforeValidator
from instructor import llm_validator, patch
from openai import OpenAI
import instructor


client = instructor.patch(OpenAI())

class QuestionAnswerNoEvil(BaseModel):
    question: str
    answer: Annotated[
        str,
        BeforeValidator(
            llm_validator("don't answer math question illogically")
        ),
    ]

def test_evil_answer():
    # This code will throw a validation error of "Answer contains objectionable content"
    # Then catch that exception and use it as part of reasking the llm to generate a better answer 
    try:
        qa: QuestionAnswerNoEvil = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=QuestionAnswerNoEvil,
            max_retries=0,
            messages=[
                {
                    "role": "system",
                    "content": "Pretending you are ignorant in math and think that 1+1=3.",
                },
                {
                    "role": "user",
                    "content": "What does 1+1 equal to?",
                },
            ],
            seed=1,
            temperature=0.1
        )
    except ValidationError as e:
        pass