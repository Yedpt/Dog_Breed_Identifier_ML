# Script de instalación para Dog Breed Identifier ML Project
# Resuelve el problema de PyTorch con sufijos especiales (+cpu, +cu118)

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host "🐕 DOG BREED IDENTIFIER - INSTALACIÓN DE DEPENDENCIAS" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host ""

# Verificar entorno virtual
if (-not $env:VIRTUAL_ENV) {
    Write-Host "⚠️  Advertencia: No estás en un entorno virtual" -ForegroundColor Yellow
    Write-Host "   Recomendamos activar .venv primero:" -ForegroundColor Yellow
    Write-Host "   .\.venv\Scripts\Activate.ps1" -ForegroundColor Cyan
    Write-Host ""
    $continue = Read-Host "¿Continuar de todas formas? (s/n)"
    if ($continue -ne "s") {
        Write-Host "❌ Instalación cancelada" -ForegroundColor Red
        exit 1
    }
}

Write-Host "📦 Paso 1: Instalando PyTorch con CUDA 11.8..." -ForegroundColor Yellow
Write-Host "   (Esto puede tomar varios minutos - archivos grandes)" -ForegroundColor Gray
Write-Host ""

python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error al instalar PyTorch" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✅ PyTorch instalado correctamente" -ForegroundColor Green
Write-Host ""

Write-Host "📦 Paso 2: Instalando dependencias del Backend API..." -ForegroundColor Yellow
Write-Host ""

# Instalar dependencias del backend
Set-Location backend
python -m pip install -r requirements_backend.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error al instalar dependencias del backend" -ForegroundColor Red
    Set-Location ..
    exit 1
}

Set-Location ..

Write-Host ""
Write-Host "✅ Dependencias del backend instaladas" -ForegroundColor Green
Write-Host ""

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host "🎉 INSTALACIÓN COMPLETADA EXITOSAMENTE" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host ""

Write-Host "📋 Paquetes instalados:" -ForegroundColor Yellow
python -m pip show torch | Select-String "Name|Version"
Write-Host ""

Write-Host "🚀 Próximos pasos:" -ForegroundColor Cyan
Write-Host "   1. cd backend" -ForegroundColor White
Write-Host "   2. uvicorn app.main:app --reload" -ForegroundColor White
Write-Host "   3. Abrir http://localhost:8000/docs" -ForegroundColor White
Write-Host ""
