# Global Repository Server

## Getting started

This document will show you how to take complete advantage of the Raum carrier server services. Raum is already prepackaged to be able to be ran
on any system that is based on Debian without any issues and enables compatibility with both 64 bit ARM and AMD platforms.
<br><br>

<h3>Installation</h3>

<b>Public Access Carriers</b> <hr>
To setup the Raum server you must first ensure that all domains that are to be used for it are pointing to the servers public IP and ensure that
the "api" sub-domain is set to port 8000. If this is not set correctly Raum will not be accessible from the public internet.

<b>Intranet Carriers</b> <hr>
If you are setting up an intranet carrier, it is suggested that you use a VPN with high bandwidth. Since your carrier will be private a domain
will not need to be assigned. After a complete setup of the carrier, you will be able to connect to it via the server IP on port 8000.

<b>Private Carriers</b> <hr>
If you are setting up a private carrier you will be able to enable variable storage since you will only be storing your own data on it.
This will be located in the config.ini file under []

<h3>Configuration</h3>

<b>config.ini</b> <hr>
The config.ini file included in this package is able to be updated before, during and after set up and installation.
You are able to change database addresses, credentials aswell as other server related settings in this file.

<b>Command Line Arguments</b> <hr>
You can add --help on end of the main.py file to access information regarding command line arguments.

<h3>Usage</h3>

To use the server as is you will want to initially set it up via the 'setup.py' command that is provided in this repo
After successful completion of the setup, you will then be able to use 'main.py' to run the server.
