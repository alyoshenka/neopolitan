from distutils.core import setup

setup(
    name="neopolitan",
    version="0.1.0",
    author="alyo",
    author_email="", # todo: necessary?
    packages=["neopolitan"], # todo: what?
    include_package_data=True, # todo: what?
    url="https://pypi.org/project/neopolitan/0.1.0/", # todo: correct?
    license="LICENSE",
    description="Neopolitan: a library for displaying text on LED boards"
    long_description=open("README.md").read()
    install_requires=[
        "pygame", # todo: more?
    ]
)