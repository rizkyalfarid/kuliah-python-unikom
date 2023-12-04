program BarisanFibonacci;

uses crt;
//Kamus
var
 N, Suku1, Suku2, Fibo, i : integer;
begin
 //Memasukkan banyak suku (N)
 write('Banyak Sukuk (N) : ', );readln(N)
 //Validasi banyak suku (N)
 while( N < 0) or ( N > 20) do
 begin
   write('Banyk suku harus antara 1 - 20, ulangi!!');
   readln;
   gotoxy(1,2); clreol;
   //masukkan banyak suku (N)
   gotoxy(19,1); clreol; readln(N)
   end. //endwhile
   readln;
end

