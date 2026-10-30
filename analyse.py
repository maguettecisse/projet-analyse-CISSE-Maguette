import pandas as pd
import matplotlib.pyplot as plt
import json
# ==================================
# 1. LECTURE DES DONNEES
# ==================================

df = pd.read_csv("data/logs_reseau.csv")

print("Nombre de lignes initiales :", len(df))


# ==================================
# 2. NETTOYAGE DES DONNEES
# ==================================

# Suppression des doublons
print("Nombre de doublons :", df.duplicated().sum())

df = df.drop_duplicates()

print("Nombre de lignes après suppression :", len(df))


# Mise en majuscules des protocoles
df["protocol"] = df["protocol"].str.upper()


# Remplacement des valeurs manquantes
mediane = df["bytes_sent"].median()

df["bytes_sent"] = df["bytes_sent"].fillna(mediane)

print("Médiane utilisée :", mediane)


# ==================================
# 3. VERIFICATION DU NETTOYAGE
# ==================================

print("\nInformations après nettoyage :")

print(df.info())

print("\nValeurs manquantes restantes :")
print(df.isnull().sum())

# ==================================
# 4. CALCUL DES INDICATEURS
# ==================================

# Nombre de lignes après nettoyage
nb_lignes_apres_nettoyage = len(df)

# Port le plus fréquent
top_port = int(df["dst_port"].value_counts().idxmax())

# Pourcentage de connexions bloquées
taux_deny_pct = round(
    (df["action"].str.upper() == "DENY").mean() * 100, 2
)

# Adresse IP ayant contacté le plus de ports distincts
ip_scanner = (
    df.groupby("src_ip")["dst_port"]
    .nunique()
    .idxmax()
)

# Adresse IP ayant envoyé le plus de données
ip_exfiltration = (
    df.groupby("src_ip")["bytes_sent"]
    .sum()
    .idxmax()
)

# Affichage des résultats
print("\n===== RESULTATS DE L'ANALYSE =====")

print("Nombre de lignes :", nb_lignes_apres_nettoyage)
print("Port le plus fréquent :", top_port)
print("Taux DENY :", taux_deny_pct, "%")
print("IP scanner :", ip_scanner)
print("IP exfiltration :", ip_exfiltration)

# ==================================
# 5. ENREGISTREMENT DES RESULTATS
# ==================================

resultats = {
    "nb_lignes_apres_nettoyage": nb_lignes_apres_nettoyage,
    "top_port": top_port,
    "taux_deny_pct": taux_deny_pct,
    "ip_scanner": ip_scanner,
    "ip_exfiltration": ip_exfiltration
}

# Enregistrer dans un fichier JSON
with open("resultats.json", "w", encoding="utf-8") as fichier:
    json.dump(resultats, fichier, indent=4, ensure_ascii=False)

print("\nRésultats enregistrés dans resultats.json")

# ==================================
# 6. GRAPHIQUE 1 : TOP 10 DES PORTS
# ==================================

top_ports = df["dst_port"].value_counts().head(10)

plt.figure(figsize=(10, 5))

top_ports.plot(kind="bar")

plt.title("Les 10 ports les plus utilisés")
plt.xlabel("Ports de destination")
plt.ylabel("Nombre de connexions")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("figures/top_ports.png")

plt.close()

# ==================================
# GRAPHIQUE 2 : ALLOW / DENY
# ==================================

repartition = df["action"].str.upper().value_counts()

plt.figure(figsize=(7, 5))

repartition.plot(kind="pie", autopct="%1.1f%%")

plt.title("Répartition des connexions ALLOW et DENY")
plt.ylabel("")

plt.tight_layout()

plt.savefig("figures/repartition_actions.png")

plt.close()
autopct="%1.1f%%"

# ==================================
# GRAPHIQUE 3 : VOLUME PAR APPAREIL
# ==================================

volume_appareils = df.groupby("device_type")["bytes_sent"].sum()

plt.figure(figsize=(9, 5))

volume_appareils.plot(kind="bar")

plt.title("Volume de données envoyé par type d'appareil")
plt.xlabel("Type d'appareil")
plt.ylabel("Volume total envoyé (octets)")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("figures/volume_appareils.png")

plt.close()

# Informations supplémentaires pour le rapport

nb_ports_scanner = df.groupby("src_ip")["dst_port"].nunique().loc[ip_scanner]

volume_ip_exfiltration = df.groupby("src_ip")["bytes_sent"].sum().loc[ip_exfiltration]

print("\n--- Informations supplémentaires ---")
print("Nombre de ports différents contactés par le scanner :", nb_ports_scanner)
print("Volume total envoyé par l'IP suspecte :", volume_ip_exfiltration, "octets")