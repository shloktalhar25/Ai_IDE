# In this file we are creating our custom tools written in the 
# form of functions . 
# Agents would call this function tools and get the things done
# this is the sandbox



import os

WORKSPACE = "workspace"

def safe_path(path):
    full =os.path.abspath(os.path.join(WORKSPACE,path))
    if not full.startswith(os.path.abspath(WORKSPACE)):
        raise Exception("security Violation")
    return full

def create_folder(path):
    full = safe_path(path)
    os.makedirs(full,exist_ok=True)
    return f"Folder Created at {path}"


def write_file(path, content):
    full = safe_path(path)

    folder = os.path.dirname(full)
    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())

    return f"File written: {path}"
