import config

house=config.parse("housekeeping.yaml")
excess_files=house.keep(dry_run=True)

for e in excess_files:
    print(f"room {e[0]}")
    for f in e[1]:
        print(f"\t{f}")