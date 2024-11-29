from setuptools import setup, find_packages

setup(
    name="your-project-name",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0.1',
        'Werkzeug>=2.0.1',
        'PyJWT>=2.1.0',
        'python-dotenv>=0.19.0',
        'SQLAlchemy>=1.4.23',
        'requests>=2.26.0',
        'gunicorn>=20.1.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.5',
            'flake8>=3.9.2',
            'black>=21.7b0',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yourproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
