import pandas as pd 
import argparse
import os
                    
def read_args():
    parser = argparse.ArgumentParser(description='Read output directory of the model we evaluate.')
    parser.add_argument('--meta_path', type=str, help='The file path for input file')
    parser.add_argument('--docid_path', type=str, help='The file path for out path')
    args = parser.parse_args()
    meta_path = args.meta_path
    docid_path = args.docid_path

    return meta_path, docid_path

def meta_to_docids(meta_path, docid_path):
    # Convert meta file to docids file for MuDA
    input_df = pd.read_csv(meta_path, header=None, delimiter="\t")
    doc_ids= [element for line in input_df.iloc[:, [0]].values for element in line ] 
    print ("Checking the length of the doc_ids is same to src and ref:", len(doc_ids))

    with open(docid_path, "w") as wf:
        for i in doc_ids:
            wf.write(f"{i}\n")
    

def main():
    meta_path, docid_path= read_args()
    meta_to_docids(meta_path, docid_path)

if __name__ == "__main__":
    main()