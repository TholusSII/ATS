@echo off
setlocal EnableExtensions
cd /d "%~dp0"

set "JOB=00_Modelisation_Mecanismes"

echo ============================================================
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

rem Nettoyer aussi les auxiliaires éventuellement créés avec l'ancien nom.
for %%N in (02_ModelisationMecanismes 02_Modelisation_Mecanismes) do (
  for %%E in (
    aux toc out mw lof lot idx ilg ind
    fdb_latexmk fls synctex.gz bbl blg nav snm vrb
  ) do (
    if exist "%%N.%%E" (
      attrib -R "%%N.%%E" >nul 2>&1
      del /F /Q "%%N.%%E" >nul 2>&1
    )
  )
)

if exist "%JOB%.aux" goto :cleanerror
if exist "%JOB%.toc" goto :cleanerror
if exist "%JOB%.out" goto :cleanerror
if exist "%JOB%.mw"  goto :cleanerror

echo Dossier propre.
echo.
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

echo Troisieme compilation pour stabiliser les references...
pdflatex -interaction=nonstopmode -halt-on-error "%JOB%.tex"
if errorlevel 1 goto :error

echo.
echo Compilation terminee : %JOB%.pdf
exit /b 0

:cleanerror
echo.
echo ERREUR : un fichier auxiliaire n'a pas pu etre supprime.
echo Fermer l'editeur PDF et tout processus pdflatex, puis relancer ce script.
echo Fichiers a verifier : %JOB%.aux, %JOB%.toc, %JOB%.out, %JOB%.mw
exit /b 2

:error
echo.
echo La compilation a echoue. Consulter %JOB%.log.
echo Avant une nouvelle tentative, relancer ce script depuis le debut.
exit /b 1
