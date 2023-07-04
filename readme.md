
1-docker-compose up

2- http://localhost:8069/web?debug=1

-Carpeta addons/ para instalar modulos

--Crear base addons:
1.sudo docker exec -u root -t -i (id contenedor) /bin/bash
2./usr/bin/odoo scaffold (nombremodulo) /mnt/extra-addons
3.Carpeta addons contendra nuevo modulo vacio

