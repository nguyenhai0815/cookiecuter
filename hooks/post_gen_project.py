import os
import shutil
import subprocess

# Lấy các component types từ Cookiecutter
types = "{{ cookiecutter.component_types }}".replace(" ", "").split(",")

# Đặt đường dẫn thư mục gốc của dự án Laravel
base_path = os.path.join(os.getcwd(), "app", "Http")

# Xoá thư mục Controllers nếu không chọn Controller
if "Controller" not in types:
    controller_path = os.path.join(base_path, "Controllers", "{{ cookiecutter.namespace_folder }}")
    shutil.rmtree(controller_path, ignore_errors=True)

# Xoá thư mục Services nếu không chọn Service
if "Service" not in types:
    service_path = os.path.join(base_path, "Services", "{{ cookiecutter.namespace_folder }}")
    shutil.rmtree(service_path, ignore_errors=True)

# Lấy tên model và namespace từ cookiecutter
model_name = "{{ cookiecutter.model_name }}".strip()
namespace = "{{ cookiecutter.namespace_folder }}".strip()

def run_artisan(command):
    print(f"👉 Running: php artisan {command}")
    try:
        laravel_root = os.getcwd()  # hoặc chỉ rõ path cụ thể nếu cần
        subprocess.run(f"php artisan {command}", shell=True, check=True, cwd=laravel_root)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")

# Lệnh tạo Model và Migration
run_artisan(f"make:model {model_name} --migration")

# Lệnh tạo Request trong thư mục Admin
run_artisan(f"make:request {namespace}/{model_name}Request")

# Lệnh tạo Resource trong thư mục Admin
run_artisan(f"make:resource {namespace}/{model_name}Resource")
