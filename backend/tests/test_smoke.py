import dictation_server


def test_smoke():
    assert hasattr(dictation_server, "main")
