from tools import create_directory , write_file



def agent_decide(task: str):
    """
    Simulated LLM output.
    In real systems, this would come from an LLM.
    """

    if "python hello world project" in task.lower():
        return [
            {
                "tool": "create_directory",
                "args": {"path": "hello_project"}
            },
            {
                "tool": "write_file",
                "args": {
                    "path": "hello_project/main.py",
                    "content": (
                        "def main():\n"
                        "    print('Hello, World from Agent!')\n\n"
                        "if __name__ == '__main__':\n"
                        "    main()\n"
                    )
                }
            }
        ]

    return []




def run_agent(task: str):
    """
    Executes the agent plan step by step.
    """
    print(f"[AGENT] Task received: {task}")

    actions = agent_decide(task)

    for step, action in enumerate(actions, start=1):
        tool = action["tool"]
        args = action["args"]

        print(f"[AGENT] Step {step}: Calling tool '{tool}'")

        if tool == "create_directory":
            create_directory(**args)

        elif tool == "write_file":
            write_file(**args)

        else:
            print(f"[AGENT] Unknown tool: {tool}")


if __name__ == "__main__":
    user_task = "Create a python hello world project"
    run_agent(user_task)