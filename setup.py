import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.1.0"

REPO_NAME = "Fraud-Transaction-Detection"
AUTHER_USER_NAME = "dhruvenvaghela"
SRC_REPO="FraudDetection",
AUTHER_EMAIL="dhruvenvaghela09@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHER_USER_NAME,
    author_email=AUTHER_EMAIL,
    description="Fraud Detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)