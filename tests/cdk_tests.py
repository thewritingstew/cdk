from nose.tools import *
from cdk.Menu import *

def test_menu_items():
    menu = Menu()
    assert_equal(menu.welcomeText, "Welcome to Crags and Danger Kingdom!\nWhat would you like to do today?")
    assert_equal(menu.promptText, "Please make your selection below:")
    assert_equal(menu.menuOptions, {'1':"Carson's game", "2":"Davis' game"})
    assert_equal(menu.menuDecoration, (70*'='))
    
def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
