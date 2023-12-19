@echo off
SET THEFILE=d:\hitungno2\hitunngs.exe
echo Linking %THEFILE%
c:\dev-pas\bin\ldw.exe  D:\HitungNo2\rsrc.o -s   -b base.$$$ -o d:\hitungno2\hitunngs.exe link.res
if errorlevel 1 goto linkend
goto end
:asmend
echo An error occured while assembling %THEFILE%
goto end
:linkend
echo An error occured while linking %THEFILE%
:end
