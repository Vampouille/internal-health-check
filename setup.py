from setuptools import setup, find_packages

requires = []

setup(name='internal_healthchecks',
      version='0.0',
      description='Test internal services like ldap and database',
      #long_description="SAC/CAS suissealpine WSGI service",
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      entry_points="""\
      [paste.app_factory]
      main = internal_healthchecks:main
      """,
)
