import subprocess


def generate_uml_diagram(code_str, output_file):
    """
    Cette méthode prend en entrée une chaîne de code Python et un nom de fichier de sortie,
    génère un diagramme de classe UML à partir du code, et le sauvegarde au format DOT dans un fichier.
    """
    # Création d'un fichier temporaire pour stocker le code Python
    tmp_file = 'tmp.py'
    with open(tmp_file, 'w') as f:
        f.write(code_str)

    # Appel à Pyreverse pour générer le diagramme UML
    cmd = f'pyreverse -o dot {tmp_file}'
    subprocess.run(cmd.split(), check=True)

    # Renommage du fichier de sortie généré par Pyreverse
    dot_file = f'{tmp_file}_dot.png'
    subprocess.run(f'mv classes.dot {dot_file}'.split(), check=True)

    # Lecture du contenu du fichier DOT
    with open(dot_file, 'r') as f:
        dot_content = f.read()

    # Sauvegarde du fichier DOT dans un fichier de sortie
    with open(output_file, 'w') as f:
        f.write(dot_content)

    # Suppression des fichiers temporaires
    subprocess.run(f'rm {tmp_file} {dot_file}'.split(), check=True)


import re

def generate_prompt(dot_file_path, code_string):
    # Ouvrir le fichier DOT et le lire en tant que chaîne de caractères
    with open(dot_file_path, "r") as dot_file:
        dot_string = dot_file.read()

    # Extraire les noms des classes et des méthodes à partir du fichier DOT
    class_names = re.findall(r"class\s+(\w+)\s+\{", dot_string)
    method_names = re.findall(r"\blabel\s+=\s+\"(\w+)\\n", dot_string)

    # Extraire les commentaires du code source
    comments = re.findall(r'""".+?"""', code_string, re.DOTALL)

    # Créer une liste de dictionnaires contenant les informations sur chaque méthode de chaque classe
    method_info = []
    for class_name in class_names:
        class_methods = []
        for method_name in method_names:
            if method_name.startswith(class_name):
                method_docstring = ""
                for comment in comments:
                    if method_name in comment:
                        method_docstring = comment.strip('"""').strip()
                        break
                class_methods.append({
                    "name": method_name,
                    "docstring": method_docstring
                })
        method_info.append({
            "class_name": class_name,
            "methods": class_methods
        })

    # Générer le prompt à partir des informations extraites
    prompt = ""
    for class_info in method_info:
        prompt += f"La classe {class_info['class_name']} a les méthodes suivantes :\n"
        for method in class_info["methods"]:
            prompt += f"- {method['name']}: {method['docstring']}\n"
        prompt += "\n"

    return prompt
