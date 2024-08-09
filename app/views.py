from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadores(request):
    
    {"nome": "Matheus Cunha", "numero": "25",
     "posicao": "Goleiro", "nascimento": "24/05/2001 (23 anos)",
     "cidade": "Tupi Paulista, SP", "foto": "matheuscunha.webp"},
    
    {"nome": "David Luiz", "numero": "23",
     "posicao": "Zagueiro", "nascimento": "22/04/1987 (37 anos)",
     "cidade": "Diadema, SP", "foto": "davidluiz.webp"},
    
    {"nome": "Leonardo Pereira", "numero": "4",
     "posicao": "Zagueiro", "nascimento": "31/01/1996 (28 anos)",
     "cidade": "Curitiba, PR", "foto": "leopereira.webp"},
    
    {"nome": "Varela", "numero": "2",
     "posicao": "Lateral Direito",
     "nascimento": "24/03/1993 (31 anos)",
     "cidade": "Montevidéu, Uruguai", "foto": "varela.webp"},
    
    {"nome": "Matías Viña", "numero": "17",
     "posicao": "Lateral Esquerdo", "nascimento": "09/11/1997 (26 anos)",
     "cidade": "Empalme Olmos, Uruguai", "foto": "matiasvina.webp"},
    
    {"nome": "Gerson Santos da Silva", "numero": "8",
     "posicao": "Volante", "nascimento": "20/05/1997 (27 anos)",
     "cidade": "Rio de Janeiro, RJ", "foto": "gerson.webp"},
    
    {"nome": "Giorgian De Arrascaeta", "numero": "14",
     "posicao": "Meia", "nascimento": "01/06/1994 (30 anos)",
     "cidade": "Nuevo Berlín, Uruguai", "foto": "arrascaeta.webp"},
    
    {"nome": "Victor Hugo", "numero": "29",
     "posicao": "Meia", "nascimento": "11/05/2004 (20 anos)",
     "cidade": "Rio de Janeiro, RJ", "foto": "victorhugo.webp"},
    
    {"nome": "Lorran", "numero": "19",
     "posicao": "Meia", "nascimento": "04/07/2006 (18 anos)",
     "cidade": "Rio de Janeiro, RJ", "foto": "lorran.webp"},
    
    {"nome": "Gabriel Barbosa", "numero": "99",
     "posicao": "Atacante", "nascimento": "30/08/1996 (27 anos)",
     "cidade": "São Bernardo do Campo, SP", "foto": "gabigol.webp"},
    
    {"nome": "Pedro Guilherme", "numero": "9",
     "posicao": "Atacante", "nascimento": "20/06/1997 (27 anos)",
     "cidade": "Rio de Janeiro, RJ", "foto": "pedroguilherme.webp"}
    
    context = {
        "jogadores": jogadores,
    }

    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")