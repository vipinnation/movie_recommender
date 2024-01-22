from setuptools import setup, find_packages

setup(
    name='Movie Recommender App',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit==0.90.0',
        'pandas==1.3.3',
        # Include any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'app = app:main',
        ],
    },
)
