import os

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'dictknife[load] >= 0.3.1',
    "prestring",
    "marshmallow<3.0",
    "magicalimport",
]

docs_extras = []

tests_require = [
    "testmarker",
]

testing_extras = tests_require + []
try:
    from testmarker.setupcmd import test
except ImportError:
    from setuptools.command.test import test

setup(
    name='swagger-marshmallow-codegen',
    version='0.4.0',
    description='generating marshmallow\'s schema from swagger definition file',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords='swagger,codegen,marshmallow,code-generation,schema',
    author="podhmo",
    author_email="ababjam61@gmail.com",
    url="https://github.com/podhmo/swagger-marshmallow-codegen",
    packages=find_packages(exclude=["swagger_marshmallow_codegen.tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': docs_extras,
    },
    cmdclass={"test": test},
    tests_require=tests_require,
    test_suite="swagger_marshmallow_codegen.tests",
    entry_points="""
      [console_scripts]
swagger-marshmallow-codegen=swagger_marshmallow_codegen.cmd:main
"""
)
