program MenjumlahkanAngka1Sampai10;
{I.S : Diberikan harga pencacah (i) = 10}
{F.S : Menampilkan hasil penjumlahan 1 + 2 .. 10}

uses crt;
//Kamus
var
   Hasil, i : integer; {Hasil:hasil penjumlahan}
begin
   //Inisialisasi var. Hasil
   Hasil := 0;
   {write('Hasil = ');
   for i := 1 to 10 do
   begin
     write(i);
     if( i < 10)
       then
         begin
         write(' + ');
        end
     Hasil := Hasil + i;
   end;?}

   {for i := 10 downto 1 do
   begin
     write(i);
     if( i < 10)
       then
         begin
         write(' + ');
        end
     Hasil := Hasil + i;}
      i := 1;
      {while(1 <= 10) do
        begin
          write(i);
          if( i < 10)
            then
            begin
              write(' + ');
            end;
          Hasil := Hasil + 1;
          i := i - 1;
         end;}

         //Bentuk repeat until cacah naik
         i := i;
         repeat
           write(i);
           if( i < 10)
             then
             begin
               write(' + ');
             end;
          Hasil := Hasil + i;
          i := i + 1;



     //Menampilkan hasil penjumlahan
     writeln;
     write('     = ', Hasil);
     readln;
end.
