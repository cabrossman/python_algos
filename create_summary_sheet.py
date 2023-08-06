import os
import pandas as pd
from pathlib import Path
import re
import openai

openai.api_key = os.getenv('OPENAI_KEY')

def filter_python_code(code):
    # Remove single line comments
    code = re.sub(r'#[^\n]*', '', code)

    # Remove multi-line comments
    code = re.sub(r'"""(.*?)"""', '', code, flags=re.DOTALL)
    code = re.sub(r"'''(.*?)'''", '', code, flags=re.DOTALL)
    
    # Remove lines that include print or assert
    result = []
    lines = code.split("\n")
    for line in lines:
        stripped = line.strip()
        if 'assert' not in stripped and 'print' not in stripped:
            result.append(stripped)
    return "\n".join(result)

data = []
for folder in [d for d in os.listdir() if os.path.isdir(d)]:
    for file in Path(folder).rglob("*.py"):
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            code = f.read()
            #code = filter_python_code(code)
            data.append([folder, file.name, code])

df = pd.DataFrame(data, columns=['folder', 'file', 'code'])

# Filter rows where 'folder' starts with an uppercase letter
df = df[df['folder'].str[0].str.isupper()]

def get_chat_completion(code, sys):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": sys},
            {"role": "user", "content": '```{}```'.format(code)},
        ]
    )
    return response["choices"][0]["message"]['content']

def get_summary_for_row(row, current, total):
    SYSTEM = """
    highlight the most important step of the main algorithm to remember. 
    If more than one step list them. But only highlight what may be 
    considered the most important things to remember. Dont be verbose.  
    """
    try:
        result = get_chat_completion(str(row), SYSTEM)
        print(f"Row {current} of {total}: Successfully fetched summary for file {row['file']} in folder {row['folder']}")
    except Exception as e:
        print(f"Row {current} of {total}: Error fetching summary for file {row['file']} in folder {row['folder']}: {e}")
        result = None  # or return an appropriate default value
    return result

def get_problem_for_row(row, current, total):
    SYSTEM = """
    Write a summary of the problem the algorithm is attempting to solve. 
    Dont be verbose. Summarize in 1-3 sentences For example here is a great output:
    ```Given an integer array nums of length n and an integer target, 
    find three integers in nums such that the sum is closest to target.```
    """
    try:
        result = get_chat_completion(str(row), SYSTEM)
        print(f"Row {current} of {total}: Successfully fetched summary for file {row['file']} in folder {row['folder']}")
    except Exception as e:
        print(f"Row {current} of {total}: Error fetching summary for file {row['file']} in folder {row['folder']}: {e}")
        result = None  # or return an appropriate default value
    return result

total_rows = df.shape[0]
df['summary'] = [get_summary_for_row(row, i+1, total_rows) for i, row in df.iterrows()]
df['problem'] = [get_problem_for_row(row, i+1, total_rows) for i, row in df.iterrows()]
df.drop('code', axis=1, inplace=True)
df.to_csv('summary.csv', index=False)