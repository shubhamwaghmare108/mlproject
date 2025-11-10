from setuptools import find_packages,setup

HYPENDOT = "-e ."
def get_requirements(file_name:str)->list[str]:
    requirements = []
    with open(file_name) as file:
        requirements.append(file.readline())
        requirements = [req.replace("\n","") for req in requirements]
        if HYPENDOT in requirements:
            requirements.remove(HYPENDOT)
    return requirements


setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Shubham Waghmare",
    author_email = "scwagh123@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)