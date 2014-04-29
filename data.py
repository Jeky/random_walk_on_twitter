import os.path

PATH = '/Users/jeky/dataset/twitter/lucene/'
ORINGNAL_FILE = os.path.join(PATH, 'twitter.graph')
RW_FILE = os.path.join(PATH, 'rw.txt')
RW_PATH = os.path.join(PATH, 'rw_data/')
NODE_OUT_DEGREE_FILE = os.path.join(PATH, 'to.dist')
NODE_IN_DEGREE_FILE = os.path.join(PATH, 'from.dist')
ID_LIST_FILE = os.path.join(PATH, 'node.list')
RANK_FILE = os.path.join(PATH, 'rank.dist')
ESITMATE_FILE = os.path.join(PATH, 'estimate.txt')