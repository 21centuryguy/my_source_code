import urllib.request
import packaging.version
import distutils.version
data = json.loads(urllib.request.urlopen('https://pypi.python.org/pypi/SQLAlchemy/json').readall().decode('utf-8'))
max([distutils.version.LooseVersion(release) for release in data['releases'] if not packaging.version.parse(release).is_prerelease])