AVISO = "Esta herramienta es informativa y no reemplaza la asesoría financiera profesional"


def mensaje_dictamen(dictamen):
    if dictamen.van > 0:
        titulo = "Esta decisión sí te conviene"
    else:
        titulo = "Esta decisión no es recomendable"
    return f"{titulo}. {AVISO}."
