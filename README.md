# Plugin Mute 

This is simple plugin built for b3 (Big Brother Bot http://bigbrotherbot.net) and CoD4 game. The plugin is ment to allow you to mute a player in game to prevent him from speaking. The play can still write his messages in an ingame chat but for every message he will get a single warning.

# Commands

   !mute < player/ID > < on/off >
   
# Description

The original version of this file was built so it muted a player only for a single map or untill the player reconnects. In this version the mute is permenant and will be saved to the database and reamin active until the player changes his GUID or some admin removes the mute. Currently the command will be availabe to full admins and above (see plugin_mute.xml to changes)

# Instalation

To install this plugin, you will first need to run .sql file in your database to create the table for storing the muted players. After that place the mute.py file in your b3/extplugins folder and plugin_mute.xml to b3/explugins/config/ folder. And add this line to your b3.xml file 
```xml
<plugin name="mute" config="@conf/plugin_mute.xml"/>
```

# Authors
Original author: Spoon ( http://forum.bigbrotherbot.net/plugins-by-spoon/cod4-mute/ )
Modified version: Igor Ilic
