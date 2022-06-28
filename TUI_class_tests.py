from TUI_class import *

# TESTS

def test_screen_menu_row():
    print('testing: test_Screen().menu_row()')
    myscreen = Screen(this_max_len=100)
    a = myscreen.menu_row()
    b = myscreen.menu_row('1')
    c = myscreen.menu_row('12')
    d = myscreen.menu_row('1', char_separator='123') # keyargs is optional
    e = myscreen.menu_row('My Real menu_item', ' -*- ')
    print(a,len(a))
    print(b, len(b))
    print(c, len(c))
    print(d, len(d))
    print(e, len(e))
    print('test_Screen().menu_row() completed.\n')
    pass

def test_string_header_row():
    print('testing: test_Screen().header()')
    myscreen = Screen(this_max_len=100, this_char_sep='*')
    a = myscreen.header()
    b = myscreen.header('1')
    c = myscreen.header('12')
    d = Screen(this_char_sep='-*-').header('default size max_len')
    e = Screen(this_char_sep='-*-', this_max_len=100).header('My Real Header')
    print(a,len(a))
    print(b, len(b))
    print(c, len(c))
    print(d, len(d))
    print(e, len(e))
    print('test_string_header_row() completed.\n')
    pass


def test_screen_border():
    a = Screen(this_char_border='1').border()
    print(a, len(a))

    a = Screen(this_char_border='2', this_max_len=100).border('*')
    print(a, len(a))

    myscreen = Screen(this_char_border='3')
    r1 = myscreen.border()
    print('r1:', r1, len(r1))

    r2 = myscreen.border('4')
    print('r2:', r2, len(r2))
    print('test_Screen().border() completed.\n')
    pass

def test_new_screen():
    print('test_new_screen() method...')
    a = Screen()
    newscreen_string = a.new_screen()
    print(newscreen_string)
    print('test_new_screen() completed.\n')


# example of Usage
def example():
    ''' example of Usage of TUI_class
    '''

    # configure main menu and secondary menu
    mainmenu_list=[
        'Header of Main Menu',
        'Type 1. to use main function 1',
        'Type 2. to use main function 2',
        '',
        'some other text description',
        'Press <enter> to continue to next menu',
        'Press "q" to quit',
        'end of main menu'
    ]
    MainMenu = Screen(this_max_len=70,
                      this_char_sep='*',
                      this_char_border='*',
                      this_menu_list=mainmenu_list)


    secondmenu_list=[
        'Header of Second Menu',
        'Type "b" to go back to Main Menu',
        'Press "q" to quit',
        '',
        'end of second menu',
    ]
    SecondMenu = Screen(this_max_len=50,
                        this_char_sep='-',
                        this_menu_list = secondmenu_list)

    # starting screen:
    print(Screen().new_screen())
    print(MainMenu.show_menu())
    #prompt = True
    prompt = input("type here:")

    while True:
        # 0. check if quit
        if prompt == "q":
            #print(10* "# # # # END PROGRAM # # # # # ")
            input('<press anything to exit>...')
            break

        # 1. clear screen
        print(Screen().new_screen())
        # 2. show what user typed
        print(f'User typed: {prompt}')

        # 3. list all input statements to execute functions
        if prompt == '1':
            print(Screen().border('#'))
            print('execute function 1')
            print(Screen().border('#'))
        elif prompt == '2':
            print(Screen().border('#'))
            print('execute function 2')
            print(Screen().border('#'))
        # 4. check for navigation menu: what to print
        if prompt == "" or prompt ==  None:
            print(SecondMenu.show_menu())
        elif prompt == "b":
            print(MainMenu.show_menu())

        else:
            print(MainMenu.show_menu())

        # wait for new selection
        prompt = input("type here:")

# MAIN for test
if __name__ == '__main__':
    print(f'\nStarting tests for this module: {__name__}')
    test_new_screen()
    test_screen_menu_row()
    test_string_header_row()
    test_screen_border()
    print('\nTests completed.')
