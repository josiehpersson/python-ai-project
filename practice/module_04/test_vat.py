# the code to test. It adds 25% VAT, the swedish moms.
def add_vat(price: int) -> float:
    return round(price * 1.25)

# test_add_vat is the test. Its name starts with test_, so pytest finds it.
def test_add_vat():
    # assert checks the answer
    assert add_vat(100) == 125

# Output:
#============================= test session starts ==============================
#platform win32 -- Python 3.14.8, pytest-9.1.1, pluggy-1.7.0
#rootdir: /Users/you/python-ai-project
#collected 1 item
#
#practice/module_04/test_vat.py .                                         [100%]
#
#============================== 1 passed in 0.00s ===============================

# platform darwin is your system, then the versions.
# rootdir is the folder pytest ran from, your project folder
# collected 1 item: pytest found 1 test.
# practice/module_04/test_vat.py  . is the file, and one dot per test that passed.
# [100%] is how far it has come.
# 1 passed in 0.00s is the summary: how many passed, and how long it took.

# pytest also makes a folder .pytest_cache in your project folder, which you see in VS Code.
# pytest keeps notes about the last run there.
# the folder has its own .gitignore, so Git leaves it out.