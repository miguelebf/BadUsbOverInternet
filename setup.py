from setuptools import setup, find_packages

setup(
    name='Buoi',
    version='1.0',
    author='Miguel Bustamante',
    author_email='miguelbustamantef@gmailcom',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    python_requires='>=3.6',
    scripts=['scripts/badusb']
)