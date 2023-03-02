# -*-*-*-真正的ChatGPT, GPT-3.5版。-*-*-*-

import os
import openai
from tenacity import retry, stop_after_attempt, wait_random  # for exponential backoff

openai.api_key = "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"

print("if you want to stop the conversation, please input 'quit'")  # 提示想终止聊天时输入"quit"


@retry(stop=stop_after_attempt(8), wait=wait_random(min=1, max=5))  # 反复提交问题，这里指定提交6次,每次等待1-3秒。可根据自己情况修改。
def chat(prompt):
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


text = ""  # 设置一个字符串变量
turns = []  # 设置一个列表变量，turn指对话时的话轮
while True:  # 能够连续提问
    question = input(">>>You: ")
    if len(question.strip()) == 0:  # 如果输入为空，提醒输入问题
        print("please input your question")
    elif question.lower() == "quit":  # 如果输入为"quit"，程序终止
        print(">>>AI: See You Next Time!")
        break
    else:
        prompt = text + "\n" + question
        if len(prompt) <= 2000:  # 避免撑爆。ChatGpt API最大处理1500个词左右: prompt+completion不能超过2048个token，约1500个自然词。
            result = chat(prompt)
        else:
            result = chat(prompt[-2000:])  # 因为len(prompt)算的是字符数,2000这个字符数可以自己调整，估计不超过5000一般都可以。
        turns += [question] + [result]  # 只有这样迭代才能连续提问理解上下文
        print(">>>AI:", result)
        if len(turns) <= 6:  # 指定一定的话轮语境以保证对话的连续性，这里指定为6次。你可以根据实际情况修改。
            text = " ".join(turns)
        else:
            text = " ".join(turns[-6:])
