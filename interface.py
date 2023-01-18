import db
import queryINSERT
import querySELECT
import queryUPDATE
import queryDELETE

from tkinter import *
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText

# def mainpage(root):
#     frame1 = Frame(master=root, borderwidth=1, relief=SOLID)
#     label1 = Label(master=frame1,  text="frame1")
#     label1.pack(anchor=NW)
#     frame1.pack(anchor=NW, fill=X, padx=5, pady=5)


def changeParameters(root):
    def changeP():
        db.changeParametrs(host.get(), port.get(), user.get(), password.get(), database.get())

    frame1 = Frame(master=root, borderwidth=1)
    label1 = Label(master=frame1,  text="change Parameters")
    label1.pack()

    host=StringVar()
    port = StringVar()
    user = StringVar()
    password = StringVar()
    database = StringVar()

    hostEnt=Entry(master=frame1,textvariable=host)
    portEnt = Entry(master=frame1,textvariable=port)
    userEnt = Entry(master=frame1, textvariable=user)
    passwordEnt = Entry(master=frame1, textvariable=password)
    dbEnt = Entry(master=frame1, textvariable=database)

    hostEnt.insert(0,db.parametrs['host'])
    portEnt.insert(0,db.parametrs['port'])
    userEnt.insert(0,db.parametrs['user'])
    passwordEnt.insert(0,db.parametrs['password'])
    dbEnt.insert(0,db.parametrs['db'])

    hostEnt.pack()
    portEnt.pack()
    userEnt.pack()
    passwordEnt.pack()
    dbEnt.pack()

    button1 = Button(master=frame1, text='ввод', command=changeP)
    button1.pack()
    frame1.pack(fill=BOTH)


def initdb(mainframe, word_editor):
    label = Label(master=mainframe, text="\n\n")
    label.pack()
    def INITDB():
        text1 = db.initDataBase()
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='создать таблицы', command=INITDB)
    button1.pack()
##########################################################################

def framePeopleINSERT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="INSERT")
    label2 = Label(master=mainframe, text="Введите фио, дату рождения,название программы и номер выпуска")
    label1.pack()
    label2.pack()
    fullname = StringVar()
    born = StringVar()
    nameProgram = StringVar()
    releaseNumber = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=born)
    Entry3 = Entry(master=mainframe, textvariable=nameProgram)
    Entry4 = Entry(master=mainframe, textvariable=releaseNumber)
    Entry1.pack()
    Entry2.pack()
    Entry3.pack()
    Entry4.pack()
    def INSERT():
        text1 = queryINSERT.insertPeople(fullname.get(), born.get(), nameProgram.get(), releaseNumber.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='ввод', command=INSERT)
    button1.pack()

def framePeopleSELECT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="SELECT")
    label1.pack()
    def SELECT():
        text1 = querySELECT.selectPeople()
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='вывод всего содержимого таблицы', command=SELECT)
    button1.pack()


    label2 = Label(master=mainframe, text="Введите название программы и номер")
    label2.pack()
    nameProgram = StringVar()
    releaseNumber = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=releaseNumber)
    Entry1.pack()
    Entry2.pack()
    def keySELECTp():
        text1 = querySELECT.selectKeyPeopleProgram(nameProgram.get(), releaseNumber.get())
        print(text1)
        word_editor.insert(END, text1)
    button2 = Button(master=mainframe, text='вывод по ключу', command=keySELECTp)
    button2.pack()

    label3= Label(master=mainframe, text="Введите фио и дату рождения")
    label3.pack()
    fullname = StringVar()
    born = StringVar()
    Entry3 = Entry(master=mainframe, textvariable=fullname)
    Entry4 = Entry(master=mainframe, textvariable=born)
    Entry3.pack()
    Entry4.pack()
    def keySELECTn():
        text1 = querySELECT.selectKeyPeopleProgram(fullname.get(), born.get())
        print(text1)
        word_editor.insert(END, text1)
    button3 = Button(master=mainframe, text='вывод по ключу', command=keySELECTn)
    button3.pack()



