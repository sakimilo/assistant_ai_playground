import pydantic
import instructor
import openai
from openai import OpenAI


# Enables the response_model 
client = instructor.patch(OpenAI())

class UserDetail(pydantic.BaseModel):
    name: str
    age: int
    
    def introduce(self):
        return f"Hello I'm {self.name} and I'm {self.age} years old"

def test_instructor_userdetails():

    user: UserDetail = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": "Extract Jason is 25 years old"},
        ]
    )

    # Now we get a plain old python object! 
    assert user.name == "Jason"
    assert user.age == 25
    assert user.introduce() == "Hello I'm Jason and I'm 25 years old"
