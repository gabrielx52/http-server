"""Setup file for http-server package."""
from setuptools import setup


setup(
    name="http-server",
    description="Python http server package.",
    author=["Michael Shinners", "Gabriel Meringolo"],
    author_email=["michaelshinners@gmail.com", "gabriel.meringolo@gmail.com"],
    license="MIT",
    py_modules=["client", "server", "concurrency_server"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
    }
)
