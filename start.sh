#!/bin/sh
# 启动 Caddy 服务器
caddy start --config /app/Caddyfile --adapter caddyfile

# 启动后端服务
python main.py --host 0.0.0.0 --port 8000