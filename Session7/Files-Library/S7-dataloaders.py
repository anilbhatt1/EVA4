# Import the torch library
import torch 

# Class to create a Data Loader 
# Data Loader is a place holder using which weload the train and test data sets.
Class DataLoader:
      
    def __init__(self, shuffle, batch_size, seed):
        self.shuffle = True,
        self.batch_size = 128,
        self.seed    = 1
         
        cuda = torch.cuda.is_available()
            
        if cuda:
           torch.cuda.manual_seed(seed) # Seed is for reproducibility
      
        # # dataloader arguments # # which we load
        self.dataloader_args = dict(shuffle=shuffle, batch_size=batch_size, num_workers=4, pin_memory=True) if cuda else dict(shuffle=shuffle, batch_size=batch_size)

        def load(self, data):
            return torch.utils.data.DataLoader(data, **self.dataloader_args)
     
        
      
