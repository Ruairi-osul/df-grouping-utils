from setuptools import setup, find_packages

with open("requirements.txt") as f:
    reqs = f.read().splitlines()

with open("README.md", "r") as fh:
    long_discription = fh.read()

description = "Dataframe extention package."
setup(
    name="df-grouping-utils",
    description=description,
    long_discription=long_discription,
    long_discription_content_type="text/markdown",
    version="0.0.1",
    url="https://github.com/Ruairi-osul/df-grouping-utils",
    author="Ruairi O'Sullivan",
    author_email="ruairi.osullivan.work@gmail.com",
    include_package_data=True,
    license="GNU GPLv3",
    keywords="data-analysis",
    project_urls={"Source": "https://github.com/Ruairi-osul/df-grouping-utils"},
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=reqs,
)
