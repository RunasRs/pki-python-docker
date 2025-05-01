
docker.desktop : https://www.docker.com/products/docker-desktop/

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
➡️ : serveur1.org
🔑 : /pki/3-Serveurs/serveur1.org/serveur1.org.key
📜 : /pki/3-Serveurs/serveur1.org/serveur1.org.crt
📜 : /pki/3-Serveurs/serveur1.org/ca.crt
Géréner un certificat .pfx/.p12/.jks pour serveur1.org (6 caractères) (o/n) : o
Mot de passe pour serveur1.org (pfx/p12/jsk) :
🔐 : /pki/3-Serveurs/serveur1.org/serveur1.org.pfx
🔐 : /pki/3-Serveurs/serveur1.org/serveur1.org.p12
🔐 : /pki/3-Serveurs/serveur1.org/serveur1.org.jks
```
![Capture d'écran 2025-04-30 184854](https://github.com/user-attachments/assets/e8b9154c-b249-4035-bc0f-3d5abfbcf73f)

## FQDN sur localhost:
```sh
echo '127.0.0.1 serveur1.org' >> /etc/hosts
```
```powershell
notepad C:\Windows\System32\drivers\etc\hosts
127.0.0.1 serveur1.org
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
