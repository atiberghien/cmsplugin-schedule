from setuptools import setup, find_packages

setup(
    name='cmsplugin-schedule',
    version='0.1',
    description='Allow to deal with events in django cms',
    author='Alban Tiberghien',
    author_email='alban.tiberghien@gmail.com',
    url='http://github.com/atibergien/cmsplugin-schedule',
    packages=find_packages(),
    install_requires=[],
    keywords='schedule event django cms django-cms',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
