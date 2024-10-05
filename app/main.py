import subprocess

if __name__ == "__main__":
    subprocess.run(["uvicorn", "main:app", "--reload", "--port", "8000"])
    

