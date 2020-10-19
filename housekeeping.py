import argparse as arg
import config

def pars_flags():
    arg_parser= arg.ArgumentParser()
    arg_parser.add_argument('--room',nargs='?',action='append',type=str,required=False)
    arg_parser.add_argument('--dry-run',action='store_true',required=False)
    arg_parser.add_argument('keep',action='store')
    return arg_parser.parse_args()



house=config.parse("housekeeping.yaml")
flags=pars_flags()

print (flags)
if flags.keep:

    house.keep(rooms=flags.room,dry_run=flags.dry_run)
    excess_files=house.keep(dry_run=flags.dry_run)
    for e in excess_files:
        print(f"room {e[0]}")
        for f in e[1]:
            print(f"\t{f}")
