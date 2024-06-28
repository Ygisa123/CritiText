from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
print("Connexion réussie à MongoDB")
db = client.BookSell

# Insertion de données dans la collection "produits"
produits_data = [
    {
        "nom": "Good Quality Dog Food",
        "description": "I have bought several of the Vitality canned dog food products and have found them all to be of good quality. The product looks more like a stew than a processed meat and it smells better. My Labrador is finicky and she appreciates this product better than most.",
        "prix": 5
    },
    {
        "nom": "Not as Advertised",
        "description": "Product arrived labeled as Jumbo Salted Peanuts...the peanuts were actually small sized unsalted. Not sure if this was an error or if the vendor intended to represent the product as 'Jumbo'.",
        "prix": 1
    },
    {
        "nom": "Delight says it all",
        "description": "This is a confection that has been around a few centuries. It is a light, pillowy citrus gelatin with nuts - in this case Filberts. And it is cut into tiny squares and then liberally coated with powdered sugar. And it is a tiny mouthful of heaven. Not too chewy, and very flavorful. I highly recommend this yummy treat. If you are familiar with the story of C.S. Lewis' 'The Lion, The Witch, and The Wardrobe' - this is the treat that seduces Edmund into selling out his Brother and Sisters to the Witch.",
        "prix": 4
    },
    {
        "nom": "Cough Medicine",
        "description": "If you are looking for the secret ingredient in Robitussin I believe I have found it. I got this in addition to the Root Beer Extract I ordered (which was good) and made some cherry soda. The flavor is very medicinal.",
        "prix": 2
    },
    {
        "nom": "Great taffy",
        "description": "Great taffy at a great price. There was a wide assortment of yummy taffy. Delivery was very quick. If you're a taffy lover, this is a deal.",
        "prix": 5
    },
    {
        "nom": "Nice Taffy",
        "description": "I got a wild hair for taffy and ordered this five pound bag. The taffy was all very enjoyable with many flavors: watermelon, root beer, melon, peppermint, grape, etc. My only complaint is there was a bit too much red/black licorice-flavored pieces (just not my particular favorites). Between me, my kids, and my husband, this lasted only two weeks! I would recommend this brand of taffy -- it was a delightful treat.",
        "prix": 4
    },
    {
        "nom": "Great! Just as good as the expensive brands!",
        "description": "This saltwater taffy had great flavors and was very soft and chewy. Each candy was individually wrapped well. None of the candies were stuck together, which did happen in the expensive version, Fralinger's. Would highly recommend this candy! I served it at a beach-themed party and everyone loved it!",
        "prix": 5
    },
    {
        "nom": "Wonderful, tasty taffy",
        "description": "This taffy is so good. It is very soft and chewy. The flavors are amazing. I would definitely recommend you buying it. Very satisfying!!",
        "prix": 5
    },
    {
        "nom": "Yay Barley",
        "description": "Right now I'm mostly just sprouting this so my cats can eat the grass. They love it. I rotate it around with Wheatgrass and Rye too.",
        "prix": 5
    },
    {
        "nom": "Healthy Dog Food",
        "description": "This is a very healthy dog food. Good for their digestion. Also good for small puppies. My dog eats her required amount at every feeding.",
        "prix": 5
    },
    {
        "nom": "The Best Hot Sauce in the World",
        "description": "I don't know if it's the cactus or the tequila or just the unique combination of ingredients, but the flavor of this hot sauce makes it one of a kind! We picked up a bottle once on a trip we were on and brought it back home with us and were totally blown away! When we realized that we simply couldn't find it anywhere in our city we were bummed. Now, because of the magic of the internet, we have a case of the sauce and are ecstatic because of it. If you love hot sauce...I mean really love hot sauce, but don't want a sauce that tastelessly burns your throat, grab a bottle of Tequila Picante Gourmet de Inclan. Just realize that once you taste it, you will never want to use any other sauce. Thank you for the personal, incredible service!",
        "prix": 5
    },
    {
        "nom": "My cats LOVE this 'diet' food better than their regular food",
        "description": "One of my boys needed to lose some weight and the other didn't. I put this food on the floor for the chubby guy, and the protein-rich, no by-product food up higher where only my skinny boy can jump. The higher food sits going stale. They both really go for this food. And my chubby boy has been losing about an ounce a week.",
        "prix": 5
    },
    {
        "nom": "My Cats Are Not Fans of the New Food",
        "description": "My cats have been happily eating Felidae Platinum for more than two years. I just got a new bag and the shape of the food is different. They tried the new food when I first put it in their bowls and now the bowls sit full and the kitties will not touch the food. I've noticed similar reviews related to formula changes in the past. Unfortunately, I now need to find a new food that my cats will eat.",
        "prix": 1
    },
    {
        "nom": "Fresh and greasy!",
        "description": "Good flavor! These came securely packed... they were fresh and delicious! I love these Twizzlers!",
        "prix": 4
    },
    {
        "nom": "Strawberry Twizzlers - Yummy",
        "description": "The Strawberry Twizzlers are my guilty pleasure - yummy. Six pounds will be around for a while with my son and I.",
        "prix": 5
    }
]

db.produits.insert_many(produits_data)
