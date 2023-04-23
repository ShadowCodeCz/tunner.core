from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    "Programming Language :: Python :: 3"
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent'
]

# with open("README.md", "r") as fh:
#     long_description = fh.read()

description = "Command Executor"

setup(
    name='tunnercore',
    version='0.1',
    packages=find_packages(),
    # TODO: fix
    package_data={
        "tunnercore": ['*', '*/*', '*/*/*', '*/*/*/*'],
    },
    url='',
    project_urls={
        'Source': '',
        'Tracker': '',
    },
    author='ShadowCodeCz',
    author_email='shadow.code.cz@gmail.com',
    description=description,
    long_description="",
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    keywords='command executor',
    install_requires=["generic_design_patterns", "yapsy",],
)