#Imports
from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
from random import randint
import re
import webbrowser


#Patterns
pattern_calcul1 = r"[0-9]+(C|c)alcul(e|é|er)"
pattern_calcul2 = r"[0-9]+|(C|c)alcul(e|é|er)"
pattern_disc_bien1 = r"((B|b)ien)|((C|c|ç|S|s)a (V|v)a)|((H|h)eureu(x|(se)))|((C|c)ontent(e)?)"
pattern_disc_mal = r"((P|p)as)|((M|m)al)"
pattern_jeu = r"(J|j)(eu|(ou(er|e|é|ons)))"
pattern_parler = r"(P|p)arl(er|é|e|es)|(D|d)iscu(ter|té|te|ssion)"
pattern_lia = r"(E|e)s(|t)( ||-)tu|(T|t)('| |)a(pp|p)e(l|ll)e(s|)|(T|t)on( |)nom|(T|t)(u|)('| |)es q(u|)i"
pattern_météo = r"(M|m)(é|e)t(é|e)o|(T|t)emp(s|)|(t|T)emp(é|e)ratur(e|)"
pattern_quitter = r"(Q|q)(u|)i((tt)|t)((er)|é|e)|(A|a)u( |)revoi(r|)|(A|a)dieu"
pattern_traduction = r"(T|t)radu(ire|ction)"
pattern_utilisateur = r"(Q|q)ui( |)(S|s)ui(s|)|(m|M)on( |)(N|n)om|(J|j)e(| )m('| |)a(pp|p)e(ll|l)e"


#Fenêtre principale
window = Tk()
window.title("Lia")
window.iconbitmap("icone.ico")


#Fonctions
def aide():
        """Ouvre une fenêtre comportant une liste de possibilités lorsque l'utilisateur clique sur l'option correspondante dans la barre de menu,"""
        help_window = Tk()
        help_window.title("Aide")
        help_window.iconbitmap("icone.ico")
        help_list = Label(help_window, text= "Quelques exemples de ce que peut faire Lia:   \n • Afficher la météo\n • Discuter\n • Donner le nom de l'utilisateur\n • Donner son nom\n • Effectuer un calcul\n • Effectuer une recherche Internet \n • Exprimer un avis sur un film\n • Faire deviner un nombre à l'utilisateur\n • Quitter le logiciel\n • Traduire une phrase", bg= "white", fg= "DarkSlateGray").pack()


def calcul():
        """Détecte un calcul dans la saisie de l'utilisateur et demande confirmation pour l'effectuer"""
        if re.search(pattern_calcul1, input_get) or re.search(pattern_calcul2, input_get):
            calcul = re.sub(r"[A-Za-z]", "",input_get)
            rep = askokcancel("Calcul", "Voulez-vous effectuer ce calcul ? " + calcul)
            if rep==1:
                calcul = re.sub(r"[+]", "%2B",calcul)
                webbrowser.open('https://www.google.com/search?safe=strict&ei=j3j9WrSFPMObU9OnleAN&q=' + calcul)
                window.bell()
                messages.insert(INSERT, "[Lia]: Et voilà ! Y a-t-il autre chose que je puisse faire ?\n")
            else:
                window.bell()
                messages.insert(INSERT, "[Lia]: Désolée, j'ai mal compris, que puis-je faire pour vous?\n")


def couleur_fond():
        """Ouvre une fenêtre permettant de régler la couleur de fond lorsque l'utilisateur clique sur l'option correspondante dans la barre de menu,"""
        (triple, couleur) = askcolor()
        messages.config(bg=couleur)
        menu1.config(activebackground=couleur)
        menu2.config(activebackground=couleur)


def couleur_texte():
        """Ouvre une fenêtre permettant de régler la couleur du texte lorsque l'utilisateur clique sur l'option correspondante dans la barre de menu,"""
        (triple, couleur) = askcolor()
        messages.config(fg=couleur)
        menu1.config(activeforeground=couleur)
        menu2.config(activeforeground=couleur)


