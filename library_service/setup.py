from setuptools import setup

setup(
    name='library_service',
    packages=['library_service'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)