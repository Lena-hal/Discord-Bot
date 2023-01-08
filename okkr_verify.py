import praw, time;
MIN_ACCOUNT_KARMA = 50 #minimalní počet post karmy a comment karmy skombinované dohromady (defaultně je 50)
MIN_ACCOUNT_AGE = 2592000 #minimalní čas v sekundách od založení učtu uživatele (defaultně je 30 dní (2592000))

reddit = praw.Reddit( #nastavení reddit API bota aby dokazal komunikovat s reddit servry
    client_id="CLUShvO1vgmUTNnGR_4iaA",
    client_secret="5mxpwxkmiqhOf793qIJf7GrnkVmBGQ",
    user_agent="<consloe:okkrbot:0.1>",
)

def auth_user(username:str): #funkce na authentifikaci uživatele 
    if type(username) != str: # zjistí jestli byla zadaná hodnota string
        raise TypeError("\n\nZadaná hodnota musí být string, bohužel ale zadaná hodnota string nebyl :(\n\n")
    else:
        if username[:2] == "u/":
            username = username[2:]
        if reddit.request("GET", "/api/username_available.json?user=" +username):
            return "ADNE" # Account does not exist

        user = reddit.redditor(username) #najde uživatele v databazi uživatelů
    total_karma = user.link_karma+ user.comment_karma #vypočíta počet karmy
    total_time = time.time()-user.created_utc # vypočítá čas od založení učtu
    if total_karma > MIN_ACCOUNT_KARMA and MIN_ACCOUNT_AGE < total_time: #pokud splňuje podmínky vrátí True, jinak vrát False
        return "PS" #Podmínky Splněny
    else:
        return "PN" #Podmínky Nesplněny