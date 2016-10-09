#!/usr/bin/python
#coding: utf-8

import sys
import commands

print "Ejecutando sccript de concesiones y reservas dhcp."
if len(sys.argv)>1:
	if sys.argv[1] == "-l":
		concedidas = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep lease.*.{ |sort |uniq")
		concedidas = concedidas.replace("lease", "IP Concedida:");
		concedidas = concedidas.replace("{", "");
		reservadas = commands.getoutput("cat /etc/dhcp/dhcpd.conf |grep host -A2|grep 'fixed-address' |sort |uniq")
		reservadas = reservadas.replace("fixed-address", "IP Reservada:");
		reservadas = reservadas.replace(";", "");
		print "IP concedidas"
		print concedidas
		print "IP reservadas"
        	if reservadas is None or reservadas == "":
			print "No hay ip reservadas"
        	else: 
        		print reservadas

	elif "." in sys.argv[1]: 
		concedidas = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep -A6 '%s' |grep 'hardware ethernet' | sort |uniq" % sys.argv[1])
		concedidas = concedidas.replace("hardware ethernet", "MAC:");
		concedidas = concedidas.replace(";", "");
		if len(concedidas) > 0:
			print "IP %s concedida: " % sys.argv[1]
			print concedidas
		else:
			print "No hay concesiones para la ip %s " % sys.argv[1]

else:
	print "Error de sintaxis: Introduce un argumento, -l o una IP"
