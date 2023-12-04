program Menentukan_indeks_Nilai;
{I.S : Pengguna memasukkan sebuah nilai}
{F.S : Menampilkan indeks nilai}
uses crt;
//kamus:
var
  Nilai : integer;
  //Nilai : real
  Indeks : char;
begin
  //memasukkan sebuah nilai
  write('Masukkan sebuah nilai :'); readln(Nilai);
  //Menentukan indeks nilai
  {
  if (Nilai >= 80) and (Nilai <= 100)
     then
         Indeks := 'A'
     else
         if (Nilai >= 70) and (Nilai <= 79)
            then
                Indeks := 'B'
                       else
                         if (Nilai >= 60) and (Nilai <= 69)
                           then
                             Indeks := 'C'
                           else
                            if (Nilai >= 50) and (Nilai <= 59)
                              then
                                Indeks := 'D'
                              else
                                 if(Nilai >= 0) and (Nilai <= 49)
                                   then
                                     Indeks := 'E';
                                   else
                                   Indeks := 'Salah Nilai'

 //menampilkan indeks nilai
 write('Indeks Nilai             : ',Indeks);
 readln;

 //memasukkan sebuah nilai
  write('Masukkan sebuah nilai :'); readln(Nilai);
  //Menentukan indeks nilai
  if (Nilai >= 80) and (Nilai <= 100)
     then
         Indeks := 'A'
     else
         if (Nilai >= 70) and (Nilai <= 80)
            then
                Indeks := 'B'
                       else
                         if (Nilai >= 60) and (Nilai <= 70)
                           then
                             Indeks := 'C'
                           else
                            if (Nilai >= 50) and (Nilai <= 60)
                              then
                                Indeks := 'D'
                              else
                                 if(Nilai >= 0) and (Nilai <= 50)
                                   then
                                     Indeks := 'E';
                                   else
                                   Indeks := 'Salah Nilai'
  }
  case (Nilai) of
    80..100 : Indeks := 'A';
    70..79 : Indeks := 'B';
    60..69 : Indeks := 'C';
    50..59 : Indeks := 'D';
    0..49 : Indeks := 'E';
  else
    Indeks := 'Salah Nilai';
  end; //endcase
 //menampilkan indeks nilai
 write('Indeks Nilai             : ',Indeks);
 readln;
end.