def créateurs():
        """Ouvre une fenêtre comportant des infos sur les créateurs lorsque l'utilisateur clique sur l'option correspondante dans la barre de menu,"""
        id_window = Tk()
        id_window.title("Créateurs")
        id_window.iconbitmap("icone.ico")
        id_list = Label(id_window, text= "BRUEL Maxime - HIAULT Lilian - TEISSEDRE Alexis\n ISN - Lycée Emile Duclaux - 15000 Aurillac - 2017/2018\n\n Merci d'utiliser Lia.", bg= "white", fg="DarkSlateGray").pack()


def detect_trad():
        """Detecte une demande de traduction et ouvre une fenêtre permettant de régler la langue de départ"""
        global mot_trad
        def depart():
            """Associe la langue de départ à une variable et ouvre une nouvelle fenêtre pour la langue d'arrivée."""
            global lang_dep
            global arrive_list
            global langue_list_window2
            lang_dep_index = depart_list.curselection()
            if lang_dep_index != ():
                lang_dep = depart_list.get(lang_dep_index)
                langue_list_window1.destroy()
                langue_list_window2 = Tk()
                langue_list_window2.title("Langue d'arrivée")
                arrive_list = Listbox(langue_list_window2, selectmode= SINGLE, activestyle= "none", relief= FLAT, selectbackground= "LightBlue", selectforeground="navy", width=60)
                langue_list_window2.iconbitmap("icone.ico")
                arrive_list.pack()
                for item in ["français", "anglais", "allemand", "espagnol", "chinois", "japonais", "arabe"]:
                    arrive_list.insert(END, item)
                Button(langue_list_window2, text="Valider", bg= "LightBlue", activebackground= "green", fg="green", activeforeground= "white", relief= GROOVE, command=arrive).pack()
            else:
                showerror("Erreur","Vous n'avez selectionné aucune langue!\nVeuillez réessayer.")
        def arrive():
            """Associe la langue d'arrivée à une variable et fournit la traduction depuis google traduction"""
            global lang_ar
            lang_ar_index = arrive_list.curselection()
            if lang_ar_index != ():
                lang_ar = arrive_list.get(lang_ar_index)
                dico = {"français":"fr", "anglais":"en", "allemand":"de","espagnol":"es","coreen":"ko","japonais":"ja","portugais":"pt","albanais":"sq","arabe":"ar","bielorusse":"be","bosniaque":"bs","birman":"my","bulgare":"bg","croate":"hr","hongrois":"hu","indonesien":"id","italien":"it","hindi":"hi","islandais":"is","irlandais":"ga","grec":"el","neerlandais":"nl","russe":'ru',"suedois":"sv","slovaque":"sk","tcheque":"cs","turc":"tr","ukrainien":"uk","vietnamien":"vi","norvegien":"no","hebreu":"iw","hawaien":"haw","latin":"la","chinois":"zh-CN"}
                a = dico[lang_dep]
                b = dico[lang_ar]
                webbrowser.open("https://translate.google.fr/?hl=#"+a+"/"+b+"/"+mot_trad)
                langue_list_window2.destroy()
                window.bell()
                messages.insert(INSERT, "[Lia]: Voici votre traduction de <" + mot_trad + "> depuis <" + lang_dep + "> vers <" + lang_ar +">. Que voulez-vous d'autre ?\n")
                input_user.set("")
            else:
                showerror("Erreur","Vous n'avez selectionné aucune langue!\nVeuillez réessayer.")
        if re.search(pattern_traduction, input_get):
            window.bell()
            mot_trad = input("Entrez ici ce que vous voulez traduire")
            langue_list_window1 = Tk()
            langue_list_window1.title("Langue de départ")
            depart_list = Listbox(langue_list_window1, selectmode= SINGLE, activestyle= "none", relief= FLAT, selectbackground= "LightBlue", selectforeground="navy", width=60)
            langue_list_window1.iconbitmap("icone.ico")
            depart_list.pack()
            for item in ["français", "anglais", "allemand", "espagnol", "chinois", "japonais", "arabe"]:
                depart_list.insert(END, item)
            Button(langue_list_window1, text="Valider", bg= "LightBlue", activebackground= "green", fg="green", activeforeground= "white", relief= GROOVE, command=depart).pack()


