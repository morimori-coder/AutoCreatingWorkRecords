import json

def get_json_data(file_name):
    # jsonでseleniumで利用する情報を保存している
    jsonData = open(file_name, 'r', encoding='utf=8')
    data = json.load(jsonData)
    jsonData.close()

    return data


