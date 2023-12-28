# Auto-Fishtank
-----
**Thursday 28th December 2023.**
Spoke to Telmo, and started using VSCode to populate the Github repository correctly. We have put all the older details into a folder called old stuff.
Hopefully this will be a better layout (and correct way) of doing it all.

** This is Draft Fishy_v_03

I got hung up on populating the Fish & Plants db. I have left that for now and now I have created the db with no sample data.
I had a big issue in trying to get the python code to work on PostgreSQL (I am a bit dumb with PostgreSQL), so I concentrated on getting it to work with SQLite.
Attached is the python script to create the db, a document describing the db, (i will work on the formatting later :-), a ERD diagram, the sqlite db file and a document for some additional stuff like samples of the inner and outer joins etc.

Go and have a look and give me your thoughts please.
-----




**Tuesday 10th October 2023.**

**I created a Draft Fishy_v_02 Pre-release with the tag of WIP**

· 1 commit to main since this release
 WIP
 fecd96a 

I got hung up on populating the Fish & Plants db. I have left that for now and now I have created the db with no sample data.

I had a big issue in trying to get the python code to work on PostgreSQL (I am a bit dumb with PostgreSQL), so I concentrated on getting it to work with SQLite.

Attached is the python script to create the db, a document describing the db, (i will work on the formatting later :-), a ERD diagram, the sqlite db file and a document for some additional stuff like samples of the inner and outer joins etc.

Go and have a look and give me your thoughts please.
-------------


OK Guys, looks like you are on you holidays, so I spke to mate "ChatGPT" and I have produces the psql db creation script, to create the initial tabels etc.
This is created on a Debian 12 linux machine using python 3.11.4
My script requires 3 files to be in the same directy when launching.
Dockerfile, pslq-start.sh and fishy-create-psql-db.py.
The script will create a docker image from the postresql native image, add a user with a defined password and create a db. It will then launch the python script to createthe tables in the database.
in the pslq-start.sh and fishy-create-psql-db.py there are variables set for the passwords, users etc.

Run it and let me know how you get on.

Sunday 30th July 2023:

I created a folder for sample volume calculator (its called "vol-calc")
Here I placed the Volume calculator samples. There is a simple sample GUI version and the complete text version. There are also a number of reference web links, the best one for the formulas etc is https://www.omnicalculator.com/other/aquarium-volume
and this link, https://www.inchcalculator.com/aquarium-tank-volume-calculator/  scroll down the page and follow the link "Find even more volume formulas on our volume calculator." for more formulas.
