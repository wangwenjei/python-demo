import openai
from tenacity import retry, stop_after_attempt, wait_random
import json

openai.api_key = "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"


@retry(stop=stop_after_attempt(6), wait=wait_random(min=1, max=3))
def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                           temperature=0.5, )
    message = json.dumps(completions.choices[0].text, ensure_ascii=False)
    return message
