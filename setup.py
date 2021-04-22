from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="aws-create-ec2",
    version="0.1.0",
    description="creating an ec2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements.txt")},
)