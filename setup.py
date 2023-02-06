from setuptools import setup

setup(name="clashofclans-api",
      version="1.0.1",
      description="A Clash of Clans API",
      long_description=open('README.rst').read(),
      author="Luca Koch",
      author_email="luca.koch@aon.at",
      url="https://github.com/Acul747/ClashofClans-API",
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 3.11",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python"],
      license="MIT License",
      keywords=["coc", "clash", "clashofclans"],
      include_package_data=True,
      python_requires='>=3.11',
      install_requires=[
          "requests~=2.28.2"
      ]
)
