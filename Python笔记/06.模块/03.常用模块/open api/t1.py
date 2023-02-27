import openai

openai.api_key = "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"


def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                           temperature=0.5, )

    message = completions.choices[0].text
    print(message)


# askChatGPT("你知道西游记吗")

while True:
    problem = input('输入你的问题: ')
    askChatGPT(question=problem)
