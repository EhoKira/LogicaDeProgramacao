#!/bin/bash

output_dir="/evidencias"
log_file="auth.log"

mkdir -p "$output_dir"
cp "$log_file" "output_dir/syslog.log"
echo "Evidencias coletadas"