def discussion():
        """Permet une discussion basique avec l'utilisateur lorsqu'il le souhaite"""
        if re.search(pattern_parler, input_get):
            messages.insert(INSERT, "[Lia]: Comment-allez vous ? [Répondez dans la console Python] \n")
            phrase1 = input("Comment-allez vous ?")
            messages.insert(INSERT, "[Vous]: " + phrase1 + "\n")
            """Demande à l'utilisateur son humeur"""
            if re.search(pattern_disc_bien1, phrase1) and not re.search(pattern_disc_mal, phrase1):
                messages.insert(INSERT, "[Lia]: Tant mieux !\n")
                print("Tant mieux !")
            elif re.search(pattern_disc_mal, phrase1):
                messages.insert(INSERT, "[Lia]: C'est triste...\n")
                print("C'est triste...")
            else:
                messages.insert(INSERT, "[Lia]: Je suis désolée, je n'ai pas compris.\n")
                print("Je suis désolée, je n'ai pas compris.")
            phrase1 = input("Que faites-vous ?")
            messages.insert(INSERT, "[Lia]: Que faites-vous ? [Répondez dans la console Python]\n")
            messages.insert(INSERT, "[Vous]: " + phrase1 + "\n")
            """Demande à l'utilisateur ce qu'il fait"""
            if re.search(pattern_jeu, phrase1):
                phrase1 = input("Intéressant ! A quel jeu jouez-vous ?")
                messages.insert(INSERT, "[Vous]: " + phrase1 + "\n")
                print("C'est bien.")
            elif re.search(pattern_parler, phrase1):
                messages.insert(INSERT, "[Lia]: A qui parlez-vous ? [Répondez dans la console Python] \n")
                phrase1 = input("A qui parlez-vous ?")
                messages.insert(INSERT, "[Vous]: " + phrase1 + "\n")
                if re.search(r"(T|t)oi|( (T|t)e )((P|p)arl(er|é|e|es)|(D|d)iscu(ter|té|te|ssion))",phrase1):
                    messages.insert(INSERT, "[Lia]: Merci de discuter avec moi !\n")
                    print("Merci de discuter avec moi !")
                else:
                    nom2 = re.sub(r"Je", "", phrase1)
                    nom2 = re.sub(pattern_parler, "", nom2)
                    nom2 = re.findall(r"[A-Z][a-z]+", nom2)
                    if len(nom2) == 1:
                        nom2 = nom2[0]
                        messages.insert(INSERT, "[Lia]: Saluez " + nom2 + " de ma part !\n")
                        print("[Lia]: Saluez " + nom2 + " de ma part !")


                    else:
                        messages.insert(INSERT, "[Lia]: Dites-lui bonjour de ma part !\n")
                        print("Dites-lui bonjour de ma part !")
            else:
                messages.insert(INSERT, "[Lia]: Intéressant.\n")
                print("[Lia]: Intéressant.")


def identification():
        """Associe une variable au nom de l'utilisateur lorsqu'il clique sur le bouton [Valider] affiché au lancement du programme et écrit un message différent si le bouton [Déja venu?] est coché.
Lie la touche <Entry> du clavier à la fonction réponse()"""
        global nom
        utilisateur.destroy()
        deja_venu.destroy()
        input_get = input_field.get()
        nom = input_get
        print(input_get)
        messages.insert(INSERT, "[Vous]: ")
        messages.insert(INSERT, '%s\n' % input_get)
        window.bell()
        if dj_var.get() == 0:
            messages.insert(INSERT, "[Lia]: Bienvenue, ")
            messages.insert(INSERT, input_get)
        else:
            messages.insert(INSERT, "[Lia]: Ah c'est vous, ")
            messages.insert(INSERT, input_get)
        messages.insert(INSERT, '%s\n' % "! Posez-moi une question!")
        input_user.set('')
        input_field.bind("<Return>", réponse)
        input_field.bind("KP_Enter", réponse)


def météo():
        """Recherche la météo sur Google si l'utilisateur le demande,"""
        if re.search(pattern_météo, input_get):
            window.bell()
            messages.insert(INSERT, "[Lia]: Voici la météo.\n")
            messages.insert(INSERT, "[Lia]: Y a-t-il autre chose que je puisse faire ?\n")
            webbrowser.open('https://www.google.com/search?q=m%C3%A9t%C3%A9o&ie=utf-8&oe=utf-8&client=firefox-b')


