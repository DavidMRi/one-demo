from setuptools import setup, Extension

one_module = Extension('_one',
                       sources=[],
                       include_dirs=['.'],
                       libraries=['one'],
                       library_dirs=['.'])

setup(
    name='one',
    version='1.0',
    author='David Méndez Ribera',
    description='SWIG Python wrapper for libone',
    py_modules=["one"],
    ext_modules=[one_module],
    package_dir={'': '.'},
)
