# Housekeeping
an automated tool for keeping your backup!

## Install

clone repo from reopsitory with the following command
```
git clone <repo_address>
```

run install script
```
housekeeping/install.sh
```

## Getting started

### configuration
housekeeping policies are very much like a real householder!

so first you should declare your houses , then for each house declare some room and after that define a schadule for each room

1) /etc/housekeeping.yaml and add the houses parent directory (i.e. housekeeping.d)

    your housekeping.yaml should look like something like that:
    
    ```house-directories: house-directories: /etc/housekeeping.d```

2) go to your houses parent directory (here we use the predefine value of etc/housekeeping.d) and create a directory for each house
    ```cd /etc/housekeeping.d
    mkdir house1
    mkdir house-eternal 
    .
    .
    .
    ```
3) now in order to add a room to your house just easy make a config file for your room and put it in your house directory
    ```
    cd house1
    touch room1
    ```
4) the content of your room's config file should look something like that
    ```
    path: <path/to/your/data/location>

    pattern: "regex for files you want to be considered for clean up"

    cycles:
      - HOURLY
      - DAILY
      - MONTHLY
      - YEARLY
      - costume:
          unit: 10000
          bound: 20000
  
    actions:
        pre_script :
        - echo
        - "pre"
        post_script:
        - echo
        - "post"
        on_fail_script:
        - echo
        - "on_fail"
    ```
5) done! now you are ready to use your personal housekeeping service just run ```housekeeping keep --all-houses``` for quick start or read the commandline tool section for more detail 

### Room configuration file

+ path: each room configuration file should at least have a path declering the location in which you want to cleanup
+ pattern(optional): if you want to cleanup file with a certian filename (i.e. *.data files) you can use pattern 
    
    if remains empty housekeeping would consider it as .* (all files)
+  cycles(optional): the schaduling system for your room cleanup plan

    you can add any item from HOURLY,DAILY,WEEKLY,MONTHLY,YEARLY, or you can define your own cycle if you need

    what housekeeping does is that it makes sure that for a given cycle (i.e. DAILY) there are at most 1 file for a period of that cycle (here 1 day) till the deadline of that cycle (here 1 week) 

    you can also add costume cycles too , just need to define its unit and bound and you are good to go!
    
+  actions(optional): you can configure a set of action prior , after and in case of failure for each room by filling the ```post_script```,```pre_script``` and ```on_fail_script``` section of the ```actions```

### CommandLine tool
    
to clean up everything simply run 

```housekeeping keep --all-houses```

to specify a house run 

```
housekeeping keep --house house_name
housekeeping keep --h house_name
```

to specify a certain room , run

```
housekeeping keep --house house_name --room room_name
housekeeping keep --h house_name --r room_name
```

you can run the housekeeping command for multiple rooms in a same house as well
```
housekeeping keep --house house_name --room room_name1 room_name2 --room room_name3
housekeeping keep --h house_name --r room_name1 --r room_name2 --r room_name3
```

to run in debug mode add the ```--dry-run``` flag
```
housekeeping keep --house house_name --room room_name --dry-run
```

