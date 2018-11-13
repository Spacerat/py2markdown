from setuptools import setup

setup(
    name="py2markdown",
    version="0.0.1",
    description="Make markdown files from python source",
    url="http://github.com/Spacerat/py2markdown",
    author="http://github.com/Spacerat",
    author_email="spacerat3004@gmail.com",
    license="MIT",
    packages=["py2markdown"],
    entry_points={"console_scripts": ["py2markdown=py2markdown.cli:main"]},
    zip_safe=False,
    install_requires=["click"],
)

