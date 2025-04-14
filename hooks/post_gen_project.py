import os
import shutil

types = "{{ cookiecutter.component_types }}".replace(" ", "").split(",")

base_path = os.path.join(os.getcwd(), "{{ cookiecutter.project_slug }}", "Http")

if "Controller" not in types:
    controller_path = os.path.join(base_path, "Controllers")
    shutil.rmtree(controller_path, ignore_errors=True)

if "Service" not in types:
    service_path = os.path.join(base_path, "Services")
    shutil.rmtree(service_path, ignore_errors=True)
