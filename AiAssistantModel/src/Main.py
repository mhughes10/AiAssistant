from SourceMaterial import inaapInfo
from openai import OpenAI

client = OpenAI()

question = ""

while question != "quit":
    question = input("(enter prompt / 'quit' to exit): ")
    if question != "quit":
        prompt = f"""Use the below manual on the Packetalk Inaap System to answer the subsequent question. Try to include where and how in your response. If the answer cannot be found, write "I'm not sure. Please specify.".

        Manual:
        \"\"\
        {inaapInfo()}
        \"\"\
        
        Question: {question}
        """
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": "you are a helpful assistant."},
                {"role": "user",
                 "content": f"{prompt}"}],
            temperature= 0.5)
        #display(Markdown(response.choices[0].message.content))
        print(response.choices[0].message.content)