def framePeopleUPDATE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите фио, дату рождения,название программы и номер выпуска")
    label2 = Label(master=mainframe, text="Введите новые значения фио, дату рождения,название программы и номер выпуска")
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()
    var8 = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=var1)
    Entry2 = Entry(master=mainframe, textvariable=var2)
    Entry3 = Entry(master=mainframe, textvariable=var3)
    Entry4 = Entry(master=mainframe, textvariable=var4)
    Entry5 = Entry(master=mainframe, textvariable=var5)
    Entry6 = Entry(master=mainframe, textvariable=var6)
    Entry7 = Entry(master=mainframe, textvariable=var7)
    Entry8 = Entry(master=mainframe, textvariable=var8)
    label1.pack()
    Entry1.pack()
    Entry2.pack()
    Entry3.pack()
    Entry4.pack()
    label2.pack()
    Entry5.pack()
    Entry6.pack()
    Entry7.pack()
    Entry8.pack()
    def UPDATE():
        text1 = queryUPDATE.updatePeople(var1.get(),
                                         var2.get(),
                                         var3.get(),
                                         var4.get(),
                                         var5.get(),
                                         var6.get(),
                                         var7.get(),
                                         var8.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='UPDATE', command=UPDATE)
    button1.pack()

def framePeopleDELETE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите фио, дату рождения,название программы и номер выпуска")
    label1.pack()
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=var1)
    Entry2 = Entry(master=mainframe, textvariable=var2)
    Entry3 = Entry(master=mainframe, textvariable=var3)
    Entry4 = Entry(master=mainframe, textvariable=var4)
    Entry1.pack()
    Entry2.pack()
    Entry3.pack()
    Entry4.pack()
    def DELETE():
        text1 = queryDELETE.deletePeople(var1.get(),
                                         var2.get(),
                                         var3.get(),
                                         var4.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='удалить', command=DELETE)
    button1.pack()


def framePeople(mainframe, word_editor):
    label = Label(master=mainframe, text="")
    label.pack()
    chooseQUERY = ttk.Notebook(master=mainframe)
    chooseQUERY.pack(fill=BOTH)

    frameINSERT = ttk.Frame(master=chooseQUERY)
    frameSELECT = ttk.Frame(master=chooseQUERY)
    frameUPDATE = ttk.Frame(master=chooseQUERY)
    frameDELETE = ttk.Frame(master=chooseQUERY)

    frameINSERT.pack(fill=BOTH)
    frameSELECT.pack(fill=BOTH)
    frameUPDATE.pack(fill=BOTH)
    frameDELETE.pack(fill=BOTH)

    chooseQUERY.add(frameINSERT, text="INSERT")
    chooseQUERY.add(frameSELECT, text="SELECT")
    chooseQUERY.add(frameUPDATE, text="UPDATE")
    chooseQUERY.add(frameDELETE, text="DELETE")

    framePeopleINSERT(frameINSERT, word_editor)
    framePeopleSELECT(frameSELECT, word_editor)
    framePeopleUPDATE(frameUPDATE, word_editor)
    framePeopleDELETE(frameDELETE, word_editor)

##########################################################################

def frameProgramReleaseINSERT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="INSERT")
    label2 = Label(master=mainframe, text="Введите название программы, номер выпуска и дату премьеры")
    label1.pack()
    label2.pack()
    nameProgram = StringVar()
    channel = StringVar()
    rating = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=channel)
    Entry3 = Entry(master=mainframe, textvariable=rating)
    Entry1.pack()
    Entry2.pack()
    Entry3.pack()
    def INSERT():
        text1 = queryINSERT.insertProgramRelease(nameProgram.get(), channel.get(), rating.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='ввод', command=INSERT)
    button1.pack()

