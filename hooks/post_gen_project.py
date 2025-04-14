import os
import shutil
from pathlib import Path

from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import FailedHookException

def render_and_write(template_file, target_path, context):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)

    content = template.render(cookiecutter=context)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w') as f:
        f.write(content)

component_type = '{{ cookiecutter.component_type }}'
namespace_folder = '{{ cookiecutter.namespace_folder }}'
controller_name = '{{ cookiecutter.controller_name }}'

context = {
    'namespace_folder': namespace_folder,
    'controller_name': controller_name
}

# Normalize for loop
types = [c.strip() for c in component_type.split(',')]

if 'Controller' in types:
    render_and_write(
        'controller.stub',
        f'app/Http/Controllers/{namespace_folder}/{controller_name}Controller.php',
        context
    )

if 'Service' in types:
    render_and_write(
        'service.stub',
        f'app/Http/Services/{namespace_folder}/{controller_name}Service.php',
        context
    )
