from setuptools import setup, find_packages

setup(
    name='PyPokerEngine',
    version='1.0.3',
    author='ItzRabbs',
    description='Poker engine for poker AI development in Python',
    license='MIT',
    keywords='python poker emgine ai',
    url='https://github.com/ItzRabbs/PyPokerEngine',
    packages=[pkg for pkg in find_packages() if pkg != "tests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
)
