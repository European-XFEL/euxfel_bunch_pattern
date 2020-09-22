from setuptools import setup, find_packages

version_ns = {}
with open('src/euxfel_bunch_pattern/_version.py') as f:
    exec(f.read(), version_ns)

with open('README.rst') as f:
    readme = f.read()

def _install():
    try:
        from utils import set_cpp_header
        set_cpp_header()
    except ImportError:
        print("WARNING: Could not run set_cpp_header!")
        return False
    return True

setup(name='euxfel_bunch_pattern',
      version=version_ns['__version__'],
      description='Decoding EuXFEL bunch pattern tables',
      long_description=readme,
      url='https://git.xfel.eu/gitlab/karaboDevices/euxfel_bunch_pattern',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      package_data={},
      install_requires=['numpy'],
      install_success=_install()
)
