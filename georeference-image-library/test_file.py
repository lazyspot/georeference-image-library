from file import File

file1 = File("test.tar.gz")

def test_file_1_extension():
    assert file1.get_extension == ".tar.gz"


def test_virtual_file1_get_file():
    assert file1.get_filename == "test"


def test_virtual_file1_get_filename():
    assert file1.name == "test.tar.gz"


def test_file1_empty_directory():
    assert str(file1.parent) == "."


file2 = File("/directory/file.c")


def test_file2_get_file():
    assert file2.name == "file.c"


def test_file2_get_filename():
    assert file2.get_filename == "file"


def test_file2_get_extension():
    assert file2.get_extension == ".c"


def test_file2_single_path():
    assert str(file2) == "/directory/file.c"


def test_file2_single_directory():
    assert str(file2.parent) == "/directory"


file3 = File("/dec/directory/lok/source.n")


def test_file3_get_filename():
    assert file3.name == "source.n"


def test_file3_get_file():
    assert file3.get_filename == "source"


def test_file3_get_extension():
    assert file3.get_extension == ".n"


def test_file3_single_path():
    assert str(file3) == "/dec/directory/lok/source.n"


def test_file3_single_directory():
    assert str(file3.parent) == "/dec/directory/lok"


def test_file3_change_slash_to_backslash():
    assert file3.parent.get_directory_str_backslash() == "\dec\directory\lok" == '\dec\directory\lok'


def test_file3_change_backslash_to_slash():
    assert file3.parent.get_directory_str_slash() == "/dec/directory/lok"


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
