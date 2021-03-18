from setuptools import setup
import json

setup(
    name="zakuro_cache",
    version="0.0.1",
    short_description="Zakuro module used to keep python scripts execution logs and results in a cached memory.",
    long_description="Zakuro module used to keep python scripts execution logs and results in a cached memory.",
    packages=json.load(open("packages.json", "r")),
    url='https://zakuro.ai',
    license='ZakuroAI',
    author='ZakuroAI',
    python_requires='>=3.6',
    install_requires=[l.rsplit() for l in open("requirements.txt", "r")],
    author_email='info@zakuro.ai',
    description='Zakuro module used to keep python scripts execution logs and results in a cached memory.',
    platforms="linux_debian_10_x86_64",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ZakuroAI License",
    ]
)

