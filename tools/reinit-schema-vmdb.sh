#!/usr/bin/env bash
if [ -z $PYTHONPATH ]; then
    export PYTHONPATH=/nail/srv
fi
mysql -uroot -e "grant all on *.* to 'mars'@'localhost' identified by 'mars'"
mysql -uroot -e "grant all on *.* to 'mia'@'%' identified by 'mia'"
mysql -uroot -e "drop schema if exists mars";
mysql -uroot -e "create schema mars"

`dirname $0`/../db/schema/maker.py --yes -R:
