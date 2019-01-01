from setuptools import setup, find_packages
from example_service import __version__

def requirements():
    with open('requirements.txt') as f:
        return [dep for dep in f.read().split('\n')
                if dep.strip() != '' and not dep.startswith('-e')]


setup(name='example_service',
      version=__version__,
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=requirements(),
      entry_points="""
      [console_scripts]
      example-service = example_service.run:main
      """)
