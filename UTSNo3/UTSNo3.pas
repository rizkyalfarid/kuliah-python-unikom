program KatakDalamSumur;
{I.S: Pengguna memasukkan nama pengguna dan katasandi}
{F.S: Menampilkan jumlah hari}

uses crt;
//kamus
const
  Pengguna = 'Rizky';
  Sandi = '10123028';
var
  NamaPengguna,Katasandi : string;
  Ulang : integer;
begin
  //memasukkan login
  gotoxy(52,13); textcolor(3); write('<< L O G I N >>');
  gotoxy(50,14); textcolor(3); write('Nama Pengguna : ');
  textcolor;(15); readln(NamaPengguna);

  gotoxy(49,15); textcolor(3); write('Katasandi     : ');
  textcolor;(15); readln(Katasandi);

  //verifikasi login
  Ulang := 1;
  while((NamaPengguna <> Pengguna) or (Katasandi <> Sandi)) and (Ulang < 3) do
   begin
     gotoxy(49,16); textcolor(13); write('Login gagal, Ulang!');
     readln;
     gotoxy(49,16); clreol;
     gotoxy(65,14); clreol;
     gotoxy(65,15); clreol;
     gotoxy(65,14); clreol; textcolor(15); readln(NamaPengguna)
     gotoxy(65,15); clreol; textcolor(15); readln(Katasandi)
     Ulang := Ulang + 1;
   end;

   //menghitung hari

   if(NamaPengguna = Pengguna ) and (Katasandi = Sandi)
     then
       begin
         clrscr;
         writeln('<< Menghitung Hari >>');
       end
       else
         begin
           gotoxy(45,14); textcolor(13); write('Maaf, Sudah 3 Kali gagal Login!');

         end;
  readln;

end.
