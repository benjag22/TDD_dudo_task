# Kata TDD: Simulador del Juego Dudo Chileno

## Integrantes

* Benjamín Alonso Gonzalez Saavedra(benjag22).
* Benjamín Alejandro Jimenez Ruiz(Jhonweedmann).
* Martin Daniel Gonzalez Cifuentes(hukier).

## Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/benjag22/TDD_dudo_task.git
   cd TDD_dudo_task
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv .venv
   ```

3. **Activar entorno virtual**
   
   En Windows:
   ```bash
   .venv\Scripts\activate
   ```
   
   En macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar las pruebas:
```bash
pytest
```

Para ejecutar las pruebas con cobertura:
```bash
pytest --cov
```

```
src/
├── juego/
│   ├── dado.py
│   ├── cacho.py
│   ├── validador_apuesta.py
│   ├── contador_pintas.py
│   ├── arbitro_ronda.py
│   └── gestor_partida.py
├── servicios/
tests/
├── test_dado.py
├── test_cacho.py
├── test_validador_apuesta.py
├── test_contador_pintas.py
├── test_arbitro_ronda.py
└── test_gestor_partida.py
```

