@echo off
cls
title Agente Ressegurinho

echo 🤖 Agente Ressegurinho - Iniciando...

REM Backend
echo [1/2] Backend configurando...
start "Backend" cmd /k "cd agent && uv venv && call .venv\Scripts\activate.bat && uv sync && uv run main.py"

REM Aguardar backend
timeout /t 10 /nobreak >nul

REM Frontend  
echo [2/2] Frontend configurando...
start "Frontend" cmd /k "cd agent-ui && npm install && npm run dev"

echo.
echo ✅ Sistema iniciando em segundo plano
echo ⏳ Aguarde 30 segundos
echo 🌐 Depois acesse: http://localhost:3000
echo.

timeout /t 25 /nobreak >nul
start http://localhost:3000
echo 🎉 Pronto! Sistema aberto no navegador.