import os
import sys
import subprocess
import getpass
import re

def gen_certificat(key, csr, crt, nom, pwd, ca_key, ca_crt):
    try:
        subprocess.run(['openssl', 'genrsa', '-out', key, '2048'], check=True, stderr=subprocess.DEVNULL)
        print(f"🔑 : {key}")
        config_template = os.path.join(pwd, '1-Config', 'config-serveur.cnf')
        config_serveur  = os.path.join(pwd, '3-Serveurs', nom, f'config-{nom}.cnf')
        pwd_serveurs    = os.path.join(pwd, '3-Serveurs', nom)

        with open(config_template, 'r') as file:
            config_content = file.read()
        config_content = config_content.replace('SERVEUR.DOMAINE', nom)
        with open(config_serveur, 'w') as file:
            file.write(config_content)

        subprocess.run(['openssl', 'req', '-new', '-key', key, '-out', csr, '-config', config_serveur], check=True, stderr=subprocess.DEVNULL)
        subprocess.run(['openssl', 'req', '-config', config_serveur, '-x509', '-days', '825', '-CA', ca_crt, '-CAkey', ca_key, '-in', csr, '-out', crt], check=True, stderr=subprocess.DEVNULL)
        print(f"📜 : {crt}")
        subprocess.run(['cp', ca_crt, pwd_serveurs], check=True, stderr=subprocess.DEVNULL)
        print(f"📜 : {pwd_serveurs}/ca.crt")
        subprocess.run(['rm', '-f', config_serveur], check=True, stderr=subprocess.DEVNULL)
        subprocess.run(['rm', '-f', csr], check=True, stderr=subprocess.DEVNULL)

    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)

def gen_pkcs12(jks, pfx, p12, key, crt, ca_crt, nom):
    try:
        if input(f"Géréner un certificat .pfx/.p12/.jks pour {nom} (6 caractères) (o/n) : ") == "o":
            MDP = ''
            while len(MDP) < 6:
                MDP = getpass.getpass(f"Mot de passe pour {nom} (pfx/p12/jsk) : ")
                if len(MDP) >= 6:
                    subprocess.run(['openssl', 'pkcs12', '-export', '-out', pfx, '-inkey', key, '-in', crt, '-certfile', ca_crt, '-passout', f'pass:{MDP}'], check=True, stderr=subprocess.DEVNULL)
                    subprocess.run(['openssl', 'pkcs12', '-export', '-out', p12, '-inkey', key, '-in', crt, '-certfile', ca_crt, '-passout', f'pass:{MDP}'], check=True, stderr=subprocess.DEVNULL)
                    subprocess.run(['keytool', '-importkeystore', '-srckeystore', p12, '-srcstoretype', 'PKCS12', '-destkeystore', jks, '-deststoretype', 'JKS', '-deststorepass', MDP, '-srcstorepass', MDP], check=True, stderr=subprocess.DEVNULL)
                    print(f"🔐 : {pfx}")
                    print(f"🔐 : {p12}")
                    print(f"🔐 : {jks}")
                else:
                    print(f"❌ Mot de passe invalide (6 caractères)")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)

def check_certificat(paths):
    Trouve = False
    for path in paths:
        if os.path.exists(path):
            print(f"⚠️: Le fichier existe - {path} ")
            Trouve = True
    return Trouve


if __name__ == "__main__":

    nom_serveur = input("Veuillez entrer le nom de votre serveur : ")
    regex = r'^[A-Za-z0-9_\-\.]+$'
    if re.search(regex, nom_serveur):
        print(f"➡️ : {nom_serveur}")
    else:
        print(f"❌ Nom du serveur invalide")
        sys.exit(1)

    pwd_script = os.path.dirname(os.path.abspath(__file__))
    pwd_ca_key = os.path.join(pwd_script, '2-CA', 'ca.key')
    pwd_ca_crt = os.path.join(pwd_script, '2-CA', 'ca.crt')

    serveur_dir = os.path.join(pwd_script, '3-Serveurs', nom_serveur)
    os.makedirs(serveur_dir, exist_ok=True)

    serveur_key = os.path.join(serveur_dir, f'{nom_serveur}.key')
    serveur_csr = os.path.join(serveur_dir, f'{nom_serveur}.csr')
    serveur_crt = os.path.join(serveur_dir, f'{nom_serveur}.crt')
    serveur_pfx = os.path.join(serveur_dir, f'{nom_serveur}.pfx')
    serveur_p12 = os.path.join(serveur_dir, f'{nom_serveur}.p12')
    serveur_jks = os.path.join(serveur_dir, f'{nom_serveur}.jks')

    check = [serveur_key, serveur_csr, serveur_crt, serveur_jks, serveur_pfx, serveur_p12]

    if check_certificat(check):
        if input(f"Géréner un nouveau certificat pour {nom_serveur} (o/n) : ") == "o":
            gen_certificat(serveur_key, serveur_csr, serveur_crt, nom_serveur, pwd_script, pwd_ca_key, pwd_ca_crt)
            gen_pkcs12(serveur_jks, serveur_pfx, serveur_p12, serveur_key, serveur_crt, pwd_ca_crt, nom_serveur)
        else:
            gen_pkcs12(serveur_jks, serveur_pfx, serveur_p12, serveur_key, serveur_crt, pwd_ca_crt, nom_serveur)
    else:
        gen_certificat(serveur_key, serveur_csr, serveur_crt, nom_serveur, pwd_script, pwd_ca_key, pwd_ca_crt)
        gen_pkcs12(serveur_jks, serveur_pfx, serveur_p12, serveur_key, serveur_crt, pwd_ca_crt, nom_serveur)
