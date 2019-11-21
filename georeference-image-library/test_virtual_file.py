from virtual_file import VirtualFile

testfile1 = VirtualFile(path="test.tar.gz")
testfile2 = VirtualFile(path="/directory/file.c")

def test_double_value_extension():
    assert testfile1.get_extension == ".tar.gz"


def test_get_file_name():
    assert testfile1.get_filename == "test"





def test_get_extension():
    assert testfile2.get_extension == ".c"

def test_get_file_name():
    assert testfile2.get_filename == "file"


print("path: " + testfile1.get_path)
print("extension: " + testfile1.get_extension)
