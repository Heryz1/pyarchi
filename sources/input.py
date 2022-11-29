
class KeyAction:
    action = []

    def print_help():
        for key in KeyAction.action:
            print(f"{key['key']} {key['detail']}")

    def quit():
        """ To be sure that proramm is corretly stopped, c-x is processed by a high layer method"""
        pass

    def create():
        """ Create a new component"""
        pass

    def add_action(key_info):
        """Add a new keybinding to list"""
        KeyAction.action.append(key_info)

    def add_action_high(key, detail, cmd):
        """Add a new keybinding to list"""
        KeyAction.action.append(
            {'key': key, 'detail': detail, 'cmd': cmd})

    def check(key_pressed) -> bool:
        """Check key pressed with key in list"""
        # check if key is c-x to quit programm
        if key_pressed == 'c-x':
            return True
        for key in KeyAction.action:
            if key['key'] == key_pressed:
                key['cmd']()
                key_found = True
        if key_found is None:
            print("Error key not found")


KeyAction.add_action_high('h', ': Show this help', KeyAction.print_help)
KeyAction.add_action_high('c-x', ': Quit programm', KeyAction.quit)
KeyAction.add_action_high('c', ': Create a new block', KeyAction.create)

# def __init__(self) -> None:
#     """Init Interactive Move object and run async to retrieve input concurrently"""
#     asyncio.run(self.run())

# def check(self) -> None:
#     pass

# async def run(self):
#     """ Get user inputs, check user inputs, process user inputs"""
#     done = asyncio.Event()
#     input = create_input()

#     def retrieve_key():
#         for key_press in input.read_keys():
#             # print(key_press)
#             done_process = KeyAction.check(key_press.key)
#             # if key_press.key == keys.controlc:
#             if done_process == True:
#                 done.set()

#     with input.raw_mode():
#         with input.attach(retrieve_key):
#             await done.wait()


class Input:
    pass
