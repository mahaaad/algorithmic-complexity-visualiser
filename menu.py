def do_menu (title, choices):

    while True:
        print('\n' + title + '\n')
        for choice_num in range(len(choices)):
            print(str(choice_num + 1) + '. ' + choices[choice_num])
        print('\nX. Exit')
        print()
        choice = input("Your choice: ")
        try:
            choice = int(choice)
            if (choice > 0 and choice <= len(choices)):
                return choice
        except ValueError:
            pass
        if choice in ['x','X']:
            return None
        print('\nInvalid choice. Try again.')

if __name__ == '__main__':
    # Test code
    m = ['This', 'That', 'The other thing', 'Something else, again']
    while True:
        c = do_menu('Test Menu',m)
        if c is None:
            break
        print('\nValid choice:', c)
    
    
