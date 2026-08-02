@echo off
setlocal EnableExtensions
cd /d "%~dp0"

set "JOB=00_Lois_Entree_Sortie"

echo ============================================================
echo Cours 03 fusionne : lois E/S et transmetteurs
echo Nettoyage complet des fichiers auxiliaires
echo ============================================================

for %%E in (
  aux toc out mw lof lot idx ilg ind
  fdb_latexmk fls synctex.gz bbl blg nav snm vrb
) do (
  if exist "%JOB%.%%E" (
    attrib -R "%JOB%.%%E" >nul 2>&1
    del /F /Q "%JOB%.%%E" >nul 2>&1
  )
)

if exist "%JOB%.aux" goto :cleanerror
if exist "%JOB%.toc" goto :cleanerror
if exist "%JOB%.out" goto :cleanerror
if exist "%JOB%.mw"  goto :cleanerror

echo Premiere compilation...
pdflatex -interaction=nonstopmode -halt-on-error "%JOB%.tex"
if errorlevel 1 goto :error

if exist "%JOB%.idx" (
  echo Construction de l'index...
  makeindex "%JOB%.idx"
  if errorlevel 1 goto :error
)

echo Deuxieme compilation...
pdflatex -interaction=nonstopmode -halt-on-error "%JOB%.tex"
if errorlevel 1 goto :error

echo Troisieme compilation...
pdflatex -interaction=nonstopmode -halt-on-error "%JOB%.tex"
if errorlevel 1 goto :error

echo.
echo Compilation terminee : %JOB%.pdf
exit /b 0

:cleanerror
echo.
echo ERREUR : un fichier auxiliaire n'a pas pu etre supprime.
echo Fermer le PDF et tout processus pdflatex, puis relancer le script.
exit /b 2

:error
echo.
echo La compilation a echoue. Consulter %JOB%.log.
exit /b 1
