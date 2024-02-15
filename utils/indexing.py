import json
from utils.wordprocess import WordProcess

class Indexing():
    def apply_index(self, inputs, index):
        '''
            split sentence into words and put it
            in dictionary
        '''
        title_words = inputs.title.split()
        sn = int(inputs.id)

        for word in title_words:
            if word in index:
                if sn not in index[word]:
                    index[word].append(sn)
            else:
                index[word] = [sn]
        return index
    
    def full_index(self, df):
        '''
            loop all papper 's title and make indexing
        '''
        index = dict()
        for x in range(len(df)):
            inpt = df.loc[x,:]
            ind = self.apply_index(inputs=inpt, index=index)
        return ind
    
    def construct_index(self):
        '''
            driver program to construct inverted index
        '''
        wordprocess = WordProcess()
        queue = wordprocess.preprocess_df()
        ind = self.full_index(df=queue)
        with open('indexes.json', 'w') as json_file:
            json.dump(ind, json_file, sort_keys=True, indent=4)

