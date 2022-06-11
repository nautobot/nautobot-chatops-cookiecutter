#!/bin/bash
# Copyright (c) 2016 Mattermost, Inc. All Rights Reserved.
# See License.txt for license information.

echo "Starting MySQL"
/entrypoint.sh mysqld &

until mysqladmin -hlocalhost -P3306 -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" processlist &> /dev/null; do
	echo "MySQL still not ready, sleeping"
	sleep 5
done

echo "Updating CA certificates"
update-ca-certificates --fresh >/dev/null

if [ ! -e "/mm/mattermost-data/users" ]; then
    echo "-- Adding admin user --"
    mattermost user create --system_admin --email "admin@ntc.com" --username "admin" --password "Ntc01234!!" &> /dev/null
	echo "-- Adding ntcbot user --"
	mattermost user create --system_admin --email "ntcbot@ntc.com" --username "ntcbot" --password "Ntc01234!!" &> /dev/null
	echo "-- Converting user to bot --"
	mattermost user convert ntcbot --bot
	echo "-- Creating ntcteam team --"
	mattermost team create --name ntcteam --display_name "NTC Team"
	echo "-- Adding users to ntcteam team"
	mattermost team add ntcteam admin ntcbot
	echo "Starting platform"
	cd mattermost
	exec mattermost --config=config/config_docker.json
else
	echo "Starting platform"
	cd mattermost
	exec mattermost --config=config/config_docker.json
fi
