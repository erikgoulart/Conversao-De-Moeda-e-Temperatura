# Taxas de câmbio fixas (exemplo)
RATES = {
    ('USD', 'BRL'): 5.0,
    ('BRL', 'USD'): 1 / 5.0,
    ('EUR', 'BRL'): 5.5,
    ('BRL', 'EUR'): 1 / 5.5,
    ('USD', 'EUR'): 0.91,
    ('EUR', 'USD'): 1 / 0.91,
}

def converter_moeda(valor, de, para):
    de, para = de.upper(), para.upper()
    if de == para:
        return valor
    chave = (de, para)
    if chave in RATES:
        return valor * RATES[chave]
    else:
        return None

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9