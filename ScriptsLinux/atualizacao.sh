#!/bin/bash

echo "Verificando atualizações disponíveis: "
apt-get update
apt-get upgrade -s | grep "upgraded,"


