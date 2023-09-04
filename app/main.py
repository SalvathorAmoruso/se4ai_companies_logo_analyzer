from utils.project import project
from utils.credentials import credentials
from src.data.make_dataset import synchronize_companies
from src.models.train_model import train

if __name__ == '__main__':
    #project.create_project()
    #credentials.get_credentials()
    #synchronize_companies()
    train()


