from setuptools import setup, find_packages

setup(
    name='clashofclans-api',
    version='0.0.6',
    description='This is an easy to use API of the game Clash of Clans',
    long_description="NOT READY TO USE",
    author='Luca Sebastian Koch',
    author_email='luca.sebastian.koch@gmail.com',
    # maintainer="",
    # maintainer_email="",
    url='https://github.com/Acul747/Clash-of-Clans-API',
    # download_url="",
    license='MIT',
    packages=["coc"],
    py_modules=["clashofclans"],
    install_requires=[
        'requests',
    ],
    keywords=['Clash of Clans', 'clash of clans', 'coc', 'coc api', 'clashofclans', 'clashofclans api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
