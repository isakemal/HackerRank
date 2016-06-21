import sys

def stack_activity(stack, command_set):
    _commands = command_set.split()
    _command = _commands[0]
    _parms =  _commands[1:]

    if _command.lower() == 'push':
        stack.append(int(_parms[0])) #only push first item
    elif _command.lower() == 'pop':
        stack = stack[:-1]
    elif _command.lower() == 'inc':
        stack = map(lambda x: x + int(_parms[1]), stack[:int(_parms[0])]) + stack[int(_parms[0]):]
    else:
        raise ValueError("Incorrect command specified: {}".format(command))

    if len(stack)==0:
        print "EMPTY"
    else:
        print(stack[-1])
    return stack

if __name__ == '__main__':
    stack = []
    the_commands = ['push 4', 'pop', 'push 3', 'push 5', 'push 2', 'inc 3 1', 'pop', 'push 1', 'inc 2 2', 'push 4', 'pop', 'pop']
    for command in the_commands:
        stack = stack_activity(stack, command)
        print stack
"""
    stack = []
    s = raw_input("")
    while s:
        stack_activity(stack, s)
        s = raw_input("")
"""
