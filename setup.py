from setuptools import setup, find_packages

setup(
    name = 'eecom',
    version = '1.0.0.dev',
    keywords='energy data analysis',
    description = 'a data analysis toolkit for energy data',
    long_description = 'a toolkit for energy manager to identify energy efficiency and conservation opportunity',
    license = 'MIT License',
    url = 'https://github.com/energy725/eecom',
    author = 'Jacky ZHAN',
    author_email = 'zhanlei.energy@gmail.com',
    packages = find_packages(exclude=['docs']),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['pandas', 'numpy'],
)