def calcular_prestacao(valor_casa: float, salario: float, anos: int) -> dict:
    """
    Calcula o valor da prestação e verifica se o financiamento pode ser aprovado.
    Retorna um dicionário com os resultados.
    """
    if valor_casa <= 0 or salario <= 0 or anos <= 0:
        return {
            "status": "error",
            "message": "All values must be greater than zero."
        }

    meses = anos * 12
    prestacao = valor_casa / meses
    limite = salario * 0.33 

    if prestacao <= limite:
        aprovado = True
        mensagem = "Financing APPROVED."
    else:
        aprovado = False
        mensagem = f"Financing DENIED. Max monthly payment allowed: R${limite:.2f}."

    return {
        "housevalue": valor_casa,
        "salary": salario,
        "years": anos,
        "monthly_installment": round(prestacao, 2),
        "max_affordable": round(limite, 2),
        "approved": aprovado,
        "message": mensagem
    }


if __name__ == "__main__":
    try:
        casa = float(input("Enter the house value (R$): "))
        salario = float(input("Enter your monthly salary (R$): "))
        anos = int(input("How many years to pay? "))

        resultado = calcular_prestacao(casa, salario, anos)

        print("\nResult:")
        for chave, valor in resultado.items():
            print(f"{chave}: {valor}")

    except ValueError:
        print("Invalid input. Please enter numerical values only.")