def frameProgramReleaseSELECT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="SELECT")
    label1.pack()
    def SELECT():
        text1 = querySELECT.selectProgramRelease()
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='вывод всего содержимого таблицы', command=SELECT)
    button1.pack()

    label2 = Label(master=mainframe, text="Введите название программы и номер")
    label2.pack()
    nameProgram = StringVar()
    releaseNumber = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=releaseNumber)
    Entry1.pack()
    Entry2.pack()
    def keySELECT():
        text1 = querySELECT.selectKeyProgramRelease(nameProgram.get(), releaseNumber.get())
        print(text1)
        word_editor.insert(END, text1)
    button2 = Button(master=mainframe, text='вывод по ключу', command=keySELECT)
    button2.pack()


def frameProgramReleaseUPDATE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название программы")
    label2 = Label(master=mainframe, text="Введите новые значения название программы, номер выпуска и дату премьеры")
    nameProgram = StringVar()
    releaseNumber = StringVar()
    newNameProgram = StringVar()
    newNumber = StringVar()
    premiere = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=releaseNumber)
    Entry3 = Entry(master=mainframe, textvariable=newNameProgram)
    Entry4 = Entry(master=mainframe, textvariable=newNumber)
    Entry5 = Entry(master=mainframe, textvariable=premiere)
    label1.pack()
    Entry1.pack()    
    Entry2.pack()
    label2.pack()
    Entry3.pack()
    Entry4.pack()
    Entry5.pack()
    def UPDATE():
        text1 = queryUPDATE.updateProgramRelease(nameProgram.get(),
                                                 releaseNumber.get(),
                                                 newNameProgram.get(),
                                                 newNumber.get(),
                                                 premiere.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='UPDATE', command=UPDATE)
    button1.pack()

def frameProgramReleaseDELETE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название программы и номер")
    label1.pack()
    nameProgram = StringVar()
    releaseNumber = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=releaseNumber)
    Entry1.pack()
    Entry2.pack()
    def DELETE():
        text1 = queryDELETE.deleteProgramRelease(nameProgram.get(), releaseNumber.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='удалить', command=DELETE)
    button1.pack()


def frameProgramRelease(mainframe, word_editor):
    label = Label(master=mainframe, text="")
    label.pack()
    chooseQUERY = ttk.Notebook(master=mainframe)
    chooseQUERY.pack(fill=BOTH)

    frameINSERT = ttk.Frame(master=chooseQUERY)
    frameSELECT = ttk.Frame(master=chooseQUERY)
    frameUPDATE = ttk.Frame(master=chooseQUERY)
    frameDELETE = ttk.Frame(master=chooseQUERY)

    frameINSERT.pack(fill=BOTH)
    frameSELECT.pack(fill=BOTH)
    frameUPDATE.pack(fill=BOTH)
    frameDELETE.pack(fill=BOTH)

    chooseQUERY.add(frameINSERT, text="INSERT")
    chooseQUERY.add(frameSELECT, text="SELECT")
    chooseQUERY.add(frameUPDATE, text="UPDATE")
    chooseQUERY.add(frameDELETE, text="DELETE")

    frameProgramReleaseINSERT(frameINSERT, word_editor)
    frameProgramReleaseSELECT(frameSELECT, word_editor)
    frameProgramReleaseUPDATE(frameUPDATE, word_editor)
    frameProgramReleaseDELETE(frameDELETE, word_editor)

##########################################################################

def frameTVProgramINSERT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="INSERT")
    label2 = Label(master=mainframe, text="Введите название программы, канала и режиссера")
    label1.pack()
    label2.pack()
    nameProgram = StringVar()
    channel = StringVar()
    rating = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=channel)
    Entry3 = Entry(master=mainframe, textvariable=rating)
    Entry1.pack()
    Entry2.pack()
    Entry3.pack()
    def INSERT():
        text1 = queryINSERT.insertTVProgram(nameProgram.get(), channel.get(), rating.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='ввод', command=INSERT)
    button1.pack()

