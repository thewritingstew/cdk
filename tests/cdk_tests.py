from nose.tools import *
from cdk.Menu import *
from cdk.Engine import *

def test_menu_items():
    engine = Engine('default')
    menu = Menu(engine.menuList)
    assert_equal(menu.welcomeText, "Welcome to Crags and Danger Kingdom!\nWhat would you like to do today?")
    assert_equal(menu.promptText, "Please make your selection below:")
    assert_equal(menu.menuOptions, {1:"Carson's game", 2:"Davis' game", 0:"Quit"})
    assert_equal(menu.menuDecoration, (70*'='))

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
