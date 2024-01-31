import requests
from mytoken import token

HTTP_STATUS = 201

class YandexDisk:
    
    URL_FILE = 'https://cloud-api.yandex.net/v1/disk/resources/files' 
    URL_UPLOAD = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    
    def __init__(self, token: str):
        self.token = token
        
    @property    
    def header(self):
        return {'Content-Type': 'Application/json',
                 'Accept': 'application/json',
                'Authorization': f'OAuth {self.token}'
               }
    def get_files_list(self):
        response = requests.get(self.URL_FILE,headers=self.header)
        print('good')
        return response.json()

    def get_upload(self, ya_disk_path):
        params = {'path': ya_disk_path, 'overwrite':'true'}
        response = requests.get(self.URL_UPLOAD, headers=self.header, params=params)
        upload_url = response.json().get('href')
        return upload_url

    def upload_file(self, ya_disk_path, file_path):
        upload_link = self.get_upload(ya_disk_path)
        with open(file_path,'rb') as file_obj:
            response = requests.put(upload_link,data=file_obj)
            if response.status_code == HTTP_STATUS:
                print('Успешная загрузка')

        return response.status_code

if __name__ == '__main__':
    instance = YandexDisk(token)
    path_to_file = 'testing.txt'
    print(instance.upload_file(path_to_file,path_to_file))
   
