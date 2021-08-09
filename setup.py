import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NHXCrypt",
    version="v1.1.2",
    author="NHXTech",
    author_email="chmuhammadsohaib@gmail.com",
    description="NHXCrypt is a module that uses NHXCrypt-8--128 Algorithms to encrypt and decrypt the files using a single key with a 'mathless cryptography' technique.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chmuhammadsohaib/NHXCrypt",
    packages=setuptools.find_packages(),
    keywords = 'NHXCrypt NHX NHXTech chmuhammadsohaib Cryptography',
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
