import telnetlib
import getpass

host = raw_input("Enter Switch IP Address: ")
user = raw_input("Enter Your Telnet Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("enable \n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("conf t\n")
tn.write("vlan 10\n")
tn.write("name PythonVLAN10\n")
tn.write("vlan 20\n")
tn.write("name PythonVLAN20\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
