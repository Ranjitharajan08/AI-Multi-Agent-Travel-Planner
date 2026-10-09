import os

def save_output(filename, content):
    os.makedirs("reports", exist_ok=True)

    with open(f"reports/{filename}", "w", encoding="utf-8") as file:
        file.write(content)