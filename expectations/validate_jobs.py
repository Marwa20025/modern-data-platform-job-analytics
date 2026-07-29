import pandas as pd

FILE = "data/processed/jobs_clean.csv"

df = pd.read_csv(FILE)

print("Validation des données...\n")

# Test 1 : ID unique
assert df["id"].is_unique, "❌ Les IDs ne sont pas uniques"
print("✅ IDs uniques")

# Test 2 : Titre non vide
assert df["title"].notna().all(), "❌ Des titres sont manquants"
print("✅ Tous les titres sont présents")

# Test 3 : Entreprise non vide
assert df["company_name"].notna().all(), "❌ Des entreprises sont manquantes"
print("✅ Toutes les entreprises sont présentes")

# Test 4 : Publication valide
df["publication_date"] = pd.to_datetime(df["publication_date"])
assert df["publication_date"].notna().all(), "❌ Dates invalides"
print("✅ Toutes les dates sont valides")

print("\n🎉 Validation terminée avec succès !")