import os

def post_mkvirtualenv_source(path):
  virtual_env = os.environ.get('VIRTUAL_ENV')
  gopath = os.path.join(virtual_env, 'gopath')
  os.mkdir(gopath)
  return post_activate_source(None)


def post_activate_source(args):
  virtual_env = os.environ.get('VIRTUAL_ENV')
  gopath = os.path.join(virtual_env, 'gopath')
  return """

# Set GOPATH and PATH for maximum awesome

if [ -d "%(gopath)s" ]; then
  export OLD_GOPATH=$GOPATH
  export GOPATH=%(gopath)s
  export PATH=%(gopath)s/bin:$PATH

  [ -z "`alias gohere`" ] && alias gohere="export GOPATH=\\$GOPATH:\\`pwd\\`"
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
