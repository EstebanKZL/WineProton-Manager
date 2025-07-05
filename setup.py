from setuptools import setup, find_packages

setup(
    name="WineProtonManager",
    version="1.1.0",
    description="Advanced Wine and Proton environment manager for Linux",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="EstebanKZL",
    author_email="tu@email.com",
    url="https://github.com/EstebanKZL/WineProtonManager",
    packages=find_packages(),
    install_requires=[
        'PyQt5>=5.15.0',
    ],
    entry_points={
        'console_scripts': [
            'wineprotonmanager=src.wineprotonmanager:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Desktop Environment :: K Desktop Environment (KDE)',
        'Topic :: System :: Systems Administration',
    ],
)
4. .gitignore
