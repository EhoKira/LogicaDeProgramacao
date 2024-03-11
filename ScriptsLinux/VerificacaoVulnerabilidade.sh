#!/bin/bash

sistema="Ubuntu"
versao="20.04"

vulnerabilidade=$(grep "$sitema $versao" cve_database.txt)

if[-n "$vulnerabilidade"]; then
	echo "Vulnerabilidade conhecida encontrada no sistema $sistema $versao."
else
	echo "Nenhuma vulnerabilidade conhecida encontrada."
fi

