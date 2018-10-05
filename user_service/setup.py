from setuptools import setup

setup(
    name='user_service',
    packages=['user_service'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)