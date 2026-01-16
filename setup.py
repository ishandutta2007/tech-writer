from setuptools import setup, find_packages

setup(
    name='codeguardian',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'codeguardian = codeguardian.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to map and document codebases using AI agents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/codeguardian',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
