Taiga contrib google auth
=========================

The Taiga plugin for google authentication.

Installation
------------
### Production env

#### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-google-auth2` with:

```bash
  pip install taiga-contrib-google-auth2
```

Modify your `settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["taiga_contrib_google_auth"]

  # Get these from https://console.cloud.google.com/apis/credentials
  CLIENT_ID = "GOOGLE_API_CLIENT_ID"
  CLIENT_SECRET = "GOOGLE_API_CLIENT_SECRET"
  REDIRECT_URI = "GOOGLE_API_REDIRECT_URI"
  RESTRICT_LOGIN = ["GOOGLE_RESTRICT_LOGIN"]
  ALLOW_DOMAIN = ["GOOGLE_API_ALLOW_DOMAIN"]
```

#### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the `taiga-contrib-google-auth2` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/seyriz/taiga-contrib-google-auth/tags/$(pip show taiga-contrib-google-auth2 | awk '/^Version: /{print $2}')/front/dist"  "google-auth"
```

Include in your `dist/conf.json` in the 'contribPlugins' list the value `"/plugins/google-auth/google-auth.json"`:

```json
...
    "googleClientId": "GOOGLE_API_CLIENT_ID",
    "contribPlugins": [
        (...)
        "/plugins/google-auth/google-auth.json"
    ]
...
```

### Dev env

#### Taiga Back

Clone the repo and

```bash
  cd taiga-contrib-google-auth2/back
  workon taiga
  pip install -e .
```

Modify `taiga-back/settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["taiga-contrib-google-auth2"]

    # Get these from https://console.cloud.google.com/apis/credentials
    CLIENT_ID = "GOOGLE_API_CLIENT_ID"
    CLIENT_SECRET = "GOOGLE_API_CLIENT_SECRET"
    REDIRECT_URI = "GOOGLE_API_REDIRECT_URI"
    RESTRICT_LOGIN = "GOOGLE_RESTRICT_LOGIN"
    ALLOW_DOMAIN = "GOOGLE_API_ALLOW_DOMAIN"
```

#### Taiga Front

After clone the repo link `dist` in `taiga-front` plugins directory:

```bash
  cd taiga-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../taiga-contrib-google-auth2/dist google-auth
```

Include in your `dist/conf.json` in the 'contribPlugins' list the value `"/plugins/google-auth/google-auth.json"`:

```json
...
    "googleClientId": "GOOGLE_API_CLIENT_ID",
    "contribPlugins": [
        (...)
        "/plugins/google-auth/google-auth.json"
    ]
...
```

In the plugin source dir `taiga-contrib-google-auth2/front` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.

Running tests
-------------

We only have backend tests, you have to add your `taiga-back` directory to the
PYTHONPATH environment variable, and run py.test, for example:

```bash
  cd back
  add2virtualenv /home/taiga/taiga-back/
  py.test
```
