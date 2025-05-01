#!/bin/bash

sed -i "s/Country/$(awk 'NR==1' /pki/.env )/g" /pki/1-Config/config-ca.cnf
sed -i "s/State_or_Province_Name/$(awk 'NR==2' /pki/.env )/g" /pki/1-Config/config-ca.cnf
sed -i "s/Locality_Name/$(awk 'NR==3' /pki/.env )/g" /pki/1-Config/config-ca.cnf
sed -i "s/Organization_Name/$(awk 'NR==4' /pki/.env )/g" /pki/1-Config/config-ca.cnf
sed -i "s/Organizational_Unit_Name/$(awk 'NR==5' /pki/.env )/g" /pki/1-Config/config-ca.cnf
sed -i "s/Common_Name/$(awk 'NR==6' /pki/.env )/g" /pki/1-Config/config-ca.cnf

sed -i "s/Country/$(awk 'NR==1' /pki/.env )/g" /pki/1-Config/config-serveur.cnf
sed -i "s/State_or_Province_Name/$(awk 'NR==2' /pki/.env )/g" /pki/1-Config/config-serveur.cnf
sed -i "s/Locality_Name/$(awk 'NR==3' /pki/.env )/g" /pki/1-Config/config-serveur.cnf
sed -i "s/Organization_Name/$(awk 'NR==4' /pki/.env )/g" /pki/1-Config/config-serveur.cnf
sed -i "s/Organizational_Unit_Name/$(awk 'NR==5' /pki/.env )/g" /pki/1-Config/config-serveur.cnf