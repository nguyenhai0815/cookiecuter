import os
import shutil

component_type = "{{ cookiecutter.component_type }}".split(',')

if 'Controller' not in component_type:
    os.remove("app/Http/Controllers/{{cookiecutter.namespace_folder}}/{{cookiecutter.controller_name}}Controller.php")

if 'Service' not in component_type:
    os.remove("app/Http/Services/{{cookiecutter.namespace_folder}}/{{cookiecutter.controller_name}}Service.php")
