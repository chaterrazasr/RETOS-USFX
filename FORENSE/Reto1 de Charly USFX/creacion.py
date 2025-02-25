from scapy.all import *
import random

# Definir la bandera y dividirla en dos partes
bandera_parte1 = "USFX{d1f1c1l"
bandera_parte2 = "_d3_V3R_L4_Fl4g}"
bandera_completa = bandera_parte1 + bandera_parte2

ip_origen = "192.168.1.100"
ip_destino = "192.168.1.200"
puerto_origen = random.randint(30000, 65000)
puerto_destino = 80

def crear_paquete_http(metodo, ruta, carga=None):
    if metodo == "GET":
        carga_http = f"{metodo} {ruta} HTTP/1.1\r\nHost: trello.com\r\n\r\n"
    elif metodo == "POST":
        longitud_contenido = len(carga) if carga else 0
        carga_http = f"{metodo} {ruta} HTTP/1.1\r\nHost: hello.com\r\nContent-Length: {longitud_contenido}\r\n\r\n"
        if carga:
            carga_http += carga
    return IP(src=ip_origen, dst=ip_destino) / TCP(sport=puerto_origen, dport=puerto_destino) / Raw(load=carga_http)

# Crear paquetes con tráfico normal y las partes de la bandera ocultas
paquetes = []

# Lista de POST falsos para despistar
posts_falsos = [
    "usuario=juan_perez&contrasena=secreto123",
    "correo=usuario@ejemplo.com&boletin=verdadero",
    "id_producto=1234&cantidad=2",
    "comentario=Excelente+artículo!&id_publicacion=5678",
    "busqueda=programacion+python",
    "inicio_sesion=admin&contrasena=admin123",
    "titulo=Nueva+Publicación&contenido=Lorem+ipsum",
    "categoria=electronica&precio=299.99",
    "nombre=Maria+Garcia&edad=30&ciudad=La+Paz",
    "token=a1b2c3d4e5f6g7h8i9j0",
    "calificacion=5&opinion=Servicio+excelente",
    "idioma=es&pais=BO",
    "dispositivo=movil&sistema_operativo=android",
    "suscripcion=premium&duracion=12meses"
]

# Agregar paquetes GET y POST aleatorios
for _ in range(50):  # Aumentamos el número de paquetes para más ruido
    if random.choice([True, False]):
        # Agregar GET
        paquetes.append(crear_paquete_http("GET", f"/pagina{random.randint(1,20)}.html"))
    else:
        # Agregar POST falso
        datos_post = random.choice(posts_falsos)
        paquetes.append(crear_paquete_http("POST", "/enviar", datos_post))

# Insertar el paquete POST con la segunda parte de la bandera en una posición aleatoria
datos_bandera2 = f"parte2={bandera_parte2}&id={random.randint(1000,9999)}"
paquetes.insert(random.randint(0, len(paquetes)), crear_paquete_http("POST", "/api/datos", datos_bandera2))

# Insertar el paquete POST con la primera parte de la bandera casi al final
datos_bandera1 = f"parte1={bandera_parte1}&id={random.randint(1000,9999)}"
paquetes.insert(len(paquetes) - 5, crear_paquete_http("POST", "/api/datos", datos_bandera1))

# Guardar los paquetes en un archivo .pcap
wrpcap("septiembre.pcap", paquetes)
print("Archivo septiembre.pcap creado exitosamente.")

# Imprimir información adicional
print(f"Número total de paquetes: {len(paquetes)}")
print(f"Bandera completa (no mostrar a los participantes): {bandera_completa}")