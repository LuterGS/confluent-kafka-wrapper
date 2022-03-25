import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

install_requires = [
    "confluent_kafka==1.8.2"
]

setuptools.setup(
    name="confluent-kafka-wrapper",
    version="0.0.3",
    author="LuterGS",
    author_email="koo04034@gmail.com",
    description="easy-use wrapper for confluent-kafka-wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    url="https://github.com/LuterGS/confluent-kafka-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],

)