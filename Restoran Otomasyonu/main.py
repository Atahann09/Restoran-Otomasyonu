from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('Menu.db')
c = conn.cursor()

class rezervasyonyap:
    def __init__(self, pencere):
        self.pencere = pencere
        self.sol = Frame(pencere,width=1000,height=500,bg='White')
        self.sol.pack(side=LEFT)
        self.baslik = Label(self.sol,text="ATEŞ RESTORAN",font=('calibri 40 bold'),fg='red',bg='white')
        self.baslik.place(x=350, y=25)
        self.isim = Label(self.sol, text="İsim", width=20, font=(' bold', 10))
        self.isim.place(x=270, y=120)
        self.Telefon = Label(self.sol, text="Telefon Numarası",width=20,font=(' bold', 10))
        self.Telefon.place(x=270, y=170)
        self.Kisisayisi = Label(self.sol, text="Kişi sayısı",width=20,font=(' bold', 10))
        self.Kisisayisi.place(x=270, y=220)

        self.isim = Entry(self.sol, width=30)
        self.isim.place(x=430, y=120)
        self.Telefon = Entry(self.sol, width=30)
        self.Telefon.place(x=430, y=170)
        self.Kisisayisi = Entry(self.sol, width=30)
        self.Kisisayisi.place(x=430, y=220)
        self.Kayit = Button(self.sol, text="Rezervasyon Yap", width=20, height=2, bg='red', fg='White',font = ('calibri bold',12),
                            command=self.kayitlar)
        self.Kayit.place(x=450, y=300)

    def kayitlar(self):
        self.isim = self.isim.get()
        self.Telefon = self.Telefon.get()
        self.Kisisayisi = self.Kisisayisi.get()

        if self.isim == '' or self.Telefon == '' or self.Kisisayisi == '':
            tkinter.messagebox.showinfo("Bilgi" , "Tüm boş kutuları doldurun.")
        else:
            c.execute('CREATE TABLE IF NOT EXISTS rezervasyon (isim TEXT,Telefon TEXT,Kisisayisi TEXT)')
            c.execute('INSERT INTO rezervasyon(isim,Telefon,Kisisayisi) VALUES(?,?,?)',(self.isim, self.Telefon,self.Kisisayisi,))
            conn.commit()
            tkinter.messagebox.showinfo("Bilgi", "Rezervasyonunuz alındı.")
            self.pencere.destroy()

