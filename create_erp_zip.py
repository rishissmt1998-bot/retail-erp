import zipfile
import os

project_name = "retail_erp"
folders = [
    f"{project_name}/inventory",
    f"{project_name}/sales",
    f"{project_name}/customers",
    f"{project_name}/users",
    f"{project_name}/templates",
    f"{project_name}/static",
]

files = {
    f"{project_name}/manage.py": "# Django manage.py placeholder",
    f"{project_name}/{project_name}/__init__.py": "",
    f"{project_name}/{project_name}/settings.py": "# Django settings.py placeholder",
    f"{project_name}/{project_name}/urls.py": "# Django urls.py placeholder",
    f"{project_name}/{project_name}/wsgi.py": "# Django wsgi.py placeholder",
    f"{project_name}/{project_name}/asgi.py": "# Django asgi.py placeholder",
    f"{project_name}/requirements.txt": "Django>=4.2\ngunicorn\npsycopg2-binary\nwhitenoise",
    f"{project_name}/Procfile": "web: gunicorn retail_erp.wsgi",
    f"{project_name}/runtime.txt": "python-3.11.9",
    f"{project_name}/README.md": "# Dharma Data Center Retail ERP\n\nRetail ERP built with Django.",
}

zip_filename = f"{project_name}_starter.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        zipf.write(folder, folder)
    for filepath, content in files.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)
        zipf.write(filepath)

print(f"✅ Created ZIP file: {zip_filename}")
