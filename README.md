# Auto-Docstring-python-file
This repository allows to auto document a python file via GPT_3-5 by dividing the code by functions and methods. It then creates a succinct summary of all the code

Linux:
Create an environnement conda:
```
conda create --name comment python=3.7
```

Active environnement:
```
conda activate comment
```

Install all dependency:
```
pip install openai
pip install autopep8
```

OpenAI:
You must have openaiKey to use this program. 
Create openAI_key.txt file in the same folder of comment_py_file.py, paste your openAIkey and save it

Principle:
When the program is run, 3 folders are created if missing: Push_code_here where the code to be commented will be deposited, Original where a copy of each code before modification will be copied and Modified where the commented code will be created.
The program looks for the presence of file in Push_code_here every 2 seconds. When a file is dropped, it copies it to Original, then comments it in Modified.
The program works correctly with python files, for c files, tests remain to be done.