class restoransiparis:
    def __init__(self, pencere):
        self.pencere = pencere
        self.sol = Frame(pencere, width=800, height=720, bg='White')
        self.sol.pack(side=LEFT)
        self.sag = Frame(pencere, width=400, height=720, bg='White')
        self.sag.pack(side=RIGHT)

        self.baslik = Label(self.sol, text="ATEŞ RESTORAN", font=('calibri 40 bold'), fg='black', bg='White')
        self.baslik.place(x=330, y=10)

        self.Kebap = Label(self.sol, text="KEBAP : 30 tl", width=20, font=(' bold', 10))
        self.Kebap.place(x=10, y=100)
        self.Kebap_gir = Entry(self.sol, width=30)
        self.Kebap_gir.place(x=200, y=100)

        self.Tost = Label(self.sol, text="TOST : 10 tl", width=20, font=(' bold', 10))
        self.Tost.place(x=10, y=140)
        self.Tost_gir = Entry(self.sol, width=30)
        self.Tost_gir.place(x=200, y=140)

        self.Lahmacun = Label(self.sol, text="Lahmacun : 15 tl", width=20, font=(' bold', 10))
        self.Lahmacun.place(x=10, y=180)
        self.Lahmacun_gir = Entry(self.sol, width=30)
        self.Lahmacun_gir.place(x=200, y=180)

        self.tavuk = Label(self.sol, text="Tavuk Izgara : 15 tl", width=20, font=(' bold', 10))
        self.tavuk.place(x=10, y=220)
        self.tavuk_gir = Entry(self.sol, width=30)
        self.tavuk_gir.place(x=200, y=220)

        self.burger = Label(self.sol, text="Burger : 12 tl", width=20, font=(' bold', 10))
        self.burger.place(x=10, y=260)
        self.burger_gir = Entry(self.sol, width=30)
        self.burger_gir.place(x=200, y=260)

        self.Makarna = Label(self.sol, text="Makarna : 7 tl", width=20, font=(' bold', 10))
        self.Makarna.place(x=10, y=300)
        self.Makarna_gir = Entry(self.sol, width=30)
        self.Makarna_gir.place(x=200, y=300)

        self.Pide = Label(self.sol, text="PİDE : 20 tl", width=20, font=(' bold', 10))
        self.Pide.place(x=430, y=100)
        self.Pide_gir = Entry(self.sol, width=30)
        self.Pide_gir.place(x=620, y=100)

        self.kunefe = Label(self.sol, text="Künefe : 7 tl", width=20, font=(' bold', 10))
        self.kunefe.place(x=430, y=140)
        self.kunefe_gir = Entry(self.sol, width=30)
        self.kunefe_gir.place(x=620, y=140)

        self.sutlac = Label(self.sol, text="Sütlaç : 5 tl", width=20, font=(' bold', 10))
        self.sutlac.place(x=430, y=180)
        self.sutlac_gir = Entry(self.sol, width=30)
        self.sutlac_gir.place(x=620, y=180)

        self.Kola = Label(self.sol, text="Kola : 3 tl", width=20, font=(' bold', 10))
        self.Kola.place(x=430, y=220)
        self.Kola_gir = Entry(self.sol, width=30)
        self.Kola_gir.place(x=620, y=220)

        self.Ayran = Label(self.sol, text="Ayran : 3 tl", width=20, font=(' bold', 10))
        self.Ayran.place(x=430, y=260)
        self.Ayran_gir = Entry(self.sol, width=30)
        self.Ayran_gir.place(x=620, y=260)

        self.Su = Label(self.sol, text="Su : 2 tl", width=20, font=(' bold', 10))
        self.Su.place(x=430, y=300)
        self.Su_gir = Entry(self.sol, width=30)
        self.Su_gir.place(x=620, y=300)

        self.kayit = Button(self.sol, text="HESAP TOPLAMI", width=30, height=2, bg='black', fg='white',font =('calibri 12 bold'),
                            command=self.siparisler)
        self.kayit.place(x=300, y=370)

    def siparisler(self):

        self.val1 = self.Kebap_gir.get()
        self.val2 = self.Pide_gir.get()
        self.val3 = self.Lahmacun_gir.get()
        self.val4 = self.tavuk_gir.get()
        self.val5 = self.burger_gir.get()
        self.val6 = self.Makarna_gir.get()
        self.val7 = self.Tost_gir.get()
        self.val8 = self.kunefe_gir.get()
        self.val9 = self.sutlac_gir.get()
        self.val10 = self.Kola_gir.get()
        self.val11 = self.Ayran_gir.get()
        self.val12 = self.Su_gir.get()

        if (
                self.val1 == '' and self.val2 == '' and self.val3 == '' and self.val4 == '' and self.val5 == '' and self.val6 == ''
                and self.val7==''and self.val8 == ''and self.val9 == ''and self.val10 == '' and self.val11 == '' and self.val12 == ''):
            tkinter.messagebox.showinfo("Bilgi", "Hiç siparişiniz yok.")
        else:
            if self.val1 == '':
                self.val1 = '0'
            if self.val2 == '':
                self.val2 = '0'
            if self.val3 == '':
                self.val3 = '0'
            if self.val4 == '':
                self.val4 = '0'
            if self.val5 == '':
                self.val5 = '0'
            if self.val6 == '':
                self.val6 = '0'
            if self.val7 == '':
                self.val7 = '0'
            if self.val8 == '':
                self.val8 = '0'
            if self.val9 == '':
                self.val9 = '0'
            if self.val10 == '':
                self.val10 = '0'
            if self.val11 == '':
                self.val11 = '0'
            if self.val12 == '':
                self.val12 = '0'
            self.blok = Label(self.sag, text=" HESAP ", font=('calibri 30 bold'), fg='Red', bg='white')
            self.blok.place(x=0, y=0)
            toplam = 0
            self.kutu = Text(self.sag, width=50, height=40)
            self.kutu.place(x=20, y=60)
            q = 30 * int(self.val1)
            toplam += q
            self.kutu.insert(END, " " + str(self.val1) +" Porsiyon Kebap --> " + str(q)+" tl" + "\n")
            q = 20 * int(self.val2)
            toplam += q
            self.kutu.insert(END, " " + str(self.val2) +" Porsiyon Pide --> " + str(q)+" tl" + "\n")
            q = 15 * int(self.val3)
            toplam += q
            self.kutu.insert(END, " " + str(self.val3) +" Porsiyon Lahmacun --> " + str(q)+" tl" + "\n")
            q = 15 * int(self.val4)
            toplam += q
            self.kutu.insert(END, " " + str(self.val4) +" Porsiyon Tavuk Izgara --> " + str(q)+" tl" + "\n")
            q = 12 * int(self.val5)
            toplam += q
            self.kutu.insert(END, " " + str(self.val5) +" Porsiyon Burger --> " + str(q)+" tl" + "\n")
            q = 7 * int(self.val6)
            toplam += q
            self.kutu.insert(END, " " + str(self.val6) +" Porsiyon Makarna --> " + str(q)+" tl" + "\n")
            q = 10 * int(self.val7)
            toplam += q
            self.kutu.insert(END, " " + str(self.val7) +" Porsiyon Tost --> " + str(q)+" tl" + "\n")
            q = 7 * int(self.val8)
            toplam += q
            self.kutu.insert(END, " " + str(self.val8) +" Porsiyon Künefe --> " + str(q)+" tl" + "\n")
            q = 5 * int(self.val9)
            toplam += q
            self.kutu.insert(END, " " + str(self.val9) +" Porsiyon Sütlaç --> " + str(q)+" tl" + "\n")
            q = 3 * int(self.val10)
            toplam += q
            self.kutu.insert(END, " " + str(self.val10) +" Adet Kola --> " + str(q)+" tl" + "\n")
            q = 3 * int(self.val11)
            toplam += q
            self.kutu.insert(END, " " + str(self.val11) +" Adet Ayran --> " + str(q)+" tl" + "\n")
            q = 2 * int(self.val12)
            toplam += q
            self.kutu.insert(END, " " + str(self.val12) +" Adet Su --> " + str(q)+" tl" + "\n")
            self.kutu.insert(END, " Toplam Hesap = " + str(toplam) + "  tl.")
            self.val13 = str(toplam)
            self.kayit = Button(self.sag, text="Öde", width=20, height=2, bg='black', fg='white', command=self.odeme)
            self.kayit.place(x=200, y=350)

    def odeme(self):
        c.execute(
            'CREATE TABLE IF NOT EXISTS siparisler(Kebap TEXT,Pide TEXT,Tost TEXT,Lahmacun TEXT,'
            'tavuk TEXT,burger TEXT,Makarna TEXT,kunefe TEXT,sutlac TEXT,Kola TEXT,Ayran TEXT,Su TEXT,Hesap TEXT)')
        c.execute('INSERT INTO siparisler(Kebap,Pide,Tost,Lahmacun,tavuk,burger,Makarna,kunefe,sutlac,Kola,Ayran,'
                  'Su,Hesap) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6,self.val7,self.val8,
                   self.val9,self.val10,self.val11,self.val12,self.val13))
        conn.commit()
        tkinter.messagebox.showinfo("Bilgi", "Yine bekleriz.")
        self.pencere.destroy()


