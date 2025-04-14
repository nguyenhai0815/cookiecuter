import os
import shutil
from pathlib import Path

component_types = '{{ cookiecutter.component_type }}'.replace('[', '').replace(']', '').replace("'", "").split(', ')
namespace = '{{ cookiecutter.namespace_folder }}'
controller_name = '{{ cookiecutter.controller_name }}'

base_path = Path.cwd()

def create_file(from_template, to_path):
    with open(from_template, 'r') as f:
        content = f.read()

    content = content.replace('{{ namespace_folder }}', namespace).replace('{{ controller_name }}', controller_name)
    os.makedirs(os.path.dirname(to_path), exist_ok=True)
    with open(to_path, 'w') as f:
        f.write(content)

if 'Controller' in component_types:
    create_file(
        'templates/controller.stub',
        f'app/Http/Controllers/{namespace}/{controller_name}Controller.php'
    )

if 'Service' in component_types:
    create_file(
        'templates/service.stub',
        f'app/Http/Services/{namespace}/{controller_name}Service.php'
    )
