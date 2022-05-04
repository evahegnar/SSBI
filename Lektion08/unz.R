
#Unzipbiten är inte särskilt konstig - vi ger bara path till zipfilen och säger vad vi ska hämta
tmp <- unz("C:\\Users\\carlj\\OneDrive\\Skrivbord\\Power\ BI\\Lektion9\\Master.zip", "Teams.csv")


teams <- read.csv(tmp)

#Exkludera denna i Power BI - den är bara till för att se så att vår unzip fungerar som vi vill!
View(teams)



