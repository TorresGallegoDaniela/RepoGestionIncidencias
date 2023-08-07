from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='reportBug',
    packages=['reportBug'],
    version='0.1',
    description='Gestión de incidencias de tipo bug',
    author='daniela',
    author_email='daniela@dsinno.io',
    url='https://github.com/TorresGallegoDaniela/GestionIncidenciasTipoBug',
    classifiers=[],
    license='MIT',
    install_requires=[
        'pika'
    ]
)