# MyTools @FYG - created and tested 13/06/2022
# class Screen creates an Object with TUI screen attributes and methods
# methods from this class return printable strings

class Screen:
    ''' <class Screen> creates an Object with TUI screen attributes and methods.
    Customize border characters and separators, <header> and <row> formats
    .show_menu() creates and returns a string of a rectangle Menu
    <return> printable strings
    '''

    # default class constants
    MENU_LIST = ['default menu header', 'default menu item n.1']
    CHAR_SEP = '-'
    MAX_LEN = 50

    HEADER_SEP_L = '| '
    HEADER_SEP_R = ' |'
    HEADER_SEP = '|'

    CHAR_BORDER = '-'

    # init each screen with variables with default constants
    # can be overwritten by initializing the object with new args
    def __init__(self,
                 this_menu_list=MENU_LIST,
                 this_char_sep=CHAR_SEP,
                 this_max_len=MAX_LEN,
                this_header_sep_l=HEADER_SEP_L,
                this_header_sep_r=HEADER_SEP_R,
                this_char_border=CHAR_BORDER):

        #print('object created.')
        self.this_menu_list = this_menu_list
        self.this_char_sep = this_char_sep
        self.this_max_len = this_max_len
        self.this_header_sep_l = this_header_sep_l
        self.this_header_sep_r = this_header_sep_r
        self.this_char_border = this_char_border

    def header(self, title='title'):
        '''method create a header_string with Screen variables and a Title
        <return> header_string
        '''
        title=str(title)
        # building the header_string
        #-----| title |-----

        header_text_separator1 = '| '
        header_text_separator2 = ' |'
        title=str(title) #force string format
        row=[]

        len_disp = self.this_max_len -len(self.this_header_sep_l) -len(self.this_header_sep_r) # header space '| xxx |'
        len_disp = len_disp - len(title)
        len_disp = (len_disp/len(self.this_char_sep))

        first_half = int(len_disp/2)
        second_half = int(len_disp - first_half)

        # calculate fill gap due header and char_separator even/odd lengh
        fill = (self.this_max_len
                - len(self.this_header_sep_l)
                - len(self.this_header_sep_r)
                - len(title)
                - first_half*len(self.this_char_sep)
                - second_half*len(self.this_char_sep)
               )

        #print(f'{len_disp=}\n{fill=}\n{first_half=}\n{second_half=}')
        #row.append(self.HEADER_SEP)
        row.append((first_half)*self.this_char_sep)
        row.append(self.this_header_sep_l)

        if fill==2:
            row.append(' ')
            row.append(title)
            row.append(' ')

        elif fill==1:
            row.append(title)
            row.append(' ')
        else:
            row.append(title)

        row.append(self.this_header_sep_r)
        row.append((second_half)*self.this_char_sep)
        #row.append(self.HEADER_SEP)

        header_string = ''.join(row)

        return header_string # function returns a string to be printed

    def new_screen(self,new_rows=100):
        'returns <new_rows> as string \n'
        try:
            new_screen_string = '\n' * new_rows
        except:
            new_screen_string = '\n' * 100
        return new_screen_string

    def menu_row(self, menu_item='<menu_item>', char_separator=' '):
        ''' FUNCTION returns a printable string of ONE ROW for item menu format LEFT-ALIGNED
        <return> string
        '''

        max_len = self.this_max_len
        menu_item = str(menu_item)
        #menu_item_text_separator1 = '| '
        #menu_item_text_separator2 = ' |'
        menu_item_text_separator1 = self.HEADER_SEP_L
        menu_item_text_separator2 = self.HEADER_SEP_R

        row=[]

        len_disp = max_len -len(menu_item_text_separator1) -len(menu_item_text_separator2) # menu_item space '| xxx |'
        len_disp = len_disp - len(menu_item)
        len_disp = int(len_disp/len(char_separator))

        first_half = int(len_disp/2)
        second_half = int(len_disp - first_half)

        # calculate fill gap due menu_item and char_separator even/odd lengh
        fill = (max_len
                - len(menu_item_text_separator1)
                - len(menu_item_text_separator2)
                - len(menu_item)
                - first_half*len(char_separator)
                - second_half*len(char_separator)
               )

        row.append(menu_item_text_separator1)
        row.append(menu_item)

        while fill > 0:
            row.append(' ')
            fill-=1

        row.append(char_separator*len_disp)
        row.append(menu_item_text_separator2)

        string_row = ''.join(row)

        return string_row

    def border(self, custom_div=None):
        '''<border> method returns a string with <Screen.this_char_border> as char_separator
        and size <Screen.this_max_len>
        '''

        if custom_div is not None:
            custom_div=str(custom_div)
            rept = int(self.this_max_len / len(custom_div))
            border_string = rept * custom_div
        else:
            rept = int(self.this_max_len / len(self.this_char_border))
            border_string = rept * self.this_char_border

        return border_string

    def show_menu(self,menu=[]):
        '''<show_menu> method receives a list of strings as menu_item
        the first item on the list is formatted as the <header>
        the rest of the items are formatted as <menu_row>
        this method uses the default <border> to finish the screen
        '''

        screen_string = []
        if len(menu) == 0:
            menu = self.this_menu_list
        if not type(menu) == list:
            return f'<error> method .show_menu({menu=}) should be a list'
        #first item of menu should be header
        if len(menu) >= 2:
            screen_string.append(self.header(menu[0]))
            for item in menu[1:]:
                screen_string.append(self.menu_row(item))
            # end of menu
            screen_string.append(self.border())
        else:
            print('<error>: len(menu) < 2')
        return '\n'.join(screen_string)


# MAIN for test
if __name__ == '__main__':
    print(f'\nExample of Usage - module: {__name__}')
    '''
    test_new_screen()
    test_screen_menu_row()
    test_string_header_row()
    test_screen_border()

    print('\nTests completed.')

    '''
    try:
        from TUI_class_tests import example
        example()
    except:
        print('Could not find TUI_class_tests.py module.')
        print('example() not loaded.')
else:
    print(f'\nModule imported: {__name__}.')
