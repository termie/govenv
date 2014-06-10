
import os

def post_mkvirtualenv(path):
  virtual_env = os.environ.get('VIRTUAL_ENV')
  os.mkdir(os.path.join(virtual_env, 'gopath'))


def post_activate_source(args):
  virtual_env = os.environ.get('VIRTUAL_ENV')
  gopath = os.path.join(virtual_env, 'gopath')
  return """

# Set GOPATH and PATH for maximum awesome

if [ -d "%(gopath)s" ]; then
  export OLD_GOPATH=$GOPATH
  export GOPATH=%(gopath)s
  export PATH=%(gopath)s/bin:$PATH
fi

""" % locals()


def post_deactivate_source(args):
  return """

# Reset the GOPATH
if [ -n "$OLD_GOPATH" ]; then
  export GOPATH=$OLD_GOPATH
  unset OLD_GOPATH
fi
"""
