[![Build Status](https://travis-ci.org/pablodav/ansible_nagios_common_nrpe.svg?branch=master)](https://travis-ci.org/pablodav/ansible_nagios_common_nrpe)

# Vars for group/vars (probably you will use all group here)

You can configure the servers to listen with one of two vars: 

    common_nagios_servers: "127.0.0.1, someip, someothernagioserver"
or 

    nagios_server_group: group_name
     
The nagios_server_group name will be used to extract the addresses of nagios servers from nagios host facts from that group      
