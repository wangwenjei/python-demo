import openai
from tenacity import retry, stop_after_attempt, wait_random

openai.api_key = "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"


@retry(stop=stop_after_attempt(6), wait=wait_random(min=1, max=3))
def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine,
                                           prompt=prompt,
                                           max_tokens=1024,
                                           n=1,
                                           stop=None,
                                           temperature=0.5, )

    message = completions.choices[0].text

    if len(message) != 0:
        return message
    else:
        raise Exception
