from datetime import datetime

def generer_ips(ip_list):
    generated_ips = []
    for ip in ip_list:
        for i in range(2, 257):
            new_ip = ip.rsplit('.', 1)[0] + f'.{i}'
            generated_ips.append(new_ip)
    return generated_ips

# Demander à l'utilisateur le chemin du fichier contenant les adresses IP
fichier_ip = input("Veuillez entrer le chemin du fichier contenant les adresses IP : ")

# Lire les adresses IP à partir du fichier
with open(fichier_ip, 'r') as file:
    liste_ips = [line.strip() for line in file]

# Générer les nouvelles adresses IP
resultat = generer_ips(liste_ips)

# Obtenir la date et l'heure actuelles
now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")

# Créer le nom du fichier résultant
nom_fichier_resultat = f"RANGED_{timestamp}.txt"

# Écrire le résultat dans le fichier
with open(nom_fichier_resultat, 'w') as file_resultat:
    for ip in resultat:
        file_resultat.write(f"{ip}\n")

print(f"Le résultat a été enregistré dans le fichier : {nom_fichier_resultat}")