def frameTVProgramSELECT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="SELECT")
    label1.pack()
    def SELECT():
        text1 = querySELECT.selectTVProgram()
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='вывод всего содержимого таблицы', command=SELECT)
    button1.pack()

    label2 = Label(master=mainframe, text="Введите название программы")
    label2.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()
    def keySELECT():
        text1 = querySELECT.selectKeyTVProgram(channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button2 = Button(master=mainframe, text='вывод по ключу', command=keySELECT)
    button2.pack()


def frameTVProgramUPDATE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название программы")
    label2 = Label(master=mainframe, text="Введите новые значения название программы, канала и режиссера")
    nameProgram = StringVar()
    newNameProgram = StringVar()
    newchannel = StringVar()
    rating = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=newNameProgram)
    Entry3 = Entry(master=mainframe, textvariable=newchannel)
    Entry4 = Entry(master=mainframe, textvariable=rating)
    label1.pack()
    Entry1.pack()
    label2.pack()
    Entry2.pack()
    Entry3.pack()
    Entry4.pack()
    def UPDATE():
        text1 = queryUPDATE.updateTVProgram(nameProgram.get(), newNameProgram.get(), newchannel.get(), rating.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='UPDATE', command=UPDATE)
    button1.pack()

def frameTVProgramDELETE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название программы")
    label1.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()
    def DELETE():
        text1 = queryDELETE.deleteTVProgram(channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='удалить', command=DELETE)
    button1.pack()


def frameTVProgram(mainframe, word_editor):
    label = Label(master=mainframe, text="")
    label.pack()
    chooseQUERY = ttk.Notebook(master=mainframe)
    chooseQUERY.pack(fill=BOTH)

    frameINSERT = ttk.Frame(master=chooseQUERY)
    frameSELECT = ttk.Frame(master=chooseQUERY)
    frameUPDATE = ttk.Frame(master=chooseQUERY)
    frameDELETE = ttk.Frame(master=chooseQUERY)

    frameINSERT.pack(fill=BOTH)
    frameSELECT.pack(fill=BOTH)
    frameUPDATE.pack(fill=BOTH)
    frameDELETE.pack(fill=BOTH)

    chooseQUERY.add(frameINSERT, text="INSERT")
    chooseQUERY.add(frameSELECT, text="SELECT")
    chooseQUERY.add(frameUPDATE, text="UPDATE")
    chooseQUERY.add(frameDELETE, text="DELETE")


    frameTVProgramINSERT(frameINSERT, word_editor)
    frameTVProgramSELECT(frameSELECT, word_editor)
    frameTVProgramUPDATE(frameUPDATE, word_editor)
    frameTVProgramDELETE(frameDELETE, word_editor)

##########################################################################

def frameRatingINSERT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="INSERT")
    label2 = Label(master=mainframe, text="Введите название программы, канала и рейтинг")
    label1.pack()
    label2.pack()
    nameProgram = StringVar()
    channel = StringVar()
    rating = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=channel)
    Entry3 = Entry(master=mainframe, textvariable=rating)
    Entry1.pack()
    Entry2.pack()
    Entry3.pack()

    def INSERT():
        text1 = queryINSERT.insertRating(nameProgram.get(), channel.get(), rating.get())
        print(text1)
        word_editor.insert(END, text1)

    button1 = Button(master=mainframe, text='ввод', command=INSERT)
    button1.pack()


def frameRatingSELECT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="SELECT")
    label1.pack()

    def SELECT():
        text1 = querySELECT.selectRating()
        print(text1)
        word_editor.insert(END, text1)

    button1 = Button(master=mainframe, text='вывод всего содержимого таблицы', command=SELECT)
    button1.pack()

    label2 = Label(master=mainframe, text="Введите название программы")
    label2.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()

    def keySELECT():
        text1 = querySELECT.selectKeyRating(channel.get())
        print(text1)
        word_editor.insert(END, text1)

    button2 = Button(master=mainframe, text='вывод по ключу', command=keySELECT)
    button2.pack()


