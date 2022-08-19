import argparse
import logging
from pathlib import Path
import sys

from datetime import datetime
import multiprocessing as mp


LOGGER = logging.getLogger(__name__)

class DefaultParser(argparse.ArgumentParser):
    def error(self, message):
        self._print_message('[Error]:\n')
        self._print_message(f'{message}\n\n')
        self.print_help()
        self.exit(status=2)

        
def main():
    parser = DefaultParser(prog='Program_name',
                           description='Description of the program'
                           )

    parser.add_argument(
        '-v', '--verbose',
        help='Display more detailed messages during processing.',
        action='store_true',
    )

    parser.add_argument(
        '-d', '--debug',
        help='Display VERY detailed messages during processing.',
        action='store_true',
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # add sub menu
    process_parser = subparsers.add_parser('sub1', help='First sub-command to run \'cli_sub1\' function.')
    process_parser.set_defaults(func=cli_sub1)

    beta_bake_parser = subparsers.add_parser('sub2', help='Second sub-command to run \'cli_sub2\' function.')
    beta_bake_parser.set_defaults(func=cli_sub2)

    # parsed and function arguments
    parsed_args, func_args = parser.parse_known_args(sys.argv[1:])

    if parsed_args.verbose:
        logging.basicConfig(level=logging.INFO)
    elif parsed_args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    parsed_args.func(func_args)

    return parser


def cli_sub1(cmd_args):
    parser = DefaultParser(
        prog='sub1 command',
        description='First command description.',
    )

    parser.add_argument(
        '-d', '--data_dir',
        required=True,
        type=Path,
        help='Base directory.',
    )

    parser.add_argument(
        '-a','--all',
        required=False,
        action='store_true',
        default=False,
        help='Run all function.'
    )                                                                                                  
    
    parser.add_argument(
        '-th', '--threads',
        required=False,
        type=int,
        default=mp.cpu_count(),
        help='Number of threads to run jobs (default : '+str(mp.cpu_count())+' ).'
    )


    args = parser.parse_args(cmd_args)

    start = datetime.now()
    if args.all:
        run1_function(args.data_dir,
                      args.threads,
                      )
    finish = datetime.now()
    print(f'\n\033[92mElapsed time : {finish - start}.\033[0m')
    print(f'Started  at {start}. \nFinished at {finish}.\n')


def cli_sub2(cmd_args):
    parser = DefaultParser(
        prog='sub1 command',
        description='First command description.',
    )

    parser.add_argument(
        '-d', '--data_dir',
        required=True,
        type=Path,
        help='Base directory.',
    )

    parser.add_argument(
        '-th', '--threads',
        required=False,
        type=int,
        default=mp.cpu_count(),
        help='Number of threads to run jobs (default : '+str(mp.cpu_count())+' ).'
    )
    
    args = parser.parse_args(cmd_args)

    start = datetime.now()
    run1_function(args.data_dir,
                  args.threads,
                  )
    
    finish = datetime.now()
    print(f'\n\033[92mElapsed time : {finish - start}.\033[0m')
    print(f'Started  at {start}. \nFinished at {finish}.\n')


def run1_function(path,threads):
    print('\n* Function 1:',path, threads)

def run2_function(path,threads):
    print('\n* Function 2:',path, threads)

def cli_app():
    main()
