import cmd
from pp2i import *
from i2pp import *


class Running(cmd.Cmd):
    intro = ("======================================\n"
             "   Infix, Prefix, Postfix Converter  \n"
             "======================================\n(Type 'help' or 'help <cmd>' to see more details)")
    prompt = "--> "

    def emptyline(self):
        pass

    def do_convert(self, x):
        """Type 'convert to infix' or 'convert to prefix, postfix'"""
        if x == "to infix":
            print("Type 'no' to stop...")
            while True:
                m = input("'postfix' or 'prefix': ")
                if m == 'no':
                    break
                elif m == "postfix":
                    c = input("- Input postfix expr: ")
                    print("- Output:", post_to_i(c))
                elif m == "prefix":
                    c = input("- Input prefix expr: ")
                    print("- Output: ", pre_to_i(c))
                else:
                    print(f"No option '{m}'")
        elif x == 'to prefix, postfix':
            print("... Type 'no' to stop ...")
            while True:
                m = input("Select 'i to post', 'i to pre', 'pre to post' or 'post to pre': ")
                if m == 'no':
                    break
                elif m == 'i to post':
                    while True:
                        c = input("- Infix expr: ")
                        if c == 'no':
                            break
                        try:
                            print(i_to_post(c))
                        except KeyError:
                            print("Input contains white space...")
                elif m == 'i to pre':
                    while True:
                        c = input("- Infix expr: ")
                        if c == 'no':
                            break
                        try:
                            print(i_to_pre(c))
                        except KeyError:
                            print("Input contains white space...")
                elif m == 'pre to post':
                    while True:
                        c = input("- Prefix expr: ")
                        if c == 'no':
                            break
                        else:
                            print(pre_to_post(c))
                elif m == 'post to pre':
                    while True:
                        c = input("- Postfix expr: ")
                        if c == 'no':
                            break
                        else:
                            print(post_to_pre(c))
                else:
                    print(f"No option '{m}'")
        else:
            print(f"No option '{x}'")

    def do_calc(self, expr):
        """Evaluate an expression: 'calc expr'"""
        mode = input("Select 'infix', 'postfix' or 'prefix' mode for calculating: ")
        if mode != 'infix':
            print(calc(expr, mode))
        elif mode == 'infix':
            try:
                print(eval(expr))
            except SyntaxError:
                print("Invalid expression")
            except NameError:
                print("Invalid expression")
        else:
            print(f"No option '{mode}'")

    def do_quit(self, x):
        """Exit the program"""
        return True


Running().cmdloop()
