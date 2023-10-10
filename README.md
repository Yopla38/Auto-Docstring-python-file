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
Open openAI_key.txt file and paste your openAIkey string, save it

Run:
python comment_py_file.py

Principle:
Usage : 
        
        simple file : python comment_py_file.py -f path_of_py_file_to_comment
        watchdog : python comment_file_py.py 
                    When the program is run, 3 folders are created if missing: Push_code_here where the 
                    code to be commented will be deposited (can be folder), Original where a copy of each code and file 
                    before modification will be copied and Modified where the commented code will be created.
                    The program looks for the presence of file in Push_code_here every 2 seconds. When 
                    a file is dropped, it copies it to Original, then comments it in Modified.
                    The program works correctly with python files, for c files, tests remain to be done.
                    Other parameters : -o copy_folders
                                       -m modified_folder
                                       -p push_folder
