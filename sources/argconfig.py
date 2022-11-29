import argparse

my_test_args = '-i'


class ArgConfig:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="draw components for fast design architecture",
                                         exit_on_error=True, add_help=True)

        parser.add_argument(metavar='n',    # Option name
                            nargs='?',        # Max number of apparition of the command, '*' unlimited
                            help='-n <project path> : Create a new project file at path',
                            dest='new_project_path',    # defines the attribute name
                            )
        parser.add_argument(metavar='l',
                            nargs='?',
                            help='-l <project file path> : Load file project',
                            dest='load project path')
        parser.add_argument('-i',
                            # metavar='i',
                            # nargs=1,
                            help='Open program in interactive mode',
                            dest='interactive',
                            action='store_true')
        self.args = parser.parse_args([my_test_args])

    def get_config(self):
        return self.args


if __name__ == "__main__":
    cfg = ArgConfig()
    print("toto")