def frameRatingUPDATE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название программы")
    label2 = Label(master=mainframe, text="Введите новые значения программы, канала и рейтинга")
    label1.pack()
    nameProgram = StringVar()
    newNameProgram = StringVar()
    newchannel = StringVar()
    rating = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=nameProgram)
    Entry2 = Entry(master=mainframe, textvariable=newNameProgram)
    Entry3 = Entry(master=mainframe, textvariable=newchannel)
    Entry4 = Entry(master=mainframe, textvariable=rating)
    label1.pack()
    Entry1.pack()
    label2.pack()
    Entry2.pack()
    Entry3.pack()
    Entry4.pack()

    def UPDATE():
        text1 = queryUPDATE.updateOwnerChannel(nameProgram.get(),
                                               newNameProgram.get(),
                                               newchannel.get(),
                                               rating.get())
        print(text1)
        word_editor.insert(END, text1)

    button1 = Button(master=mainframe, text='UPDATE', command=UPDATE)
    button1.pack()


def frameRatingDELETE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название программы")
    label1.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()

    def DELETE():
        text1 = queryDELETE.deleteRating(channel.get())
        print(text1)
        word_editor.insert(END, text1)

    button1 = Button(master=mainframe, text='удалить', command=DELETE)
    button1.pack()


def frameRating(mainframe, word_editor):
    label = Label(master=mainframe, text="")
    label.pack()
    chooseQUERY = ttk.Notebook(master=mainframe)
    chooseQUERY.pack(fill=BOTH)

    frameINSERT = ttk.Frame(master=chooseQUERY)
    frameSELECT = ttk.Frame(master=chooseQUERY)
    frameUPDATE = ttk.Frame(master=chooseQUERY)
    frameDELETE = ttk.Frame(master=chooseQUERY)

    frameINSERT.pack(fill=BOTH)
    frameSELECT.pack(fill=BOTH)
    frameUPDATE.pack(fill=BOTH)
    frameDELETE.pack(fill=BOTH)

    chooseQUERY.add(frameINSERT, text="INSERT")
    chooseQUERY.add(frameSELECT, text="SELECT")
    chooseQUERY.add(frameUPDATE, text="UPDATE")
    chooseQUERY.add(frameDELETE, text="DELETE")

    frameRatingINSERT(frameINSERT, word_editor)
    frameRatingSELECT(frameSELECT, word_editor)
    frameRatingUPDATE(frameUPDATE, word_editor)
    frameRatingDELETE(frameDELETE, word_editor)


##########################################################################

def frameOwnerChannelINSERT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="INSERT")
    label2 = Label(master=mainframe, text="Введите название канала и владельца")
    label1.pack()
    label2.pack()
    channel = StringVar()
    broadcast = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry2 = Entry(master=mainframe, textvariable=broadcast)
    Entry1.pack()
    Entry2.pack()

    def INSERT():
        text1 = queryINSERT.insertOwnerChannel(channel.get(), broadcast.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='ввод', command=INSERT)
    button1.pack()

