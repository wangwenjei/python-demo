# -*-*-*-改进版，尝试用tenacity库的retry修饰器，指定提交时间和次数。-*-*-*-

import os
import openai
from tenacity import retry, stop_after_attempt, wait_random

openai.api_key = "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"
print("if you want to stop the conversation, please input 'quit'")  # 提示想终止聊天时输入"quit"


@retry(stop=stop_after_attempt(6), wait=wait_random(min=1, max=3))  # 反复提交问题，这里指定提交6次,每次等待1-3秒。可根据自己情况修改。
def chat(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["Human:", "AI:"]
    )
    answer = response["choices"][0]["text"].strip()
    if len(answer) != 0:  # 避免返回空白
        return answer
    else:
        raise Exception


text = ""  # 设置一个字符串变量
turns = []  # 设置一个列表变量，turn指对话时的话轮
while True:  # 能够连续提问
    question = input(">>>You: ")
    if len(question.strip()) == 0:  # 如果输入为空，提醒输入问题
        print("please input your question")
    elif question.lower() == "quit":  # 如果输入为"quit"，程序终止
        print("\nAI: See You Next Time!")
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
