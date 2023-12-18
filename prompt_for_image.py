from openai import OpenAI

client = OpenAI()

if False:
    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1
    )
elif False:
    response = client.images.edit(
        model="dall-e-2",
        image=open("./images/image_without_flamingo.png", "rb"),
        mask=open("./images/image_with_mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo",
        n=1,
        size="1024x1024"
    )
else:
    response = client.images.create_variation(
        image=open("./images/winnie_the_pooh.png", "rb"),
        n=2,
        size="1024x1024"
    )

image_url = response.data[0].url
print(image_url)