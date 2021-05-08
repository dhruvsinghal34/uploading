import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)
        for rootfolders,subfolders,files in os.walk(file_from):
            for file in files:
                localPath=os.path.join(file_from,file)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'k1er0qhzCeMAAAAAAAAAARrPwXsrHYqAaolcxtGorjUcCaPq8I6DVSad3f2i1fBs'
    transferData = TransferData(access_token)

    file_from = 'C:/Dhruv/projects/story'
    file_to = '/test_dropbox/story'  

    
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
