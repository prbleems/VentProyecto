# Plan de Pruebas Automatizadas

## 1. Propósito  
Este documento describe las pruebas automatizadas implementadas para verificar el correcto funcionamiento de los distintos módulos de la plataforma **Vent**. Incluye pruebas de unidad y de integración (mockeadas) para:

- Carrito de compras  
- Gestión de usuarios (registro / login)  
- Catálogo de productos  
- Procesos de pago (Webpay / Transbank)  

---

## 2. Alcance  
Se probarán los siguientes módulos y endpoints:

| Módulo                  | Archivo de Test                            | Tipo             |
|-------------------------|--------------------------------------------|------------------|
| Carrito de compras      | `cart/tests/test_core.py`                  | Unitario         |
| Registro de usuario     | `users/tests/test_signup.py`               | Unitario         |
| Catálogo de productos   | `catalog/tests/test_products.py`           | Unitario/Integr. |
| Pago real               | `orders/tests/test_payments.py`            | Integración      |
| Pago mockeado (Mocky)   | `orders/tests/test_payments_mock.py`       | Integración      |

---

## 3. Resumen de las pruebas

### 3.1 Carrito de compras (`cart/tests/test_core.py`)
- **test_add_to_cart**  
  - **Objetivo**: Añadir un producto al carrito de sesión.  
  - **Entrada**: GET o POST a `/cart/add/<product_id>/`.  
  - **Salida esperada**: Redirección (302) y la página “Tu carrito” contiene el producto.

- **test_remove_from_cart**  
  - **Objetivo**: Quitar un producto del carrito de sesión.  
  - **Entrada**: GET o POST a `/cart/remove/<product_id>/`.  
  - **Salida esperada**: Redirección (302) y “Tu carrito” ya no muestra ese producto.

### 3.2 Registro de usuario (`users/tests/test_signup.py`)
- **test_signup_page_loads**  
  - **Objetivo**: Verificar que la página de registro carga sin errores.  
  - **Entrada**: GET a `/accounts/signup/`.  
  - **Salida esperada**: Código 200 y presencia del formulario.

- **test_signup_creates_user**  
  - **Objetivo**: Un POST con datos válidos crea un usuario.  
  - **Entrada**: POST con `username`, `email` y `password`.  
  - **Salida esperada**: Redirección (302) a la página de login o perfil.

### 3.3 Catálogo de productos (`catalog/tests/test_products.py`)
- **test_product_list**  
  - **Objetivo**: La vista lista de productos muestra los artículos existentes.  
  - **Entrada**: GET a `/`.  
  - **Salida esperada**: Código 200 y al menos un producto en el contexto.

- **test_product_detail**  
  - **Objetivo**: La vista de detalle muestra datos correctos.  
  - **Entrada**: GET a `/product/<slug>/`.  
  - **Salida esperada**: Código 200 y atributos del producto.

### 3.4 Pago real contra Transbank (`orders/tests/test_payments.py`)
- **test_checkout_redirects_to_webpay**  
  - **Objetivo**: `order_checkout` redirige a Webpay si hay items.  
  - **Entrada**: POST a `/orders/checkout/` con carrito no vacío.  
  - **Salida esperada**: 302 a URL de Webpay con `token_ws`.

- **test_finish_without_token**  
  - **Objetivo**: Si falta `token_ws`, redirige al catálogo.  
  - **Entrada**: GET a `/orders/finish/` sin `token_ws`.  
  - **Salida esperada**: 302 a `/`.

### 3.5 Pago mockeado (`orders/tests/test_payments_mock.py`)
- Se usan mocks de Mocky.io para simular diversos escenarios:
  1. **200 OK autorizado**  
  2. **200 OK rechazado (`DECLINED`)**  
  3. **503 Service Unavailable**  

- **test_payment_success**  
  - Simula respuesta `AUTHORIZED` y verifica redirección o flujo correcto.

- **test_payment_declined**  
  - Simula `DECLINED` y valida renderizado de `order_failed.html`.

- **test_payment_endpoint_unavailable**  
  - GET al endpoint `/orders/payment/` devuelve 503.

---

## 4. Entorno de Pruebas  
- **Framework**: Django `TestCase` + `Client`  
- **Ejecución**:  
  ```bash
  source venv/Scripts/activate
  python manage.py test
