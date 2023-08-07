from setuptools import setup

readme = open("README.md", "r") 

setup(
    name='incidentsBug',
    packages=['incidentsBug'],
    version='0.1',
    long_description=readme.read(),
    description='Gestión de incidencias de tipo bug',
    author='daniela',
    author_email='daniela@dsinno.io',
    url='https://github.com/TorresGallegoDaniela/RepoGestionIncidencias',
    classifiers=[],
    license='MIT',
    install_requires=[
        'pika'
    ]
)
