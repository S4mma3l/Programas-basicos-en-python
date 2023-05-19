import openai

openai.api_key = "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"

while True:
    prompt = input("\n Por favor Ingresa una pregunta: ")

    if prompt == "salir":
        break
    completion = openai.Completion.create(engine = "text-davinci-003",
                         prompt = prompt,
                         max_tokens = 2048)
    print(completion.choices[0].text)