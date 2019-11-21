from virtual_file import VirtualFile

virtual_file1 = VirtualFile(path="test.tar.gz")


def test_virtual_file1_get_filename():
    assert virtual_file1.get_filename == "test.tar.gz"


def test_virtual_file1_get_file():
    assert virtual_file1.get_file == "test"


def test_virtual_file1_double_value_extension():
    assert virtual_file1.get_extension == ".tar.gz"


def test_virtual_file1_path():
    assert virtual_file1.get_path == "test.tar.gz"


def test_file1_empty_directory():
    assert virtual_file1.get_directory == ""


virtual_file2 = VirtualFile(path="/directory/file.c")


def test_virtual_file2_get_filename():
    assert virtual_file2.get_filename == "file.c"


def test_virtual_file2_get_file():
    assert virtual_file2.get_file == "file"


def test_virtual_file2_get_extension():
    assert virtual_file2.get_extension == ".c"


def test_virtual_file2_single_path():
    assert virtual_file2.get_path == "/directory/file.c"


def test_virtual_file2_single_directory():
    assert virtual_file2.get_directory == "/directory/"


virtual_file3 = VirtualFile(path="/dec/directory/lok/source.n")


def test_virtual_file3_get_filename():
    assert virtual_file3.get_filename == "source.n"


def test_virtual_file3_get_file():
    assert virtual_file3.get_file == "source"


def test_virtual_file3_get_extension():
    assert virtual_file3.get_extension == ".n"


def test_virtual_file3_single_path():
    assert virtual_file3.get_path == "/dec/directory/lok/source.n"


def test_virtual_file3_single_directory():
    assert virtual_file3.get_directory == "/dec/directory/lok/"


# def test_virtual_file3_change_slash_to_backslash():
#     virtual_file3.change_slash_to_backslash()
#     assert virtual_file3.get_directory == '\dec\directory\lok\\'
#
#
# def test_virtual_file3_change_backslash_to_slash():
#     virtual_file3.change_backslash_to_slash()
#     assert virtual_file3.get_directory == "/dec/directory/lok/"
#
#
# virtual_file4 = VirtualFile(path="\mej\sr\kleep\mmf\sess.j")
#
#
# def test_virtual_file4_get_filename():
#     assert virtual_file4.get_filename == "sess.j"
#
#
# def test_virtual_file4_change_slash_to_backslash():
#     virtual_file4.change_slash_to_backslash()
#     assert virtual_file4.get_directory == "\mej\sr\kleep\mmf\sess.j"
#
#
# def test_virtual_file4_get_directory():
#     assert virtual_file4.get_directory == "\mej\sr\kleep\mmf\\"
#
#
# def test_virtual_file4_change_backslash_to_slash():
#     virtual_file4.change_backslash_to_slash()
#     assert virtual_file4.get_directory == "/mej/sr/kleep/mmf/"
