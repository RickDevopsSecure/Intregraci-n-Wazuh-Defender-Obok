# Integración de Microsoft Defender y Obok Hypercube con Wazuh en AWS

## Descripción
Este proyecto tiene como objetivo integrar **Microsoft Defender** y **ObOK Hypercube** con **Wazuh** en AWS para el monitoreo y análisis de eventos de seguridad. La implementación permitirá la recopilación, correlación y visualización de alertas provenientes de estas plataformas dentro de Wazuh, proporcionando una mayor visibilidad sobre incidentes y amenazas.

## Arquitectura
La integración sigue el siguiente flujo:
1. **Microsoft Defender** genera alertas y eventos de seguridad.
2. **ObOK Hypercube** actúa como un sistema de correlación y análisis avanzado.
3. Los logs de **Microsoft Defender** y **ObOK Hypercube** son enviados a **Wazuh** para su procesamiento y almacenamiento.
4. **Wazuh** aplica reglas de detección, genera alertas y permite la visualización a través de su interfaz web.
5. Opcionalmente, se puede integrar **Elastic Stack** para una mayor capacidad de análisis y dashboards personalizados.

## Requisitos Previos
### Infraestructura
- **Servidor Wazuh** configurado en AWS.
- **Elastic Stack** opcionalmente instalado para visualización avanzada.
- **Acceso a API de Microsoft Defender** para obtener logs.
- **ObOK Hypercube** configurado como fuente de datos.

### Permisos y Configuración
- Credenciales de acceso a **Microsoft Defender API**.
- Configuración de **Wazuh Agents** en los endpoints protegidos.
- Integración de **ObOK Hypercube** con Wazuh mediante reenvío de logs.

## Instalación
### 1. Configurar Wazuh en AWS
- Implementar una instancia de Wazuh Server en AWS EC2.
- Configurar almacenamiento y networking adecuados.
- Validar conectividad con los sistemas origen (Microsoft Defender y ObOK Hypercube).

### 2. Integración con Microsoft Defender
- Obtener credenciales de API desde el portal de Microsoft Defender.
- Configurar una integración personalizada en Wazuh para extraer eventos de Microsoft Defender.
- Configurar reglas de correlación para las amenazas detectadas.

### 3. Integración con ObOK Hypercube
- Configurar el envío de logs de seguridad de ObOK Hypercube hacia Wazuh.
- Crear reglas de correlación específicas para eventos provenientes de ObOK Hypercube.

## Configuración en Wazuh
1. Modificar el archivo de configuración de Wazuh (`/var/ossec/etc/ossec.conf`) para incluir la recolección de logs de Microsoft Defender y ObOK Hypercube.
2. Agregar reglas y decoders personalizados para la correcta interpretación de los eventos.
3. Validar que los logs se estén procesando correctamente ejecutando:
   ```sh
   sudo wazuh-logtest
   ```
4. Reiniciar el servicio de Wazuh para aplicar cambios:
   ```sh
   sudo systemctl restart wazuh-manager
   ```

## Verificación y Monitoreo
- Usar la interfaz de Wazuh para validar la recepción de eventos.
- Revisar la generación de alertas en base a las reglas configuradas.
- Integrar dashboards en **Kibana** (si se usa Elastic Stack) para una mejor visualización.

## Contribuciones
Si deseas contribuir a este proyecto, puedes enviar un **pull request** con mejoras en la configuración, reglas personalizadas o documentación adicional.

## Licencia
Este proyecto está bajo la licencia **MIT**.

