#coding:utf-8

try: # pip <= 9.0.1
    from pip.req import parse_requirements
except: # pip >= 10.0.1
    from pip._internal.req import parse_requirements

from setuptools import find_packages, setup

with open("./VERSION.txt", "r") as f:
    version = f.read().strip()

setup(
    name='Respider',
    version=version,
    description='A mini spider framework, like Scrapy',
    packages=find_packages(exclude=[]),
    author='troy',
    author_email='totiee@163.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='#',
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False, # 用于Windows卸载不会报错
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
