#!/bin/bash

log_file="auth.log"
limite_tentativas=5

tentativas=$(grep "FailedPassword" "log_file" | wc -l)

if ["$tentativas" -ge "limite_tentativas"];then
	echo "Possível ataque de força bruta detectado"
else
	echo "Nenhuma atividade de força bruta detectada"
fi

