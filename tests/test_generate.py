from pathlib import Path
from gendiff.scripts.gendiff import generate_diff


def test_generate():
    path1 = Path('/Users/webdron/python-project-50/tests/fixtures/file1.json')
    path2 = Path('/Users/webdron/python-project-50/tests/fixtures/file2.json')
    path_res = Path('/Users/webdron/python-project-50/tests/fixtures/result')
    result = open(path_res).read()
    assert generate_diff(path1, path2) == result