def police_texte():
        """Ouvre une fenêtre permettant de régler la police du texte à partir d'une liste lorsque l'utilisateur clique sur l'option correspondante dans la barre de menu,"""
        font_list_window = Tk()
        font_list_window.title("Polices")
        font_list = Listbox(font_list_window, selectmode= SINGLE, activestyle= "none", relief= FLAT, selectbackground= "LightBlue", selectforeground="navy", width=40)
        font_list_window.iconbitmap("icone.ico")
        font_list.pack()
        for item in ["Arial", "Bahnschrift", "Courier", "Fixedsys", "Gabriola", "Impact", "Simsun", "Symbol", "Times", "Verdana"]:
            font_list.insert(END, item)
        def applique_police():
            """Applique la police sélectionnée dans la boîte de dialogue,"""
            index = font_list.curselection()
            if index != ():
                messages.configure(font= font_list.get(index))
                font_list_window.destroy()
            else:
                showerror("Erreur","Vous n'avez selectionné aucune police!\nVeuillez réessayer.")
                font_list_window.destroy()
        Button(font_list_window, text="Valider", bg= "LightBlue", activebackground= "green", fg="green", activeforeground= "white", relief= GROOVE, command=applique_police).pack()


def quitter(event):
        """Ouvre une fenêtre demandant une confirmation pour quitter le logiciel si  l'utilisateur le demande dans le champ de saisie,"""
        if re.search(pattern_quitter, input_get):
            window.bell()
            messages.insert(INSERT, "[Lia]: Bye!\n")
            rep = askokcancel("Quitter", "Vous partez déjà?")
            if rep==1:
                window.destroy()
            else:
                window.bell()
                messages.insert(INSERT, "[Lia]: Vous êtes encore là! Que puis-je pour vous?\n")


def random_number_game():
    """Jeu : trouver un entier entre 1 et 100"""
    if re.search(pattern_jeu, input_get):
        messages.insert(INSERT, "[Lia]: Trouvez un entier entre 1 et 100 !\n [Lia]: Entrez 1 pour jouer ! [Répondez dans la console Python] \n")
        print("Trouvez un entier entre 1 et 100 !")
        question1 = eval(input("Entrez 1 pour jouer !"))
        score = 0
        if question1 == 1:
            nombre = randint(1,100)
            reponse = 0
            messages.insert(INSERT, "Nombre entre 1 et 100 : [Répondez dans la console Python]\n")
            while reponse != nombre:
                score += 1
                reponse = eval(input("Nombre entre 1 et 100 :"))
                messages.insert(INSERT, "[Vous]: " + str(reponse) + "\n")
                if reponse > nombre:
                    print(random_number_game_high())
                    messages.insert(INSERT, "[Lia]: " + random_number_game_high() + "\n")
                elif reponse <nombre:
                    print(random_number_game_small())
                    messages.insert(INSERT, "[Lia]: " + random_number_game_small() + "\n")
            messages.insert(INSERT, "[Lia]: Vous avez gagné ! Votre score est :" + str(score) + ".\n")
            print("Bravo ! Vous avez gagné ! Votre score est :", score, ".")
        else:
            messages.insert(INSERT, "[Lia]: Au revoir !\n")
            return "Au revoir !"


def random_number_game_high():
    """Renvoie une indication si le nombre entré dans le jeu est trop grand"""
    list_high = ["Trop grand !","Le nombre cherché est plus petit !", "Votre réponse est trop grande.", "Trop élevé !"]
    return list_high[randint(0,len(list_high)-1)]


def random_number_game_small():
    """Renvoie une indication si le nombre entré dans le jeu est trop petit"""
    list_high = ["Trop petit !","Le nombre cherché est plus grand !", "Votre réponse est trop petite.", "Pas assez grand !"]
    return list_high[randint(0,len(list_high)-1)]


