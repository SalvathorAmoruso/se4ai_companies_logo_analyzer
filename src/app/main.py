from src.data.make_dataset import synchronize_companies
from src.models.similarity_model import get_similar_items
from src.utils.credentials.credentials import get_credentials
from src.utils.project.project import create_project
from src.models.train_model import train
from src.models.train_model import apply_train

if __name__ == '__main__':
    #create_project()
    #print(get_credentials())
    #synchronize_companies()
    #train()
    #apply_train()
    get_similar_items("https://cdn3d.iconscout.com/3d/free/thumb/free-netflix-2950136-2447898.png")


