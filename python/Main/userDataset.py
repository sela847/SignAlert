
from torch.utils.data import Dataset, DataLoader
import numpy
from PIL import Image
import math

class userData(Dataset):
    def __init__(self, numpy_array,transform =None):
        # data loading
        self.x = (numpy_array[:,1:])
        self.y = (numpy_array[:,[0]]) 
        self.n_samples = numpy_array.shape[0]
        self.transform = transform
    # Getting each item in the dataset
    def __getitem__(self,index):
        image = self.x[index].reshape((28,28))
        if self.transform:
            return  self.transform(image), self.y[index]
        return image, self.y[index]
    
    # Returning length of the dataset
    def __len__(self):
        return self.n_samples

if __name__ == '__main__':
    
    dataset = userData('/Users/shaaranelango/Downloads/project-1-python-team_16/dataset/sign_mnist_train.csv')
    dataloader = DataLoader(dataset= dataset, batch_size=4, num_workers=2)
    # dataiter = iter(dataloader)
    # data = next(dataiter)
    # features,labels = data
    # print(features, labels)
    # print(features.shape)
    # im = features[0].numpy()
    # im = Image.fromarray(im)
    # im = im.convert("L")
       
    # im.save("testeddd.jpeg")

## All of below is testing
# training loop
    num_epochs = 2
    total_samples = len(dataset)
    n_iterations = math.ceil(total_samples/4)
    print(total_samples,n_iterations)

    for epoch in range(num_epochs):
        for i, (inputs,labels) in enumerate(dataloader):
        #forward-backward pass, update
            if (i+1) % 500 == 0:
                print(f'epoch {epoch+1}/{num_epochs} , step {i+1}/{n_iterations}, inputs {inputs}')