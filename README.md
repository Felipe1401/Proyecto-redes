
# Proyecto Redes COM4102 - Segundo Semestre 2023

Repositorio con códigos y resultados del proyecto de redes.

## Comenzando

Estas instrucciones proporcionarán una copia del proyecto en funcionamiento en su máquina local para fines de testing.

### Prerrequisitos

Las dependencias requeridas son:

```
$pip install numpy
$pip install scapy
```

### Instalación

Para instalar:

```
$git clone https://github.com/Felipe1401/Proyecto-redes.git
```

### Test

Test de archivo sin traffic shaping:
```
$python detection.py './Screenshots_and_results/results/with_traffic_shapping/wiresharkClienteR2 2.pcapng'
NO Traffic Shaping detected!
```

Test de archivo con traffic shaping:
```
$python detection.py './Screenshots_and_results/results/with_traffic_shapping/wiresharkCLIENTER2.pcapng'
Traffic Shaping detected!
```

## Construido con

* [Python](https://www.python.org) - Lenguaje para el desarrollo

## Autores

* **Nicolás Araya** - [UsuarioGitHub](https://github.com/)
* **Felipe Gómez** - [Felipe1401](https://github.com/Felipe1401/)
* **Manuel Muñoz** - [ManuelM11](https://github.com/ManuelM11)

## Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para detalles.
