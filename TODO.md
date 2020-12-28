# TODO

## Database:

- [ ] Legge til brukere
    - Brukernavn
    - Passord
    - ManyToManyField til favoritt quizark (spørsmål.txt)
- [ ] Legge til quizark
    - ManyToOneField til bruker som lagde quizarket
    - Fil felt til å laste opp quizark
    - Quizarket må ha en gyldig syntaks, spørsmål og svar blir splittet av :
    - Når quizarket blir lastet opp kjøres første del av pythonscriptet (math_game), men i steden for å legge søprsmål og svar i et dictonary, så blir de lastet opp i databasen
- [ ] Legge til spørsmål
    - Blir automatisk laget ut ifra quizark
    - Har et spørsmålfelt
    - Et svarfelt
    - ManyToManyFiled til quizark, samme spørsmål kan finnes på flere ark

## Nettside

- [ ] Stilark
- [ ] Logo
- [ ] Api for å slippe å reloade hele siden for å skjekke om svaret er riktig
- [ ] Påloggingside
- [ ] Registreringside
- [ ] Side med spørsmål
