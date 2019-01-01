from setuptools import setup, find_packages


def requirements():
    with open('requirements.txt') as f:
        return [dep for dep in f.read().split('\n')
                if dep.strip() != '' and not dep.startswith('-e')]


setup(name='example_service',
      version="0.1",
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=requirements())
