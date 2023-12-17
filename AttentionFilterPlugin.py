import PyIO
import PyPluMA
import pickle

class AttentionFilterPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)
    def run(self):
        pass
    def output(self, outputfile):
        infile = open(PyPluMA.prefix()+"/"+self.parameters["scorefile"], "rb")
        attn_df_test = pickle.load(infile)
        attn_mod = attn_df_test[attn_df_test[self.parameters["x"]]==self.parameters["value"]]
        outfile = open(outputfile, "wb")
        pickle.dump(attn_mod, outfile)
