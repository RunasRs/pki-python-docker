import os
import sys
import subprocess

def gen_ca(pwd, config, key, crt):
    if os.path.isfile(config):
        os.makedirs(f"{pwd}/2-CA", exist_ok=True)
        print(f"📁 : {pwd}/2-CA")
        os.makedirs(f"{pwd}/3-Serveurs", exist_ok=True)
        print(f"📁 : {pwd}/3-Serveurs")
        try:
            subprocess.run([ 'openssl', 'genrsa', '-out', key, '4096'], check=True, stderr=subprocess.DEVNULL)
            print(f"🔑 : {key}")
            subprocess.run([ 'openssl', 'req', '-config', config,'-key', key, '-new', '-x509', '-days', '3650', '-sha256', '-out', crt], check=True, stderr=subprocess.DEVNULL)
            print(f"📜 : {crt}")

        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur OpenSSL : {e}")
            sys.exit(1)
    else:
        print(f"❌ {config}")
        sys.exit(1)

if __name__ == "__main__":

    pwd_script = os.path.dirname(os.path.abspath(__file__))
    pwd_config_ca = os.path.join(pwd_script, '1-Config', 'config-ca.cnf')
    pwd_config_serveur = os.path.join(pwd_script, '1-Config', 'config-serveur.cnf')
    ca_key = os.path.join(pwd_script, '2-CA', 'ca.key')
    ca_crt = os.path.join(pwd_script, '2-CA', 'ca.crt')
    gen_ca(pwd_script, pwd_config_ca, ca_key, ca_crt)
