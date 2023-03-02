import openai
from tenacity import retry, stop_after_attempt, wait_random

openai.api_key = "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"


@retry(stop=stop_after_attempt(6), wait=wait_random(min=1, max=3))
def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine,
                                           prompt=prompt,
                                           max_tokens=4096,
                                           n=1,
                                           stop=None,
                                           temperature=0.5,
                                           )

    message = completions.choices[0].text

    if len(message) != 0:
        return message
    else:
        raise Exception


@retry(stop=stop_after_attempt(8), wait=wait_random(min=1, max=5))  # 反复提交问题，这里指定提交6次,每次等待1-3秒。可根据自己情况修改。
def ChatGPT_turbo(question):
    prompt = question
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content'].strip()
        if len(answer) != 0:  # 避免返回空白
            return answer
        else:
            raise Exception
    except Exception as e:
        print(e)
