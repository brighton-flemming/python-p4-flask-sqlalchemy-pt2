import os
import pkgutil

def list_packages_and_modules(directory):
    packages = []
    modules = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                module_name = os.path.splitext(file)[0]
                modules.append(module_name)

        for dir in dirs:
            package_name = os.path.relpath(os.path.join(root, dir), directory).replace(os.sep, '.')
            packages.append(package_name)

    return packages, modules

if __name__ == "__main__":
    target_directory = "/home/brighton/python-p4-flask-sqlalchemy-pt2/server/app.py"  
    packages, modules = list_packages_and_modules(target_directory)

    print("Packages:")
    for package in packages:
        print(package)

    print("\nModules:")
    for module in modules:
        print(module)