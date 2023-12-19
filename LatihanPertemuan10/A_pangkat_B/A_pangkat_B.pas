program ApangkatB;
{I.S : Pengguna memasukkan harga A dan Harga B}
{F.S : Menampilkan A pangkat B menggunakan operator perkalian}

uses crt;

// Kamus :
var
  A, B: integer;

procedure IsiAB(var A, B: integer);
{I.S. : Pengguna memasukkan harga A dan Harga B}
{F.S : Menghasilkan harga A dan Harga B}
begin
  // memasukkan harga A dan harga B
  write('Masukkan Harga A : ');
  readln(A);
  write('Masukkan Harga B : ');
  readln(B);

  // validasi harga B
  while B < 0 do
  begin
    gotoxy(25, 2);
    textcolor(13);
    write('Harga B tidak boleh negatif, ulangiiiii. Tekan enter!!');
    readln;
    gotoxy(25, 2);
    clreol;
    textcolor(15);
    write('Masukkan Harga B : ');
    readln(B);
  end; // endwhile
end;

function Pangkat(A, B: integer): integer;
{ I.S : Harga A dan Harga B sudah terdefinisi }
{ F.S. : Menghasilkan fungsi A Pangkat B }
var
  i, PangkatAB: integer;
begin
  if B = 0 then
    Pangkat := 1
  else if B = 1 then
    Pangkat := A
  else
  begin
    PangkatAB := A;
    for i := 2 to B do
      PangkatAB := PangkatAB * A;

    Pangkat := PangkatAB;
  end;
end;

procedure TampilPangkat(A, B: integer);
{I.S. : Harga A dan Harga B sudah terdefinisi}
{F.S : Menampilkan A pangkat B menggunakan operator perkalian}
var // kamus lokal
  i: integer;
begin
  write(A:2, ' Pangkat ', B:2, ' = ');

  if B > 1 then
  begin
    for i := 2 to B do
    begin
      write(A);
      if i <> B then
        write(' x ');
    end;
    writeln;
    write('              = ');
  end;

  write(Pangkat(A, B));
end;

// badan program utama
begin
  clrscr;
  IsiAB(A, B);
  TampilPangkat(A, B);
  readln;
end.

