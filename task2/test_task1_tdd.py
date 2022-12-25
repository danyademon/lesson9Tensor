import task1_tdd

def test_str_to_bytes_hello_world():
    assert task1_tdd.str_to_bytes(['привет', 'мир']) == [b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82', b'\xd0\xbc\xd0\xb8\xd1\x80']

def test_bytes_to_str_hello_world():
    assert task1_tdd.bytes_to_str([b'hello', b'world']) == ['hello', 'world']
