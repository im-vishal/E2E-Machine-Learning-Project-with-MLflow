from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "e2e-machine-learning-project-with-mlflow"
AUTHOR_USER_NAME = "im-vishal"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "iamvirtualvishal@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    description='A small python package for ml app.',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license='',
)
