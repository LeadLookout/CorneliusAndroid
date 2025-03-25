from setuptools import setup, find_packages

setup(
    name='cornelius',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your dependencies here
        # 'dependency1',
        # 'dependency2',
    ],
    entry_points={
        'console_scripts': [
            'cornelius=cornelius.main:main',  # Adjust this to your main module and function
        ],
    },
)
