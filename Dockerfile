FROM odoo:14.0

LABEL MAINTAINER Pau Gallego <paugf2004@gmail.com>
USER root

WORKDIR /odoo_app
COPY requirements.txt .
RUN pip install -r requirements.txt
