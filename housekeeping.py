#!/home/kycilius/anaconda3/bin/python3 
import argparse as arg
import config
import logging as logger

config_path="/etc/housekeeping.yaml"

def pars_flags():
    arg_parser= arg.ArgumentParser()
    arg_parser.add_argument('--room',nargs='?',action='append',type=str,required=False)
    arg_parser.add_argument('--dry-run',action='store_true',required=False)
    arg_parser.add_argument('keep',action='store')
    
    house_gp = arg_parser.add_mutually_exclusive_group(required=True)
    house_gp.add_argument('--house',action='store',type=str)
    house_gp.add_argument('--all-houses',action='store_true')
    return arg_parser.parse_args()

houses=config.parse(config_path)
flags=pars_flags()

if flags.dry_run:
    logger.warning("running in debug mode")
    logger.warning("just showing the comming plan (fallowing files wont get deleted)")
        
target_houses=houses
if flags.house:
    target_houses=[house for house in houses if house.name==flags.house]

for house in target_houses:
    logger.warning(f"starting the job for house {house.name}")
    if True or flags.keep:
        excess_files=house.keep(rooms=flags.room,dry_run=flags.dry_run)
        if not flags.dry_run:
            for e in excess_files:
                logger.warning(f"room {e[0]}")
                for f in e[1]:
                    logger.warning(f"\t{f}")
