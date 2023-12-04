program Seleksi_Pemilu;
{I.S. : Pengguna memasukkan umur dan status pernikahan}
{F.S. : Menampilkan boleh memilih atau tidak}
uses crt;
//kamus
var
  Umur : integer;
  Menikah : char;
begin
  write('Masukkan umur :'); readln;
  //menentukan boleh atau tidak
  if(Umur < 17)
   then
   begin
      //Memasukkan status pernikahan
      write('Menikah[Y/T'); readln(Menikah);
      Menikah := upcase(Menikah);
      Menikah := (Menikah);
       {if(Menikah = 'Y')
         then
           write('Anda boleh ikut pemilu')
         else
           write('Anda belum boleh ikut pemilu');}
         case (menikah) of
           'Y' : write('Anda boleh ikut pemilu');
           'T' : write('Anda belum boleh ikut pemilu');
           else
             write('Hanya boleh di isi "Y" atau "T" ')
           end; //endcase
   end
   else
    write('Anda boleh ikut pemilu');
   readln;
