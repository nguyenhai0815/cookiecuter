import os
import shutil
import subprocess

types = "{{ cookiecutter.component_types }}".replace(" ", "").split(",")

base_path = os.path.join(os.getcwd(), "{{ cookiecutter.project_slug }}", "Http")

if "Controller" not in types:
    controller_path = os.path.join(base_path, "Controllers")
    shutil.rmtree(controller_path, ignore_errors=True)

if "Service" not in types:
    service_path = os.path.join(base_path, "Services")
    shutil.rmtree(service_path, ignore_errors=True)

model_name = "{{ cookiecutter.model_name }}".strip()
namespace = "{{ cookiecutter.namespace_folder }}".strip()

def run_artisan(command):
    print(f"👉 Running: php artisan {command}")
    try:
        subprocess.run(f"php artisan {command}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")

# Tạo model + migration
if model_name:
    run_artisan(f"make:model {model_name} --migration")

    # Tạo FormRequest
    run_artisan(f"make:request Http/Requests/{namespace}/{model_name}Request")

    # Tạo Resource
    run_artisan(f"make:resource Http/Resources/{namespace}/{model_name}Resource")
