install
nfs --server 192.168.2.23 --dir=/export/centos/5.4
lang {{ system.profile.lang }}
keyboard {{ system.profile.keyboard }}

# text mode installation
text

### dhcp netz
network --device {{ system.profile.boot_device.name }} --bootproto dhcp

# root passwort
rootpw --iscrypted blahblahblah

# firewall
{% if system.profile.firewall %}
firewall --enabled --port=22:tcp,7886:tcp
{% else %}
firewall --disabled
{% endif %}

# passwd/shadow
authconfig --enableshadow --enablemd5

# selinux
{% if system.profile.selinux %}
selinux --enforcing
{% else %}
selinux --disabled
{% endif %}

timezone --utc {{ system.profile.timezone }}
bootloader --location=mbr --driveorder=sda 

clearpart --all --initlabel
{% for disk in system.disks.all %}
{% for partition in disk.partitions.all %}
part {{ partition.mountpoint }} {% if partition.fstype %}--fstype={{ partition.fstype }}{% endif %} --ondisk={{ disk.name }} --size={{ partition.size }} {% if partition.primary %}--asprimary{% endif %}
{% endfor %}
{% endfor %}


# reboot after install

reboot

%packages
@base
@core
@text-internet
keyutils
iscsi-initiator-utils
trousers
bridge-utils
fipscheck
device-mapper-multipath
strace