def réponse(event):
        """Fournit une réponse à une saisie de l'utilisateur en lançant toutes les fonctions qui identifient des patterns et y répondent.
Ouvre une page Google recherchant la saisie de l'utilisateur si aucun pattern n'est reconnu.
Réinitialise le champ de saisie."""
        global input_get
        input_get = input_field.get()
        print(input_get)
        messages.insert(INSERT, "[Vous]: ")
        messages.insert(INSERT, '%s\n' % input_get)
        quitter(event)
        météo()
        retour_nom_utilisateur()
        retour_nom_lia()
        detect_trad()
        discussion()
        random_number_game()
        calcul()
        if not re.search(pattern_calcul1, input_get) and not re.search(pattern_calcul2, input_get) and not re.search(pattern_disc_bien1, input_get) and not re.search(pattern_disc_mal, input_get) and not re.search(pattern_jeu, input_get) and not re.search(pattern_parler, input_get) and not re.search(pattern_lia, input_get) and not re.search(pattern_météo, input_get) and not re.search(pattern_quitter, input_get) and not re.search(pattern_traduction, input_get) and not re.search(pattern_utilisateur, input_get):
            window.bell()
            messages.insert(INSERT, "[Lia]: Je ne sais pas comment vous répondre. Mais voici ce que dit Google à propos de <" + input_get + ">\n" )
            webbrowser.open('https://www.google.com/search?source=hp&ei=8_ICW7r5OM2x0gXy0YywBw&q='+ input_get + '&oq=' + input_get + '&gs_l=psy-ab.3..0l10.2862.3747.0.4187.6.5.0.0.0.0.131.284.2j1.4.0....0...1c.1.64.psy-ab..2.3.284.0..0i131k1.62.P-z-Mz7Vw2A')
        input_user.set('')
        return "break"


def retour_nom_lia():
        """Retourne le nom de Lia si l'utilisateur le demande,"""
        if re.search(pattern_lia, input_get):
            window.bell()
            messages.insert(INSERT, "[Lia]: Je m'appelle Lia.\n")


def retour_nom_utilisateur():
        """Retourne le nom de l'utilisateur s'il le demande,"""
        if re.search(pattern_utilisateur, input_get):
            window.bell()
            messages.insert(INSERT, "[Lia]: Vous êtes ")
            messages.insert(INSERT, nom)
            messages.insert(INSERT, ".\n")


#Barre de menu avec plusieurs sous-catégories ("cases")
menubar = Menu(window)
menu1 = Menu(menubar,tearoff=0, activebackground= "LightBlue", activeforeground= "navy")
menu1.add_command(label= "Modifier la couleur de fond", command= couleur_fond)
menu1.add_command(label= "Modifier la couleur du texte", command= couleur_texte)
menu1.add_separator()
menu1.add_command(label= "Modifier la police du texte", command= police_texte)
menubar.add_cascade(label= "Options", menu= menu1)
menu2 = Menu(menubar, tearoff=0, activebackground= "LightBlue", activeforeground= "navy")
menu2.add_command(label="Aide", command= aide)
menu2.add_command(label="Créateurs", command= créateurs)
menubar.add_cascade(label="A propos", menu= menu2)
window.config(menu=menubar)


#Boite de dialogue
messages = Text(window, bg ="LightBlue", font="Bahnschrift", fg="Blue", padx=5, pady=5, relief=FLAT)
messages.pack()
messages.insert(INSERT, "[Lia]: Bonjour, je suis Lia. A qui ai-je l'honneur ?\n")
window.bell()


#Zone de saisie texte
input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X, padx=5, pady=5)


#Boutons d'identification de l'utilisateur
deja_venu = Frame(window)
deja_venu.pack(side=LEFT, padx=5)
dj_var = IntVar()
Checkbutton(deja_venu, text="Déja venu?", bg="LightBlue", activebackground= "navy", relief= GROOVE, fg= "Blue", activeforeground = "white", variable= dj_var, onvalue='1', offvalue='0').pack()
utilisateur = Frame(window)
utilisateur.pack(side=RIGHT,padx=5,pady=5)
Label(utilisateur, text = "Entrez votre nom et cliquez sur le bouton: ").pack(side=LEFT)
Button(utilisateur, text="Valider", bg= "LightBlue", activebackground= "Green", fg="green", activeforeground= "white", relief= GROOVE, command = identification).pack()


#Affichage de la fenêtre principale (comportant tout le reste)
window.mainloop()