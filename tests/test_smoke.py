"""Smoke tests: the package imports and exposes a version."""

from guardgate import __version__


def test_version_is_a_non_empty_string() -> None:
    assert isinstance(__version__, str)
    assert __version__
