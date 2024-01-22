# setup.py
from setuptools import setup, find_packages

setup(
    name='face64',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'face64=face64.src.main_script:main'
        ],
    },
    test_suite='test_face64',
    tests_require=[
        'unittest',
    ],
)
