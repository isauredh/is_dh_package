from is_dh_package.lib import try_me

def test_try_me():
    assert len(try_me()) == 8
