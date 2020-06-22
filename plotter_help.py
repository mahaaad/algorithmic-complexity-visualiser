import menu
import plotter
import inspect
import textwrap

def my_dedent(s, trim_limit=4):
    """Returns string s after first removing the first trim_limit spaces from
    lines that begin with at least trim_limit spaces.
    """
    s_lines = s.splitlines()
    for i in range(len(s_lines)):
        if len(s_lines[i]) > 0:
            if s_lines[i][:trim_limit] == trim_limit * ' ':
                s_lines[i] = s_lines[i][trim_limit:]
    return '\n'.join(s_lines)

def main():
    # Get a list of plotter.plot()'s exported functions (values from the dict)
    plot_functions = list(plotter.plot().values())
    # Get the plot() function's signature (arguments list)
    plot_signature = str(inspect.signature(plotter.plot))
    # Get the functions's names, signatures, and their docstring comments
    plot_function_names = []
    plot_function_signatures = []
    plot_function_docs = []
    for plot_function in plot_functions:
        # I'm formatting the function identifiers to look like dict keys:
        plot_function_names.append('[\'' + plot_function.__name__ + '\']')
        plot_function_signatures.append(str(inspect.signature(plot_function)))
        plot_function_docs.append(plot_function.__doc__)
    # Kill the tkinter window that plotter.plot() created.
    # (The 5th function in the dict, plot_functions[4], is an alias for
    # destroy().)
    plot_functions[4]()

    while True:
        choice = menu.do_menu('Choose one to see its description:',
                              ['Module plotter (plotter.py)',
                               'Function plotter.plot',
                               'Functions returned by plotter.plot'])
        if choice is None: # Exit choice
            break # out of program loop
        if choice == 1:
            print('\nModule plotter:')
            print(plotter.__doc__)
        elif choice == 2:
            print()
            plot_header = 'Function plot' + plot_signature
            print(textwrap.fill(plot_header, initial_indent='',
                                subsequent_indent='    '))
            print('\n' + my_dedent(plotter.plot.__doc__))
        elif choice == 3: # Present submenu of functions returned by plot()
            while True:
                choice = menu.do_menu(('Choose a function returned by '\
                                       'plotter.plot() to see its description:'),
                                      plot_function_names)

                if choice is None: # Exit choice
                    break # out of inner loop

                print()
                plot_function_header = 'Function ' + \
                                       plot_function_names[choice-1] + \
                                       plot_function_signatures[choice-1]
                print(textwrap.fill(plot_function_header, initial_indent='',
                                    subsequent_indent='    '))
                print()
                print(my_dedent(plot_function_docs[choice-1], trim_limit=8))
    
main()
