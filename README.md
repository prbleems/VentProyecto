
# Vent - Proyecto E-commerce

Vent es una plataforma de e-commerce desarrollada con Django que permite gestionar un catálogo de productos, carrito de compras, registro y login de usuarios, y procesos de pago integrados con Transbank (Webpay).

## 🚀 Funcionalidades principales

- Catálogo de productos
- Registro e inicio de sesión de usuarios
- Carrito de compras persistente
- Proceso de pago con integración a Transbank (Webpay)
- Pruebas unitarias y de integración
- Mock de pagos utilizando [mocky.io](https://www.mocky.io/)

## ✅ Requisitos

- Python 3.9 o superior
- pip
- Virtualenv (opcional, pero recomendado)

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/prbleems/VentProyecto.git
cd VentProyecto
```

### 2. Crear y activar entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

## 🧪 Ejecutar pruebas

Para correr todas las pruebas automatizadas, ejecuta:

```bash
python manage.py test
```

Se incluyen pruebas para:

- Carrito de compras  
- Gestión de usuarios  
- Catálogo de productos  
- Procesos de pago (Transbank / Webpay)  
- Mock de pagos usando [mocky.io](https://www.mocky.io/)
