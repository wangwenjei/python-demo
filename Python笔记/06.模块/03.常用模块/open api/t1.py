#!/usr/bin/env python3

# Import open AI OS and System Modules
import openai, os, sys

prompt = sys.argv[1]
openai.api_key = os.environ['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']

completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)
