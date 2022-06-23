# my TUI tools
try:
    from TUI_class import * # class Screen
except:
    print('Could not find TUI_class.py module.')



#Global Variables
MAIN_MENU = [
    'MAIN_MENU: VRising Tools',
    '1. send message to server.',
    '2: > checklog Menu. ',
    '3: check AWS instance and VRising Server status',
    '4: VRising stop aws instance and server',
    '5: VRising start aws_instance and server',
    'Type <q> to quit.'
    ]
LOG_MENU = [
    'LOG_MENU: VRising_checkLog functions',
    '1. checkLog().get_performance(): 1 <int as X rows>',
    '2. last x rows from log: 2 <int as X rows>',
    '3. last user log chunk: 3 <str as username>',
    '-',
    'Type <b> to go back to MAIN_CMD_SCREEN',
    'Type <q> to quit.'
    ]


# class for interface
class AppInterface():
    # create AppInterface instance
    # also provides custom variables related to
    def __init__(self, name='main_menu', menu_index={'main_menu':Screen()}):
        self.name = name # default name is "main_menu"
        self.all_menus = menu_index # dict of menus, with Screen objects
        self.current_menu = self.all_menus[self.name] # default screen is new instance of Screen object
        self.last_user_cmd = None
        self.sys_msg = None
        self.args = []

    def __repr__(self):
        return f'''
        <Current Menu:{self.name=}
        {self.all_menus.keys()=}
        {self.last_user_cmd=}
        {self.sys_msg=}
        >'''

    def _reset_msgs(self):
        self.last_user_cmd = None
        self.sys_msg = None

    def set_screen(self, name='main_menu'):
        self.name = name
        self.current_menu = self.all_menus[self.name]

    def show(self):
        # you can define the interface design in AppInterface.show() method.
        print(Screen().new_screen(50)) # clear terminal screen with 100 new rows (OBS: THIS IS hardcoded dependency to <class Screen>)
        if self.last_user_cmd is not None:
            print(f'<user_cmd>: {self.last_user_cmd}') # first line is last_user_cmd
        if self.sys_msg is not None:
            print(f'<sys_msg>: {self.sys_msg}') # second line is any remaining sys_msg
        print(self.current_menu.show_menu()) # prints Screen table (OBS: THIS IS hardcoded dependency to <class Screen>)
        prompt = f'({self.name} prompt): '
        self.last_user_cmd = input(f'{prompt}') # prompts for user input with AppInterface.name (active menu)

        #parse user Input
        self.args = self.last_user_cmd.split(' ')
        user_choice = self.args[0]

        user_choice # sets new user full command [user_choice] [cmd_args]
        self.sys_msg = None # resets sys_msg
        return user_choice


"""

BOILERPLATE FOR MAIN() FUNCTION

# config app templates. Create all needed menu screen layout with <class Screen>
MainMenu = Screen(this_menu_list=MAIN_MENU, this_max_len=75)
LogMenu = Screen(this_menu_list=LOG_MENU, this_max_len=75)

# create a menu_index with <keys> as interface name and <values>  as <class Screen>
menu_index = {'main_menu':MainMenu, 'log_menu':LogMenu}

# starting config for interface:
# you can define the interface design in AppInterface.show() method.
interface = AppInterface(name='main_menu', menu_index=menu_index)

while True:
    # prints current menu wait for user_cmd
    interface.show()

    # 0. first check exit infinit loop
    if user_choice == 'q':
        input('<press ENTER to exit>...')
        break

    # 1. check which menu is active
    # MAIN_MENU user_choiceS:
    elif interface.name == 'main_menu':
        # 2. parse user_cmd according to interface.name
        if user_choice == '1':
            # user_choice: 1. send message to server
            print(f'\nPlaceholder: {interface.last_user_cmd=}')
        elif user_choice == '2':
            # user_choice: 2. checkLog menu
            interface.set_screen('log_menu')
        else:
            interface.sys_msg = f'Could not find <{interface.last_user_cmd}> in <{interface.name}>'
    # LOG_MENU user_choiceS:
    elif interface.name == 'log_menu':
        # 2. parse user_cmd according to interface.name
        if user_choice == '1':
            # user_choice: 1.
            print(f'\nPlaceholder: {interface.last_user_cmd=}')
        elif user_choice == '2':
            # user_choice: 2.
            print(f'\nPlaceholder: {interface.last_user_cmd=}')
        elif user_choice == '3':
            # user_choice: 2.
            print(f'\nPlaceholder: {interface.last_user_cmd=}')
        elif user_choice == 'b':
            # user_choice: b.
            interface.set_screen('main_menu')
            #print(f'\nPlaceholder: {interface.last_user_cmd=}')
        else:
            #menu ERROR handler
            interface.sys_msg = f'Could not find <{interface.last_user_cmd}> in <{interface.name}>'
"""
