@echo off
SET THEFILE=d:\fibonacci\barisanfibonacci.exe
echo Linking %THEFILE%
c:\dev-pas\bin\ldw.exe  D:\Fibonacci\rsrc.o -s   -b base.$$$ -o d:\fibonacci\barisanfibonacci.exe link.res
if errorlevel 1 goto linkend
goto end
:asmend
echo An error occured while assembling %THEFILE%
goto end
:linkend
echo An error occured while linking %THEFILE%
:end
