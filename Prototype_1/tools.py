import os


# base directory where the agent is allowed to work

WORKSPACE_ROOT= "workspace"


def create_directory(path:str):
    '''
    safely create a directory inside the workspace

    '''

    full_path = os.path.join(WORKSPACE_ROOT,path)
    os.makedirs(full_path,exist_ok=True)
    print(f"[TOOL] Directory created:{full_path}")


def write_file(path:str,content: str):
    '''
    safely crate/ write a file inside the workspace (ex:main.py)
    '''

    full_path = os.path.join(WORKSPACE_ROOT, path)

    # ensuring parent directory exits
    os.makedirs(os.path.dirname(full_path),exist_ok=True)

    with open(full_path,"w",encoding="utf-8") as f:
        f.write(content)

    print(f"[TOOLS] File written:{full_path}")

    