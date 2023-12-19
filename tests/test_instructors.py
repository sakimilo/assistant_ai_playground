import pydantic
import instructor
import openai
from openai import OpenAI


# Enables the response_model 
client = instructor.patch(OpenAI())

class UserDetail(pydantic.BaseModel):
    """
    This is a python object that capture user's information
    such as name, age, email address and phone number.
    """
    name: str
    age: int
    email: str
    phone_number: str
    
    def introduce(self):
        return f"Hello I'm {self.name} and I'm {self.age} years old"

def test_instructor_userdetails():

    user: UserDetail = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": "People call me Jason. I was born in year 1999."},
        ]
    )

    # Now we get a plain old python object! 
    assert user.name == "Jason"
    assert user.age == 24
    assert user.introduce() == "Hello I'm Jason and I'm 24 years old"


if __name__ == "__main__":

    user: UserDetail = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": "People call me Jason. I was born in year 1999. You can reach out to my through abc@hiz.com, or by 96811234"},
        ]
    )
    print(user)