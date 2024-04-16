interruptor1 = False
interruptor2 = False
interruptor3 = False

# Primeira visita à sala das lâmpadas
interruptor1 = True

# Volta para a sala com os interruptores e desliga o interruptor 1
interruptor1 = False

# Segunda visita à sala das lâmpadas
interruptor2 = True

# Verifica o estado das lâmpadas
if interruptor1:
    print("O interruptor 1 controla a lâmpada acesa.")
if interruptor2:
    print("O interruptor 2 controla a lâmpada quente.")
if not interruptor1 and not interruptor2:
    print("O interruptor 3 controla a lâmpada fria.")