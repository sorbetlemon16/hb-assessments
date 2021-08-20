"""Invoke tasks."""

from invoke import Collection, task, call
import sys

sys.path.append("..")
from tasklib.build import (
    clean_sphinx_build,
    build_sphinx,
    build_zip,
    build_solution_scantron,
)
from tasklib.upload import upload_sphinx_build, upload_zip
from tasklib.dev import build_sphinx_dev, init_githooks


@task(name="build", pre=[call(build_sphinx_dev, builder="handouts")])
def build_handouts_dev(c):
    """Run Sphinx autobuild server."""

    print("Done")


@task(
    name="build",
    pre=[
        clean_sphinx_build,
        call(build_sphinx, builder="handouts", view=True),
    ],
)
def build_handouts(c):
    """Build handouts."""

    print("Finished building handouts.")


@task(
    pre=[
        clean_sphinx_build,
        call(build_sphinx, builder="handouts", view=False),
        upload_sphinx_build,
    ]
)
def upload_handouts(c, view=True):
    """Upload handouts."""

    print("Finished uploading handouts.")
    if view:
        c.run(f"open {c.deploy.url_root}/{c.slug}")


@task(
    name="build",
    pre=[
        clean_sphinx_build,
        call(build_sphinx, builder="handouts", view=False),
        build_zip,
    ],
)
def build_starter_code(c):
    """Build starter code archive."""

    print("Finished buiding starter code zip file.")


@task(name="deploy", pre=[build_starter_code, upload_zip])
def upload_starter_code(c):
    """Deploy starter code."""

    print("Finished uploading starter code!")


@task(
    name="build",
    pre=[
        clean_sphinx_build,
        call(build_sphinx, builder="handouts", view=False),
        build_solution_scantron,
        call(build_zip, is_solution=True),
    ],
)
def build_solution_code(c):
    """Build solution code archive."""

    print("Finished building solution code.")


@task(
    name="deploy",
    pre=[build_solution_code, call(upload_zip, is_solution=True)],
)
def upload_solution_code(c):
    """Deploy solution code."""


@task(pre=[upload_handouts])
def deploy_all(c):
    """Deploy asssessment."""

dev = Collection("dev")
dev.add_task(build_handouts_dev)
dev.add_task(init_githooks)

handouts = Collection("handouts")
handouts.add_task(build_handouts)

starter_code = Collection("startercode")
starter_code.add_task(build_starter_code)

solution_code = Collection("solutioncode")
solution_code.add_task(build_solution_code)

ns = Collection()
ns.add_collection(handouts)
ns.add_collection(starter_code)
ns.add_collection(solution_code)
ns.add_collection(dev)
ns.add_task(deploy_all, name="deploy")
