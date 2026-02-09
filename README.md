## Installation
`PS C:\Users\w11>`
```ps
git clone https://github.com/RunasRs/pki-python-docker.git
```
```ps
cd pki-python-docker
```
* `.env` Modifiez les variables de votre organisation.
```
C  = FR
ST = France
L  = Paris
O  = ORG
OU = IT
CN = ORG Root CA
```
```powershell
docker-compose up --build -d
```


## Utilisation
`PS C:\Users\w11\pki-python-docker>`
```powershell
docker exec -it pki certificat
```
```
Veuillez entrer le nom de votre serveur : serveur1.org
 ■ : /pki/3-Serveurs/serveur1.org/serveur1.org.key
 ▢ : /pki/3-Serveurs/serveur1.org/serveur1.org.crt
 ▢ : /pki/3-Serveurs/serveur1.org/ca.crt
Géréner un certificat .pfx pour serveur1.org (6 caractères) (o/n) : o
Mot de passe pour serveur1.org (pfx) :
 ▣ : /pki/3-Serveurs/serveur1.org/serveur1.org.pfx
```
<img width="1295" height="198" alt="image" src="https://github.com/user-attachments/assets/0153bbd1-aa93-433a-918a-03c3e344b2ff" />


## FQDN sur localhost:
```powershell
notepad C:\Windows\System32\drivers\etc\hosts
```
```r
127.0.0.1 serveur1.org
```

```sh
echo '127.0.0.1 serveur1.org' >> /etc/hosts
```

## Ajouter l'autorité de certification racine:

⚙️ : Windows
```powershell
Import-Certificate ca.crt -CertStoreLocation Cert:\LocalMachine\Root
```
⚙️ : Debian/Ubuntu
```sh
sudo cp ca.crt /usr/local/share/ca-certificates/ca.crt
sudo update-ca-certificates
```
⚙️ : Oracle
```
sudo cp ~/ca.crt /etc/pki/ca-trust/source/anchors/ca.crt
sudo update-ca-trust
```
