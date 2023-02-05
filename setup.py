from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(name="clashofclans-api",
      version="0.1.5",
      description="A Clash of Clans API",
      long_description=open('README.rst').read(),
      author="Luca Koch",
      author_email="luca.koch@aon.at",
      # maintainer="",
      # maintainer_email="",
      url="https://github.com/Acul747/Database",
      # download_url="",
      # packages=["ClashofClans"],
      # py_modules=["str"],
      # scripts=["str"],
      # ext_modules=List["Extension"],
      classifiers=["Development Status :: 1 - Planning",
                   "Environment :: Web Environment",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python"],
      # distclass="Type[Distribution]",
      # script_name="",
      # script_args=["str"],
      # options=Mapping[str, Any]
      license="MIT License",
      keywords=["coc", "clash", "clashofclans"],
      # platforms=["str"],
      # cmdclass=Mapping[str, Type[Command]],
      # data_files=list[tuple[str, list[str]]],
      # package_dir=Mapping[str, str],

      # obsoletes: list[str] = ...,
      # provides: list[str] = ...,
      # requires: list[str] = ...,
      # command_packages: list[str] = ...,
      # command_options: Mapping[str, Mapping[str, tuple[Any, Any]]] = ...,
      # package_data: Mapping[str, list[str]] = ...,
      include_package_data=True,
      # libraries: list[str] = ...,
      # headers: list[str] = ...,
      # ext_package: str = ...,
      # include_dirs: list[str] = ...,
      # password: str = ...,
      # fullname: str = ...,

      install_requires=[
          "requests~=2.28.2"
      ]
      )
