from setuptools import setup, find_packages

setup(
    name='ai-recipe-generator',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='An AI-powered recipe generator for specific foods using Rasa and SpaCy.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'rasa',
        'spacy',
        'pandas',
        'numpy',
        'scikit-learn',
        'flask',  # if you plan to create a web interface
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)