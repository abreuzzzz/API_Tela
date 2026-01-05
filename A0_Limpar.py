import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 🔐 Lê o segredo e salva como credentials.json
gdrive_credentials = os.getenv("GDRIVE_SERVICE_ACCOUNT")
with open("credentials.json", "w") as f:
    json.dump(json.loads(gdrive_credentials), f)

# 📌 Autenticação com Google
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# === IDs das planilhas ===
planilhas_ids = {
    "Financeiro_contas_a_receber_Tela": "1ZUt99lEI4P8MkRdybPSef8PKQYpyYe1-YVbqRdflzQ8",
    "Financeiro_contas_a_pagar_Tela": "1-tKwSB1QfLl1RMJ2KR_aKh7VBEIHTWpKQp__dBp0LAc",
    "Financeiro_Completo_Tela": "13M1i37Ujt-JiG68yBn60r_0tiZkCACKsZuYnle6UI2I"
}

print("🗑️ Iniciando exclusão COMPLETA de todas as linhas das planilhas...")

# 1. Limpa TUDO de Contas a Receber
print("\n📋 Limpando: Financeiro_contas_a_receber_Tela")
planilha_receber = client.open_by_key(planilhas_ids["Financeiro_contas_a_receber_Tela"])
aba_receber = planilha_receber.sheet1
aba_receber.clear()
print("  ✅ Todas as linhas excluídas (incluindo cabeçalho)")

# 2. Limpa TUDO de Contas a Pagar
print("\n📋 Limpando: Financeiro_contas_a_pagar_Tela")
planilha_pagar = client.open_by_key(planilhas_ids["Financeiro_contas_a_pagar_Tela"])
aba_pagar = planilha_pagar.sheet1
aba_pagar.clear()
print("  ✅ Todas as linhas excluídas (incluindo cabeçalho)")

# 3. Limpa TUDO de Financeiro Completo - Aba principal (sheet1)
print("\n📋 Limpando: Financeiro_Completo_Tela (sheet1)")
planilha_completo = client.open_by_key(planilhas_ids["Financeiro_Completo_Tela"])
aba_completo = planilha_completo.sheet1
aba_completo.clear()
print("  ✅ Todas as linhas excluídas (incluindo cabeçalho)")

# 4. Limpa TUDO de Financeiro Completo - Aba Dados_Pivotados (se existir)
print("\n📋 Limpando: Financeiro_Completo_Tela (Dados_Pivotados)")
try:
    aba_pivotada = planilha_completo.worksheet("Dados_Pivotados")
    aba_pivotada.clear()
    print("  ✅ Todas as linhas excluídas (incluindo cabeçalho)")
except:
    print("  ⚠️ Aba 'Dados_Pivotados' não encontrada")

print("\n🎉 Limpeza completa concluída com sucesso!")
print("⚠️ ATENÇÃO: Todas as linhas foram removidas, incluindo os cabeçalhos")
