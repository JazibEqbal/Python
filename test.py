# s = ' #hello'
# x = s.strip('#')
# print(x)
# print(len(x))
# print(len(s))


import ast
import os

directory = r"/home/jazib-eqbal/PycharmProjects/Python"

for filename in os.listdir(directory):
    if filename.endswith(".py"):
        filepath = os.path.join(directory, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                tree = ast.parse(file.read(), filename=filename)

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    print(node.name)

        except Exception as e:
            print(f"Error reading {filename}: {e}")