from setuptools import setup, find_packages
from orotangi import __version__ as version

install_requires = [
    'Django==1.11.18',
    'djangorestframework==3.6.2',
    'django-cors-headers==2.0.2',
    'django-filter==1.0.2',
    'python-dateutil==2.6.0'
]

setup(
    name='orotangi',
    version=version,
    description='Your Thoughts, Everywhere',
    author='FoxMaSk',
    maintainer='FoxMaSk',
    author_email='foxmask@trigger-happy.eu',
    maintainer_email='foxmask@trigger-happy.eu',
    url='https://github.com/foxmask/orotangi',
    download_url="https://github.com/foxmask/orotangi/"
                 "archive/orotangi-" + version + ".zip",
    packages=find_packages(exclude=['orotangi/local_settings']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Database',

    ],
    install_requires=install_requires,
    include_package_data=True,
)
