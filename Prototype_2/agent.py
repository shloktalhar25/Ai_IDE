# in this file we are going to write the code for agent
# which would make use of llm brain(call_llm() function) 
# and connect it with appropriate tool to perform work
print("agent file loaded")

import json
from llm import call_llm
from tools import create_folder, write_file




#This tells the LLM how to behave.
SYSTEM_PROMPT = """
You are a coding agent
You are allowed to use only these tools:

create_folder(path)
write_file(path,content)

You must respond ONLY in valid JSON
You must output a list of action.


Example:
[
  {
    "tool": "create_folder",
    "args": {"path": "backend"}
  },
  {
    "tool": "write_file",
    "args": {
      "path": "backend/main.py",
      "content": "print('hello')"
    }
  }
]


"""


# AGENT EXECUTER 

SYSTEM_PROMPT = SYSTEM_PROMPT
 
def run_agent(user_prompt):
    plan_text =call_llm(SYSTEM_PROMPT,user_prompt)

    print("\nLLM PLAN",plan_text)

    actions = json.loads(plan_text)

    for i, action in enumerate(actions,1):
        tool = action["tool"]
        args = action["args"]

        print(f"\n Step{i} {tool}")

        print("TOOL =", tool)
        print("ARGS =", args)

        if tool == "create_folder":
            result = create_folder(**args)
        elif tool == "write_file":
            result = write_file(**args)
        else:
            result = "Unknown tool"

        print("RESULT =", result)


if __name__ == "__main__":
    user_prompt = input("Enter your request:")
    run_agent(user_prompt)


