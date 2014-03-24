
import invoke

# Based on https://github.com/pyca/cryptography/blob/master/tasks.py


@invoke.task
def release(version):
    invoke.run("git tag -a uvwsgi-{0} -m \"uvwsgi {0} release\"".format(version))
    invoke.run("git push --tags")

    invoke.run("python setup.py sdist")
    invoke.run("twine upload -r pypi dist/uvwsgi-{0}*".format(version))

