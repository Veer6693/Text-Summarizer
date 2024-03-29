import setuptools

with open("README.md", 'r', encoding='utf-8') as f :
    description = f.read()


__version__ = "0.0.1"
REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Veer6693"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "veerpatel66930@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for Summarizer app",
    long_description=description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"" : "src"},
    packages=setuptools.find_packages(where="src")
)