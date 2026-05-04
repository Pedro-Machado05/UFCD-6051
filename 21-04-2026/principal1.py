# --- CALCULADORA DE IVA PRONTA A USAR ---

def calcular_iva():
    print("-" * 30)
    print("      CÁLCULO DE IVA")
    print("-" * 30)

    try:
        # O .replace(',', '.') permite que o utilizador use a vírgula decimal
        entrada_valor = input("Digite o valor base (€): ").replace(',', '.')
        valor_base = float(entrada_valor)
        
        entrada_taxa = input("Digite a taxa de IVA (ex: 23): ").replace(',', '.')
        taxa_iva = float(entrada_taxa)

        # Lógica de cálculo
        montante_iva = valor_base * (taxa_iva / 100)
        total_final = valor_base + montante_iva

        # Exibição dos resultados com 2 casas decimais
        print("\n" + "=" * 30)
        print(f"Subtotal:       {valor_base:10.2f}€")
        print(f"IVA ({taxa_iva}%):    {montante_iva:10.2f}€")
        print("-" * 30)
        print(f"TOTAL:          {total_final:10.2f}€")
        print("=" * 30)

    except ValueError:
        print("\n[ERRO]: Por favor, insira apenas números.")

if __name__ == "__main__":
    calcular_iva()
    # Mantém a janela aberta até carregar numa tecla
    input("\nPressione Enter para fechar...")