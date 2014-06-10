from setuptools import setup

setup(
  name='govenv',
  version='0.1',
  description = 'Golang Enhancements to virtualenv',
  url='https://github.com/termie/govenv',
  packages=['govenv'],
  author='Andy Smith',
  author_email='github@anarkystic.com',
  entry_points={
    'virtualenvwrapper.post_mkvirtualenv': [
      'gopath = govenv.gopath:post_mkvirtualenv',
      ],
    'virtualenvwrapper.post_activate_source': [
      'gopath = govenv.gopath:post_activate_source',
      ],
    'virtualenvwrapper.post_deactivate_source': [
      'gopath = govenv.gopath:post_deactivate_source',
      ],
    },
  )
