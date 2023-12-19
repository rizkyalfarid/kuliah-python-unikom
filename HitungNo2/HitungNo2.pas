program HitungS;

{Kamus}
uses crt;
var
   N, i : integer;
   S, Pembilang, Penyebut : real;

begin
   //memastikan banyak suku
   write('Banyak suku yang akan di hitung (N) : ');
   readln(N);

   //validasi banyak suku
   while (N < 1) or (N > 10) do
     begin
       write('Banyak suku harus antara 1 - 10, ulangi.. tekan enter!');
       readln;
       gotoxy (1,2); clreol;
       gotoxy(38,1); clreol;
     end;//endwhile

     //menghitung s
     S:= 0;
     Pembilang := 1;
     Penyebut := 1;
     write('S = ')
     for i := 1 to N do
     begin
       Pembilang := Penyebut * i;
       Penyebut := Pembilang + i;
       if( i mod 2 = 1)
           begin
               write(' - ', Pembilang:0:0 '/', Penyebut:0:0);
               S := S - Pembilang/Penyebut;
           end
           else
           begin
               write(' + ', Pembilang:0:0 '/', Penyebut:0:0);
               S := S + Pembilang/Penyebut;
           end;
     end;
     writeln;
     write(' = ', S:0:3);
     readln;

end.
