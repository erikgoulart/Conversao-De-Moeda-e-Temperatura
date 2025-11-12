import requests

# ======== COTAÇÕES AUTOMÁTICAS ========

def obter_cotacao(valor, de, para):
    """Busca cotação em tempo real usando frankfurter.app."""
    de = de.upper()
    para = para.upper()
    try:
        url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()
        # Frankfurter retorna a cotação dentro de 'rates'
        if "rates" in dados and para in dados["rates"]:
            return dados["rates"][para]
        else:
            print("⚠️ Erro na resposta da API:", dados)
            return None
    except Exception as e:
        print("❌ Erro ao acessar a API:", e)
        return None

# ======== CONVERSÃO DE MOEDA ========

def converter_moeda(valor, de, para):
    """Converte automaticamente entre moedas com fallback local."""
    de, para = de.upper(), para.upper()
    if de == para:
        return valor

    try:
        cotacao = obter_cotacao(valor, de, para)
        if cotacao:
            return cotacao  # Frankfurter já retorna o valor convertido
    except:
        pass  # Se falhar, tenta o backup local

    # ===== Plano B: taxas fixas =====
    RATES = {
        ('USD', 'BRL'): 5.0,
        ('BRL', 'USD'): 1 / 5.0,
        ('EUR', 'BRL'): 5.5,
        ('BRL', 'EUR'): 1 / 5.5,
        ('USD', 'EUR'): 0.91,
        ('EUR', 'USD'): 1 / 0.91,
    }
    chave = (de, para)
    if chave in RATES:
        return valor * RATES[chave]
    else:
        return None

# ======== CONVERSÃO DE TEMPERATURA ========

def converter_temperatura(valor, de, para):
    """Converte entre Celsius, Fahrenheit e Kelvin."""
    de, para = de.upper(), para.upper()
    if de == para:
        return valor

    # Celsius para outras
    if de == "C" and para == "F":
        return (valor * 9/5) + 32
    if de == "C" and para == "K":
        return valor + 273.15

    # Fahrenheit para outras
    if de == "F" and para == "C":
        return (valor - 32) * 5/9
    if de == "F" and para == "K":
        return (valor - 32) * 5/9 + 273.15

    # Kelvin para outras
    if de == "K" and para == "C":
        return valor - 273.15
    if de == "K" and para == "F":
        return (valor - 273.15) * 9/5 + 32

    return None

# ======== FUNÇÃO PRINCIPAL ========

def converter(valor, de, para):
    """Detecta se é temperatura ou moeda e faz a conversão correta."""
    de, para = de.upper(), para.upper()

    # Se for temperatura
    if de in ["C", "F", "K"] and para in ["C", "F", "K"]:
        return converter_temperatura(valor, de, para)

    # Caso contrário, trata como moeda
    return converter_moeda(valor, de, para)