def frameOwnerChannelSELECT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="SELECT")
    label1.pack()
    def SELECT():
        text1 = querySELECT.selectOwnerChannel()
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='вывод всего содержимого таблицы', command=SELECT)
    button1.pack()

    label2 = Label(master=mainframe, text="Введите название канала")
    label2.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()
    def keySELECT():
        text1 = querySELECT.selectKeyOwnerChannel(channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button2 = Button(master=mainframe, text='вывод по ключу', command=keySELECT)
    button2.pack()


def frameOwnerChannelUPDATE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название канала")
    label2 = Label(master=mainframe, text="Введите новые значения название канала и владельца")
    label1.pack()
    channel = StringVar()
    newchannel = StringVar()
    broadcast = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry2 = Entry(master=mainframe, textvariable=newchannel)
    Entry3 = Entry(master=mainframe, textvariable=broadcast)
    label1.pack()
    Entry1.pack()
    label2.pack()
    Entry2.pack()
    Entry3.pack()
    def UPDATE():
        text1 = queryUPDATE.updateOwnerChannel(newchannel.get(),broadcast.get(),channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='UPDATE', command=UPDATE)
    button1.pack()

def frameOwnerChannelDELETE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название канала")
    label1.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()
    def DELETE():
        text1 = queryDELETE.deleteOwnerChannel(channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='удалить', command=DELETE)
    button1.pack()


def frameOwnerChannel(mainframe, word_editor):
    label = Label(master=mainframe, text="")
    label.pack()

    chooseQUERY = ttk.Notebook(master=mainframe)
    chooseQUERY.pack(fill=BOTH)


    frameINSERT = ttk.Frame(master=chooseQUERY)
    frameSELECT = ttk.Frame(master=chooseQUERY)
    frameUPDATE = ttk.Frame(master=chooseQUERY)
    frameDELETE = ttk.Frame(master=chooseQUERY)

    frameINSERT.pack(fill=BOTH)
    frameSELECT.pack(fill=BOTH)
    frameUPDATE.pack(fill=BOTH)
    frameDELETE.pack(fill=BOTH)

    chooseQUERY.add(frameINSERT, text="INSERT")
    chooseQUERY.add(frameSELECT, text="SELECT")
    chooseQUERY.add(frameUPDATE, text="UPDATE")
    chooseQUERY.add(frameDELETE, text="DELETE")


    frameOwnerChannelINSERT(frameINSERT, word_editor)
    frameOwnerChannelSELECT(frameSELECT, word_editor)
    frameOwnerChannelUPDATE(frameUPDATE, word_editor)
    frameOwnerChannelDELETE(frameDELETE, word_editor)

##########################################################################
def frameTVchannelINSERT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="INSERT")
    label2 = Label(master=mainframe, text="Введите название канала и способ трансляции")
    label1.pack()
    label2.pack()
    channel = StringVar()
    broadcast = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry2 = Entry(master=mainframe, textvariable=broadcast)
    Entry1.pack()
    Entry2.pack()

    def INSERT():
        text1 = queryINSERT.insertTVchannel(channel.get(),broadcast.get())
        print(text1)
        word_editor.insert(END,text1)
    button1 = Button(master=mainframe, text='ввод', command=INSERT)
    button1.pack()

