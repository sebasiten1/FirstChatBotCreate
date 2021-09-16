# chat-bots_first_part
Prérequis: rien

Création d’un chat-bots 

Langages : Python .


Grâce à ce projet j’effleure le monde de l’intelligence artificielle ; je découvre les langages
Python  et je rajoute un savoir-faire sur mon cv.

Une implémentation web de [ChatterBot](https://github.com/gunthercox/ChatterBot) utilisant Flask.
## Comment déployer ceci sur un serveur web ?
Si vous n'avez pas de serveur dédié, je vous recommande vivement d'utiliser [PythonAnywhere](https://www.pythonanywhere.com/), [AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/) ou [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) pour héberger votre application.

### Déploiement sur Heroku
Si vous déployez sur Heroku, vous devrez changer l'adaptateur de base de données de `chatterbot.storage.SQLStorageAdapter` à `chatterbot.storage.MongoDatabaseAdapter` puisque SQLite3 n'est pas supporté. Pour ce faire, il suffit de changer la ligne suivante :

`english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")`

... to use the MongoDB adapter:

```
english_bot = ChatBot("English Bot", 
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = mongodb_name,
                     database_uri = mongodb_uri)
```
... where `mongodb_name` is the name of the database you wish to connect to and `mongodb_uri` is the URI of a remote instance of MongoDB.