class anasayfa:

    def __init__(self, giris):
        self.giris = giris
        self.sol = Frame(giris, width=1000, height=500, bg='White')
        self.sol.pack(side=LEFT)
        self.baslik = Label(self.sol, text="ATEŞ RESTORAN", font=('calibri 40 bold'), fg='red', bg='White')
        self.baslik.place(x=330, y=40)
        self.baslik = Label(self.sol, text="HOŞGELDİNİZ", font=('calibri 20 bold'), fg='red', bg='White')
        self.baslik.place(x=430, y=100)

        def butontikla():
            but2 = Tk()
            det = rezervasyonyap(but2)
            but2.geometry("1000x500")
            but2.resizable(False, False)
            but2.mainloop()

        def butontikla2():
            but2 = Tk()
            siparisler = restoransiparis(but2)
            but2.geometry("1200x500")
            but2.resizable(False, False)
            but2.mainloop()

        self.a = Button(giris, text="REZERVASYON YAP", command=butontikla, width=50, height=2, fg="white", bg="black",font = "calibri 13 bold")
        self.c = Button(giris, text="SİPARİŞ VER", command=butontikla2, width=50, height=2, fg="white", bg="black",font = "calibri 13 bold")

        self.a.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.c.place(relx=0.5, rely=0.6, anchor=CENTER)


mf = Tk()
m = anasayfa(mf)
mf.geometry("1000x500")
mf.configure(background="White")
mf.resizable(0, 0)
mf.mainloop()