def frameTVchannelSELECT(mainframe, word_editor):
    label1 = Label(master=mainframe, text="SELECT")
    label1.pack()
    def SELECT():
        text1 = querySELECT.selectTVchannel()
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='вывод всего содержимого таблицы', command=SELECT)
    button1.pack()

    label2 = Label(master=mainframe, text="Введите название канала")
    label2.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()
    def keySELECT():
        text1 = querySELECT.selectKeyTVchannel(channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button2 = Button(master=mainframe, text='вывод по ключу', command=keySELECT)
    button2.pack()


def frameTVchannelUPDATE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название канала")
    label2 = Label(master=mainframe, text="Введите новые значения название канала и способ трансляции")
    label1.pack()
    channel = StringVar()
    newchannel = StringVar()
    broadcast = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry2 = Entry(master=mainframe, textvariable=newchannel)
    Entry3 = Entry(master=mainframe, textvariable=broadcast)
    label1.pack()
    Entry1.pack()
    label2.pack()
    Entry2.pack()
    Entry3.pack()
    def UPDATE():
        text1 = queryUPDATE.updateTVchannel(newchannel.get(),broadcast.get(),channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='UPDATE', command=UPDATE)
    button1.pack()

def frameTVchannelDELETE(mainframe, word_editor):
    label1 = Label(master=mainframe, text="Введите название канала")
    label1.pack()
    channel = StringVar()
    Entry1 = Entry(master=mainframe, textvariable=channel)
    Entry1.pack()
    def DELETE():
        text1 = queryDELETE.deleteTVchannel(channel.get())
        print(text1)
        word_editor.insert(END, text1)
    button1 = Button(master=mainframe, text='удалить', command=DELETE)
    button1.pack()


def frameTVchannel(mainframe, word_editor):
    label = Label(master=mainframe, text="")
    label.pack()
    chooseQUERY = ttk.Notebook(master=mainframe)
    chooseQUERY.pack(fill=BOTH)


    frameINSERT = ttk.Frame(master=chooseQUERY)
    frameSELECT = ttk.Frame(master=chooseQUERY)
    frameUPDATE = ttk.Frame(master=chooseQUERY)
    frameDELETE = ttk.Frame(master=chooseQUERY)

    frameINSERT.pack(fill=BOTH)
    frameSELECT.pack(fill=BOTH)
    frameUPDATE.pack(fill=BOTH)
    frameDELETE.pack(fill=BOTH)

    chooseQUERY.add(frameINSERT, text="INSERT")
    chooseQUERY.add(frameSELECT, text="SELECT")
    chooseQUERY.add(frameUPDATE, text="UPDATE")
    chooseQUERY.add(frameDELETE, text="DELETE")


    frameTVchannelINSERT(frameINSERT, word_editor)
    frameTVchannelSELECT(frameSELECT, word_editor)
    frameTVchannelUPDATE(frameUPDATE, word_editor)
    frameTVchannelDELETE(frameDELETE, word_editor)

##########################################################################





def tabsNoteook(root, word_editor):
    frameTabsNoteook = Frame(master=root)
    frameTabsNoteook.pack(fill=BOTH)

    label = Label(master=frameTabsNoteook, text="")
    label.pack()

    chooseTabs = ttk.Notebook(master=frameTabsNoteook)
    chooseTabs.pack(fill=BOTH)

    frame1 = ttk.Frame(master=chooseTabs)
    frame2 = ttk.Frame(master=chooseTabs)
    frame3 = ttk.Frame(master=chooseTabs)
    frame4 = ttk.Frame(master=chooseTabs)
    frame5 = ttk.Frame(master=chooseTabs)
    frame6 = ttk.Frame(master=chooseTabs)

    frame1.pack(fill=BOTH)
    frame2.pack(fill=BOTH)
    frame3.pack(fill=BOTH)
    frame4.pack(fill=BOTH)
    frame5.pack(fill=BOTH)
    frame6.pack(fill=BOTH)

    chooseTabs.add(frame1, text="TVchannel")
    chooseTabs.add(frame2, text="OwnerChannel")
    chooseTabs.add(frame3, text="Rating")
    chooseTabs.add(frame4, text="TVProgram")
    chooseTabs.add(frame5, text="ProgramRelease")
    chooseTabs.add(frame6, text="People")

    frameTVchannel(frame1, word_editor)
    frameOwnerChannel(frame2, word_editor)
    frameRating(frame3, word_editor)
    frameTVProgram(frame4, word_editor)
    frameProgramRelease(frame5, word_editor)
    framePeople(frame6, word_editor)


def dbInterface():
    root = Tk()
    root.title("клиент postgresql")
    root.geometry("600x500")

    chooseTabs = ttk.Notebook(master=root)
    chooseTabs.pack(fill=BOTH)

    frame1 = ttk.Frame(master=chooseTabs)
    frame2 = ttk.Frame(master=chooseTabs)

    word_editor = ScrolledText(master=frame2, wrap="word")

    changeParameters(frame1)
    tabsNoteook(frame2, word_editor)
    initdb(frame1, word_editor)

    frame1.pack(fill=BOTH)
    frame2.pack(fill=BOTH)
    chooseTabs.add(frame1, text="Настройки")
    chooseTabs.add(frame2, text="Таблицы")

    label1 = Label(master=frame2, text="output log ")
    label1.pack()
    #outputText = StringVar()

    word_editor.pack(fill=BOTH)
    #word_editor.insert(END,chars="qwerty")
    root.mainloop()


if __name__ == '__main__':
    dbInterface()

